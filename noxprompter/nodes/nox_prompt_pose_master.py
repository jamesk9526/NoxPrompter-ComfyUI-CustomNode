from __future__ import annotations

from typing import Dict, List

from ..common import PresetMixin, option_keys
from ..constants import (
    POSE_BASELINE_NEGATIVES,
    POSE_LIGHTING_SETUPS,
    POSE_MASTER_PROFILES,
    POSE_SET_DESIGNS,
    POSE_ENERGY_LEVELS,
)


class NoxPromptPoseMaster(PresetMixin):
    """Direct non-NSFW pose staging with camera, lighting, and coaching guidance."""

    CATEGORY = "NoxPrompter/Posing"
    FUNCTION = "stage_pose"
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = (
        "pose_prompt",
        "pose_negative",
        "pose_brief",
        "guidance_notes",
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
                        "default": "Lead performer demonstrating confident posture",
                    },
                ),
                "pose_profile": (
                    option_keys(POSE_MASTER_PROFILES),
                    {"default": "Heroic Stand"},
                ),
            },
            "optional": {
                "pose_intent": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "Capture a confident, story-driven stance for key art coverage",
                    },
                ),
                "body_highlights": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "elongated lines, balanced weight, expressive hands",
                    },
                ),
                "expression_focus": (
                    "STRING",
                    {"multiline": True, "default": "steady gaze, relaxed smile"},
                ),
                "movement_cue": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "slow inhale, gentle posture reset between takes",
                    },
                ),
                "staging_marks": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "mark lead foot placement, keep shoulders aligned with key light",
                    },
                ),
                "support_props": ("STRING", {"multiline": True, "default": ""}),
                "pose_tags": (
                    "STRING",
                    {"multiline": True, "default": "pose, confident, cinematic"},
                ),
                "lighting_setup": (
                    option_keys(POSE_LIGHTING_SETUPS),
                    {"default": "Soft Studio"},
                ),
                "set_design": (
                    option_keys(POSE_SET_DESIGNS),
                    {"default": "Studio Seamless"},
                ),
                "energy_level": (
                    option_keys(POSE_ENERGY_LEVELS),
                    {"default": "Focused Drive"},
                ),
                "coaching_focus": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "Offer clear coaching cues and celebrate confident delivery.",
                    },
                ),
                "comfort_considerations": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "Monitor posture comfort, rotate breaks, and provide hydration reminders.",
                    },
                ),
                "safety_equipment": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "camera_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "include_negative_baseline": (
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
    custom_prompt: str = "",
    subject_focus: str = "Lead performer demonstrating confident posture",
    pose_profile: str = "Heroic Stand",
        pose_intent: str = "Capture a confident, story-driven stance for key art coverage",
        body_highlights: str = "elongated lines, balanced weight, expressive hands",
        expression_focus: str = "steady gaze, relaxed smile",
        movement_cue: str = "slow inhale, gentle posture reset between takes",
        staging_marks: str = "mark lead foot placement, keep shoulders aligned with key light",
        support_props: str = "",
        pose_tags: str = "pose, confident, cinematic",
        lighting_setup: str = "Soft Studio",
        set_design: str = "Studio Seamless",
        energy_level: str = "Focused Drive",
        camera_notes: str = "",
        coaching_focus: str = "Offer clear coaching cues and celebrate confident delivery.",
        comfort_considerations: str = "Monitor posture comfort, rotate breaks, and provide hydration reminders.",
        safety_equipment: str = "",
        include_negative_baseline: bool = True,
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
            "energy_level": energy_level,
            "camera_notes": camera_notes,
            "coaching_focus": coaching_focus,
            "comfort_considerations": comfort_considerations,
            "safety_equipment": safety_equipment,
            "include_negative_baseline": include_negative_baseline,
        }

        config, preset_status = self._apply_preset_action(
            "pose_master",
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
        energy_level = config.get("energy_level", energy_level)
        camera_notes = config.get("camera_notes", camera_notes)
        coaching_focus = config.get("coaching_focus", coaching_focus)
        comfort_considerations = config.get("comfort_considerations", comfort_considerations)
        safety_equipment = config.get("safety_equipment", safety_equipment)
        include_negative_baseline = bool(
            config.get("include_negative_baseline", include_negative_baseline)
        )

        pose_cfg = self._resolve_pose_option(
            pose_profile,
            POSE_MASTER_PROFILES,
        )
        lighting_cfg = self._resolve_pose_option(
            lighting_setup,
            POSE_LIGHTING_SETUPS,
        )
        set_cfg = self._resolve_pose_option(
            set_design,
            POSE_SET_DESIGNS,
        )
        energy_cfg = self._resolve_pose_option(
            energy_level,
            POSE_ENERGY_LEVELS,
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
        if energy_cfg.get("prompt"):
            primary_parts.append(energy_cfg["prompt"])
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
            negatives.extend(POSE_BASELINE_NEGATIVES)
        pose_negative = ", ".join(self._unique_sequence(negatives))

        brief_parts: List[str] = []
        if pose_cfg.get("notes"):
            brief_parts.append(f"Pose note: {pose_cfg['notes']}")
        if lighting_cfg.get("notes"):
            brief_parts.append(f"Lighting: {lighting_cfg['notes']}")
        if set_cfg.get("notes"):
            brief_parts.append(f"Set: {set_cfg['notes']}")
        if energy_cfg.get("notes"):
            brief_parts.append(f"Energy: {energy_cfg['notes']}")
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

        guidance_parts: List[str] = []
        if coaching_focus.strip():
            guidance_parts.append(f"Coaching: {coaching_focus.strip()}")
        if comfort_considerations.strip():
            guidance_parts.append(f"Comfort: {comfort_considerations.strip()}")
        if safety_equipment.strip():
            guidance_parts.append(f"Safety gear: {safety_equipment.strip()}")
        for source in (
            pose_cfg.get("notes"),
            lighting_cfg.get("notes"),
            set_cfg.get("notes"),
            energy_cfg.get("notes"),
        ):
            if source:
                guidance_parts.append(source)
        if camera_notes.strip():
            guidance_parts.append(f"Camera: {camera_notes.strip()}")
        guidance_notes = " | ".join(self._unique_sequence(guidance_parts))

        return pose_prompt, pose_negative, pose_brief, guidance_notes, preset_status

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

    def _resolve_pose_option(
        self,
        selection: str,
        options: Dict[str, Dict[str, str]],
    ) -> Dict[str, str]:
        key = self._match_option_key(selection, options)
        fallback = "None" if "None" in options else next(iter(options))
        source_key = key or fallback
        base = dict(options.get(source_key, {}))

        prompt = (base.get("prompt") or "").strip()
        base["prompt"] = prompt

        notes_value = base.get("notes", base.get("summary", ""))
        base["notes"] = (notes_value or "").strip()

        return base

    def _match_option_key(self, selection: str, options: Dict[str, Dict[str, str]]) -> str | None:
        normalized = (selection or "").strip().lower()
        if not normalized:
            return None
        for key in options.keys():
            if key.lower() == normalized:
                return key
        return None


__all__ = ["NoxPromptPoseMaster"]
