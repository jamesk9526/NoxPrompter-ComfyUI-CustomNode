from __future__ import annotations

from ..common import PresetMixin, _resolve_with_custom, _split_tokens
from ..constants import (
    CUSTOM_OPTION,
    HUMAN_DESIGN_BEAUTY_MARK_OPTIONS,
    HUMAN_DESIGN_BODY_SHAPE_OPTIONS,
    HUMAN_DESIGN_BODY_TYPE_OPTIONS,
    HUMAN_DESIGN_EYE_COLOR_OPTIONS,
    HUMAN_DESIGN_EYE_DETAIL_OPTIONS,
    HUMAN_DESIGN_FACE_OPTIONS,
    HUMAN_DESIGN_GENDER_OPTIONS,
    HUMAN_DESIGN_GENITAL_OPTIONS,
    HUMAN_DESIGN_HAIR_COLOR_OPTIONS,
    HUMAN_DESIGN_HAIR_LENGTH_OPTIONS,
    HUMAN_DESIGN_HAIR_STYLE_OPTIONS,
    HUMAN_DESIGN_HEIGHT_OPTIONS,
    HUMAN_DESIGN_SKIN_DETAIL_OPTIONS,
    HUMAN_DESIGN_SKIN_TONE_OPTIONS,
)

class NoxPromptHumanDesigner(PresetMixin):
    """Curate adult human anatomy and styling breakdowns."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "gender": (list(HUMAN_DESIGN_GENDER_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Adult Woman"}),
                "height": (list(HUMAN_DESIGN_HEIGHT_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Average"}),
                "face_type": (list(HUMAN_DESIGN_FACE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Oval"}),
                "body_type": (list(HUMAN_DESIGN_BODY_TYPE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Athletic"}),
                "body_shape": (list(HUMAN_DESIGN_BODY_SHAPE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Hourglass"}),
            },
            "optional": {
                "hair_length": (list(HUMAN_DESIGN_HAIR_LENGTH_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Shoulder"}),
                "hair_color": (list(HUMAN_DESIGN_HAIR_COLOR_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Deep Brunette"}),
                "hair_style": (list(HUMAN_DESIGN_HAIR_STYLE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Loose Waves"}),
                "eye_detail": (list(HUMAN_DESIGN_EYE_DETAIL_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Almond Focus"}),
                "eye_color": (list(HUMAN_DESIGN_EYE_COLOR_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Amber Luminescence"}),
                "skin_tone": (list(HUMAN_DESIGN_SKIN_TONE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Warm Honey"}),
                "skin_detail": (list(HUMAN_DESIGN_SKIN_DETAIL_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Soft Glow"}),
                "beauty_marks": (list(HUMAN_DESIGN_BEAUTY_MARK_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Bare"}),
                "genital_description": (list(HUMAN_DESIGN_GENITAL_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Discrete"}),
                "accent_features": ("STRING", {"multiline": True, "default": ""}),
                "pose_hint": ("STRING", {"default": ""}),
                "consent_language": ("STRING", {"default": "All subjects depicted are consenting adults aged 18+."}),
                "safety_addendum": ("STRING", {"default": ""}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                "gender_custom": ("STRING", {"default": ""}),
                "height_custom": ("STRING", {"default": ""}),
                "face_type_custom": ("STRING", {"default": ""}),
                "body_type_custom": ("STRING", {"default": ""}),
                "body_shape_custom": ("STRING", {"default": ""}),
                "hair_length_custom": ("STRING", {"default": ""}),
                "hair_color_custom": ("STRING", {"default": ""}),
                "hair_style_custom": ("STRING", {"default": ""}),
                "eye_detail_custom": ("STRING", {"default": ""}),
                "eye_color_custom": ("STRING", {"default": ""}),
                "skin_tone_custom": ("STRING", {"default": ""}),
                "skin_detail_custom": ("STRING", {"default": ""}),
                "beauty_marks_custom": ("STRING", {"default": ""}),
                "genital_description_custom": ("STRING", {"default": ""}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("design_prompt", "feature_sheet", "adult_notes", "preset_status")
    FUNCTION = "design"
    CATEGORY = "NoxPrompter/Human"

    def design(
        self,
        gender,
        height,
        face_type,
        body_type,
        body_shape,
        hair_length="Shoulder",
        hair_color="Deep Brunette",
        hair_style="Loose Waves",
        eye_detail="Almond Focus",
        eye_color="Amber Luminescence",
        skin_tone="Warm Honey",
        skin_detail="Soft Glow",
        beauty_marks="Bare",
        genital_description="Discrete",
        accent_features="",
        pose_hint="",
        consent_language="All subjects depicted are consenting adults aged 18+.",
        safety_addendum="",
        negative_prompt="",
        gender_custom="",
        height_custom="",
        face_type_custom="",
        body_type_custom="",
        body_shape_custom="",
        hair_length_custom="",
        hair_color_custom="",
        hair_style_custom="",
        eye_detail_custom="",
        eye_color_custom="",
        skin_tone_custom="",
        skin_detail_custom="",
        beauty_marks_custom="",
        genital_description_custom="",
        preset_action="none",
        preset_name="",
    ):
        config = {
            "gender": gender,
            "height": height,
            "face_type": face_type,
            "body_type": body_type,
            "body_shape": body_shape,
            "hair_length": hair_length,
            "hair_color": hair_color,
            "hair_style": hair_style,
            "eye_detail": eye_detail,
            "eye_color": eye_color,
            "skin_tone": skin_tone,
            "skin_detail": skin_detail,
            "beauty_marks": beauty_marks,
            "genital_description": genital_description,
            "accent_features": accent_features,
            "pose_hint": pose_hint,
            "consent_language": consent_language,
            "safety_addendum": safety_addendum,
            "negative_prompt": negative_prompt,
            "gender_custom": gender_custom,
            "height_custom": height_custom,
            "face_type_custom": face_type_custom,
            "body_type_custom": body_type_custom,
            "body_shape_custom": body_shape_custom,
            "hair_length_custom": hair_length_custom,
            "hair_color_custom": hair_color_custom,
            "hair_style_custom": hair_style_custom,
            "eye_detail_custom": eye_detail_custom,
            "eye_color_custom": eye_color_custom,
            "skin_tone_custom": skin_tone_custom,
            "skin_detail_custom": skin_detail_custom,
            "beauty_marks_custom": beauty_marks_custom,
            "genital_description_custom": genital_description_custom,
        }

        config, preset_status = self._apply_preset_action(
            "human_designer",
            preset_action,
            preset_name,
            config,
        )

        gender = config.get("gender", gender)
        height = config.get("height", height)
        face_type = config.get("face_type", face_type)
        body_type = config.get("body_type", body_type)
        body_shape = config.get("body_shape", body_shape)
        hair_length = config.get("hair_length", hair_length)
        hair_color = config.get("hair_color", hair_color)
        hair_style = config.get("hair_style", hair_style)
        eye_detail = config.get("eye_detail", eye_detail)
        eye_color = config.get("eye_color", eye_color)
        skin_tone = config.get("skin_tone", skin_tone)
        skin_detail = config.get("skin_detail", skin_detail)
        beauty_marks = config.get("beauty_marks", beauty_marks)
        genital_description = config.get("genital_description", genital_description)
        accent_features = config.get("accent_features", accent_features)
        pose_hint = config.get("pose_hint", pose_hint)
        consent_language = config.get("consent_language", consent_language)
        safety_addendum = config.get("safety_addendum", safety_addendum)
        negative_prompt = config.get("negative_prompt", negative_prompt)
        gender_custom = config.get("gender_custom", gender_custom)
        height_custom = config.get("height_custom", height_custom)
        face_type_custom = config.get("face_type_custom", face_type_custom)
        body_type_custom = config.get("body_type_custom", body_type_custom)
        body_shape_custom = config.get("body_shape_custom", body_shape_custom)
        hair_length_custom = config.get("hair_length_custom", hair_length_custom)
        hair_color_custom = config.get("hair_color_custom", hair_color_custom)
        hair_style_custom = config.get("hair_style_custom", hair_style_custom)
        eye_detail_custom = config.get("eye_detail_custom", eye_detail_custom)
        eye_color_custom = config.get("eye_color_custom", eye_color_custom)
        skin_tone_custom = config.get("skin_tone_custom", skin_tone_custom)
        skin_detail_custom = config.get("skin_detail_custom", skin_detail_custom)
        beauty_marks_custom = config.get("beauty_marks_custom", beauty_marks_custom)
        genital_description_custom = config.get("genital_description_custom", genital_description_custom)

        gender_prompt, gender_notes = _resolve_with_custom(gender, gender_custom, HUMAN_DESIGN_GENDER_OPTIONS)
        height_prompt, height_notes = _resolve_with_custom(height, height_custom, HUMAN_DESIGN_HEIGHT_OPTIONS)
        face_prompt, face_notes = _resolve_with_custom(face_type, face_type_custom, HUMAN_DESIGN_FACE_OPTIONS)
        body_type_prompt, body_type_notes = _resolve_with_custom(body_type, body_type_custom, HUMAN_DESIGN_BODY_TYPE_OPTIONS)
        body_shape_prompt, body_shape_notes = _resolve_with_custom(body_shape, body_shape_custom, HUMAN_DESIGN_BODY_SHAPE_OPTIONS)
        hair_length_prompt, hair_length_notes = _resolve_with_custom(hair_length, hair_length_custom, HUMAN_DESIGN_HAIR_LENGTH_OPTIONS)
        hair_color_prompt, hair_color_notes = _resolve_with_custom(hair_color, hair_color_custom, HUMAN_DESIGN_HAIR_COLOR_OPTIONS)
        hair_style_prompt, hair_style_notes = _resolve_with_custom(hair_style, hair_style_custom, HUMAN_DESIGN_HAIR_STYLE_OPTIONS)
        eye_detail_prompt, eye_detail_notes = _resolve_with_custom(eye_detail, eye_detail_custom, HUMAN_DESIGN_EYE_DETAIL_OPTIONS)
        eye_color_prompt, eye_color_notes = _resolve_with_custom(eye_color, eye_color_custom, HUMAN_DESIGN_EYE_COLOR_OPTIONS)
        skin_tone_prompt, skin_tone_notes = _resolve_with_custom(skin_tone, skin_tone_custom, HUMAN_DESIGN_SKIN_TONE_OPTIONS)
        skin_detail_prompt, skin_detail_notes = _resolve_with_custom(skin_detail, skin_detail_custom, HUMAN_DESIGN_SKIN_DETAIL_OPTIONS)
        beauty_marks_prompt, beauty_marks_notes = _resolve_with_custom(beauty_marks, beauty_marks_custom, HUMAN_DESIGN_BEAUTY_MARK_OPTIONS)
        genital_prompt, genital_notes = _resolve_with_custom(genital_description, genital_description_custom, HUMAN_DESIGN_GENITAL_OPTIONS)

        hair_components = [hair_length_prompt, hair_color_prompt, hair_style_prompt]
        hair_description = ", ".join(part for part in hair_components if part)

        eye_components = [eye_detail_prompt, eye_color_prompt]
        eye_description = ", ".join(part for part in eye_components if part)

        skin_components = [skin_tone_prompt, skin_detail_prompt]
        skin_description = ", ".join(part for part in skin_components if part)

        def _as_sentence(text: str) -> str:
            cleaned = (text or "").strip()
            if not cleaned:
                return ""
            return cleaned if cleaned[-1] in ".!?" else f"{cleaned}."

        core_segments = [gender_prompt, height_prompt, body_type_prompt, body_shape_prompt, face_prompt]
        core_description = ", ".join(part for part in core_segments if part)

        prompt_fragments = []
        if core_description:
            prompt_fragments.append(core_description)
        if skin_description:
            prompt_fragments.append(f"Skin: {skin_description}")
        if eye_description:
            prompt_fragments.append(f"Eyes: {eye_description}")
        if hair_description:
            prompt_fragments.append(f"Hair: {hair_description}")
        if beauty_marks_prompt:
            prompt_fragments.append(f"Beauty marks: {beauty_marks_prompt}")
        if genital_prompt:
            prompt_fragments.append(f"Anatomy: {genital_prompt}")

        accent_tokens = _split_tokens(accent_features)
        if accent_tokens:
            prompt_fragments.append("Accent features: " + ", ".join(dict.fromkeys(accent_tokens)))

        if pose_hint.strip():
            prompt_fragments.append(f"Pose cue: {pose_hint.strip()}")

        design_prompt = " ".join(filter(None, (_as_sentence(fragment) for fragment in prompt_fragments)))

        feature_lines = [
            f"Gender/Sex: {gender_prompt}" if gender_prompt else "",
            f"Height: {height_prompt}" if height_prompt else "",
            f"Face Type: {face_prompt}" if face_prompt else "",
            f"Body Type: {body_type_prompt}" if body_type_prompt else "",
            f"Body Shape: {body_shape_prompt}" if body_shape_prompt else "",
        ]
        if skin_description:
            feature_lines.append(f"Skin: {skin_description}")
        if hair_description:
            feature_lines.append(f"Hair: {hair_description}")
        if eye_description:
            feature_lines.append(f"Eyes: {eye_description}")
        if genital_prompt:
            feature_lines.append(f"Genital Description: {genital_prompt}")
        if beauty_marks_prompt:
            feature_lines.append(f"Beauty Marks: {beauty_marks_prompt}")
        if accent_tokens:
            feature_lines.append("Accent Features: " + ", ".join(dict.fromkeys(accent_tokens)))
        if pose_hint.strip():
            feature_lines.append(f"Pose Cue: {pose_hint.strip()}")
        feature_sheet = " | ".join(line for line in feature_lines if line)

        adult_notes_parts = [
            "All descriptions apply to consenting adults aged 18+.",
            consent_language.strip(),
        ]

        curated_notes = [
            gender_notes,
            height_notes,
            face_notes,
            body_type_notes,
            body_shape_notes,
            hair_length_notes,
            hair_color_notes,
            hair_style_notes,
            eye_detail_notes,
            eye_color_notes,
            skin_tone_notes,
            skin_detail_notes,
            beauty_marks_notes,
            genital_notes,
        ]
        adult_notes_parts.extend(note for note in curated_notes if note)
        if safety_addendum.strip():
            adult_notes_parts.append(safety_addendum.strip())
        if negative_prompt.strip():
            adult_notes_parts.append("Negative Prompt: " + negative_prompt.strip())

        adult_notes = " | ".join(dict.fromkeys(part for part in adult_notes_parts if part))

        return (design_prompt, feature_sheet, adult_notes, preset_status)

__all__ = ["NoxPromptHumanDesigner"]
