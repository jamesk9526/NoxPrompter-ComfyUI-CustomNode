from __future__ import annotations

from ..common import PresetMixin, PromptFragmentFilter
from ..constants import FORMULA_CONFIGS

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
                "aesthetic_palette": ("STRING", {"multiline": True, "default": "Daylight rim lighting | Soft diffusion fill | Warm tone bounce | Balanced composition"}),
                "dynamic_palette": ("STRING", {"multiline": True, "default": "Running motion arcs | Joyful expressions | Pan-right sweep | Crane follow"}),
                "style_palette": ("STRING", {"multiline": True, "default": "Anime cinematic tonality | Tilt-shift miniature effect"}),
                "keyword_style": (["auto", "inline", "compact"], {"default": "auto"}),
                "quality_profile": (["Balanced", "Cinematic", "Minimal", "Narrative"], {"default": "Balanced"}),
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
        aesthetic_palette="",
        dynamic_palette="",
        style_palette="",
        keyword_style="auto",
        quality_profile="Balanced",
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
            "aesthetic_palette": aesthetic_palette,
            "dynamic_palette": dynamic_palette,
            "style_palette": style_palette,
            "keyword_style": keyword_style,
            "quality_profile": quality_profile,
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
        aesthetic_palette = config.get("aesthetic_palette", aesthetic_palette)
        dynamic_palette = config.get("dynamic_palette", dynamic_palette)
        style_palette = config.get("style_palette", style_palette)
        keyword_style = config.get("keyword_style", "auto")
        quality_profile = config.get("quality_profile", "Balanced")
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
        aesthetic_prompts, aesthetic_summary = self._parse_palette(aesthetic_palette)
        dynamic_prompts, dynamic_summary = self._parse_palette(dynamic_palette)
        style_prompts, style_summary = self._parse_palette(style_palette)

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
                prompt_fragments.append(f"Aesthetic palette: {', '.join(aesthetic_prompts)}")
            elif aesthetic_prompts:
                prompt_fragments.extend(aesthetic_prompts)

            if dynamic_prompts:
                prompt_fragments.append(f"Dynamic palette: {', '.join(dynamic_prompts)}")

            if "stylization" in structure and style_prompts:
                prompt_fragments.append(f"Stylization: {', '.join(style_prompts)}")
            elif style_prompts:
                prompt_fragments.extend(style_prompts)

        camera_block = camera_directives.strip()
        if camera_block:
            prompt_fragments.append(f"Camera direction: {camera_block}")

        combined_custom = self._split_keywords(custom_keywords)
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

        aesthetic_sections = []
        if lighting_summary.strip():
            aesthetic_sections.append(lighting_summary.strip())
        if aesthetic_summary:
            aesthetic_sections.append(f"Aesthetic palette: {aesthetic_summary}")
        if style_summary:
            aesthetic_sections.append(f"Stylization: {style_summary}")
        aesthetic_notes = " | ".join(filter(None, aesthetic_sections))

        dynamic_notes_sources = []
        if dynamic_summary:
            dynamic_notes_sources.append(f"Dynamic palette: {dynamic_summary}")
        if quality_profile:
            dynamic_notes_sources.append(f"Quality profile: {quality_profile}")
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
            if note_lines:
                dynamic_notes_sources.extend(note_lines)
        if camera_block:
            dynamic_notes_sources.append(f"Camera: {camera_block}")
        if lighting_technical_notes.strip():
            tech_lines = [line.strip() for line in lighting_technical_notes.splitlines() if line.strip()]
            if tech_lines:
                dynamic_notes_sources.extend(tech_lines)
        if filter_summary:
            dynamic_notes_sources.append(filter_summary)

        dynamic_notes = " | ".join(filter(None, dynamic_notes_sources))

        return (prompt_text, neg_text, aesthetic_notes, dynamic_notes, preset_status)

    def _parse_palette(self, text):
        tokens = self._split_keywords(text)
        tokens = list(dict.fromkeys(tokens))
        summary = ", ".join(tokens) if tokens else ""
        return tokens, summary

    def _split_keywords(self, text):
        if not text:
            return []
        separators = [",", "\n", ";", "|"]
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
