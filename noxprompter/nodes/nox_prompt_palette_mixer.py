from __future__ import annotations

from typing import Any, Dict, List, Tuple
from ..common import PresetMixin
from ..constants import *  # noqa: F403

class NoxPromptPaletteMixer(PresetMixin):
    """Generate palette overrides and keyword clusters for the builder."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mood_profile": (list(PALETTE_PROFILES.keys()), {"default": "Moody Nightfall"}),
                "intensity": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.05}),
            },
            "optional": {
                "include_effects": ("BOOLEAN", {"default": True}),
                "custom_palette": ("STRING", {"multiline": True, "default": ""}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("palette_overrides", "custom_keywords", "notes", "preset_status")
    FUNCTION = "mix_palette"
    CATEGORY = "NoxPrompter/Companions"

    def mix_palette(
        self,
        mood_profile,
        intensity,
        include_effects=True,
        custom_palette="",
        preset_action="none",
        preset_name="",
    ):
        config = {
            "mood_profile": mood_profile,
            "intensity": intensity,
            "include_effects": include_effects,
            "custom_palette": custom_palette,
        }

        config, preset_status = self._apply_preset_action(
            "palette_mixer",
            preset_action,
            preset_name,
            config,
        )

        mood_profile = config.get("mood_profile", "Moody Nightfall")
        intensity = float(config.get("intensity", 0.5))
        include_effects = bool(config.get("include_effects", True))
        custom_palette = config.get("custom_palette", "")

        profile = PALETTE_PROFILES.get(mood_profile)
        if not profile:
            overrides_text = custom_palette.strip()
            custom_keywords = ", ".join(self._split_keywords(custom_palette))
            notes = "Custom palette applied. Profile not found."
            return (overrides_text, custom_keywords, notes, preset_status)

        overrides = {key: list(values) for key, values in profile.get("overrides", {}).items()}

        if intensity >= 0.6:
            for key, values in profile.get("intense_overrides", {}).items():
                overrides.setdefault(key, []).extend(values)

        if include_effects and profile.get("effects"):
            overrides.setdefault("special_effect", []).extend(profile["effects"])

        override_lines = []
        for key, values in overrides.items():
            deduped = list(dict.fromkeys(value for value in values if value))
            if deduped:
                override_lines.append(f"{key}: {', '.join(deduped)}")

        if custom_palette.strip():
            override_lines.append(custom_palette.strip())

        overrides_text = "\n".join(override_lines).strip()

        keywords = list(profile.get("keywords", []))
        if intensity >= 0.6:
            keywords.extend(profile.get("intense_keywords", []))
        if include_effects:
            keywords.extend(profile.get("effect_keywords", []))
        if custom_palette.strip():
            keywords.extend(self._split_keywords(custom_palette))

        keywords = list(dict.fromkeys(kw.strip() for kw in keywords if kw and kw.strip()))
        custom_keywords = ", ".join(keywords)

        notes_parts = [profile.get("description", mood_profile)]
        notes_parts.append(f"Intensity: {intensity:.2f}")
        if include_effects and profile.get("effects"):
            notes_parts.append("Special effects included: " + ", ".join(profile["effects"]))
        if keywords:
            notes_parts.append("Keywords curated for emphasis.")

        return (overrides_text, custom_keywords, " | ".join(notes_parts), preset_status)

    def _split_keywords(self, text):
        if not text:
            return []
        separators = [",", "\n", ";"]
        tokens = [text]
        for sep in separators:
            temp = []
            for token in tokens:
                temp.extend(token.split(sep))
            tokens = temp
        return [token.strip() for token in tokens if token.strip()]

__all__ = ["NoxPromptPaletteMixer"]
