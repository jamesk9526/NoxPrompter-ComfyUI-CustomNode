from __future__ import annotations

from typing import Any, Dict, List, Tuple
from ..common import PresetMixin, _resolve_with_custom, _split_tokens
from ..constants import *  # noqa: F403

class NoxPromptCamz(PresetMixin):
    """Author cam-stream ready prompts with adult-only safeguards and production notes."""

    @classmethod
    def INPUT_TYPES(cls):
        persona_keys = list(CAMZ_PERSONA_OPTIONS.keys()) + [CUSTOM_OPTION]
        stage_keys = list(CAMZ_STAGE_OPTIONS.keys()) + [CUSTOM_OPTION]
        camera_keys = list(CAMZ_CAMERA_OPTIONS.keys()) + [CUSTOM_OPTION]
        energy_keys = list(CAMZ_ENERGY_OPTIONS.keys()) + [CUSTOM_OPTION]

        return {
            "required": {
                "persona": (persona_keys, {"default": "Soft Glam Muse"}),
                "stage_theme": (stage_keys, {"default": "Velvet Boudoir"}),
                "camera_style": (camera_keys, {"default": "Intimate Close"}),
                "energy_profile": (energy_keys, {"default": "Gentle Sway"}),
            },
            "optional": {
                "wardrobe_style": ("STRING", {"multiline": True, "default": "silky lingerie set with sheer robe"}),
                "prop_list": ("STRING", {"multiline": True, "default": "vanity mirror, rose petals"}),
                "overlay_effects": ("STRING", {"multiline": True, "default": "tip goal ticker, soft sparkle particles"}),
                "chat_tone": ("STRING", {"multiline": True, "default": "sweet compliments, name drops, gratitude"}),
                "call_to_action": ("STRING", {"default": "invite viewers to join exclusive private show"}),
                "playlist_prompt": ("STRING", {"multiline": True, "default": "slow r&b, lo-fi chill"}),
                "camera_motions": ("STRING", {"multiline": True, "default": "slow zooms, minimal pans"}),
                "safety_focus": ("STRING", {"multiline": True, "default": "reinforce adult-only audience and mutual consent"}),
                "custom_persona": ("STRING", {"multiline": True, "default": ""}),
                "custom_stage": ("STRING", {"multiline": True, "default": ""}),
                "custom_camera": ("STRING", {"multiline": True, "default": ""}),
                "custom_energy": ("STRING", {"multiline": True, "default": ""}),
                "custom_negative": ("STRING", {"multiline": True, "default": ""}),
                "custom_safety_note": ("STRING", {"multiline": True, "default": ""}),
                "include_negative_baseline": ("BOOLEAN", {"default": True}),
                "include_safety_note": ("BOOLEAN", {"default": True}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("stream_prompt", "negative_prompt", "production_notes", "preset_status")
    FUNCTION = "stream"
    CATEGORY = "NoxPrompter/NSFW"

    def stream(
        self,
        persona,
        stage_theme,
        camera_style,
        energy_profile,
        wardrobe_style="",
        prop_list="",
        overlay_effects="",
        chat_tone="",
        call_to_action="",
        playlist_prompt="",
        camera_motions="",
        safety_focus="",
        custom_persona="",
        custom_stage="",
        custom_camera="",
        custom_energy="",
        custom_negative="",
        custom_safety_note="",
        include_negative_baseline=True,
        include_safety_note=True,
        preset_action="none",
        preset_name="",
    ):
        config = {
            "persona": persona,
            "stage_theme": stage_theme,
            "camera_style": camera_style,
            "energy_profile": energy_profile,
            "wardrobe_style": wardrobe_style,
            "prop_list": prop_list,
            "overlay_effects": overlay_effects,
            "chat_tone": chat_tone,
            "call_to_action": call_to_action,
            "playlist_prompt": playlist_prompt,
            "camera_motions": camera_motions,
            "safety_focus": safety_focus,
            "custom_persona": custom_persona,
            "custom_stage": custom_stage,
            "custom_camera": custom_camera,
            "custom_energy": custom_energy,
            "custom_negative": custom_negative,
            "custom_safety_note": custom_safety_note,
            "include_negative_baseline": include_negative_baseline,
            "include_safety_note": include_safety_note,
        }

        config, preset_status = self._apply_preset_action(
            "nox_camz",
            preset_action,
            preset_name,
            config,
        )

        persona = config.get("persona", persona)
        stage_theme = config.get("stage_theme", stage_theme)
        camera_style = config.get("camera_style", camera_style)
        energy_profile = config.get("energy_profile", energy_profile)
        wardrobe_style = config.get("wardrobe_style", wardrobe_style)
        prop_list = config.get("prop_list", prop_list)
        overlay_effects = config.get("overlay_effects", overlay_effects)
        chat_tone = config.get("chat_tone", chat_tone)
        call_to_action = config.get("call_to_action", call_to_action)
        playlist_prompt = config.get("playlist_prompt", playlist_prompt)
        camera_motions = config.get("camera_motions", camera_motions)
        safety_focus = config.get("safety_focus", safety_focus)
        custom_persona = config.get("custom_persona", custom_persona)
        custom_stage = config.get("custom_stage", custom_stage)
        custom_camera = config.get("custom_camera", custom_camera)
        custom_energy = config.get("custom_energy", custom_energy)
        custom_negative = config.get("custom_negative", custom_negative)
        custom_safety_note = config.get("custom_safety_note", custom_safety_note)
        include_negative_baseline = bool(config.get("include_negative_baseline", include_negative_baseline))
        include_safety_note = bool(config.get("include_safety_note", include_safety_note))

        persona_prompt, persona_note = _resolve_with_custom(persona, custom_persona, CAMZ_PERSONA_OPTIONS)
        stage_prompt, stage_note = _resolve_with_custom(stage_theme, custom_stage, CAMZ_STAGE_OPTIONS)
        camera_prompt, camera_note = _resolve_with_custom(camera_style, custom_camera, CAMZ_CAMERA_OPTIONS)
        energy_prompt, energy_note = _resolve_with_custom(energy_profile, custom_energy, CAMZ_ENERGY_OPTIONS)

        wardrobe_tokens = _split_tokens(wardrobe_style)
        prop_tokens = _split_tokens(prop_list)
        overlay_tokens = _split_tokens(overlay_effects)
        chat_tokens = _split_tokens(chat_tone)
        playlist_tokens = _split_tokens(playlist_prompt)
        motion_tokens = _split_tokens(camera_motions)

        positive_segments = [
            "4k streaming cam capture, 60fps fluidity, direct lens eye contact, cinematic webcam depth-of-field",
            persona_prompt,
            stage_prompt,
            camera_prompt,
            energy_prompt,
        ]

        if wardrobe_tokens:
            positive_segments.append("wardrobe focus: " + ", ".join(wardrobe_tokens))
        if prop_tokens:
            positive_segments.append("set dressing: " + ", ".join(prop_tokens))
        if overlay_tokens:
            positive_segments.append("live overlays: " + ", ".join(overlay_tokens))
        if chat_tokens:
            positive_segments.append("viewer interaction tone: " + ", ".join(chat_tokens))
        if playlist_tokens:
            positive_segments.append("audio bed: " + ", ".join(playlist_tokens))
        if motion_tokens:
            positive_segments.append("camera motions: " + ", ".join(motion_tokens))
        if call_to_action.strip():
            positive_segments.append(call_to_action.strip())

        stream_prompt = ", ".join(segment for segment in positive_segments if segment)

        negative_terms = []
        if include_negative_baseline:
            negative_terms.extend(NSFW_BASELINE_NEGATIVES)
        negative_terms.extend(_split_tokens(custom_negative))
        dedup_terms: List[str] = []
        seen_terms = set()
        for term in negative_terms:
            normalized = term.strip()
            if not normalized:
                continue
            key = normalized.lower()
            if key not in seen_terms:
                seen_terms.add(key)
                dedup_terms.append(normalized)
        if not dedup_terms:
            dedup_terms = list(NSFW_BASELINE_NEGATIVES)
        negative_prompt = ", ".join(dedup_terms)

        production_lines = []
        if persona_note:
            production_lines.append(f"Persona: {persona_note}")
        if stage_note:
            production_lines.append(f"Stage: {stage_note}")
        if camera_note:
            production_lines.append(f"Camera: {camera_note}")
        if energy_note:
            production_lines.append(f"Energy: {energy_note}")
        if overlay_tokens:
            production_lines.append("Overlay cues: " + ", ".join(overlay_tokens))
        if playlist_tokens:
            production_lines.append("Playlist: " + ", ".join(playlist_tokens))
        if motion_tokens:
            production_lines.append("Camera moves: " + ", ".join(motion_tokens))
        if safety_focus.strip():
            production_lines.append("Safety focus: " + safety_focus.strip())
        if call_to_action.strip():
            production_lines.append("CTA: " + call_to_action.strip())

        safety_lines = []
        if include_safety_note:
            safety_lines.append("For consenting adult audiences only. Verify age compliance and platform rules before streaming.")
        if custom_safety_note.strip():
            safety_lines.append(custom_safety_note.strip())
        if safety_lines:
            production_lines.append("Safety: " + " | ".join(safety_lines))

        production_notes = "\n".join(production_lines)

        return (
            stream_prompt.strip(),
            negative_prompt,
            production_notes,
            preset_status,
        )

__all__ = ["NoxPromptCamz"]
