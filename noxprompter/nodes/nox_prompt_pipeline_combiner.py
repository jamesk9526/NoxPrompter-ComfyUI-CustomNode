from __future__ import annotations

import re
from ..common import detect_prompt_contradictions

class NoxPromptPipelineCombiner:
    """Cascade the outputs from the Nox prompt designer suite into a master prompt."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "core_prompt": ("STRING", {"multiline": True, "default": ""}),
            },
            "optional": {
                "enhanced_prompt": ("STRING", {"multiline": True, "default": ""}),
                "character_prompt": ("STRING", {"multiline": True, "default": ""}),
                "human_prompt": ("STRING", {"multiline": True, "default": ""}),
                "wardrobe_prompt": ("STRING", {"multiline": True, "default": ""}),
                "action_prompt": ("STRING", {"multiline": True, "default": ""}),
                "lighting_prompt": ("STRING", {"multiline": True, "default": ""}),
                "nsfw_prompt": ("STRING", {"multiline": True, "default": ""}),
                "narrative_subject": ("STRING", {"multiline": True, "default": ""}),
                "narrative_scene": ("STRING", {"multiline": True, "default": ""}),
                "narrative_motion": ("STRING", {"multiline": True, "default": ""}),
                "narrative_hook": ("STRING", {"multiline": True, "default": ""}),
                "palette_overrides": ("STRING", {"multiline": True, "default": ""}),
                "custom_keywords": ("STRING", {"multiline": True, "default": ""}),
                "extra_descriptors": ("STRING", {"multiline": True, "default": ""}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                "additional_negative": ("STRING", {"multiline": True, "default": ""}),
                "safety_notes": ("STRING", {"multiline": True, "default": ""}),
                "sequence_notes": ("STRING", {"multiline": True, "default": ""}),
                "section_separator": ("STRING", {"default": "\n\n"}),
                "content_separator": ("STRING", {"default": ", "}),
                "include_labels": ("BOOLEAN", {"default": True}),
                "builder_dynamic_notes": ("STRING", {"multiline": True, "default": ""}),
                "action_notes": ("STRING", {"multiline": True, "default": ""}),
                "lighting_notes_detail": ("STRING", {"multiline": True, "default": ""}),
                "nsfw_action_notes": ("STRING", {"multiline": True, "default": ""}),
                "camz_notes": ("STRING", {"multiline": True, "default": ""}),
                "camera_overrides": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("master_prompt", "negative_prompt", "pipeline_order", "reference_notes")
    FUNCTION = "assemble_pipeline"
    CATEGORY = "NoxPrompter/Workflow"
    NOTE_SPLITTER = re.compile(r"[|\n]+")

    PIPELINE_SEQUENCE = [
        ("NoxPromptCharacterCreator → define subject identity", ["character_prompt"]),
        ("NoxPromptHumanDesigner → confirm adult anatomy & safeguards", ["human_prompt"]),
        ("NoxPromptWardrobeDesigner → lock wardrobe & accessories", ["wardrobe_prompt"]),
        ("NoxPromptNarrativeWeaver → set subject, scene, motion, hook", ["narrative_subject", "narrative_scene", "narrative_motion", "narrative_hook"]),
        ("NoxPromptActionDirector / NSFW Action Director → choreograph movement", ["action_prompt"]),
        ("NoxPromptLightingMaster → capture lighting & atmosphere", ["lighting_prompt"]),
        ("NoxPromptNSFWDesigner → apply sensual framing & safety", ["nsfw_prompt", "safety_notes"]),
        ("NoxPromptPaletteMixer → merge palette overrides & keywords", ["palette_overrides", "custom_keywords"]),
        ("NoxPromptBuilder → assemble the hero prompt", ["core_prompt", "negative_prompt"]),
        ("NoxPromptEnhancer → polish for delivery", ["enhanced_prompt"]),
        ("NoxPromptCombiner → layer alternate blends (optional)", []),
        ("NoxPromptAnalyzer → quality check (optional)", []),
    ]

    def assemble_pipeline(
        self,
        core_prompt,
        enhanced_prompt="",
        character_prompt="",
        human_prompt="",
        wardrobe_prompt="",
        action_prompt="",
        lighting_prompt="",
        nsfw_prompt="",
        narrative_subject="",
        narrative_scene="",
        narrative_motion="",
        narrative_hook="",
        palette_overrides="",
        custom_keywords="",
        extra_descriptors="",
        negative_prompt="",
        additional_negative="",
        safety_notes="",
        sequence_notes="",
        section_separator="\n\n",
        content_separator=", ",
        include_labels=True,
        builder_dynamic_notes="",
        action_notes="",
        lighting_notes_detail="",
        nsfw_action_notes="",
        camz_notes="",
        camera_overrides="",
    ):
        palette_block = self._format_palette_overrides(palette_overrides)
        keywords_block = self._format_keywords(custom_keywords)
        narrative_block = self._build_narrative([narrative_subject, narrative_scene, narrative_motion, narrative_hook])

        note_tokens = self._tokenize_notes(
            builder_dynamic_notes,
            action_notes,
            nsfw_action_notes,
            lighting_notes_detail,
            camz_notes,
            camera_overrides,
        )
        camera_tokens, motion_tokens, lighting_tokens, safety_tokens, misc_tokens = self._partition_note_tokens(note_tokens)

        action_fragments = []
        if action_prompt.strip():
            action_fragments.append(action_prompt.strip())
        motion_clause = self._format_note_clause("Motion cues", motion_tokens, content_separator)
        if motion_clause:
            action_fragments.append(motion_clause)

        lighting_fragments = []
        if lighting_prompt.strip():
            lighting_fragments.append(lighting_prompt.strip())
        lighting_clause = self._format_note_clause("Lighting cues", lighting_tokens, content_separator)
        if lighting_clause:
            lighting_fragments.append(lighting_clause)

        camera_fragments = []
        camera_clause = self._format_note_clause("", camera_tokens, content_separator)
        if camera_clause:
            camera_fragments.append(camera_clause)

        extra_fragments = []
        if extra_descriptors.strip():
            extra_fragments.append(extra_descriptors.strip())
        misc_clause = self._format_note_clause("", misc_tokens, content_separator)
        if misc_clause:
            extra_fragments.append(misc_clause)

        safety_fragments = []
        if safety_notes.strip():
            safety_fragments.append(safety_notes.strip())
        safety_clause = self._format_note_clause("", safety_tokens, content_separator)
        if safety_clause:
            safety_fragments.append(safety_clause)

        positive_sections = []

        layout = [
            ("Character & Identity", [character_prompt, human_prompt]),
            ("Narrative Context", [narrative_block]),
            ("Wardrobe & Styling", [wardrobe_prompt]),
            ("Action & Motion", action_fragments),
        ]
        if camera_fragments:
            layout.append(("Camera Direction", camera_fragments))
        layout.extend([
            ("Lighting & Atmosphere", lighting_fragments),
            ("Sensual Spotlight", [nsfw_prompt]),
            ("Palette & Keywords", [palette_block, keywords_block]),
            ("Extra Descriptors", extra_fragments),
            ("Safety & Compliance", safety_fragments),
            ("Core Prompt", [core_prompt]),
            ("Enhancement Overlay", [enhanced_prompt]),
        ])

        raw_fragments_for_consistency = []

        for label, fragments in layout:
            cleaned = [fragment.strip() for fragment in (fragments or []) if fragment and fragment.strip()]
            if not cleaned:
                continue
            section_text = content_separator.join(cleaned)
            if include_labels:
                section_text = f"{label}: {section_text}"
            positive_sections.append(section_text)
            raw_fragments_for_consistency.extend(cleaned)

        master_prompt = section_separator.join(positive_sections).strip()

        negative_terms = self._collect_terms([negative_prompt, additional_negative])
        aggregated_negative = ", ".join(negative_terms)

        pipeline_lines = []
        context = {
            "core_prompt": core_prompt,
            "enhanced_prompt": enhanced_prompt,
            "character_prompt": character_prompt,
            "human_prompt": human_prompt,
            "wardrobe_prompt": wardrobe_prompt,
            "action_prompt": action_prompt,
            "lighting_prompt": lighting_prompt,
            "nsfw_prompt": nsfw_prompt,
            "narrative_subject": narrative_subject,
            "narrative_scene": narrative_scene,
            "narrative_motion": narrative_motion,
            "narrative_hook": narrative_hook,
            "palette_overrides": palette_overrides,
            "custom_keywords": custom_keywords,
            "negative_prompt": negative_prompt,
            "safety_notes": safety_notes,
        }

        for index, (description, keys) in enumerate(self.PIPELINE_SEQUENCE, start=1):
            provided = any(context.get(key, "").strip() for key in keys) if keys else False
            status = "✓" if provided else "○"
            pipeline_lines.append(f"{index}. {status} {description}")

        if sequence_notes.strip():
            pipeline_lines.append(f"Notes: {sequence_notes.strip()}")

        pipeline_overview = "\n".join(pipeline_lines)

        # Consistency analysis across assembled fragments
        consistency_warnings = detect_prompt_contradictions(
            raw_fragments_for_consistency
            + [
                palette_overrides,
                custom_keywords,
                extra_descriptors,
                safety_notes,
                narrative_subject,
                narrative_scene,
                narrative_motion,
                narrative_hook,
            ]
        )

        reference_parts = []
        safety_reference = self._merge_lines(safety_fragments, " | ")
        if safety_reference:
            reference_parts.append(f"Safety: {safety_reference}")
        extra_palette_notes = self._collect_reference_palette(palette_overrides)
        if extra_palette_notes:
            reference_parts.append(extra_palette_notes)
        camera_reference = self._format_note_clause("", camera_tokens, ", ")
        if camera_reference:
            reference_parts.append(f"Camera: {camera_reference}")
        motion_reference = self._format_note_clause("", motion_tokens, ", ")
        if motion_reference:
            reference_parts.append(f"Motion: {motion_reference}")
        lighting_reference = self._format_note_clause("", lighting_tokens, ", ")
        if lighting_reference:
            reference_parts.append(f"Lighting: {lighting_reference}")
        descriptors_reference = self._merge_lines([
            extra_descriptors.strip(),
            self._format_note_clause("", misc_tokens, ", ")
        ], " | ")
        if descriptors_reference:
            reference_parts.append(f"Descriptors: {descriptors_reference}")
        if consistency_warnings:
            reference_parts.append("Consistency: " + " | ".join(consistency_warnings))

        reference_notes = "\n".join(reference_parts)

        return (
            master_prompt,
            aggregated_negative,
            pipeline_overview,
            reference_notes,
        )

    @classmethod
    def _tokenize_notes(cls, *chunks):
        tokens = []
        for chunk in chunks:
            if not chunk:
                continue
            for piece in cls.NOTE_SPLITTER.split(chunk):
                stripped = piece.strip()
                if not stripped:
                    continue
                cleaned = stripped.lstrip("-•").strip()
                if cleaned:
                    tokens.append(cleaned)
        return tokens

    @staticmethod
    def _partition_note_tokens(tokens):
        camera_keywords = ("camera", "lens", "orbit", "gimbal", "steadicam", "pov", "drone", "rig", "crane", "dolly")
        motion_keywords = ("motion", "tempo", "pace", "sprint", "movement", "momentum", "flow", "beat", "action", "hover")
        lighting_keywords = ("light", "lighting", "illumination", "glow", "shadow", "highlight", "exposure", "bloom")
        safety_keywords = ("safety", "consent", "risk", "protocol", "adult", "verify", "compliance", "check-in")

        camera_notes = []
        motion_notes = []
        lighting_notes = []
        safety_notes = []
        misc_notes = []

        seen = set()
        for token in tokens:
            normalized = token.strip()
            if not normalized:
                continue
            key = normalized.lower()
            if key in seen:
                continue
            seen.add(key)
            if any(keyword in key for keyword in camera_keywords):
                camera_notes.append(normalized)
            elif any(keyword in key for keyword in motion_keywords):
                motion_notes.append(normalized)
            elif any(keyword in key for keyword in lighting_keywords):
                lighting_notes.append(normalized)
            elif any(keyword in key for keyword in safety_keywords):
                safety_notes.append(normalized)
            else:
                misc_notes.append(normalized)

        return camera_notes, motion_notes, lighting_notes, safety_notes, misc_notes

    @staticmethod
    def _format_note_clause(label, tokens, separator):
        unique = []
        seen = set()
        for token in tokens:
            cleaned = token.strip()
            if not cleaned:
                continue
            key = cleaned.lower()
            if key in seen:
                continue
            seen.add(key)
            unique.append(cleaned)
        if not unique:
            return ""
        body = separator.join(unique)
        return f"{label}: {body}" if label else body

    @staticmethod
    def _merge_lines(fragments, separator):
        unique = []
        seen = set()
        for fragment in fragments:
            cleaned = (fragment or "").strip()
            if not cleaned:
                continue
            key = cleaned.lower()
            if key in seen:
                continue
            seen.add(key)
            unique.append(cleaned)
        return separator.join(unique)

    @staticmethod
    def _format_palette_overrides(palette_overrides):
        content = [line.strip() for line in palette_overrides.replace("\r", "").split("\n") if line.strip()]
        return "; ".join(content)

    @staticmethod
    def _collect_reference_palette(palette_overrides):
        content = [line.strip() for line in palette_overrides.replace("\r", "").split("\n") if line.strip()]
        if not content:
            return ""
        return "Palette: " + "; ".join(content)

    @staticmethod
    def _format_keywords(custom_keywords):
        tokens = NoxPromptPipelineCombiner._collect_terms([custom_keywords])
        return ", ".join(tokens)

    @staticmethod
    def _build_narrative(chunks):
        sentences = []
        for chunk in chunks:
            cleaned = (chunk or "").strip()
            if not cleaned:
                continue
            if cleaned[-1] not in ".!?":
                cleaned = f"{cleaned}."
            sentences.append(cleaned)
        return " ".join(sentences)

    @staticmethod
    def _collect_terms(sections):
        tokens = []
        for section in sections:
            text = (section or "").replace("\r", "\n")
            for part in text.split("\n"):
                for token in part.split(","):
                    normalized = token.strip()
                    if normalized:
                        tokens.append(normalized)
        seen = set()
        ordered = []
        for token in tokens:
            if token.lower() in seen:
                continue
            seen.add(token.lower())
            ordered.append(token)
        return ordered

__all__ = ["NoxPromptPipelineCombiner"]
