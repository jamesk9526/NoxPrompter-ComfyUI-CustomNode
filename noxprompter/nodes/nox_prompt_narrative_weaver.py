from __future__ import annotations

from typing import Any, Dict, List, Tuple
from ..common import PresetMixin
from ..constants import *  # noqa: F403

class NoxPromptNarrativeWeaver(PresetMixin):
    """Craft narrative scaffolding for the prompt builder."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "hero_archetype": (list(NARRATIVE_ARCHETYPES.keys()), {"default": "Resolute Protector"}),
                "story_tone": (list(NARRATIVE_TONES.keys()), {"default": "Hopeful Resurgence"}),
                "environment": (list(NARRATIVE_ENVIRONMENTS.keys()), {"default": "Rain-Soaked Citadel"}),
            },
            "optional": {
                "set_piece": (list(NARRATIVE_SETPIECES.keys()), {"default": "Climactic Duel"}),
                "tempo": (list(TEMPO_PROFILES.keys()), {"default": "surging"}),
                "focus_detail": ("STRING", {"multiline": True, "default": ""}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = (
        "subject_focus",
        "scene_setting",
        "motion_arc",
        "narrative_hook",
        "extra_descriptors",
        "preset_status",
    )
    FUNCTION = "weave"
    CATEGORY = "NoxPrompter/Companions"

    def weave(
        self,
        hero_archetype,
        story_tone,
        environment,
        set_piece="Climactic Duel",
        tempo="surging",
        focus_detail="",
        preset_action="none",
        preset_name="",
    ):
        config = {
            "hero_archetype": hero_archetype,
            "story_tone": story_tone,
            "environment": environment,
            "set_piece": set_piece,
            "tempo": tempo,
            "focus_detail": focus_detail,
        }

        config, preset_status = self._apply_preset_action(
            "narrative_weaver",
            preset_action,
            preset_name,
            config,
        )

        hero_archetype = config.get("hero_archetype", "Resolute Protector")
        story_tone = config.get("story_tone", "Hopeful Resurgence")
        environment = config.get("environment", "Rain-Soaked Citadel")
        set_piece = config.get("set_piece", "Climactic Duel")
        tempo = config.get("tempo", "surging")
        focus_detail = config.get("focus_detail", "")

        archetype = NARRATIVE_ARCHETYPES.get(hero_archetype, {"subject": hero_archetype, "keywords": []})
        tone = NARRATIVE_TONES.get(story_tone, {"descriptor": story_tone, "ambience": "", "hook": "", "keywords": []})
        env = NARRATIVE_ENVIRONMENTS.get(environment, {"description": environment, "details": "", "keywords": []})
        setpiece = NARRATIVE_SETPIECES.get(set_piece, {"motion": set_piece, "hook": "", "keywords": []})
        tempo_cfg = TEMPO_PROFILES.get(tempo, TEMPO_PROFILES["measured build"])

        subject_parts = [archetype.get("subject", "")]
        if tempo_cfg.get("subject_accent"):
            subject_parts.append(tempo_cfg["subject_accent"])
        if tone.get("descriptor"):
            subject_parts.append(tone["descriptor"])
        subject_focus = ", ".join(part for part in subject_parts if part).strip(", ")

        scene_parts = [env.get("description", ""), env.get("details", ""), tone.get("ambience", "")]
        scene_setting = ", ".join(part for part in scene_parts if part).strip(", ")

        motion_parts = [tempo_cfg.get("motion_prefix"), setpiece.get("motion"), tempo_cfg.get("motion_suffix")]
        motion_arc = " ".join(part.strip() for part in motion_parts if part and part.strip())

        hook_parts = [tone.get("hook"), setpiece.get("hook"), tempo_cfg.get("hook_suffix")]
        narrative_hook = " ".join(part.strip() for part in hook_parts if part and part.strip())

        descriptor_sources = [
            archetype.get("keywords", []),
            tone.get("keywords", []),
            env.get("keywords", []),
            setpiece.get("keywords", []),
            tempo_cfg.get("keywords", []),
        ]
        if focus_detail.strip():
            descriptor_sources.append(self._split_keywords(focus_detail))

        descriptors = []
        for source in descriptor_sources:
            descriptors.extend(source)
        descriptors = list(dict.fromkeys(desc.strip() for desc in descriptors if desc and desc.strip()))
        extra_descriptors = ", ".join(descriptors)

        return (
            subject_focus,
            scene_setting,
            motion_arc,
            narrative_hook,
            extra_descriptors,
            preset_status,
        )

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

__all__ = ["NoxPromptNarrativeWeaver"]
