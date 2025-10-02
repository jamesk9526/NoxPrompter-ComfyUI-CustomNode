from __future__ import annotations

from typing import Dict, List, cast

from ..common import PresetMixin, _format_notes, _resolve_with_custom, _split_tokens
from ..constants import (
    CAMERA_ADVANCED_OPTIONS,
    CAMERA_BASIC_OPTIONS,
    COLOR_TONE_OPTIONS,
    COMPOSITION_OPTIONS,
    CUSTOM_OPTION,
    LIGHTING_CAM_SETTINGS,
    LENS_ANGLE_OPTIONS,
    LENS_FOCAL_OPTIONS,
    LENS_TYPE_OPTIONS,
    MOTION_TYPE_OPTIONS,
    SHOT_SIZE_OPTIONS,
    SPECIAL_EFFECT_OPTIONS,
    TIME_OF_DAY_OPTIONS,
    VISUAL_STYLE_OPTIONS,
)


class NoxPromptCameraMaster(PresetMixin):
    """Aggregate every camera-related option into a single configurable node."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "shot_size": (list(SHOT_SIZE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Medium Shot"}),
                "lens_angle": (list(LENS_ANGLE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Three-Quarter"}),
                "camera_basic": (list(CAMERA_BASIC_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Dolly In"}),
            },
            "optional": {
                "lens_focal": (list(LENS_FOCAL_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Medium"}),
                "lens_type": (list(LENS_TYPE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Single Shot"}),
                "composition": (list(COMPOSITION_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Balanced"}),
                "time_of_day": (list(TIME_OF_DAY_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "None"}),
                "motion_type": (list(MOTION_TYPE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "None"}),
                "camera_advanced": (list(CAMERA_ADVANCED_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Steadicam Glide"}),
                "camera_rig": (list(LIGHTING_CAM_SETTINGS.keys()) + [CUSTOM_OPTION], {"default": "Cinematic"}),
                "special_effect": (list(SPECIAL_EFFECT_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "None"}),
                "color_tone": (list(COLOR_TONE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "None"}),
                "visual_style": (list(VISUAL_STYLE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "None"}),
                "focus_subject": ("STRING", {"multiline": True, "default": ""}),
                "focus_environment": ("STRING", {"multiline": True, "default": ""}),
                "movement_beats": ("STRING", {"multiline": True, "default": ""}),
                "camera_motions": ("STRING", {"multiline": True, "default": ""}),
                "accent_keywords": ("STRING", {"multiline": True, "default": ""}),
                "camera_language": ("STRING", {"multiline": True, "default": ""}),
                "rig_support": ("STRING", {"multiline": True, "default": "stabilized gimbal team"}),
                "safety_considerations": ("STRING", {"multiline": True, "default": "confirm clearance paths and harness checks"}),
                "additional_notes": ("STRING", {"multiline": True, "default": ""}),
                "shot_size_custom": ("STRING", {"multiline": True, "default": ""}),
                "lens_angle_custom": ("STRING", {"multiline": True, "default": ""}),
                "camera_basic_custom": ("STRING", {"multiline": True, "default": ""}),
                "lens_focal_custom": ("STRING", {"multiline": True, "default": ""}),
                "lens_type_custom": ("STRING", {"multiline": True, "default": ""}),
                "composition_custom": ("STRING", {"multiline": True, "default": ""}),
                "time_of_day_custom": ("STRING", {"multiline": True, "default": ""}),
                "motion_type_custom": ("STRING", {"multiline": True, "default": ""}),
                "camera_advanced_custom": ("STRING", {"multiline": True, "default": ""}),
                "camera_rig_custom": ("STRING", {"multiline": True, "default": ""}),
                "special_effect_custom": ("STRING", {"multiline": True, "default": ""}),
                "color_tone_custom": ("STRING", {"multiline": True, "default": ""}),
                "visual_style_custom": ("STRING", {"multiline": True, "default": ""}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("camera_prompt", "framing_summary", "rigging_notes", "preset_status")
    FUNCTION = "compose"
    CATEGORY = "NoxPrompter/Camera"

    def compose(
        self,
        shot_size,
        lens_angle,
        camera_basic,
        lens_focal="Medium",
        lens_type="Single Shot",
        composition="Balanced",
        time_of_day="None",
        motion_type="None",
        camera_advanced="Steadicam Glide",
        camera_rig="Cinematic",
        special_effect="None",
        color_tone="None",
        visual_style="None",
        focus_subject="",
        focus_environment="",
        movement_beats="",
        camera_motions="",
        accent_keywords="",
        camera_language="",
        rig_support="stabilized gimbal team",
        safety_considerations="confirm clearance paths and harness checks",
        additional_notes="",
        shot_size_custom="",
        lens_angle_custom="",
        camera_basic_custom="",
        lens_focal_custom="",
        lens_type_custom="",
        composition_custom="",
        time_of_day_custom="",
        motion_type_custom="",
        camera_advanced_custom="",
        camera_rig_custom="",
        special_effect_custom="",
        color_tone_custom="",
        visual_style_custom="",
        preset_action="none",
        preset_name="",
    ):
        config: Dict[str, str] = {
            "shot_size": shot_size,
            "lens_angle": lens_angle,
            "camera_basic": camera_basic,
            "lens_focal": lens_focal,
            "lens_type": lens_type,
            "composition": composition,
            "time_of_day": time_of_day,
            "motion_type": motion_type,
            "camera_advanced": camera_advanced,
            "camera_rig": camera_rig,
            "special_effect": special_effect,
            "color_tone": color_tone,
            "visual_style": visual_style,
            "focus_subject": focus_subject,
            "focus_environment": focus_environment,
            "movement_beats": movement_beats,
            "camera_motions": camera_motions,
            "accent_keywords": accent_keywords,
            "camera_language": camera_language,
            "rig_support": rig_support,
            "safety_considerations": safety_considerations,
            "additional_notes": additional_notes,
            "shot_size_custom": shot_size_custom,
            "lens_angle_custom": lens_angle_custom,
            "camera_basic_custom": camera_basic_custom,
            "lens_focal_custom": lens_focal_custom,
            "lens_type_custom": lens_type_custom,
            "composition_custom": composition_custom,
            "time_of_day_custom": time_of_day_custom,
            "motion_type_custom": motion_type_custom,
            "camera_advanced_custom": camera_advanced_custom,
            "camera_rig_custom": camera_rig_custom,
            "special_effect_custom": special_effect_custom,
            "color_tone_custom": color_tone_custom,
            "visual_style_custom": visual_style_custom,
        }

        config, preset_status = self._apply_preset_action(
            "camera_language",
            preset_action,
            preset_name,
            config,
        )

        shot_size = cast(str, config.get("shot_size", shot_size))
        lens_angle = cast(str, config.get("lens_angle", lens_angle))
        camera_basic = cast(str, config.get("camera_basic", camera_basic))
        lens_focal = cast(str, config.get("lens_focal", lens_focal))
        lens_type = cast(str, config.get("lens_type", lens_type))
        composition = cast(str, config.get("composition", composition))
        time_of_day = cast(str, config.get("time_of_day", time_of_day))
        motion_type = cast(str, config.get("motion_type", motion_type))
        camera_advanced = cast(str, config.get("camera_advanced", camera_advanced))
        camera_rig = cast(str, config.get("camera_rig", camera_rig))
        special_effect = cast(str, config.get("special_effect", special_effect))
        color_tone = cast(str, config.get("color_tone", color_tone))
        visual_style = cast(str, config.get("visual_style", visual_style))
        focus_subject = cast(str, config.get("focus_subject", focus_subject))
        focus_environment = cast(str, config.get("focus_environment", focus_environment))
        movement_beats = cast(str, config.get("movement_beats", movement_beats))
        camera_motions = cast(str, config.get("camera_motions", camera_motions))
        accent_keywords = cast(str, config.get("accent_keywords", accent_keywords))
        camera_language = cast(str, config.get("camera_language", camera_language))
        rig_support = cast(str, config.get("rig_support", rig_support))
        safety_considerations = cast(str, config.get("safety_considerations", safety_considerations))
        additional_notes = cast(str, config.get("additional_notes", additional_notes))
        shot_size_custom = cast(str, config.get("shot_size_custom", shot_size_custom))
        lens_angle_custom = cast(str, config.get("lens_angle_custom", lens_angle_custom))
        camera_basic_custom = cast(str, config.get("camera_basic_custom", camera_basic_custom))
        lens_focal_custom = cast(str, config.get("lens_focal_custom", lens_focal_custom))
        lens_type_custom = cast(str, config.get("lens_type_custom", lens_type_custom))
        composition_custom = cast(str, config.get("composition_custom", composition_custom))
        time_of_day_custom = cast(str, config.get("time_of_day_custom", time_of_day_custom))
        motion_type_custom = cast(str, config.get("motion_type_custom", motion_type_custom))
        camera_advanced_custom = cast(str, config.get("camera_advanced_custom", camera_advanced_custom))
        camera_rig_custom = cast(str, config.get("camera_rig_custom", camera_rig_custom))
        special_effect_custom = cast(str, config.get("special_effect_custom", special_effect_custom))
        color_tone_custom = cast(str, config.get("color_tone_custom", color_tone_custom))
        visual_style_custom = cast(str, config.get("visual_style_custom", visual_style_custom))

        shot_prompt, shot_notes = _resolve_with_custom(shot_size, shot_size_custom, SHOT_SIZE_OPTIONS)
        angle_prompt, angle_notes = _resolve_with_custom(lens_angle, lens_angle_custom, LENS_ANGLE_OPTIONS)
        basic_prompt, basic_notes = _resolve_with_custom(camera_basic, camera_basic_custom, CAMERA_BASIC_OPTIONS)
        focal_prompt, focal_notes = _resolve_with_custom(lens_focal, lens_focal_custom, LENS_FOCAL_OPTIONS)
        lens_type_prompt, lens_type_notes = _resolve_with_custom(lens_type, lens_type_custom, LENS_TYPE_OPTIONS)
        composition_prompt, composition_notes = _resolve_with_custom(composition, composition_custom, COMPOSITION_OPTIONS)
        time_prompt, time_notes = _resolve_with_custom(time_of_day, time_of_day_custom, TIME_OF_DAY_OPTIONS)
        motion_prompt, motion_notes = _resolve_with_custom(motion_type, motion_type_custom, MOTION_TYPE_OPTIONS)
        advanced_prompt, advanced_notes = _resolve_with_custom(camera_advanced, camera_advanced_custom, CAMERA_ADVANCED_OPTIONS)
        rig_prompt, rig_notes = _resolve_with_custom(camera_rig, camera_rig_custom, LIGHTING_CAM_SETTINGS)
        fx_prompt, fx_notes = _resolve_with_custom(special_effect, special_effect_custom, SPECIAL_EFFECT_OPTIONS)
        tone_prompt, tone_notes = _resolve_with_custom(color_tone, color_tone_custom, COLOR_TONE_OPTIONS)
        style_prompt, style_notes = _resolve_with_custom(visual_style, visual_style_custom, VISUAL_STYLE_OPTIONS)

        movement_tokens = _split_tokens(movement_beats)
        motion_tokens = _split_tokens(camera_motions)
        accent_tokens = _split_tokens(accent_keywords)

        camera_fragments: List[str] = [
            shot_prompt,
            angle_prompt,
            focal_prompt,
            lens_type_prompt,
            composition_prompt,
            time_prompt,
            basic_prompt,
            advanced_prompt,
            rig_prompt,
            motion_prompt,
            fx_prompt,
            tone_prompt,
            style_prompt,
        ]

        if focus_subject.strip():
            camera_fragments.append(f"subject focus: {focus_subject.strip()}")
        if focus_environment.strip():
            camera_fragments.append(f"environment focus: {focus_environment.strip()}")
        if movement_tokens:
            camera_fragments.append("movement beats: " + ", ".join(movement_tokens))
        if motion_tokens:
            camera_fragments.append("camera motions: " + ", ".join(motion_tokens))
        if accent_tokens:
            camera_fragments.append("accent keywords: " + ", ".join(accent_tokens))
        if camera_language.strip():
            camera_fragments.append(camera_language.strip())
        if additional_notes.strip():
            camera_fragments.append(additional_notes.strip())

        camera_prompt = ", ".join(fragment for fragment in camera_fragments if fragment).strip()
        if camera_prompt and camera_prompt[-1] not in ".!?":
            camera_prompt += "."

        summary_sections = [
            _format_notes("Shot", shot_notes, shot_prompt),
            _format_notes("Angle", angle_notes, angle_prompt),
            _format_notes("Lens", focal_notes, focal_prompt),
            _format_notes("Lens Type", lens_type_notes, lens_type_prompt),
            _format_notes("Composition", composition_notes, composition_prompt),
            _format_notes("Time", time_notes, time_prompt),
            _format_notes("Motion", motion_notes, motion_prompt),
            _format_notes("Move", basic_notes, basic_prompt),
            _format_notes("Advanced Move", advanced_notes, advanced_prompt),
            _format_notes("Rig", rig_notes, rig_prompt),
            _format_notes("FX", fx_notes, fx_prompt),
            _format_notes("Tone", tone_notes, tone_prompt),
            _format_notes("Style", style_notes, style_prompt),
        ]
        framing_summary = " | ".join(section for section in summary_sections if section)

        rigging_sections = []
        if rig_support.strip():
            rigging_sections.append(f"Rig support: {rig_support.strip()}")
        if safety_considerations.strip():
            rigging_sections.append(f"Safety: {safety_considerations.strip()}")
        if movement_tokens:
            rigging_sections.append("Movement beats: " + ", ".join(movement_tokens))
        if motion_tokens:
            rigging_sections.append("Camera motions: " + ", ".join(motion_tokens))
        if accent_tokens:
            rigging_sections.append("Accent keywords: " + ", ".join(accent_tokens))
        if camera_language.strip():
            rigging_sections.append(f"Camera language: {camera_language.strip()}")
        if additional_notes.strip():
            rigging_sections.append(additional_notes.strip())

        rigging_notes = "\n".join(f"- {section}" for section in rigging_sections if section)

        return camera_prompt, framing_summary, rigging_notes, preset_status


NoxPromptCameraLanguage = NoxPromptCameraMaster

__all__ = ["NoxPromptCameraMaster", "NoxPromptCameraLanguage"]
