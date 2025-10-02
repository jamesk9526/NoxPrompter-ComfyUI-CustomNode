from __future__ import annotations

import random
import re
from ..common import PresetMixin, PromptFragmentFilter
from ..constants import (
    CAMERA_ADVANCED_OPTIONS,
    CAMERA_BASIC_OPTIONS,
    COLOR_TONE_OPTIONS,
    COMPOSITION_OPTIONS,
    EMOTION_OPTIONS,
    FORMULA_CONFIGS,
    LENS_ANGLE_OPTIONS,
    LENS_FOCAL_OPTIONS,
    LENS_TYPE_OPTIONS,
    LIGHT_QUALITY_OPTIONS,
    LIGHT_SOURCE_OPTIONS,
    MOTION_TYPE_OPTIONS,
    SHOT_SIZE_OPTIONS,
    SPECIAL_EFFECT_OPTIONS,
    TIME_OF_DAY_OPTIONS,
    VISUAL_STYLE_OPTIONS,
)

class NoxPromptBuilder(PresetMixin):
    """Construct prompts using formulas and curated keyword palettes."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "formula": (list(FORMULA_CONFIGS.keys()), {"default": "Advanced Formula"}),
                "subject_focus": ("STRING", {"multiline": True, "default": "Battle-hardened warrior drenched in rain, wearing leather armor and fur"}),
                "scene_setting": ("STRING", {"multiline": True, "default": "Muddy battlefield at night, lightning in the distance, flames flickering"}),
                "motion_arc": ("STRING", {"multiline": True, "default": "Charges forward roaring, swings blade in a slow-motion crash zoom"}),
            },
            "optional": {
                "narrative_hook": ("STRING", {"multiline": True, "default": "Camera locks onto her determined eyes as thunder cracks overhead"}),
                "model_emphasis": ("STRING", {"multiline": True, "default": "Cinematic aesthetic control, precise semantic adherence"}),
                "light_source": (list(LIGHT_SOURCE_OPTIONS.keys()), {"default": "Daylight"}),
                "light_quality": (list(LIGHT_QUALITY_OPTIONS.keys()), {"default": "Soft Light"}),
                "time_of_day": (list(TIME_OF_DAY_OPTIONS.keys()), {"default": "Dusk"}),
                "shot_size": (list(SHOT_SIZE_OPTIONS.keys()), {"default": "Medium Close-up"}),
                "composition": (list(COMPOSITION_OPTIONS.keys()), {"default": "Balanced"}),
                "lens_focal": (list(LENS_FOCAL_OPTIONS.keys()), {"default": "Medium"}),
                "lens_angle": (list(LENS_ANGLE_OPTIONS.keys()), {"default": "None"}),
                "lens_type": (list(LENS_TYPE_OPTIONS.keys()), {"default": "Single Shot"}),
                "camera_basic": (list(CAMERA_BASIC_OPTIONS.keys()), {"default": "None"}),
                "camera_advanced": (list(CAMERA_ADVANCED_OPTIONS.keys()), {"default": "None"}),
                "color_tone": (list(COLOR_TONE_OPTIONS.keys()), {"default": "Warm Tone"}),
                "motion_type": (list(MOTION_TYPE_OPTIONS.keys()), {"default": "Running"}),
                "emotion": (list(EMOTION_OPTIONS.keys()), {"default": "Joy"}),
                "visual_style": (list(VISUAL_STYLE_OPTIONS.keys()), {"default": "Anime"}),
                "special_effect": (list(SPECIAL_EFFECT_OPTIONS.keys()), {"default": "None"}),
                "keyword_style": (["auto", "inline", "compact"], {"default": "auto"}),
                "quality_profile": (["Balanced", "Cinematic", "Minimal", "Narrative"], {"default": "Balanced"}),
                "randomize_missing": ("BOOLEAN", {"default": False}),
                "random_seed": ("INT", {"default": 0, "min": 0, "max": 1_000_000, "step": 1}),
                "palette_overrides": ("STRING", {"multiline": True, "default": ""}),
                "extra_descriptors": ("STRING", {"multiline": True, "default": "Model feature emphasis: complex & dynamic motion"}),
                "lighting_prompt": ("STRING", {"multiline": True, "default": ""}),
                "lighting_summary": ("STRING", {"multiline": True, "default": ""}),
                "lighting_technical_notes": ("STRING", {"multiline": True, "default": ""}),
                "custom_keywords": ("STRING", {"multiline": True, "default": ""}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                "prompt_prefix": ("STRING", {"default": ""}),
                "prompt_suffix": ("STRING", {"default": ""}),
                "camera_prompt": ("STRING", {"multiline": True, "default": ""}),
                "camera_summary": ("STRING", {"multiline": True, "default": ""}),
                "camera_notes": ("STRING", {"multiline": True, "default": ""}),
                "camera_directives": ("STRING", {"multiline": True, "default": ""}),
                "prompt_filter_enabled": ("BOOLEAN", {"default": True}),
                "prompt_filter_profile": (list(sorted(PromptFragmentFilter.PROFILE_PRESETS.keys())), {"default": "balanced"}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt", "negative_prompt", "aesthetic_notes", "dynamic_notes", "preset_status")
    FUNCTION = "build_prompt"
    CATEGORY = "NoxPrompter/Builders"

    def build_prompt(
        self,
        formula,
        subject_focus,
        scene_setting,
        motion_arc,
        narrative_hook="",
        model_emphasis="",
        light_source="Daylight",
        light_quality="Soft Light",
        time_of_day="Dusk",
        shot_size="Medium Close-up",
        composition="Balanced",
        lens_focal="Medium",
        lens_angle="None",
        lens_type="Single Shot",
    camera_basic="None",
    camera_advanced="None",
        color_tone="Warm Tone",
        motion_type="Running",
        emotion="Joy",
        visual_style="Anime",
        special_effect="None",
        keyword_style="auto",
        quality_profile="Balanced",
        randomize_missing=False,
        random_seed=0,
        palette_overrides="",
        extra_descriptors="",
        lighting_prompt="",
        lighting_summary="",
    lighting_technical_notes="",
        custom_keywords="",
        negative_prompt="",
        prompt_prefix="",
        prompt_suffix="",
    camera_prompt="",
    camera_summary="",
    camera_notes="",
        camera_directives="",
        prompt_filter_enabled=True,
        prompt_filter_profile="balanced",
        preset_action="none",
        preset_name="",
    ):
        config = {
            "formula": formula,
            "subject_focus": subject_focus,
            "scene_setting": scene_setting,
            "motion_arc": motion_arc,
            "narrative_hook": narrative_hook,
            "model_emphasis": model_emphasis,
            "light_source": light_source,
            "light_quality": light_quality,
            "time_of_day": time_of_day,
            "shot_size": shot_size,
            "composition": composition,
            "lens_focal": lens_focal,
            "lens_angle": lens_angle,
            "lens_type": lens_type,
            "camera_basic": camera_basic,
            "camera_advanced": camera_advanced,
            "color_tone": color_tone,
            "motion_type": motion_type,
            "emotion": emotion,
            "visual_style": visual_style,
            "special_effect": special_effect,
            "keyword_style": keyword_style,
            "quality_profile": quality_profile,
            "randomize_missing": randomize_missing,
            "random_seed": random_seed,
            "palette_overrides": palette_overrides,
            "extra_descriptors": extra_descriptors,
            "lighting_prompt": lighting_prompt,
            "lighting_summary": lighting_summary,
            "lighting_technical_notes": lighting_technical_notes,
            "custom_keywords": custom_keywords,
            "negative_prompt": negative_prompt,
            "prompt_prefix": prompt_prefix,
            "prompt_suffix": prompt_suffix,
            "camera_prompt": camera_prompt,
            "camera_summary": camera_summary,
            "camera_notes": camera_notes,
            "camera_directives": camera_directives,
            "prompt_filter_enabled": prompt_filter_enabled,
            "prompt_filter_profile": prompt_filter_profile,
        }

        config, preset_status = self._apply_preset_action(
            "prompt_builder",
            preset_action,
            preset_name,
            config,
        )

        formula = config["formula"]
        subject_focus = config["subject_focus"]
        scene_setting = config["scene_setting"]
        motion_arc = config["motion_arc"]
        narrative_hook = config.get("narrative_hook", "")
        model_emphasis = config.get("model_emphasis", "")
        light_source = config.get("light_source", "Daylight")
        light_quality = config.get("light_quality", "Soft Light")
        time_of_day = config.get("time_of_day", "Dusk")
        shot_size = config.get("shot_size", "Medium Close-up")
        composition = config.get("composition", "Balanced")
        lens_focal = config.get("lens_focal", "Medium")
        lens_angle = config.get("lens_angle", "None")
        lens_type = config.get("lens_type", "Single Shot")
        camera_basic = config.get("camera_basic", "None")
        camera_advanced = config.get("camera_advanced", "None")
        color_tone = config.get("color_tone", "Warm Tone")
        motion_type = config.get("motion_type", "Running")
        emotion = config.get("emotion", "Joy")
        visual_style = config.get("visual_style", "Anime")
        special_effect = config.get("special_effect", "None")
        keyword_style = config.get("keyword_style", "auto")
        quality_profile = config.get("quality_profile", "Balanced")
        randomize_missing = bool(config.get("randomize_missing", False))
        random_seed = int(config.get("random_seed", 0))
        palette_overrides = config.get("palette_overrides", "")
        extra_descriptors = config.get("extra_descriptors", "")
        lighting_prompt = config.get("lighting_prompt", lighting_prompt)
        lighting_summary = config.get("lighting_summary", lighting_summary)
        lighting_technical_notes = config.get("lighting_technical_notes", lighting_technical_notes)
        custom_keywords = config.get("custom_keywords", "")
        negative_prompt = config.get("negative_prompt", "")
        prompt_prefix = config.get("prompt_prefix", "")
        prompt_suffix = config.get("prompt_suffix", "")
        camera_prompt = config.get("camera_prompt", camera_prompt)
        camera_summary = config.get("camera_summary", camera_summary)
        camera_notes = config.get("camera_notes", camera_notes)
        camera_directives = config.get("camera_directives", "")
        prompt_filter_enabled = bool(config.get("prompt_filter_enabled", True))
        prompt_filter_profile = config.get("prompt_filter_profile", "balanced")

        formula_config = FORMULA_CONFIGS.get(formula, next(iter(FORMULA_CONFIGS.values())))
        overrides_map, override_custom = self._parse_palette_overrides(palette_overrides)
        rng = random.Random(random_seed) if randomize_missing else None

        prompt_fragments = []

        prefix_fragment = prompt_prefix.strip()
        if prefix_fragment:
            prompt_fragments.append(prefix_fragment)

        subject_clause = subject_focus.strip()
        if model_emphasis.strip():
            emphasis = model_emphasis.strip()
            subject_clause = f"{subject_clause}, {emphasis}" if subject_clause else emphasis
        if subject_clause:
            prompt_fragments.append(subject_clause)

        if scene_setting.strip():
            prompt_fragments.append(scene_setting.strip())

        if motion_arc.strip():
            prompt_fragments.append(motion_arc.strip())

        if narrative_hook.strip():
            prompt_fragments.append(narrative_hook.strip())

        if extra_descriptors.strip():
            prompt_fragments.append(extra_descriptors.strip())

        if lighting_prompt.strip():
            prompt_fragments.append(lighting_prompt.strip())

        if camera_prompt.strip():
            prompt_fragments.append(camera_prompt.strip())

        aesthetic_prompts, aesthetic_summaries = self._collect_category_details(
            [
                ("light_source", light_source, LIGHT_SOURCE_OPTIONS),
                ("light_quality", light_quality, LIGHT_QUALITY_OPTIONS),
                ("time_of_day", time_of_day, TIME_OF_DAY_OPTIONS),
                ("shot_size", shot_size, SHOT_SIZE_OPTIONS),
                ("composition", composition, COMPOSITION_OPTIONS),
                ("lens_focal", lens_focal, LENS_FOCAL_OPTIONS),
                ("lens_angle", lens_angle, LENS_ANGLE_OPTIONS),
                ("lens_type", lens_type, LENS_TYPE_OPTIONS),
                ("color_tone", color_tone, COLOR_TONE_OPTIONS),
            ],
            overrides_map,
            rng=rng,
            randomize_missing=randomize_missing,
        )

        dynamic_prompts, dynamic_summaries = self._collect_category_details(
            [
                ("motion_type", motion_type, MOTION_TYPE_OPTIONS),
                ("emotion", emotion, EMOTION_OPTIONS),
                ("camera_basic", camera_basic, CAMERA_BASIC_OPTIONS),
                ("camera_advanced", camera_advanced, CAMERA_ADVANCED_OPTIONS),
            ],
            overrides_map,
            rng=rng,
            randomize_missing=randomize_missing,
        )

        style_prompts, style_summaries = self._collect_category_details(
            [
                ("visual_style", visual_style, VISUAL_STYLE_OPTIONS),
                ("special_effect", special_effect, SPECIAL_EFFECT_OPTIONS),
            ],
            overrides_map,
            rng=rng,
            randomize_missing=randomize_missing,
        )

        keyword_mode = (keyword_style or "auto").lower()
        structure = formula_config.get("structure", [])

        if keyword_mode == "compact":
            combined_keywords = aesthetic_prompts + dynamic_prompts + style_prompts
            if combined_keywords:
                prompt_fragments.append(f"Keywords: {', '.join(combined_keywords)}")
        elif keyword_mode == "inline":
            for chunk in aesthetic_prompts + dynamic_prompts + style_prompts:
                prompt_fragments.append(chunk)
        else:
            if "aesthetic" in structure and aesthetic_prompts:
                prompt_fragments.append(f"Cinematic palette: {', '.join(aesthetic_prompts)}")
            elif aesthetic_prompts:
                prompt_fragments.extend(aesthetic_prompts)

            if dynamic_prompts:
                prompt_fragments.append(f"Motion dynamics: {', '.join(dynamic_prompts)}")


            if "stylization" in structure and style_prompts:
                prompt_fragments.append(f"Stylization: {', '.join(style_prompts)}")
            elif style_prompts:
                prompt_fragments.extend(style_prompts)

        camera_block = camera_directives.strip()
        if camera_block:
            prompt_fragments.append(f"Camera direction: {camera_block}")

        combined_custom = self._split_keywords(custom_keywords)
        if override_custom:
            combined_custom.extend(override_custom)
        if combined_custom:
            combined_custom = list(dict.fromkeys(filter(None, (item.strip() for item in combined_custom))))
            if combined_custom:
                prompt_fragments.append(", ".join(combined_custom))

        suffix_fragment = prompt_suffix.strip()
        if suffix_fragment:
            prompt_fragments.append(suffix_fragment)

        filter_summary = ""
        if prompt_filter_enabled:
            fragment_filter = PromptFragmentFilter(prompt_filter_profile)
            filtered_fragments = fragment_filter.organize(prompt_fragments)
            if filtered_fragments:
                prompt_fragments = filtered_fragments
            filter_summary = fragment_filter.summarize()
            if prefix_fragment:
                try:
                    prompt_fragments.remove(prefix_fragment)
                except ValueError:
                    pass
                prompt_fragments.insert(0, prefix_fragment)
            if suffix_fragment:
                try:
                    prompt_fragments.remove(suffix_fragment)
                except ValueError:
                    pass
                prompt_fragments.append(suffix_fragment)

        prompt_text = self._assemble_prompt(prompt_fragments)
        neg_text = negative_prompt.strip()

        lighting_summary = lighting_summary.strip()
        aesthetic_sections = []
        if lighting_summary:
            aesthetic_sections.append(lighting_summary)
        aesthetic_sections.extend(aesthetic_summaries)
        aesthetic_sections.extend(style_summaries)
        aesthetic_notes = " | ".join(filter(None, aesthetic_sections))

        dynamic_notes_sources = list(dynamic_summaries)
        if camera_summary.strip():
            dynamic_notes_sources.append(camera_summary.strip())
        if camera_notes.strip():
            note_lines = []
            for line in camera_notes.splitlines():
                trimmed = line.strip()
                if not trimmed:
                    continue
                if trimmed.startswith("- "):
                    trimmed = trimmed[2:].strip()
                elif trimmed.startswith("•"):
                    trimmed = trimmed[1:].strip()
                if trimmed:
                    note_lines.append(trimmed)
            if len(note_lines) > 1:
                dynamic_notes_sources.extend(note_lines)
            else:
                dynamic_notes_sources.extend(note_lines)
        if camera_block:
            dynamic_notes_sources.append(f"Camera: {camera_block}")
        if lighting_technical_notes.strip():
            tech_lines = [line.strip() for line in lighting_technical_notes.splitlines() if line.strip()]
            if len(tech_lines) > 1:
                dynamic_notes_sources.extend(tech_lines)
            else:
                dynamic_notes_sources.append(lighting_technical_notes.strip())
        if filter_summary:
            dynamic_notes_sources.append(filter_summary)
        dynamic_notes = " | ".join(filter(None, dynamic_notes_sources))

        return (prompt_text, neg_text, aesthetic_notes, dynamic_notes, preset_status)

    def _collect_category_details(self, selections, overrides, rng=None, randomize_missing=False):
        prompts = []
        summaries = []
        overrides = overrides or {}
        for key, label, options in selections:
            tokens = self._expand_selection(label)
            override_tokens = overrides.get(key, [])
            if override_tokens:
                tokens.extend(override_tokens)
            if not tokens:
                tokens.append(label)

            for token in tokens:
                option = self._resolve_option(token, options, rng=rng, randomize_missing=randomize_missing)
                prompt_text = option.get("prompt", "").strip()
                summary_text = option.get("summary", "").strip()
                if prompt_text:
                    prompts.append(prompt_text)
                if summary_text:
                    summaries.append(summary_text)

        prompts = list(dict.fromkeys(filter(None, prompts)))
        summaries = list(dict.fromkeys(filter(None, summaries)))
        return prompts, summaries

    def _resolve_option(self, label, options, rng=None, randomize_missing=False):
        normalized = (label or "").strip()
        if normalized:
            if normalized.lower() == "none":
                normalized = ""
            else:
                lower_map = {name.lower(): name for name in options.keys()}
                lookup = lower_map.get(normalized.lower())
                if lookup:
                    return options.get(lookup, options.get("None", {"prompt": "", "summary": ""}))
        if randomize_missing and rng:
            candidates = [name for name in options if name.lower() != "none" and options[name].get("prompt")]
            if candidates:
                choice = rng.choice(candidates)
                return options[choice]
        return options.get("None", {"prompt": "", "summary": ""})

    def _expand_selection(self, value):
        if not value:
            return []
        tokens = [token.strip() for token in re.split(r'[|/,]', value) if token.strip()]
        return tokens

    def _parse_palette_overrides(self, text):
        if not text or not text.strip():
            return {}, []

        overrides = {}
        custom_chunks = []
        mapping = self._palette_alias_map()

        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            if ":" in line:
                key_part, values_part = line.split(":", 1)
                canonical = mapping.get(self._normalize_token(key_part))
                values = self._split_keywords(values_part)
                if canonical and values:
                    overrides.setdefault(canonical, []).extend(values)
                elif values:
                    custom_chunks.extend(values)
            else:
                custom_chunks.extend(self._split_keywords(line))

        for key in list(overrides.keys()):
            overrides[key] = list(dict.fromkeys(overrides[key]))

        custom_chunks = list(dict.fromkeys(custom_chunks))
        return overrides, custom_chunks

    def _palette_alias_map(self):
        return {
            "light source": "light_source",
            "light sources": "light_source",
            "lighting": "light_source",
            "light quality": "light_quality",
            "light qualities": "light_quality",
            "time of day": "time_of_day",
            "time": "time_of_day",
            "shot size": "shot_size",
            "composition": "composition",
            "lens focal": "lens_focal",
            "focal length": "lens_focal",
            "lens angle": "lens_angle",
            "camera angle": "lens_angle",
            "lens type": "lens_type",
            "shot type": "lens_type",
            "camera basic": "camera_basic",
            "basic camera": "camera_basic",
            "camera advanced": "camera_advanced",
            "advanced camera": "camera_advanced",
            "color tone": "color_tone",
            "color": "color_tone",
            "motion type": "motion_type",
            "motion": "motion_type",
            "emotion": "emotion",
            "visual style": "visual_style",
            "style": "visual_style",
            "special effect": "special_effect",
            "effects": "special_effect",
        }

    def _normalize_token(self, token):
        return token.strip().lower().replace("_", " ")

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

    def _assemble_prompt(self, fragments):
        cleaned = []
        for fragment in fragments:
            segment = fragment.strip()
            if not segment:
                continue
            if segment[-1] not in ".!?":
                segment = f"{segment}."
            cleaned.append(segment)
        return " ".join(cleaned)

__all__ = ["NoxPromptBuilder"]
