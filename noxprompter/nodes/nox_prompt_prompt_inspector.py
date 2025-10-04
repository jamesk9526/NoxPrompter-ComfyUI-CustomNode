from __future__ import annotations

import re
from typing import Iterable, List, Sequence, Tuple

from ..common import (
    PresetMixin,
    PromptFragmentFilter,
    detect_prompt_contradictions,
)


class NoxPromptPromptInspector(PresetMixin):
    """Clean, analyze, and summarize prompt fragments for reuse."""

    _CATEGORY = "NoxPrompter/Analysis"

    @classmethod
    def INPUT_TYPES(cls):
        profile_names = sorted(PromptFragmentFilter.PROFILE_PRESETS.keys())
        return {
            "required": {
                "prompt_text": (
                    "STRING",
                    {"multiline": True, "default": "Detailed portrait of a fearless explorer."},
                ),
                "split_mode": (
                    ["auto", "comma", "newline", "sentence"],
                    {"default": "auto"},
                ),
                "filter_profile": (
                    profile_names + ["none"],
                    {"default": "balanced"},
                ),
                "normalize_case": ("BOOLEAN", {"default": False}),
                "remove_duplicates": ("BOOLEAN", {"default": True}),
                "max_fragments": ("INT", {"default": 24, "min": 1, "max": 99, "step": 1}),
            },
            "optional": {
                "include_negative": ("BOOLEAN", {"default": True}),
                "negative_prompt": ("STRING", {"multiline": True, "default": "low quality, blurry"}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = (
        "organized_prompt",
        "fragment_list",
        "insights",
        "metrics",
        "preset_status",
    )
    FUNCTION = "inspect_prompt"
    CATEGORY = _CATEGORY

    def inspect_prompt(
        self,
        prompt_text: str,
        split_mode: str,
        filter_profile: str,
        normalize_case: bool,
        remove_duplicates: bool,
        max_fragments: int,
        include_negative: bool = True,
        negative_prompt: str = "",
        preset_action: str = "none",
        preset_name: str = "",
    ) -> Tuple[str, str, str, str, str]:
        config = {
            "prompt_text": prompt_text,
            "split_mode": split_mode,
            "filter_profile": filter_profile,
            "normalize_case": normalize_case,
            "remove_duplicates": remove_duplicates,
            "max_fragments": max_fragments,
            "include_negative": include_negative,
            "negative_prompt": negative_prompt,
        }

        config, preset_status = self._apply_preset_action(
            "prompt_inspector",
            preset_action,
            preset_name,
            config,
        )

        prompt_text = config.get("prompt_text", prompt_text)
        split_mode = config.get("split_mode", split_mode)
        filter_profile = config.get("filter_profile", filter_profile)
        normalize_case = bool(config.get("normalize_case", normalize_case))
        remove_duplicates = bool(config.get("remove_duplicates", remove_duplicates))
        max_fragments = int(config.get("max_fragments", max_fragments))
        include_negative = bool(config.get("include_negative", include_negative))
        negative_prompt = config.get("negative_prompt", negative_prompt)

        positive_fragments = self._split_fragments(prompt_text, split_mode)
        negative_fragments = (
            self._split_fragments(negative_prompt, split_mode)
            if include_negative and negative_prompt.strip()
            else []
        )

        positive_fragments, removed_positive = self._normalize_fragments(
            positive_fragments,
            normalize_case,
            remove_duplicates,
        )
        negative_fragments, removed_negative = self._normalize_fragments(
            negative_fragments,
            normalize_case,
            remove_duplicates,
        )

        organized_positive, filter_summary = self._apply_filter(
            positive_fragments,
            filter_profile,
            max_fragments,
        )

        organized_prompt = self._assemble_prompt(organized_positive)
        fragment_list = self._render_fragment_list(organized_positive, negative_fragments)

        warning_messages = detect_prompt_contradictions(organized_positive)
        insight_parts: List[str] = []
        if filter_summary:
            insight_parts.append(filter_summary)
        if removed_positive or removed_negative:
            insight_parts.append(
                f"Removed duplicates: +{removed_positive} positive, +{removed_negative} negative"
            )
        if warning_messages:
            insight_parts.extend(f"Warning: {warning}" for warning in warning_messages)
        if not insight_parts:
            insight_parts.append("Prompt fragments left unchanged.")
        insights = " | ".join(insight_parts)

        metrics = self._build_metrics(
            prompt_text,
            organized_positive,
            negative_fragments,
            removed_positive + removed_negative,
        )

        return organized_prompt, fragment_list, insights, metrics, preset_status

    def _split_fragments(self, text: str, mode: str) -> List[str]:
        if not text:
            return []
        normalized = text.replace("\r", "\n")
        if mode == "comma":
            tokens = re.split(r"[\n,]", normalized)
        elif mode == "newline":
            tokens = re.split(r"\n+", normalized)
        elif mode == "sentence":
            tokens = re.split(r"(?<=[.!?])\s+|\n+", normalized)
        else:  # auto
            tokens = re.split(r"[\n,]|(?<=[.!?])\s+", normalized)
        return [token.strip() for token in tokens if token and token.strip()]

    def _normalize_fragments(
        self,
        fragments: Iterable[str],
        normalize_case: bool,
        remove_duplicates: bool,
    ) -> Tuple[List[str], int]:
        prepared: List[str] = []
        seen = set()
        removed = 0
        for fragment in fragments:
            cleaned = fragment.strip()
            if not cleaned:
                continue
            if normalize_case:
                cleaned = cleaned.lower()
            key = cleaned.lower()
            if remove_duplicates and key in seen:
                removed += 1
                continue
            seen.add(key)
            prepared.append(cleaned)
        return prepared, removed

    def _apply_filter(
        self,
        fragments: Sequence[str],
        profile: str,
        max_fragments: int,
    ) -> Tuple[List[str], str]:
        profile = (profile or "").strip().lower()
        if not fragments:
            return [], ""
        if profile in {"", "none"}:
            limited = list(fragments)[:max_fragments]
            return limited, ""
        filterer = PromptFragmentFilter(profile)
        organized = filterer.organize(list(fragments))
        limited = organized[:max_fragments]
        return limited, filterer.summarize()

    def _assemble_prompt(self, fragments: Sequence[str]) -> str:
        if not fragments:
            return ""
        sentences = []
        for fragment in fragments:
            cleaned = fragment.strip()
            if not cleaned:
                continue
            if cleaned[-1] not in ".!?":
                cleaned = f"{cleaned}."
            sentences.append(cleaned)
        return " ".join(sentences)

    def _render_fragment_list(
        self,
        positive: Sequence[str],
        negative: Sequence[str],
    ) -> str:
        lines: List[str] = []
        index = 1
        for fragment in positive:
            lines.append(f"{index}. [pos] {fragment}")
            index += 1
        for fragment in negative:
            lines.append(f"{index}. [neg] {fragment}")
            index += 1
        return "\n".join(lines)

    def _build_metrics(
        self,
        prompt_text: str,
        positive: Sequence[str],
        negative: Sequence[str],
        duplicates_removed: int,
    ) -> str:
        character_count = len(prompt_text.strip())
        word_count = len(prompt_text.split())
        positive_count = len(positive)
        negative_count = len(negative)
        avg_length = (
            sum(len(item) for item in positive) / positive_count
            if positive_count
            else 0
        )
        segments = [
            f"Positive fragments: {positive_count}",
            f"Negative fragments: {negative_count}",
            f"Characters: {character_count}",
            f"Words: {word_count}",
            f"Avg fragment length: {avg_length:.1f}",
        ]
        if duplicates_removed:
            segments.append(f"Duplicates removed: {duplicates_removed}")
        return " | ".join(segments)


__all__ = ["NoxPromptPromptInspector"]
