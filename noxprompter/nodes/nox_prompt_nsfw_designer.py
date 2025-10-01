from __future__ import annotations

from typing import Any, Dict, List, Tuple
from ..common import PresetMixin
from ..constants import *  # noqa: F403

class NoxPromptNSFWDesigner(PresetMixin):
    """Assemble mature-oriented prompts with responsible defaults and safeguards."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject_focus": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "Confident adult model with poised expression",
                    },
                ),
                "scene_setting": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "Softly lit studio lounge accented with plush textures",
                    },
                ),
                "pose_profile": (list(NSFW_POSE_PROFILES.keys()), {"default": "Suggestive Pinup"}),
                "wardrobe_style": (
                    list(NSFW_WARDROBE_STYLES.keys()),
                    {"default": "Silk Lingerie"},
                ),
                "tone_profile": (list(NSFW_TONE_MOODS.keys()), {"default": "Glamorous Editorial"}),
            },
            "optional": {
                "lighting_setup": (
                    list(NSFW_LIGHTING_SETUPS.keys()),
                    {"default": "Candlelit Warmth"},
                ),
                "camera_framing": (
                    list(NSFW_CAMERA_FRAMING.keys()),
                    {"default": "Intimate Portrait"},
                ),
                "explicitness_level": (
                    list(NSFW_EXPLICITNESS_LEVELS.keys()),
                    {"default": "Implied Nude"},
                ),
                "set_design": (
                    list(NSFW_SET_DESIGNS.keys()),
                    {"default": "None"},
                ),
                "heat_profile": (
                    list(NSFW_HEAT_LEVELS.keys()),
                    {"default": "Sensual"},
                ),
                "custom_pose_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_pose_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_wardrobe_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_wardrobe_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_tone_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_tone_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_lighting_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_lighting_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_camera_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_camera_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_set_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_set_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_explicitness_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_explicitness_negative": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_explicitness_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_heat_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_heat_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_heat_negative": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "detail_accent": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "soft blemish-free skin, natural curves, respectful staging",
                    },
                ),
                "nsfw_tags": ("STRING", {"multiline": True, "default": "tasteful, mature, confident"}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                "include_negative_baseline": ("BOOLEAN", {"default": True}),
                "include_safety_note": ("BOOLEAN", {"default": True}),
                "custom_safety_note": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt", "negative_prompt", "safety_notes", "preset_status")
    FUNCTION = "design_prompt"
    CATEGORY = "NoxPrompter/NSFW"

    def design_prompt(
        self,
        subject_focus,
        scene_setting,
        pose_profile,
        wardrobe_style,
        tone_profile,
        lighting_setup="Candlelit Warmth",
        camera_framing="Intimate Portrait",
        explicitness_level="Implied Nude",
        set_design="None",
        heat_profile="Sensual",
        detail_accent="",
        nsfw_tags="",
        negative_prompt="",
        include_negative_baseline=True,
        include_safety_note=True,
        custom_pose_prompt="",
        custom_pose_notes="",
        custom_wardrobe_prompt="",
        custom_wardrobe_notes="",
        custom_tone_prompt="",
        custom_tone_notes="",
        custom_lighting_prompt="",
        custom_lighting_notes="",
        custom_camera_prompt="",
        custom_camera_notes="",
        custom_set_prompt="",
        custom_set_notes="",
        custom_explicitness_prompt="",
        custom_explicitness_negative="",
        custom_explicitness_notes="",
        custom_safety_note="",
        custom_heat_prompt="",
        custom_heat_notes="",
        custom_heat_negative="",
        preset_action="none",
        preset_name="",
    ):
        config = {
            "subject_focus": subject_focus,
            "scene_setting": scene_setting,
            "pose_profile": pose_profile,
            "wardrobe_style": wardrobe_style,
            "tone_profile": tone_profile,
            "lighting_setup": lighting_setup,
            "camera_framing": camera_framing,
            "explicitness_level": explicitness_level,
            "set_design": set_design,
            "heat_profile": heat_profile,
            "detail_accent": detail_accent,
            "nsfw_tags": nsfw_tags,
            "negative_prompt": negative_prompt,
            "include_negative_baseline": include_negative_baseline,
            "include_safety_note": include_safety_note,
            "custom_pose_prompt": custom_pose_prompt,
            "custom_pose_notes": custom_pose_notes,
            "custom_wardrobe_prompt": custom_wardrobe_prompt,
            "custom_wardrobe_notes": custom_wardrobe_notes,
            "custom_tone_prompt": custom_tone_prompt,
            "custom_tone_notes": custom_tone_notes,
            "custom_lighting_prompt": custom_lighting_prompt,
            "custom_lighting_notes": custom_lighting_notes,
            "custom_camera_prompt": custom_camera_prompt,
            "custom_camera_notes": custom_camera_notes,
            "custom_set_prompt": custom_set_prompt,
            "custom_set_notes": custom_set_notes,
            "custom_explicitness_prompt": custom_explicitness_prompt,
            "custom_explicitness_negative": custom_explicitness_negative,
            "custom_explicitness_notes": custom_explicitness_notes,
            "custom_safety_note": custom_safety_note,
            "custom_heat_prompt": custom_heat_prompt,
            "custom_heat_notes": custom_heat_notes,
            "custom_heat_negative": custom_heat_negative,
        }

        config, preset_status = self._apply_preset_action(
            "nsfw_designer",
            preset_action,
            preset_name,
            config,
        )

        subject_focus = config.get("subject_focus", subject_focus)
        scene_setting = config.get("scene_setting", scene_setting)
        pose_profile = config.get("pose_profile", pose_profile)
        wardrobe_style = config.get("wardrobe_style", wardrobe_style)
        tone_profile = config.get("tone_profile", tone_profile)
        lighting_setup = config.get("lighting_setup", lighting_setup)
        camera_framing = config.get("camera_framing", camera_framing)
        explicitness_level = config.get("explicitness_level", explicitness_level)
        set_design = config.get("set_design", set_design)
        heat_profile = config.get("heat_profile", heat_profile)
        detail_accent = config.get("detail_accent", detail_accent)
        nsfw_tags = config.get("nsfw_tags", nsfw_tags)
        negative_prompt = config.get("negative_prompt", negative_prompt)
        include_negative_baseline = bool(config.get("include_negative_baseline", include_negative_baseline))
        include_safety_note = bool(config.get("include_safety_note", include_safety_note))
        custom_pose_prompt = config.get("custom_pose_prompt", custom_pose_prompt)
        custom_pose_notes = config.get("custom_pose_notes", custom_pose_notes)
        custom_wardrobe_prompt = config.get("custom_wardrobe_prompt", custom_wardrobe_prompt)
        custom_wardrobe_notes = config.get("custom_wardrobe_notes", custom_wardrobe_notes)
        custom_tone_prompt = config.get("custom_tone_prompt", custom_tone_prompt)
        custom_tone_notes = config.get("custom_tone_notes", custom_tone_notes)
        custom_lighting_prompt = config.get("custom_lighting_prompt", custom_lighting_prompt)
        custom_lighting_notes = config.get("custom_lighting_notes", custom_lighting_notes)
        custom_camera_prompt = config.get("custom_camera_prompt", custom_camera_prompt)
        custom_camera_notes = config.get("custom_camera_notes", custom_camera_notes)
        custom_set_prompt = config.get("custom_set_prompt", custom_set_prompt)
        custom_set_notes = config.get("custom_set_notes", custom_set_notes)
        custom_explicitness_prompt = config.get("custom_explicitness_prompt", custom_explicitness_prompt)
        custom_explicitness_negative = config.get("custom_explicitness_negative", custom_explicitness_negative)
        custom_explicitness_notes = config.get("custom_explicitness_notes", custom_explicitness_notes)
        custom_safety_note = config.get("custom_safety_note", custom_safety_note)
        custom_heat_prompt = config.get("custom_heat_prompt", custom_heat_prompt)
        custom_heat_notes = config.get("custom_heat_notes", custom_heat_notes)
        custom_heat_negative = config.get("custom_heat_negative", custom_heat_negative)

        pose_cfg = self._resolve_nsfw_option(
            pose_profile,
            NSFW_POSE_PROFILES,
            custom_prompt=custom_pose_prompt,
            custom_notes=custom_pose_notes,
        )
        wardrobe_cfg = self._resolve_nsfw_option(
            wardrobe_style,
            NSFW_WARDROBE_STYLES,
            custom_prompt=custom_wardrobe_prompt,
            custom_notes=custom_wardrobe_notes,
        )
        tone_cfg = self._resolve_nsfw_option(
            tone_profile,
            NSFW_TONE_MOODS,
            custom_prompt=custom_tone_prompt,
            custom_notes=custom_tone_notes,
        )
        lighting_cfg = self._resolve_nsfw_option(
            lighting_setup,
            NSFW_LIGHTING_SETUPS,
            custom_prompt=custom_lighting_prompt,
            custom_notes=custom_lighting_notes,
        )
        camera_cfg = self._resolve_nsfw_option(
            camera_framing,
            NSFW_CAMERA_FRAMING,
            custom_prompt=custom_camera_prompt,
            custom_notes=custom_camera_notes,
        )
        explicit_cfg = self._resolve_nsfw_option(
            explicitness_level,
            NSFW_EXPLICITNESS_LEVELS,
            custom_prompt=custom_explicitness_prompt,
            custom_notes=custom_explicitness_notes,
            custom_negative=custom_explicitness_negative,
        )
        set_cfg = self._resolve_nsfw_option(
            set_design,
            NSFW_SET_DESIGNS,
            custom_prompt=custom_set_prompt,
            custom_notes=custom_set_notes,
        )
        heat_cfg = self._resolve_nsfw_option(
            heat_profile,
            NSFW_HEAT_LEVELS,
            custom_prompt=custom_heat_prompt,
            custom_notes=custom_heat_notes,
            custom_negative=custom_heat_negative,
        )

        fragments = []

        subject_clause_parts = [subject_focus.strip()]
        if tone_cfg.get("prompt"):
            subject_clause_parts.append(tone_cfg["prompt"])
        if explicit_cfg.get("prompt"):
            subject_clause_parts.append(explicit_cfg["prompt"])
        if heat_cfg.get("prompt"):
            subject_clause_parts.append(heat_cfg["prompt"])
        subject_clause = ", ".join(part for part in subject_clause_parts if part)
        if subject_clause:
            fragments.append(subject_clause)

        scene_fragments = []
        if scene_setting.strip():
            scene_fragments.append(scene_setting.strip())
        set_prompt_text = set_cfg.get("prompt")
        if set_prompt_text:
            scene_fragments.append(set_prompt_text)
        if scene_fragments:
            fragments.append(". ".join(scene_fragments))

        descriptive_chunks = [
            pose_cfg.get("prompt", ""),
            wardrobe_cfg.get("prompt", ""),
            lighting_cfg.get("prompt", ""),
            camera_cfg.get("prompt", ""),
        ]
        if detail_accent.strip():
            descriptive_chunks.append(detail_accent.strip())
        descriptive_line = ", ".join(chunk for chunk in descriptive_chunks if chunk)
        if descriptive_line:
            fragments.append(descriptive_line)

        tag_list = self._split_keywords(nsfw_tags)
        if tag_list:
            fragments.append(f"Keywords: {', '.join(tag_list)}")

        prompt_text = self._assemble_sentences(fragments)

        negative_terms = []
        if include_negative_baseline:
            negative_terms.extend(NSFW_BASELINE_NEGATIVES)
        explicit_negative = self._split_keywords(explicit_cfg.get("negative", ""))
        negative_terms.extend(explicit_negative)
        heat_negative = self._split_keywords(heat_cfg.get("negative", ""))
        negative_terms.extend(heat_negative)
        negative_terms.extend(self._split_keywords(negative_prompt))
        negative_terms = list(dict.fromkeys(term.strip() for term in negative_terms if term.strip()))
        negative_text = ", ".join(negative_terms)

        safety_parts = []
        if include_safety_note:
            safety_parts.append(NSFW_DEFAULT_SAFETY_NOTE)
        notes_sources = [
            pose_cfg.get("notes"),
            wardrobe_cfg.get("notes"),
            tone_cfg.get("notes"),
            lighting_cfg.get("notes"),
            camera_cfg.get("notes"),
            explicit_cfg.get("notes"),
            set_cfg.get("notes"),
            heat_cfg.get("notes"),
        ]
        curated_notes = [note for note in notes_sources if note]
        if curated_notes:
            safety_parts.extend(list(dict.fromkeys(curated_notes)))
        if custom_safety_note.strip():
            safety_parts.append(custom_safety_note.strip())
        safety_notes = " | ".join(part for part in safety_parts if part)

        return (prompt_text, negative_text, safety_notes, preset_status)

    def _assemble_sentences(self, fragments):
        sentences = []
        for fragment in fragments:
            segment = fragment.strip()
            if not segment:
                continue
            if segment[-1] not in ".!?":
                segment = f"{segment}."
            sentences.append(segment)
        return " ".join(sentences)

    def _split_keywords(self, text):
        if not text:
            return []
        separators = [",", "\n", ";"]
        tokens = [text]
        for sep in separators:
            expanded = []
            for token in tokens:
                expanded.extend(token.split(sep))
            tokens = expanded
        return [token.strip() for token in tokens if token.strip()]

    def _resolve_nsfw_option(
        self,
        selection,
        options,
        *,
        custom_prompt="",
        custom_notes="",
        custom_negative=None,
    ):
        key = self._match_option_key(selection, options)
        fallback_key = "None" if "None" in options else next(iter(options))
        source_key = key or fallback_key
        base = dict(options.get(source_key, {}))

        prompt_parts = [part.strip() for part in [base.get("prompt", ""), custom_prompt] if part and part.strip()]
        base["prompt"] = ", ".join(dict.fromkeys(prompt_parts)) if prompt_parts else ""

        notes_parts = [part.strip() for part in [base.get("notes", ""), custom_notes] if part and part.strip()]
        if notes_parts:
            base["notes"] = " | ".join(dict.fromkeys(notes_parts))
        elif "notes" in base:
            base["notes"] = base.get("notes", "")

        if custom_negative is not None:
            negative_parts = [part.strip() for part in [base.get("negative", ""), custom_negative] if part and part.strip()]
            base["negative"] = ", ".join(dict.fromkeys(negative_parts)) if negative_parts else ""

        return base

    def _match_option_key(self, selection, options):
        normalized = (selection or "").strip()
        if not normalized:
            return None
        lookup = normalized.lower()
        for key in options.keys():
            if key.lower() == lookup:
                return key
        return None

__all__ = ["NoxPromptNSFWDesigner"]
