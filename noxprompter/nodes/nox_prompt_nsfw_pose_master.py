from __future__ import annotations

from typing import Dict, List

from ..common import PresetMixin, option_keys
from ..constants import (
    NSFW_BASELINE_NEGATIVES,
    NSFW_DEFAULT_SAFETY_NOTE,
    NSFW_EXPLICITNESS_LEVELS,
    NSFW_HEAT_LEVELS,
    NSFW_LIGHTING_SETUPS,
    NSFW_POSE_PROFILES,
    NSFW_SET_DESIGNS,
)


class NoxPromptNSFWPoseMaster(PresetMixin):
    """Curate adult-only pose direction with camera, lighting, and safety context."""

    CATEGORY = "NoxPrompter/NSFW"
    FUNCTION = "stage_pose"
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = (
        "pose_prompt",
        "pose_negative",
        "pose_brief",
        "safety_notes",
        "preset_status",
    )

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
                "subject_focus": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "Empowered adult performer showcasing confident posture",
                    },
                ),
                "pose_profile": (
                    option_keys(NSFW_POSE_PROFILES),
                    {"default": "Reclined Elegance"},
                ),
            },
            "optional": {
                "pose_intent": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "Celebrate adult confidence with graceful, empowered staging",
                    },
                ),
                "body_highlights": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "elongated lines, flattering curvature, controlled angles",
                    },
                ),
                "expression_focus": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "inviting gaze, self-assured smile",
                    },
                ),
                "movement_cue": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "slow inhale, gentle hip arch, relaxed breathing",
                    },
                ),
                "staging_marks": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "mark foot placement, cue spotlight center, ensure stable footing",
                    },
                ),
                "support_props": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "pose_tags": (
                    "STRING",
                    {"multiline": True, "default": "adult, empowered, confident"},
                ),
                "lighting_setup": (
                    option_keys(NSFW_LIGHTING_SETUPS),
                    {"default": "Candlelit Warmth"},
                ),
                "set_design": (
                    option_keys(NSFW_SET_DESIGNS),
                    {"default": "Sensual Lounge"},
                ),
                "heat_profile": (
                    option_keys(NSFW_HEAT_LEVELS),
                    {"default": "Sensual"},
                ),
                "explicitness_level": (
                    option_keys(NSFW_EXPLICITNESS_LEVELS),
                    {"default": "Implied Nude"},
                ),
                "camera_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "consent_focus": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "affirmed adult consent, ongoing verbal check-ins, respectful pacing",
                    },
                ),
                "boundary_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "safety_equipment": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "include_negative_baseline": (
                    "BOOLEAN",
                    {"default": True},
                ),
                "include_safety_note": (
                    "BOOLEAN",
                    {"default": True},
                ),
                "preset_action": (
                    ["none", "save", "load", "list"],
                    {"default": "none"},
                ),
                "preset_name": (
                    "STRING",
                    {"default": ""},
                ),
            },
        }

    def stage_pose(
        self,
        custom_prompt: str,
        subject_focus: str,
        pose_profile: str = "Reclined Elegance",
        pose_intent: str = "Celebrate adult confidence with graceful, empowered staging",
        body_highlights: str = "elongated lines, flattering curvature, controlled angles",
        expression_focus: str = "inviting gaze, self-assured smile",
        movement_cue: str = "slow inhale, gentle hip arch, relaxed breathing",
        staging_marks: str = "mark foot placement, cue spotlight center, ensure stable footing",
        support_props: str = "",
        pose_tags: str = "adult, empowered, confident",
        lighting_setup: str = "Candlelit Warmth",
        set_design: str = "Sensual Lounge",
        heat_profile: str = "Sensual",
        explicitness_level: str = "Implied Nude",
        camera_notes: str = "",
        consent_focus: str = "affirmed adult consent, ongoing verbal check-ins, respectful pacing",
        boundary_notes: str = "",
        safety_equipment: str = "",
        include_negative_baseline: bool = True,
        include_safety_note: bool = True,
        preset_action: str = "none",
        preset_name: str = "",
    ):
        config = {
            "custom_prompt": custom_prompt,
            "subject_focus": subject_focus,
            "pose_profile": pose_profile,
            "pose_intent": pose_intent,
            "body_highlights": body_highlights,
            "expression_focus": expression_focus,
            "movement_cue": movement_cue,
            "staging_marks": staging_marks,
            "support_props": support_props,
            "pose_tags": pose_tags,
            "lighting_setup": lighting_setup,
            "set_design": set_design,
            "heat_profile": heat_profile,
            "explicitness_level": explicitness_level,
            "camera_notes": camera_notes,
            "consent_focus": consent_focus,
            "boundary_notes": boundary_notes,
            "safety_equipment": safety_equipment,
            "include_negative_baseline": include_negative_baseline,
            "include_safety_note": include_safety_note,
        }

        config, preset_status = self._apply_preset_action(
            "nsfw_pose_master",
            preset_action,
            preset_name,
            config,
        )

        custom_prompt = config.get("custom_prompt", custom_prompt)
        subject_focus = config.get("subject_focus", subject_focus)
        pose_profile = config.get("pose_profile", pose_profile)
        pose_intent = config.get("pose_intent", pose_intent)
        body_highlights = config.get("body_highlights", body_highlights)
        expression_focus = config.get("expression_focus", expression_focus)
        movement_cue = config.get("movement_cue", movement_cue)
        staging_marks = config.get("staging_marks", staging_marks)
        support_props = config.get("support_props", support_props)
        pose_tags = config.get("pose_tags", pose_tags)
        lighting_setup = config.get("lighting_setup", lighting_setup)
        set_design = config.get("set_design", set_design)
        heat_profile = config.get("heat_profile", heat_profile)
        explicitness_level = config.get("explicitness_level", explicitness_level)
        camera_notes = config.get("camera_notes", camera_notes)
        consent_focus = config.get("consent_focus", consent_focus)
        boundary_notes = config.get("boundary_notes", boundary_notes)
        safety_equipment = config.get("safety_equipment", safety_equipment)
        include_negative_baseline = bool(config.get("include_negative_baseline", include_negative_baseline))
        include_safety_note = bool(config.get("include_safety_note", include_safety_note))

        pose_cfg = self._resolve_nsfw_option(
            pose_profile,
            NSFW_POSE_PROFILES,
        )
        lighting_cfg = self._resolve_nsfw_option(
            lighting_setup,
            NSFW_LIGHTING_SETUPS,
        )
        set_cfg = self._resolve_nsfw_option(
            set_design,
            NSFW_SET_DESIGNS,
        )
        heat_cfg = self._resolve_nsfw_option(
            heat_profile,
            NSFW_HEAT_LEVELS,
        )
        explicit_cfg = self._resolve_nsfw_option(
            explicitness_level,
            NSFW_EXPLICITNESS_LEVELS,
        )

        prompt_fragments: List[str] = []
        custom_fragment = (custom_prompt or "").strip()
        if custom_fragment:
            prompt_fragments.append(custom_fragment)
        primary_parts = [subject_focus.strip()]
        if pose_intent.strip():
            primary_parts.append(pose_intent.strip())
        if pose_cfg.get("prompt"):
            primary_parts.append(pose_cfg["prompt"])
        if body_highlights.strip():
            primary_parts.append(body_highlights.strip())
        if explicit_cfg.get("prompt"):
            primary_parts.append(explicit_cfg["prompt"])
        if heat_cfg.get("prompt"):
            primary_parts.append(heat_cfg["prompt"])
        primary_sentence = ", ".join(part for part in primary_parts if part)
        if primary_sentence:
            prompt_fragments.append(primary_sentence)

        staging_parts = []
        if expression_focus.strip():
            staging_parts.append(f"Expression focus: {expression_focus.strip()}")
        if movement_cue.strip():
            staging_parts.append(f"Movement cue: {movement_cue.strip()}")
        if staging_marks.strip():
            staging_parts.append(f"Stage marks: {staging_marks.strip()}")
        if support_props.strip():
            props_formatted = ", ".join(self._split_keywords(support_props)) or support_props.strip()
            staging_parts.append(f"Props: {props_formatted}")
        if staging_parts:
            prompt_fragments.append(" ".join(staging_parts))

        environment_parts = []
        if set_cfg.get("prompt"):
            environment_parts.append(set_cfg["prompt"])
        if lighting_cfg.get("prompt"):
            environment_parts.append(lighting_cfg["prompt"])
        environment_sentence = ", ".join(part for part in environment_parts if part)
        if environment_sentence:
            prompt_fragments.append(environment_sentence)
        if camera_notes.strip():
            prompt_fragments.append(f"Camera guidance: {camera_notes.strip()}")

        tag_list = self._split_keywords(pose_tags)
        if tag_list:
            prompt_fragments.append(f"Keywords: {', '.join(tag_list)}")

        pose_prompt = self._assemble_sentences(prompt_fragments)

        negatives: List[str] = []
        if include_negative_baseline:
            negatives.extend(NSFW_BASELINE_NEGATIVES)
        negatives.extend(self._split_keywords(explicit_cfg.get("negative", "")))
        negatives.extend(self._split_keywords(heat_cfg.get("negative", "")))
        pose_negative = ", ".join(self._unique_sequence(negatives))

        brief_parts: List[str] = []
        if pose_cfg.get("notes"):
            brief_parts.append(f"Pose note: {pose_cfg['notes']}")
        if lighting_cfg.get("notes"):
            brief_parts.append(f"Lighting: {lighting_cfg['notes']}")
        if set_cfg.get("notes"):
            brief_parts.append(f"Set: {set_cfg['notes']}")
        if heat_cfg.get("notes"):
            brief_parts.append(f"Heat: {heat_cfg['notes']}")
        if explicit_cfg.get("notes"):
            brief_parts.append(f"Explicitness: {explicit_cfg['notes']}")
        if camera_notes.strip():
            brief_parts.append(f"Camera: {camera_notes.strip()}")
        if expression_focus.strip():
            brief_parts.append(f"Expression: {expression_focus.strip()}")
        if movement_cue.strip():
            brief_parts.append(f"Movement: {movement_cue.strip()}")
        if body_highlights.strip():
            brief_parts.append(f"Body focus: {body_highlights.strip()}")
        if staging_marks.strip():
            brief_parts.append(f"Staging: {staging_marks.strip()}")
        props_tokens = self._split_keywords(support_props)
        if props_tokens:
            brief_parts.append("Props: " + ", ".join(props_tokens))
        if tag_list:
            brief_parts.append("Tags: " + ", ".join(tag_list))
        pose_brief = " | ".join(self._unique_sequence(brief_parts))

        safety_parts: List[str] = []
        if include_safety_note:
            safety_parts.append(NSFW_DEFAULT_SAFETY_NOTE)
        if consent_focus.strip():
            safety_parts.append(f"Consent: {consent_focus.strip()}")
        if boundary_notes.strip():
            safety_parts.append(f"Boundaries: {boundary_notes.strip()}")
        if safety_equipment.strip():
            safety_parts.append(f"Safety gear: {safety_equipment.strip()}")
        for source in (
            pose_cfg.get("notes"),
            lighting_cfg.get("notes"),
            set_cfg.get("notes"),
            heat_cfg.get("notes"),
            explicit_cfg.get("notes"),
        ):
            if source:
                safety_parts.append(source)
        if camera_notes.strip():
            safety_parts.append(f"Camera: {camera_notes.strip()}")
        safety_notes = " | ".join(self._unique_sequence(safety_parts))

        return pose_prompt, pose_negative, pose_brief, safety_notes, preset_status

    def _assemble_sentences(self, fragments: List[str]) -> str:
        sentences: List[str] = []
        for fragment in fragments:
            segment = (fragment or "").strip()
            if not segment:
                continue
            if segment[-1] not in ".!?":
                segment = f"{segment}."
            sentences.append(segment)
        return " ".join(sentences)

    def _split_keywords(self, text: str) -> List[str]:
        if not text:
            return []
        separators = [",", "\n", ";"]
        tokens = [text]
        for separator in separators:
            expanded: List[str] = []
            for token in tokens:
                expanded.extend(token.split(separator))
            tokens = expanded
        return [token.strip() for token in tokens if token.strip()]

    def _unique_sequence(self, values: List[str]) -> List[str]:
        seen = set()
        ordered: List[str] = []
        for value in values:
            cleaned = (value or "").strip()
            if not cleaned:
                continue
            key = cleaned.lower()
            if key in seen:
                continue
            seen.add(key)
            ordered.append(cleaned)
        return ordered

    def _resolve_nsfw_option(
        self,
        selection: str,
        options: Dict[str, Dict[str, str]],
    ) -> Dict[str, str]:
        key = self._match_option_key(selection, options)
        fallback = "None" if "None" in options else next(iter(options))
        source_key = key or fallback
        return dict(options.get(source_key, {}))

    def _match_option_key(self, selection: str, options: Dict[str, Dict[str, str]]) -> str | None:
        normalized = (selection or "").strip().lower()
        if not normalized:
            return None
        for key in options.keys():
            if key.lower() == normalized:
                return key
        return None


__all__ = ["NoxPromptNSFWPoseMaster"]
