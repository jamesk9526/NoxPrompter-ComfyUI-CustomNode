"""Common utilities shared across Nox Prompter nodes."""

from __future__ import annotations

import json
import os
import re
from typing import Any, Dict, List, Tuple

from .constants import CUSTOM_OPTION, PRESET_ROOT, PROMPT_CONTRADICTION_RULES


class PromptFragmentFilter:
    """Organize, deduplicate, and lightly curate prompt fragments."""

    PROFILE_PRESETS = {
        "balanced": {
            "remove": {"placeholder", "generic"},
            "max_fragments": 18,
            "priority": ["subject", "scene", "motion", "camera", "style", "extra"],
            "keywords": {
                "motion": ["motion", "camera", "move", "tempo"],
                "style": ["style", "palette", "effect", "lighting"],
                "scene": ["scene", "environment", "setting", "location"],
                "subject": ["subject", "portrait", "hero", "character"],
                "camera": ["lens", "framing", "focus"],
            },
            "insight": "Balanced profile organizes fragments from subject through stylistic flourishes.",
        },
        "cinematic": {
            "remove": {"generic", "boring", "placeholder"},
            "max_fragments": 20,
            "priority": ["subject", "scene", "camera", "motion", "style", "extra"],
            "keywords": {
                "camera": ["camera", "lens", "framing", "cinematic"],
                "style": ["film", "cinematic", "grade", "bokeh"],
                "scene": ["scene", "set", "location", "environment"],
                "motion": ["move", "motion", "tempo", "beat"],
                "subject": ["subject", "hero", "character", "actor"],
            },
            "insight": "Cinematic profile spotlights camera language alongside scene context.",
        },
        "minimal": {
            "remove": {"redundant", "generic", "placeholder"},
            "max_fragments": 12,
            "priority": ["subject", "scene", "style", "extra"],
            "keywords": {
                "style": ["palette", "style", "mood", "tone"],
                "scene": ["scene", "environment", "location"],
                "subject": ["subject", "portrait", "focus"],
            },
            "insight": "Minimal profile trims to the essentials for shorter base prompts.",
        },
        "narrative": {
            "remove": {"placeholder"},
            "max_fragments": 22,
            "priority": ["subject", "scene", "motion", "style", "extra"],
            "keywords": {
                "motion": ["motion", "beat", "arc", "tempo"],
                "scene": ["scene", "setting", "environment", "beat"],
                "subject": ["subject", "character", "hero", "protagonist"],
                "style": ["tone", "mood", "style", "palette"],
            },
            "insight": "Narrative profile preserves motion arcs and tonal descriptors for storytelling prompts.",
        },
    }

    def __init__(self, profile: str = "balanced") -> None:
        self.profile_name = (profile or "balanced").lower()
        self.profile = self.PROFILE_PRESETS.get(self.profile_name, self.PROFILE_PRESETS["balanced"])
        self._removed: List[str] = []

    def organize(self, fragments: List[str]) -> List[str]:
        prioritized: List[Tuple[str, str]] = []
        seen = set()
        for fragment in fragments:
            cleaned = self._normalize(fragment)
            if not cleaned:
                continue
            lowered = cleaned.lower()
            if any(token in lowered for token in self.profile.get("remove", [])):
                self._removed.append(cleaned)
                continue
            if lowered in seen:
                continue
            seen.add(lowered)
            bucket = self._bucket_for(cleaned)
            prioritized.append((bucket, cleaned))

        priority_order = {label: index for index, label in enumerate(self.profile.get("priority", []))}
        prioritized.sort(key=lambda item: (priority_order.get(item[0], len(priority_order)), item[1]))
        limited = prioritized[: self.profile.get("max_fragments", len(prioritized))]
        return [item[1] for item in limited]

    def summarize(self) -> str:
        insight = self.profile.get("insight", "Prompt fragments were harmonized.")
        if self._removed:
            removed = ", ".join(self._removed[:3])
            if len(self._removed) > 3:
                removed += ", ..."
            return f"{insight} Removed duplicates/noise: {removed}."
        return insight

    def _normalize(self, fragment: str) -> str:
        cleaned = (fragment or "").strip()
        cleaned = re.sub(r"\s+", " ", cleaned)
        return cleaned

    def _bucket_for(self, fragment: str) -> str:
        lowered = fragment.lower()
        keyword_map = self.profile.get("keywords", {})
        for bucket, keywords in keyword_map.items():
            if any(keyword in lowered for keyword in keywords):
                return bucket
        if lowered.startswith("camera"):
            return "camera"
        if lowered.startswith("palette"):
            return "style"
        return "extra"


def _sanitize_preset_name(name: str) -> str:
    normalized = (name or "").strip()
    if not normalized:
        return ""
    return re.sub(r"[^0-9A-Za-z._-]+", "_", normalized)


