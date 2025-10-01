from __future__ import annotations

from typing import Any, Dict, List, Tuple
from ..common import PresetMixin, _resolve_with_custom
from ..constants import *  # noqa: F403

class NoxPromptLightingMaster(PresetMixin):
    """Construct cinematic lighting blueprints with mood and safety notes."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "blueprint": (list(LIGHTING_BLUEPRINT_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Three-Point"}),
                "key_style": (list(LIGHTING_KEY_STYLE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Softbox Key"}),
            },
            "optional": {
                "fill_style": (list(LIGHTING_FILL_STYLE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Soft Fill"}),
                "backlight": (list(LIGHTING_BACKLIGHT_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Rim Strip"}),
                "practical": (list(LIGHTING_PRACTICAL_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Lantern Cluster"}),
                "atmosphere": (list(LIGHTING_ATMOSPHERE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Haze"}),
                "color_gel": (list(LIGHTING_COLOR_GEL_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Teal & Orange"}),
                "camera_settings": (list(LIGHTING_CAM_SETTINGS.keys()) + [CUSTOM_OPTION], {"default": "Cinematic"}),
                "special_technique": (list(LIGHTING_SPECIAL_TECHNIQUES.keys()) + [CUSTOM_OPTION], {"default": "Shutter Drag"}),
                "energy_level": (list(LIGHTING_ENERGY_LEVEL_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Dynamic"}),
                "safety_profile": (list(["None"] + list(LIGHTING_SAFETY_NOTES.keys()) + [CUSTOM_OPTION]), {"default": "None"}),
                "subject_description": ("STRING", {"multiline": True, "default": ""}),
                "environment_description": ("STRING", {"multiline": True, "default": ""}),
                "accent_notes": ("STRING", {"multiline": True, "default": ""}),
                "intensity_bias": ("FLOAT", {"default": 0.6, "min": 0.0, "max": 1.0, "step": 0.05}),
                "blueprint_custom": ("STRING", {"default": ""}),
                "key_style_custom": ("STRING", {"default": ""}),
                "fill_style_custom": ("STRING", {"default": ""}),
                "backlight_custom": ("STRING", {"default": ""}),
                "practical_custom": ("STRING", {"default": ""}),
                "atmosphere_custom": ("STRING", {"default": ""}),
                "color_gel_custom": ("STRING", {"default": ""}),
                "camera_settings_custom": ("STRING", {"default": ""}),
                "special_technique_custom": ("STRING", {"default": ""}),
                "energy_level_custom": ("STRING", {"default": ""}),
                "safety_profile_custom": ("STRING", {"default": ""}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("lighting_prompt", "mood_notes", "technical_notes", "preset_status")
    FUNCTION = "illuminate"
    CATEGORY = "NoxPrompter/Lighting"

    def illuminate(
        self,
        blueprint,
        key_style,
        fill_style="Soft Fill",
        backlight="Rim Strip",
        practical="Lantern Cluster",
        atmosphere="Haze",
        color_gel="Teal & Orange",
        camera_settings="Cinematic",
        special_technique="Shutter Drag",
        energy_level="Dynamic",
        safety_profile="None",
        blueprint_custom="",
        key_style_custom="",
        fill_style_custom="",
        backlight_custom="",
        practical_custom="",
        atmosphere_custom="",
        color_gel_custom="",
        camera_settings_custom="",
        special_technique_custom="",
        energy_level_custom="",
        safety_profile_custom="",
        subject_description="",
        environment_description="",
        accent_notes="",
        intensity_bias=0.6,
        preset_action="none",
        preset_name="",
    ):
        config = {
            "blueprint": blueprint,
            "key_style": key_style,
            "fill_style": fill_style,
            "backlight": backlight,
            "practical": practical,
            "atmosphere": atmosphere,
            "color_gel": color_gel,
            "camera_settings": camera_settings,
            "special_technique": special_technique,
            "energy_level": energy_level,
            "safety_profile": safety_profile,
            "blueprint_custom": blueprint_custom,
            "key_style_custom": key_style_custom,
            "fill_style_custom": fill_style_custom,
            "backlight_custom": backlight_custom,
            "practical_custom": practical_custom,
            "atmosphere_custom": atmosphere_custom,
            "color_gel_custom": color_gel_custom,
            "camera_settings_custom": camera_settings_custom,
            "special_technique_custom": special_technique_custom,
            "energy_level_custom": energy_level_custom,
            "safety_profile_custom": safety_profile_custom,
            "subject_description": subject_description,
            "environment_description": environment_description,
            "accent_notes": accent_notes,
            "intensity_bias": intensity_bias,
        }

        config, preset_status = self._apply_preset_action(
            "lighting_master",
            preset_action,
            preset_name,
            config,
        )

        blueprint = config.get("blueprint", blueprint)
        key_style = config.get("key_style", key_style)
        fill_style = config.get("fill_style", fill_style)
        backlight = config.get("backlight", backlight)
        practical = config.get("practical", practical)
        atmosphere = config.get("atmosphere", atmosphere)
        color_gel = config.get("color_gel", color_gel)
        camera_settings = config.get("camera_settings", camera_settings)
        special_technique = config.get("special_technique", special_technique)
        energy_level = config.get("energy_level", energy_level)
        safety_profile = config.get("safety_profile", safety_profile)
        blueprint_custom = config.get("blueprint_custom", blueprint_custom)
        key_style_custom = config.get("key_style_custom", key_style_custom)
        fill_style_custom = config.get("fill_style_custom", fill_style_custom)
        backlight_custom = config.get("backlight_custom", backlight_custom)
        practical_custom = config.get("practical_custom", practical_custom)
        atmosphere_custom = config.get("atmosphere_custom", atmosphere_custom)
        color_gel_custom = config.get("color_gel_custom", color_gel_custom)
        camera_settings_custom = config.get("camera_settings_custom", camera_settings_custom)
        special_technique_custom = config.get("special_technique_custom", special_technique_custom)
        energy_level_custom = config.get("energy_level_custom", energy_level_custom)
        safety_profile_custom = config.get("safety_profile_custom", safety_profile_custom)
        subject_description = config.get("subject_description", subject_description)
        environment_description = config.get("environment_description", environment_description)
        accent_notes = config.get("accent_notes", accent_notes)
        intensity_bias = float(config.get("intensity_bias", intensity_bias))
        blueprint_prompt, blueprint_notes = _resolve_with_custom(blueprint, blueprint_custom, LIGHTING_BLUEPRINT_OPTIONS)
        key_prompt, key_notes = _resolve_with_custom(key_style, key_style_custom, LIGHTING_KEY_STYLE_OPTIONS)
        fill_prompt, fill_notes = _resolve_with_custom(fill_style, fill_style_custom, LIGHTING_FILL_STYLE_OPTIONS)
        back_prompt, back_notes = _resolve_with_custom(backlight, backlight_custom, LIGHTING_BACKLIGHT_OPTIONS)
        practical_prompt, practical_notes = _resolve_with_custom(practical, practical_custom, LIGHTING_PRACTICAL_OPTIONS)
        atmosphere_prompt, atmosphere_notes = _resolve_with_custom(atmosphere, atmosphere_custom, LIGHTING_ATMOSPHERE_OPTIONS)
        gel_prompt, gel_notes = _resolve_with_custom(color_gel, color_gel_custom, LIGHTING_COLOR_GEL_OPTIONS)
        camera_prompt, camera_notes = _resolve_with_custom(camera_settings, camera_settings_custom, LIGHTING_CAM_SETTINGS)
        technique_prompt, technique_notes = _resolve_with_custom(special_technique, special_technique_custom, LIGHTING_SPECIAL_TECHNIQUES)
        energy_prompt, energy_notes = _resolve_with_custom(energy_level, energy_level_custom, LIGHTING_ENERGY_LEVEL_OPTIONS)

        intensity_text = self._describe_intensity(intensity_bias)

        lighting_fragments = [
            blueprint_prompt,
            key_prompt,
            fill_prompt,
            back_prompt,
            practical_prompt,
            atmosphere_prompt,
            gel_prompt,
            technique_prompt,
            f"energy mode: {energy_prompt}" if energy_prompt else "",
            f"subject: {subject_description.strip()}" if subject_description.strip() else "",
            f"environment: {environment_description.strip()}" if environment_description.strip() else "",
            f"intensity bias: {intensity_text}",
        ]
        lighting_prompt = ", ".join(fragment for fragment in lighting_fragments if fragment).strip()
        if lighting_prompt and lighting_prompt[-1] not in ".!?":
            lighting_prompt += "."
        if accent_notes.strip():
            lighting_prompt += f" Accents: {accent_notes.strip()}"

        mood_sections = [
            f"Blueprint: {blueprint_notes}" if blueprint_notes else "",
            f"Key: {key_notes}" if key_notes else "",
            f"Fill: {fill_notes}" if fill_notes else "",
            f"Backlight: {back_notes}" if back_notes else "",
            f"Practical: {practical_notes}" if practical_notes else "",
            f"Atmosphere: {atmosphere_notes}" if atmosphere_notes else "",
            f"Gel: {gel_notes}" if gel_notes else "",
            f"Technique: {technique_notes}" if technique_notes else "",
            f"Energy: {energy_notes}" if energy_notes else "",
        ]
        mood_notes = " | ".join(section for section in mood_sections if section)

        technical_sections = [camera_prompt]
        if camera_notes:
            technical_sections.append(f"Camera Notes: {camera_notes}")
        safety_label = ""
        safety_text = ""
        if safety_profile == CUSTOM_OPTION:
            safety_label = (safety_profile_custom or "").strip()
            if safety_label:
                safety_text = safety_label
        elif safety_profile and safety_profile != "None":
            safety_label = safety_profile
            safety_text = LIGHTING_SAFETY_NOTES.get(safety_profile, "")
        if safety_label:
            if safety_text and safety_text != safety_label:
                technical_sections.append(f"Safety: {safety_label} — {safety_text}")
            else:
                technical_sections.append(f"Safety: {safety_label}")
        technical_notes = " | ".join(section for section in technical_sections if section)

        return (lighting_prompt, mood_notes, technical_notes, preset_status)

    def _describe_intensity(self, value: float) -> str:
        clamped = max(0.0, min(1.0, value))
        if clamped < 0.2:
            return "featherweight glow"
        if clamped < 0.4:
            return "gentle build"
        if clamped < 0.6:
            return "balanced exposure"
        if clamped < 0.8:
            return "pronounced contrast"
        if clamped < 0.95:
            return "high drama punch"
        return "extreme spectacle"

__all__ = ["NoxPromptLightingMaster"]
