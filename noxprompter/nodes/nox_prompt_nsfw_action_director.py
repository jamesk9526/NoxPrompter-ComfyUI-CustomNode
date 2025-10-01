from __future__ import annotations

from typing import Any, Dict, List, Tuple
from ..common import PresetMixin, _resolve_action_option, _split_tokens
from ..constants import *  # noqa: F403

class NoxPromptNSFWActionDirector(PresetMixin):
    """Stage adult-oriented action performances with explicit safety framing."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "primary_action": (list(NSFW_ACTION_PRIMARY_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Sensual Caress"}),
            },
            "optional": {
                "secondary_action": (list(NSFW_ACTION_SECONDARY_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "None"}),
                "tempo": (list(NSFW_ACTION_TEMPO_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Slow Tease"}),
                "interaction_mode": (list(NSFW_ACTION_INTERACTION_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Solo Self-Admiration"}),
                "props": ("STRING", {"multiline": True, "default": ""}),
                "environment_mood": ("STRING", {"multiline": True, "default": ""}),
                "heat_descriptor": ("STRING", {"default": ""}),
                "camera_language": ("STRING", {"multiline": True, "default": ""}),
                "soundscape": ("STRING", {"multiline": True, "default": ""}),
                "dialogue_hook": ("STRING", {"multiline": True, "default": ""}),
                "consent_focus": ("STRING", {"multiline": True, "default": "enthusiastic consent, explicit verbal check-ins"}),
                "boundary_notes": ("STRING", {"multiline": True, "default": ""}),
                "aftercare_plan": ("STRING", {"multiline": True, "default": ""}),
                "safety_props": ("STRING", {"multiline": True, "default": ""}),
                "beat_emphasis": ("STRING", {"multiline": True, "default": ""}),
                "risk_notes": ("STRING", {"multiline": True, "default": ""}),
                "primary_action_custom": ("STRING", {"multiline": True, "default": ""}),
                "secondary_action_custom": ("STRING", {"multiline": True, "default": ""}),
                "tempo_custom": ("STRING", {"multiline": True, "default": ""}),
                "interaction_mode_custom": ("STRING", {"multiline": True, "default": ""}),
                "primary_notes": ("STRING", {"multiline": True, "default": ""}),
                "secondary_notes": ("STRING", {"multiline": True, "default": ""}),
                "tempo_notes": ("STRING", {"multiline": True, "default": ""}),
                "interaction_notes": ("STRING", {"multiline": True, "default": ""}),
                "include_safety_note": ("BOOLEAN", {"default": True}),
                "custom_safety_note": ("STRING", {"multiline": True, "default": ""}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("action_prompt", "action_summary", "safety_notes", "preset_status")
    FUNCTION = "direct"
    CATEGORY = "NoxPrompter/NSFW"

    def direct(
        self,
        primary_action,
        secondary_action="None",
        tempo="Slow Tease",
        interaction_mode="Solo Self-Admiration",
        props="",
        environment_mood="",
        heat_descriptor="",
        camera_language="",
        soundscape="",
        dialogue_hook="",
        consent_focus="enthusiastic consent, explicit verbal check-ins",
        boundary_notes="",
        aftercare_plan="",
        safety_props="",
        beat_emphasis="",
        risk_notes="",
        primary_action_custom="",
        secondary_action_custom="",
        tempo_custom="",
        interaction_mode_custom="",
        primary_notes="",
        secondary_notes="",
        tempo_notes="",
        interaction_notes="",
        include_safety_note=True,
        custom_safety_note="",
        preset_action="none",
        preset_name="",
    ):
        config = {
            "primary_action": primary_action,
            "secondary_action": secondary_action,
            "tempo": tempo,
            "interaction_mode": interaction_mode,
            "props": props,
            "environment_mood": environment_mood,
            "heat_descriptor": heat_descriptor,
            "camera_language": camera_language,
            "soundscape": soundscape,
            "dialogue_hook": dialogue_hook,
            "consent_focus": consent_focus,
            "boundary_notes": boundary_notes,
            "aftercare_plan": aftercare_plan,
            "safety_props": safety_props,
            "beat_emphasis": beat_emphasis,
            "risk_notes": risk_notes,
            "primary_action_custom": primary_action_custom,
            "secondary_action_custom": secondary_action_custom,
            "tempo_custom": tempo_custom,
            "interaction_mode_custom": interaction_mode_custom,
            "primary_notes": primary_notes,
            "secondary_notes": secondary_notes,
            "tempo_notes": tempo_notes,
            "interaction_notes": interaction_notes,
            "include_safety_note": include_safety_note,
            "custom_safety_note": custom_safety_note,
        }

        config, preset_status = self._apply_preset_action(
            "nsfw_action_director",
            preset_action,
            preset_name,
            config,
        )

        primary_action = config.get("primary_action", primary_action)
        secondary_action = config.get("secondary_action", secondary_action)
        tempo = config.get("tempo", tempo)
        interaction_mode = config.get("interaction_mode", interaction_mode)
        props = config.get("props", props)
        environment_mood = config.get("environment_mood", environment_mood)
        heat_descriptor = config.get("heat_descriptor", heat_descriptor)
        camera_language = config.get("camera_language", camera_language)
        soundscape = config.get("soundscape", soundscape)
        dialogue_hook = config.get("dialogue_hook", dialogue_hook)
        consent_focus = config.get("consent_focus", consent_focus)
        boundary_notes = config.get("boundary_notes", boundary_notes)
        aftercare_plan = config.get("aftercare_plan", aftercare_plan)
        safety_props = config.get("safety_props", safety_props)
        beat_emphasis = config.get("beat_emphasis", beat_emphasis)
        risk_notes = config.get("risk_notes", risk_notes)
        primary_action_custom = config.get("primary_action_custom", primary_action_custom)
        secondary_action_custom = config.get("secondary_action_custom", secondary_action_custom)
        tempo_custom = config.get("tempo_custom", tempo_custom)
        interaction_mode_custom = config.get("interaction_mode_custom", interaction_mode_custom)
        primary_notes = config.get("primary_notes", primary_notes)
        secondary_notes = config.get("secondary_notes", secondary_notes)
        tempo_notes = config.get("tempo_notes", tempo_notes)
        interaction_notes = config.get("interaction_notes", interaction_notes)
        include_safety_note = bool(config.get("include_safety_note", include_safety_note))
        custom_safety_note = config.get("custom_safety_note", custom_safety_note)

        primary_prompt, primary_summary = _resolve_action_option(primary_action, primary_action_custom, NSFW_ACTION_PRIMARY_OPTIONS)
        secondary_prompt, secondary_summary = _resolve_action_option(secondary_action, secondary_action_custom, NSFW_ACTION_SECONDARY_OPTIONS)
        tempo_prompt, tempo_summary = _resolve_action_option(tempo, tempo_custom, NSFW_ACTION_TEMPO_OPTIONS)
        interaction_prompt, interaction_summary = _resolve_action_option(interaction_mode, interaction_mode_custom, NSFW_ACTION_INTERACTION_OPTIONS)

        props_list = _split_tokens(props)
        beat_highlights = _split_tokens(beat_emphasis)
        risk_list = _split_tokens(risk_notes)
        safety_tool_list = _split_tokens(safety_props)

        prompt_parts = [primary_prompt]
        for fragment in (secondary_prompt, tempo_prompt, interaction_prompt):
            if fragment:
                prompt_parts.append(fragment)
        if heat_descriptor.strip():
            prompt_parts.append(heat_descriptor.strip())
        if environment_mood.strip():
            prompt_parts.append(f"set mood: {environment_mood.strip()}")
        if props_list:
            prompt_parts.append("props: " + ", ".join(props_list))
        action_prompt = ", ".join(part for part in prompt_parts if part)
        if action_prompt and action_prompt[-1] not in ".!?":
            action_prompt += "."
        if camera_language.strip():
            action_prompt += f" Camera language: {camera_language.strip()}"
        if soundscape.strip():
            action_prompt += f" Soundscape: {soundscape.strip()}"
        if dialogue_hook.strip():
            action_prompt += f" Dialogue cue: {dialogue_hook.strip()}"

        summary_segments = []
        if primary_summary:
            summary_segments.append(f"Primary: {primary_summary}")
        if primary_notes.strip():
            summary_segments.append(primary_notes.strip())
        if secondary_summary:
            summary_segments.append(f"Secondary: {secondary_summary}")
        if secondary_notes.strip():
            summary_segments.append(secondary_notes.strip())
        if tempo_summary:
            summary_segments.append(f"Tempo: {tempo_summary}")
        if tempo_notes.strip():
            summary_segments.append(tempo_notes.strip())
        if interaction_summary:
            summary_segments.append(f"Interaction: {interaction_summary}")
        if interaction_notes.strip():
            summary_segments.append(interaction_notes.strip())
        if heat_descriptor.strip():
            summary_segments.append(f"Heat: {heat_descriptor.strip()}")
        if props_list:
            summary_segments.append("Props: " + ", ".join(props_list))
        if beat_highlights:
            summary_segments.append("Beat focus: " + ", ".join(beat_highlights))
        if environment_mood.strip():
            summary_segments.append(f"Environment: {environment_mood.strip()}")
        if camera_language.strip():
            summary_segments.append("Camera: " + camera_language.strip())
        if soundscape.strip():
            summary_segments.append("Sound: " + soundscape.strip())
        if dialogue_hook.strip():
            summary_segments.append("Dialogue: " + dialogue_hook.strip())
        if consent_focus.strip():
            summary_segments.append("Consent: " + consent_focus.strip())
        action_summary = " | ".join(segment for segment in summary_segments if segment)

        safety_parts = []
        if include_safety_note:
            safety_parts.append(NSFW_DEFAULT_SAFETY_NOTE)
        if consent_focus.strip():
            safety_parts.append("Consent focus: " + consent_focus.strip())
        if boundary_notes.strip():
            safety_parts.append("Boundaries: " + boundary_notes.strip())
        if risk_list:
            safety_parts.append("Risks monitored: " + ", ".join(risk_list))
        if safety_tool_list:
            safety_parts.append("Safety tools: " + ", ".join(safety_tool_list))
        if aftercare_plan.strip():
            safety_parts.append("Aftercare: " + aftercare_plan.strip())
        if custom_safety_note.strip():
            safety_parts.append(custom_safety_note.strip())
        safety_notes = " | ".join(part for part in safety_parts if part)

        return (action_prompt.strip(), action_summary, safety_notes, preset_status)

__all__ = ["NoxPromptNSFWActionDirector"]