class PresetManager:
    """Simple JSON-based preset storage scoped per node."""

    def __init__(self, base_dir: str = PRESET_ROOT):
        self.base_dir = base_dir

    def _node_dir(self, node_key: str, ensure: bool = False) -> str:
        path = os.path.join(self.base_dir, node_key)
        if ensure:
            os.makedirs(path, exist_ok=True)
        return path

    def save(self, node_key: str, preset_name: str, data: Dict[str, Any]) -> str:
        sanitized = _sanitize_preset_name(preset_name)
        if not sanitized:
            raise ValueError("Preset name is required to save.")
        directory = self._node_dir(node_key, ensure=True)
        file_path = os.path.join(directory, f"{sanitized}.json")
        with open(file_path, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, ensure_ascii=False)
        return file_path

    def load(self, node_key: str, preset_name: str) -> Dict[str, Any]:
        sanitized = _sanitize_preset_name(preset_name)
        if not sanitized:
            raise ValueError("Preset name is required to load.")
        directory = self._node_dir(node_key)
        file_path = os.path.join(directory, f"{sanitized}.json")
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Preset '{preset_name}' not found for {node_key}.")
        with open(file_path, "r", encoding="utf-8") as handle:
            return json.load(handle)

    def list(self, node_key: str) -> List[str]:
        directory = self._node_dir(node_key)
        if not os.path.isdir(directory):
            return []
        names = []
        for entry in os.listdir(directory):
            if entry.lower().endswith(".json"):
                names.append(os.path.splitext(entry)[0])
        return sorted(names)


class PresetMixin:
    _preset_manager = PresetManager()

    def _apply_preset_action(
        self,
        node_key: str,
        preset_action: str,
        preset_name: str,
        data: Dict[str, Any],
    ) -> Tuple[Dict[str, Any], str]:
        action = (preset_action or "none").strip().lower()
        name = (preset_name or "").strip()
        status_messages: List[str] = []
        result = dict(data)

        try:
            if action == "save":
                path = self._preset_manager.save(node_key, name, result)
                rel_path = os.path.relpath(path, os.path.dirname(__file__))
                status_messages.append(f"Preset saved: {rel_path}")
            elif action == "load":
                loaded = self._preset_manager.load(node_key, name)
                for key, value in loaded.items():
                    if key in result:
                        result[key] = value
                status_messages.append(f"Preset loaded: {name}")
            elif action == "list":
                available = self._preset_manager.list(node_key)
                if available:
                    status_messages.append("Available presets: " + ", ".join(available))
                else:
                    status_messages.append("No presets saved yet.")
        except FileNotFoundError as exc:
            status_messages.append(str(exc))
        except json.JSONDecodeError as exc:
            status_messages.append(f"Preset JSON invalid: {exc}")
        except ValueError as exc:
            status_messages.append(str(exc))
        except OSError as exc:  # pragma: no cover
            status_messages.append(f"Preset action failed: {exc}")

        status = " | ".join(status_messages)
        return result, status


def _resolve_action_option(
    selection: str,
    custom_prompt: str,
    table: Dict[str, Dict[str, str]],
) -> Tuple[str, str]:
    if selection == CUSTOM_OPTION:
        value = (custom_prompt or "").strip()
        return value, ""
    record = table.get(selection)
    if record:
        return record.get("prompt", ""), record.get("summary", "")
    fallback = (selection or "").strip()
    return fallback, ""


def _resolve_option(selection: str, table: Dict[str, Dict[str, str]]) -> Tuple[str, str]:
    record = table.get(selection)
    if record:
        return record.get("prompt", ""), record.get("notes", record.get("summary", ""))
    fallback = (selection or "").strip()
    return fallback, ""


def _split_tokens(value: str) -> List[str]:
    if not value:
        return []
    tokens: List[str] = []
    for chunk in value.replace("\r", "\n").split("\n"):
        parts = [token.strip() for token in chunk.split(",") if token.strip()]
        tokens.extend(parts)
    return tokens


def _resolve_with_custom(
    selection: str,
    custom_value: str,
    table: Dict[str, Dict[str, str]],
) -> Tuple[str, str]:
    if selection == CUSTOM_OPTION:
        value = (custom_value or "").strip()
        return value, "Custom selection provided."
    prompt, notes = _resolve_option(selection, table)
    return prompt, notes


def _format_notes(label: str, notes: str, fallback: str) -> str:
    content = (notes or fallback or "").strip()
    if not content:
        return ""
    return f"{label}: {content}" if label else content


def detect_prompt_contradictions(chunks: List[str]) -> List[str]:
    """Identify conflicting descriptors across provided prompt fragments."""

    if not chunks:
        return []

    lowered_sources: List[str] = []
    for chunk in chunks:
        cleaned = (chunk or "").strip()
        if not cleaned:
            continue
        lowered_sources.append(cleaned.lower())

    warnings: List[str] = []

    for rule in PROMPT_CONTRADICTION_RULES:
        groups = rule.get("groups", {})
        detected: Dict[str, List[str]] = {}
        for group_name, keywords in groups.items():
            for keyword in keywords:
                needle = keyword.lower().strip()
                if not needle:
                    continue
                for source in lowered_sources:
                    if needle in source:
                        detected.setdefault(group_name, [])
                        if keyword not in detected[group_name]:
                            detected[group_name].append(keyword)
                        break
        if len(detected) > 1:
            fragments = []
            for group_name, matches in detected.items():
                sample = ", ".join(matches[:3])
                if len(matches) > 3:
                    sample += ", ..."
                fragments.append(f"{group_name}: {sample}")
            message = f"{rule.get('label', 'Consistency')}: " + " | ".join(fragments)
            hint = rule.get("hint")
            if hint:
                message += f" ({hint})"
            warnings.append(message)

    return warnings


__all__ = [
    "PromptFragmentFilter",
    "PresetManager",
    "PresetMixin",
    "_resolve_action_option",
    "_resolve_option",
    "_resolve_with_custom",
    "_split_tokens",
    "_format_notes",
    "detect_prompt_contradictions",
]
