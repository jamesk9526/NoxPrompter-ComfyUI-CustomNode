from __future__ import annotations

from typing import Any, Dict, List, Tuple
from ..common import PresetMixin, _resolve_action_option, _split_tokens
from ..constants import *  # noqa: F403

class NoxPromptActionDirector(PresetMixin):
    """Choreograph dynamic action beats, tempo, and supporting notes."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "primary_action": (list(ACTION_PRIMARY_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Heroic Sprint"}),
            },
            "optional": {
                "secondary_action": (list(ACTION_SECONDARY_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "None"}),
                "tempo": (list(ACTION_TEMPO_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Rising Momentum"}),
                "interaction_mode": (list(ACTION_INTERACTION_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Solo Focus"}),
                "props": ("STRING", {"multiline": True, "default": ""}),
                "environment_beat": ("STRING", {"multiline": True, "default": ""}),
                "intensity_descriptor": ("STRING", {"default": ""}),
                "camera_language": ("STRING", {"multiline": True, "default": ""}),
                "sound_design": ("STRING", {"multiline": True, "default": ""}),
                "dialogue_hook": ("STRING", {"multiline": True, "default": ""}),
                "emotional_anchor": ("STRING", {"default": ""}),
                "risk_notes": ("STRING", {"multiline": True, "default": ""}),
                "beat_emphasis": ("STRING", {"multiline": True, "default": ""}),
                "primary_action_custom": ("STRING", {"multiline": True, "default": ""}),
                "secondary_action_custom": ("STRING", {"multiline": True, "default": ""}),
                "tempo_custom": ("STRING", {"multiline": True, "default": ""}),
                "interaction_mode_custom": ("STRING", {"multiline": True, "default": ""}),
                "primary_notes": ("STRING", {"multiline": True, "default": ""}),
                "secondary_notes": ("STRING", {"multiline": True, "default": ""}),
                "tempo_notes": ("STRING", {"multiline": True, "default": ""}),
                "interaction_notes": ("STRING", {"multiline": True, "default": ""}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("action_prompt", "action_summary", "director_notes", "preset_status")
    FUNCTION = "direct"
    CATEGORY = "NoxPrompter/Action"

    def direct(
        self,
        primary_action,
        secondary_action="None",
        tempo="Rising Momentum",
        interaction_mode="Solo Focus",
        props="",
        environment_beat="",
        intensity_descriptor="",
        camera_language="",
        sound_design="",
        dialogue_hook="",
        emotional_anchor="",
        risk_notes="",
        beat_emphasis="",
        primary_action_custom="",
        secondary_action_custom="",
        tempo_custom="",
        interaction_mode_custom="",
        primary_notes="",
        secondary_notes="",
        tempo_notes="",
        interaction_notes="",
        preset_action="none",
        preset_name="",
    ):
        config = {
            "primary_action": primary_action,
            "secondary_action": secondary_action,
            "tempo": tempo,
            "interaction_mode": interaction_mode,
            "props": props,
            "environment_beat": environment_beat,
            "intensity_descriptor": intensity_descriptor,
            "camera_language": camera_language,
            "sound_design": sound_design,
            "dialogue_hook": dialogue_hook,
            "emotional_anchor": emotional_anchor,
            "risk_notes": risk_notes,
            "beat_emphasis": beat_emphasis,
            "primary_action_custom": primary_action_custom,
            "secondary_action_custom": secondary_action_custom,
            "tempo_custom": tempo_custom,
            "interaction_mode_custom": interaction_mode_custom,
            "primary_notes": primary_notes,
            "secondary_notes": secondary_notes,
            "tempo_notes": tempo_notes,
            "interaction_notes": interaction_notes,
        }

        config, preset_status = self._apply_preset_action(
            "action_director",
            preset_action,
            preset_name,
            config,
        )

        primary_action = config.get("primary_action", primary_action)
        secondary_action = config.get("secondary_action", secondary_action)
        tempo = config.get("tempo", tempo)
        interaction_mode = config.get("interaction_mode", interaction_mode)
        props = config.get("props", props)
        environment_beat = config.get("environment_beat", environment_beat)
        intensity_descriptor = config.get("intensity_descriptor", intensity_descriptor)
        camera_language = config.get("camera_language", camera_language)
        sound_design = config.get("sound_design", sound_design)
        dialogue_hook = config.get("dialogue_hook", dialogue_hook)
        emotional_anchor = config.get("emotional_anchor", emotional_anchor)
        risk_notes = config.get("risk_notes", risk_notes)
        beat_emphasis = config.get("beat_emphasis", beat_emphasis)
        primary_action_custom = config.get("primary_action_custom", primary_action_custom)
        secondary_action_custom = config.get("secondary_action_custom", secondary_action_custom)
        tempo_custom = config.get("tempo_custom", tempo_custom)
        interaction_mode_custom = config.get("interaction_mode_custom", interaction_mode_custom)
        primary_notes = config.get("primary_notes", primary_notes)
        secondary_notes = config.get("secondary_notes", secondary_notes)
        tempo_notes = config.get("tempo_notes", tempo_notes)
        interaction_notes = config.get("interaction_notes", interaction_notes)

        primary_prompt, primary_summary = _resolve_action_option(primary_action, primary_action_custom, ACTION_PRIMARY_OPTIONS)
        secondary_prompt, secondary_summary = _resolve_action_option(secondary_action, secondary_action_custom, ACTION_SECONDARY_OPTIONS)
        tempo_prompt, tempo_summary = _resolve_action_option(tempo, tempo_custom, ACTION_TEMPO_OPTIONS)
        interaction_prompt, interaction_summary = _resolve_action_option(interaction_mode, interaction_mode_custom, ACTION_INTERACTION_OPTIONS)

        props_list = _split_tokens(props)
        beat_highlights = _split_tokens(beat_emphasis)
        risk_list = _split_tokens(risk_notes)

        prompt_parts = [primary_prompt]
        for fragment in (secondary_prompt, tempo_prompt, interaction_prompt):
            if fragment:
                prompt_parts.append(fragment)
        if intensity_descriptor.strip():
            prompt_parts.append(intensity_descriptor.strip())
        if emotional_anchor.strip():
            prompt_parts.append(f"emotional through-line: {emotional_anchor.strip()}")
        if props_list:
            prompt_parts.append("props in play: " + ", ".join(props_list))
        action_prompt = ", ".join(part for part in prompt_parts if part)
        if environment_beat.strip():
            action_prompt += f". Environment beat: {environment_beat.strip()}"
        if dialogue_hook.strip():
            action_prompt += f". Dialogue hook: {dialogue_hook.strip()}"

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
        if risk_list:
            summary_segments.append("Risks: " + ", ".join(risk_list))
        action_summary = " | ".join(segment for segment in summary_segments if segment)

        note_lines = []
        if beat_highlights:
            note_lines.append("Beat emphasis: " + ", ".join(beat_highlights))
        if camera_language.strip():
            note_lines.append("Camera: " + camera_language.strip())
        if sound_design.strip():
            note_lines.append("Sound design: " + sound_design.strip())
        if risk_list:
            note_lines.append("Safety: " + ", ".join(risk_list))
        if props_list:
            note_lines.append("Props check: " + ", ".join(props_list))
        if environment_beat.strip():
            note_lines.append("Environment: " + environment_beat.strip())
        if dialogue_hook.strip():
            note_lines.append("Dialogue: " + dialogue_hook.strip())
        if emotional_anchor.strip():
            note_lines.append("Emotional anchor: " + emotional_anchor.strip())
        director_notes = "\n".join(f"- {line}" for line in note_lines if line)

        return (action_prompt.strip(), action_summary, director_notes, preset_status)

__all__ = ["NoxPromptActionDirector"]
