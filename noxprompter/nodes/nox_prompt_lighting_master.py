from __future__ import annotations

from ..common import PresetMixin, _resolve_option, option_keys
from ..constants import (
    LIGHT_SOURCE_OPTIONS,
    LIGHT_QUALITY_OPTIONS,
    LIGHTING_ATMOSPHERE_OPTIONS,
    LIGHTING_BACKLIGHT_OPTIONS,
    LIGHTING_BLUEPRINT_OPTIONS,
    LIGHTING_COLOR_GEL_OPTIONS,
    LIGHTING_ENERGY_LEVEL_OPTIONS,
    LIGHTING_FILL_STYLE_OPTIONS,
    LIGHTING_KEY_STYLE_OPTIONS,
    LIGHTING_PRACTICAL_OPTIONS,
    LIGHTING_SAFETY_NOTES,
    LIGHTING_SPECIAL_TECHNIQUES,
    TIME_OF_DAY_OPTIONS,
)

class NoxPromptLightingMaster(PresetMixin):
    """Construct cinematic lighting blueprints with mood and safety notes."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "custom_prompt": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                    },
                ),
                "blueprint": (
                    option_keys(LIGHTING_BLUEPRINT_OPTIONS),
                    {"default": "Three-Point"},
                ),
                "key_style": (
                    option_keys(LIGHTING_KEY_STYLE_OPTIONS),
                    {"default": "Softbox Key"},
                ),
            },
            "optional": {
                "light_source": (
                    option_keys(LIGHT_SOURCE_OPTIONS),
                    {"default": "Daylight"},
                ),
                "light_quality": (
                    option_keys(LIGHT_QUALITY_OPTIONS),
                    {"default": "Soft Light"},
                ),
                "time_of_day": (
                    option_keys(TIME_OF_DAY_OPTIONS),
                    {"default": "Dusk"},
                ),
                "fill_style": (
                    option_keys(LIGHTING_FILL_STYLE_OPTIONS),
                    {"default": "Soft Fill"},
                ),
                "backlight": (
                    option_keys(LIGHTING_BACKLIGHT_OPTIONS),
                    {"default": "Rim Strip"},
                ),
                "practical": (
                    option_keys(LIGHTING_PRACTICAL_OPTIONS),
                    {"default": "Lantern Cluster"},
                ),
                "atmosphere": (
                    option_keys(LIGHTING_ATMOSPHERE_OPTIONS),
                    {"default": "Haze"},
                ),
                "color_gel": (
                    option_keys(LIGHTING_COLOR_GEL_OPTIONS),
                    {"default": "Teal & Orange"},
                ),
                "special_technique": (
                    option_keys(LIGHTING_SPECIAL_TECHNIQUES),
                    {"default": "Shutter Drag"},
                ),
                "energy_level": (
                    option_keys(LIGHTING_ENERGY_LEVEL_OPTIONS),
                    {"default": "Dynamic"},
                ),
                "safety_profile": (
                    option_keys(LIGHTING_SAFETY_NOTES),
                    {"default": "None"},
                ),
                "subject_description": ("STRING", {"multiline": True, "default": ""}),
                "environment_description": ("STRING", {"multiline": True, "default": ""}),
                "accent_notes": ("STRING", {"multiline": True, "default": ""}),
                "camera_notes": ("STRING", {"multiline": True, "default": ""}),
                "intensity_bias": ("FLOAT", {"default": 0.6, "min": 0.0, "max": 1.0, "step": 0.05}),
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
    custom_prompt: str,
    blueprint: str = "Three-Point",
    key_style: str = "Softbox Key",
    light_source: str = "Daylight",
    light_quality: str = "Soft Light",
    time_of_day: str = "Dusk",
    fill_style: str = "Soft Fill",
    backlight: str = "Rim Strip",
    practical: str = "Lantern Cluster",
    atmosphere: str = "Haze",
    color_gel: str = "Teal & Orange",
    special_technique: str = "Shutter Drag",
    energy_level: str = "Dynamic",
    safety_profile: str = "None",
        subject_description="",
        environment_description="",
        accent_notes="",
        camera_notes="",
        intensity_bias=0.6,
        preset_action="none",
        preset_name="",
    ):
        config = {
            "custom_prompt": custom_prompt,
            "blueprint": blueprint,
            "key_style": key_style,
            "light_source": light_source,
            "light_quality": light_quality,
            "time_of_day": time_of_day,
            "fill_style": fill_style,
            "backlight": backlight,
            "practical": practical,
            "atmosphere": atmosphere,
            "color_gel": color_gel,
            "special_technique": special_technique,
            "energy_level": energy_level,
            "safety_profile": safety_profile,
            "subject_description": subject_description,
            "environment_description": environment_description,
            "accent_notes": accent_notes,
            "camera_notes": camera_notes,
            "intensity_bias": intensity_bias,
        }

        config, preset_status = self._apply_preset_action(
            "lighting_master",
            preset_action,
            preset_name,
            config,
        )

        custom_prompt = config.get("custom_prompt", custom_prompt)
        blueprint = config.get("blueprint", blueprint)
        key_style = config.get("key_style", key_style)
        fill_style = config.get("fill_style", fill_style)
        backlight = config.get("backlight", backlight)
        practical = config.get("practical", practical)
        atmosphere = config.get("atmosphere", atmosphere)
        color_gel = config.get("color_gel", color_gel)
        special_technique = config.get("special_technique", special_technique)
        energy_level = config.get("energy_level", energy_level)
        safety_profile = config.get("safety_profile", safety_profile)
        light_source = config.get("light_source", light_source)
        light_quality = config.get("light_quality", light_quality)
        time_of_day = config.get("time_of_day", time_of_day)
        subject_description = config.get("subject_description", subject_description)
        environment_description = config.get("environment_description", environment_description)
        accent_notes = config.get("accent_notes", accent_notes)
        camera_notes = config.get("camera_notes", camera_notes)
        intensity_bias = float(config.get("intensity_bias", intensity_bias))
        blueprint_prompt, blueprint_notes = _resolve_option(blueprint, LIGHTING_BLUEPRINT_OPTIONS)
        key_prompt, key_notes = _resolve_option(key_style, LIGHTING_KEY_STYLE_OPTIONS)
        source_prompt, source_notes = _resolve_option(light_source, LIGHT_SOURCE_OPTIONS)
        quality_prompt, quality_notes = _resolve_option(light_quality, LIGHT_QUALITY_OPTIONS)
        time_prompt, time_notes = _resolve_option(time_of_day, TIME_OF_DAY_OPTIONS)
        fill_prompt, fill_notes = _resolve_option(fill_style, LIGHTING_FILL_STYLE_OPTIONS)
        back_prompt, back_notes = _resolve_option(backlight, LIGHTING_BACKLIGHT_OPTIONS)
        practical_prompt, practical_notes = _resolve_option(practical, LIGHTING_PRACTICAL_OPTIONS)
        atmosphere_prompt, atmosphere_notes = _resolve_option(atmosphere, LIGHTING_ATMOSPHERE_OPTIONS)
        gel_prompt, gel_notes = _resolve_option(color_gel, LIGHTING_COLOR_GEL_OPTIONS)
        technique_prompt, technique_notes = _resolve_option(special_technique, LIGHTING_SPECIAL_TECHNIQUES)
        energy_prompt, energy_notes = _resolve_option(energy_level, LIGHTING_ENERGY_LEVEL_OPTIONS)

        intensity_text = self._describe_intensity(intensity_bias)

        lighting_fragments = [
            (custom_prompt or "").strip(),
            source_prompt,
            quality_prompt,
            time_prompt,
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
            f"Source: {source_notes}" if source_notes else "",
            f"Quality: {quality_notes}" if quality_notes else "",
            f"Time: {time_notes}" if time_notes else "",
            f"Blueprint: {blueprint_notes}" if blueprint_notes else "",
            f"Key: {key_notes}" if key_notes else "",
            f"Fill: {fill_notes}" if fill_notes else "",
            f"Backlight: {back_notes}" if back_notes else "",
            f"Practical: {practical_notes}" if practical_notes else "",
            f"Atmosphere: {atmosphere_notes}" if atmosphere_notes else "",
            f"Gel: {gel_notes}" if gel_notes else "",
            f"Technique: {technique_notes}" if technique_notes else "",
            f"Energy: {energy_notes}" if energy_notes else "",
            f"Camera: {camera_notes}" if camera_notes else "",
        ]
        mood_notes = " | ".join(section for section in mood_sections if section)

        technical_sections = []
        if technique_prompt:
            technical_sections.append(f"Technique: {technique_prompt}")
        if technique_notes:
            technical_sections.append(f"Technique Notes: {technique_notes}")
        if energy_prompt:
            technical_sections.append(f"Energy Mode: {energy_prompt}")
        if camera_notes:
            technical_sections.append(f"Camera Notes: {camera_notes}")
        if safety_profile and safety_profile != "None":
            safety_label = safety_profile.strip()
            safety_text = (LIGHTING_SAFETY_NOTES.get(safety_profile, "") or "").strip()
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
