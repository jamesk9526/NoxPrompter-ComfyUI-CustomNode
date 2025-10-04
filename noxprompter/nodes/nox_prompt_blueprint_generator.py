from __future__ import annotations

import random
from typing import Dict, List, Sequence, Tuple

from ..common import PresetMixin, _resolve_option
from ..constants import (
    CHARACTER_ARCHETYPE_OPTIONS,
    CHARACTER_PROFESSION_OPTIONS,
    CHARACTER_TEMPERAMENT_OPTIONS,
    CUSTOM_OPTION,
    EMOTION_OPTIONS,
    LIGHT_SOURCE_OPTIONS,
    MOTION_TYPE_OPTIONS,
    NARRATIVE_ENVIRONMENTS,
    VISUAL_STYLE_OPTIONS,
)


class NoxPromptBlueprintGenerator(PresetMixin):
    """Craft structured prompt blueprints from curated option sets."""

    _CATEGORY = "NoxPrompter/Builders"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "character_archetype": (
                    cls._choices(CHARACTER_ARCHETYPE_OPTIONS),
                    {"default": "Champion"},
                ),
                "character_profession": (
                    cls._choices(CHARACTER_PROFESSION_OPTIONS),
                    {"default": "Starship Captain"},
                ),
                "character_temperament": (
                    cls._choices(CHARACTER_TEMPERAMENT_OPTIONS),
                    {"default": "Stoic"},
                ),
                "narrative_environment": (
                    cls._choices(NARRATIVE_ENVIRONMENTS),
                    {"default": "Rain-Soaked Citadel"},
                ),
                "motion_profile": (
                    cls._choices(MOTION_TYPE_OPTIONS),
                    {"default": "Running"},
                ),
                "emotion_tag": (
                    cls._choices(EMOTION_OPTIONS),
                    {"default": "Determination"},
                ),
                "light_source": (
                    cls._choices(LIGHT_SOURCE_OPTIONS),
                    {"default": "Daylight"},
                ),
                "visual_style": (
                    cls._choices(VISUAL_STYLE_OPTIONS),
                    {"default": "Cinematic"},
                ),
                "randomize_missing": ("BOOLEAN", {"default": False}),
                "random_seed": ("INT", {"default": 42, "min": 0, "max": 1_000_000, "step": 1}),
            },
            "optional": {
                "subject_override": ("STRING", {"multiline": True, "default": ""}),
                "environment_override": ("STRING", {"multiline": True, "default": ""}),
                "motion_override": ("STRING", {"multiline": True, "default": ""}),
                "emotion_override": ("STRING", {"multiline": True, "default": ""}),
                "focus_detail": ("STRING", {"multiline": True, "default": "accent lighting, kinetic sparks"}),
                "additional_notes": ("STRING", {"multiline": True, "default": ""}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = (
        "STRING",
        "STRING",
        "STRING",
        "STRING",
        "STRING",
        "STRING",
        "STRING",
    )
    RETURN_NAMES = (
        "subject_focus",
        "scene_setting",
        "motion_arc",
        "narrative_hook",
        "palette_overrides",
        "insight_notes",
        "preset_status",
    )
    FUNCTION = "generate_blueprint"
    CATEGORY = _CATEGORY

    @staticmethod
    def _choices(table: Dict[str, Dict[str, str]]) -> List[str]:
        return list(table.keys()) + ["Randomize", CUSTOM_OPTION]

    def generate_blueprint(
        self,
        character_archetype: str,
        character_profession: str,
        character_temperament: str,
        narrative_environment: str,
        motion_profile: str,
        emotion_tag: str,
        light_source: str,
        visual_style: str,
        randomize_missing: bool,
        random_seed: int,
        subject_override: str = "",
        environment_override: str = "",
        motion_override: str = "",
        emotion_override: str = "",
        focus_detail: str = "",
        additional_notes: str = "",
        preset_action: str = "none",
        preset_name: str = "",
    ) -> Tuple[str, str, str, str, str, str, str]:
        config = {
            "character_archetype": character_archetype,
            "character_profession": character_profession,
            "character_temperament": character_temperament,
            "narrative_environment": narrative_environment,
            "motion_profile": motion_profile,
            "emotion_tag": emotion_tag,
            "light_source": light_source,
            "visual_style": visual_style,
            "randomize_missing": randomize_missing,
            "random_seed": random_seed,
            "subject_override": subject_override,
            "environment_override": environment_override,
            "motion_override": motion_override,
            "emotion_override": emotion_override,
            "focus_detail": focus_detail,
            "additional_notes": additional_notes,
        }

        config, preset_status = self._apply_preset_action(
            "blueprint_generator",
            preset_action,
            preset_name,
            config,
        )

        character_archetype = config.get("character_archetype", character_archetype)
        character_profession = config.get("character_profession", character_profession)
        character_temperament = config.get("character_temperament", character_temperament)
        narrative_environment = config.get("narrative_environment", narrative_environment)
        motion_profile = config.get("motion_profile", motion_profile)
        emotion_tag = config.get("emotion_tag", emotion_tag)
        light_source = config.get("light_source", light_source)
        visual_style = config.get("visual_style", visual_style)
        randomize_missing = bool(config.get("randomize_missing", randomize_missing))
        random_seed = int(config.get("random_seed", random_seed))
        subject_override = config.get("subject_override", subject_override)
        environment_override = config.get("environment_override", environment_override)
        motion_override = config.get("motion_override", motion_override)
        emotion_override = config.get("emotion_override", emotion_override)
        focus_detail = config.get("focus_detail", focus_detail)
        additional_notes = config.get("additional_notes", additional_notes)

        rng = random.Random(random_seed)

        archetype_prompt, archetype_notes, archetype_name = self._resolve_selection(
            character_archetype,
            subject_override,
            CHARACTER_ARCHETYPE_OPTIONS,
            randomize_missing,
            rng,
        )
        profession_prompt, profession_notes, profession_name = self._resolve_selection(
            character_profession,
            subject_override,
            CHARACTER_PROFESSION_OPTIONS,
            randomize_missing,
            rng,
        )
        temperament_prompt, temperament_notes, temperament_name = self._resolve_selection(
            character_temperament,
            subject_override,
            CHARACTER_TEMPERAMENT_OPTIONS,
            randomize_missing,
            rng,
        )
        environment_prompt, environment_notes, environment_name = self._resolve_selection(
            narrative_environment,
            environment_override,
            NARRATIVE_ENVIRONMENTS,
            randomize_missing,
            rng,
        )
        motion_prompt, motion_notes, motion_name = self._resolve_selection(
            motion_profile,
            motion_override,
            MOTION_TYPE_OPTIONS,
            randomize_missing,
            rng,
        )
        emotion_prompt, emotion_notes, emotion_name = self._resolve_selection(
            emotion_tag,
            emotion_override,
            EMOTION_OPTIONS,
            randomize_missing,
            rng,
        )
        light_prompt, light_notes, light_name = self._resolve_selection(
            light_source,
            "",
            LIGHT_SOURCE_OPTIONS,
            randomize_missing,
            rng,
        )
        style_prompt, style_notes, style_name = self._resolve_selection(
            visual_style,
            "",
            VISUAL_STYLE_OPTIONS,
            randomize_missing,
            rng,
        )

        subject_focus = self._combine_fragments(
            [
                archetype_prompt,
                profession_prompt,
                temperament_prompt,
                subject_override,
            ]
        )

        scene_setting = self._combine_fragments(
            [
                environment_prompt,
                environment_override,
                light_prompt,
                focus_detail,
            ]
        )

        motion_arc = motion_override.strip() or motion_prompt
        if motion_arc and motion_arc[-1] not in ".!?":
            motion_arc = f"{motion_arc}."

        narrative_hook = self._combine_fragments(
            [
                environment_notes,
                motion_notes,
                emotion_notes,
                style_prompt,
                additional_notes,
            ],
            separator=" | ",
        )

        palette_overrides = self._build_palette_overrides(light_name, style_name)

        insight_notes = self._build_insight_notes(
            {
                "Archetype": (archetype_name, archetype_notes),
                "Profession": (profession_name, profession_notes),
                "Temperament": (temperament_name, temperament_notes),
                "Environment": (environment_name, environment_notes or environment_prompt),
                "Motion": (motion_name, motion_notes or motion_prompt),
                "Emotion": (emotion_name, emotion_prompt or emotion_notes),
                "Lighting": (light_name, light_notes),
                "Style": (style_name, style_notes or style_prompt),
            }
        )

        if narrative_hook and motion_arc:
            narrative_hook = f"{narrative_hook} | Motion focus: {motion_arc.strip()}"

        return (
            subject_focus,
            scene_setting,
            motion_arc,
            narrative_hook,
            palette_overrides,
            insight_notes,
            preset_status,
        )

    def _resolve_selection(
        self,
        selection: str,
        custom_value: str,
        table: Dict[str, Dict[str, str]],
        randomize_missing: bool,
        rng: random.Random,
    ) -> Tuple[str, str, str]:
        choice = (selection or "").strip()
        if choice == "Randomize":
            choice = rng.choice(list(table.keys()))
        elif randomize_missing and (choice.lower() in {"none", ""}):
            eligible = [name for name in table if name.lower() != "none"] or list(table.keys())
            choice = rng.choice(eligible)
        if choice == CUSTOM_OPTION:
            text = custom_value.strip()
            return text, "", "Custom"
        prompt, notes = _resolve_option(choice, table)
        return prompt, notes, choice

    def _combine_fragments(self, fragments: Sequence[str], separator: str = ", ") -> str:
        cleaned: List[str] = []
        for fragment in fragments:
            if not fragment:
                continue
            stripped = fragment.strip()
            if stripped:
                cleaned.append(stripped)
        merged = separator.join(dict.fromkeys(cleaned))
        return merged

    def _build_palette_overrides(self, light_choice: str, style_choice: str) -> str:
        entries: List[str] = []
        if light_choice and light_choice.lower() not in {"", "none"}:
            entries.append(f"light_source: {light_choice}")
        if style_choice and style_choice.lower() not in {"", "none"}:
            entries.append(f"visual_style: {style_choice}")
        return "\n".join(entries)

    def _build_insight_notes(self, sources: Dict[str, Tuple[str, str]]) -> str:
        lines: List[str] = []
        for label, payload in sources.items():
            name, value = payload
            descriptor = (name or "").strip()
            content = (value or "").strip()
            heading = f"{label}"
            if descriptor and descriptor.lower() not in {"", "none", "custom"}:
                heading = f"{label} ({descriptor})"
            if not content:
                continue
            if content.endswith("."):
                lines.append(f"{heading}: {content}")
            else:
                lines.append(f"{heading}: {content}.")
        return "\n".join(lines)


__all__ = ["NoxPromptBlueprintGenerator"]
