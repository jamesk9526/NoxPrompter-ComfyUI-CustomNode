from __future__ import annotations

from typing import Any, Dict, List, Tuple
from ..common import PresetMixin, _resolve_with_custom, _split_tokens
from ..constants import *  # noqa: F403

class NoxPromptCharacterCreator(PresetMixin):
    """Build richly-detailed character prompts and quick-reference sheets."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "species": (list(CHARACTER_SPECIES_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Human"}),
                "archetype": (list(CHARACTER_ARCHETYPE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Champion"}),
                "profession": (list(CHARACTER_PROFESSION_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Starship Captain"}),
            },
            "optional": {
                "temperament": (list(CHARACTER_TEMPERAMENT_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Stoic"}),
                "power_source": (list(CHARACTER_POWER_SOURCE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Arcane Relic"}),
                "signature_gear": (list(CHARACTER_SIGNATURE_GEAR_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Living Blade"}),
                "visual_motif": (list(CHARACTER_VISUAL_MOTIF_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Solar Flare"}),
                "era": (list(CHARACTER_ERA_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Mythic Age"}),
                "body_type": (list(CHARACTER_BODY_TYPE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Athletic"}),
                "alignment": (list(CHARACTER_ALIGNMENT_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Lawful Good"}),
                "team_role": (list(CHARACTER_ROLE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Party Leader"}),
                "catchphrase": ("STRING", {"default": ""}),
                "signature_move": ("STRING", {"default": ""}),
                "backstory_snippet": ("STRING", {"multiline": True, "default": ""}),
                "custom_traits": ("STRING", {"multiline": True, "default": ""}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                "presence_rating": ("FLOAT", {"default": 0.75, "min": 0.0, "max": 1.0, "step": 0.05}),
                "species_custom": ("STRING", {"default": ""}),
                "archetype_custom": ("STRING", {"default": ""}),
                "profession_custom": ("STRING", {"default": ""}),
                "temperament_custom": ("STRING", {"default": ""}),
                "power_source_custom": ("STRING", {"default": ""}),
                "signature_gear_custom": ("STRING", {"default": ""}),
                "visual_motif_custom": ("STRING", {"default": ""}),
                "era_custom": ("STRING", {"default": ""}),
                "body_type_custom": ("STRING", {"default": ""}),
                "alignment_custom": ("STRING", {"default": ""}),
                "team_role_custom": ("STRING", {"default": ""}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("character_prompt", "character_sheet", "story_hooks", "preset_status")
    FUNCTION = "craft"
    CATEGORY = "NoxPrompter/Character"

    def craft(
        self,
        species,
        archetype,
        profession,
        temperament="Stoic",
        power_source="Arcane Relic",
        signature_gear="Living Blade",
        visual_motif="Solar Flare",
        era="Mythic Age",
        body_type="Athletic",
        alignment="Lawful Good",
        team_role="Party Leader",
        species_custom="",
        archetype_custom="",
        profession_custom="",
        temperament_custom="",
        power_source_custom="",
        signature_gear_custom="",
        visual_motif_custom="",
        era_custom="",
        body_type_custom="",
        alignment_custom="",
        team_role_custom="",
        catchphrase="",
        signature_move="",
        backstory_snippet="",
        custom_traits="",
        negative_prompt="",
        presence_rating=0.75,
        preset_action="none",
        preset_name="",
    ):
        config = {
            "species": species,
            "archetype": archetype,
            "profession": profession,
            "temperament": temperament,
            "power_source": power_source,
            "signature_gear": signature_gear,
            "visual_motif": visual_motif,
            "era": era,
            "body_type": body_type,
            "alignment": alignment,
            "team_role": team_role,
            "species_custom": species_custom,
            "archetype_custom": archetype_custom,
            "profession_custom": profession_custom,
            "temperament_custom": temperament_custom,
            "power_source_custom": power_source_custom,
            "signature_gear_custom": signature_gear_custom,
            "visual_motif_custom": visual_motif_custom,
            "era_custom": era_custom,
            "body_type_custom": body_type_custom,
            "alignment_custom": alignment_custom,
            "team_role_custom": team_role_custom,
            "catchphrase": catchphrase,
            "signature_move": signature_move,
            "backstory_snippet": backstory_snippet,
            "custom_traits": custom_traits,
            "negative_prompt": negative_prompt,
            "presence_rating": presence_rating,
        }

        config, preset_status = self._apply_preset_action(
            "character_creator",
            preset_action,
            preset_name,
            config,
        )

        species = config.get("species", species)
        archetype = config.get("archetype", archetype)
        profession = config.get("profession", profession)
        temperament = config.get("temperament", temperament)
        power_source = config.get("power_source", power_source)
        signature_gear = config.get("signature_gear", signature_gear)
        visual_motif = config.get("visual_motif", visual_motif)
        era = config.get("era", era)
        body_type = config.get("body_type", body_type)
        alignment = config.get("alignment", alignment)
        team_role = config.get("team_role", team_role)
        species_custom = config.get("species_custom", species_custom)
        archetype_custom = config.get("archetype_custom", archetype_custom)
        profession_custom = config.get("profession_custom", profession_custom)
        temperament_custom = config.get("temperament_custom", temperament_custom)
        power_source_custom = config.get("power_source_custom", power_source_custom)
        signature_gear_custom = config.get("signature_gear_custom", signature_gear_custom)
        visual_motif_custom = config.get("visual_motif_custom", visual_motif_custom)
        era_custom = config.get("era_custom", era_custom)
        body_type_custom = config.get("body_type_custom", body_type_custom)
        alignment_custom = config.get("alignment_custom", alignment_custom)
        team_role_custom = config.get("team_role_custom", team_role_custom)
        catchphrase = config.get("catchphrase", catchphrase)
        signature_move = config.get("signature_move", signature_move)
        backstory_snippet = config.get("backstory_snippet", backstory_snippet)
        custom_traits = config.get("custom_traits", custom_traits)
        negative_prompt = config.get("negative_prompt", negative_prompt)
        presence_rating = float(config.get("presence_rating", presence_rating))
        species_prompt, species_notes = _resolve_with_custom(species, species_custom, CHARACTER_SPECIES_OPTIONS)
        archetype_prompt, archetype_notes = _resolve_with_custom(archetype, archetype_custom, CHARACTER_ARCHETYPE_OPTIONS)
        profession_prompt, profession_notes = _resolve_with_custom(profession, profession_custom, CHARACTER_PROFESSION_OPTIONS)
        temperament_prompt, temperament_notes = _resolve_with_custom(temperament, temperament_custom, CHARACTER_TEMPERAMENT_OPTIONS)
        power_prompt, power_notes = _resolve_with_custom(power_source, power_source_custom, CHARACTER_POWER_SOURCE_OPTIONS)
        gear_prompt, gear_notes = _resolve_with_custom(signature_gear, signature_gear_custom, CHARACTER_SIGNATURE_GEAR_OPTIONS)
        motif_prompt, motif_notes = _resolve_with_custom(visual_motif, visual_motif_custom, CHARACTER_VISUAL_MOTIF_OPTIONS)
        era_prompt, era_notes = _resolve_with_custom(era, era_custom, CHARACTER_ERA_OPTIONS)
        body_prompt, body_notes = _resolve_with_custom(body_type, body_type_custom, CHARACTER_BODY_TYPE_OPTIONS)
        alignment_prompt, alignment_notes = _resolve_with_custom(alignment, alignment_custom, CHARACTER_ALIGNMENT_OPTIONS)
        role_prompt, role_notes = _resolve_with_custom(team_role, team_role_custom, CHARACTER_ROLE_OPTIONS)

        traits = _split_tokens(custom_traits)
        trait_prompt = ", ".join(traits)

        presence_descriptor = self._describe_presence(presence_rating)

        prompt_parts = [
            species_prompt,
            body_prompt,
            archetype_prompt,
            profession_prompt,
            temperament_prompt,
            power_prompt,
            motif_prompt,
            gear_prompt,
            alignment_prompt,
            role_prompt,
            f"signature move: {signature_move.strip()}" if signature_move.strip() else "",
            f"operates during {era_prompt}" if era_prompt else "",
            trait_prompt,
            f"presence reads as {presence_descriptor}",
        ]

        character_prompt = ", ".join(part for part in prompt_parts if part).strip()
        if backstory_snippet.strip():
            character_prompt = f"{character_prompt}. {backstory_snippet.strip()}" if character_prompt else backstory_snippet.strip()
        if character_prompt and character_prompt[-1] not in ".!?":
            character_prompt += "."

        sheet_lines = [
            f"Species Notes: {species_notes}" if species_notes else "",
            f"Archetype Notes: {archetype_notes}" if archetype_notes else "",
            f"Profession Notes: {profession_notes}" if profession_notes else "",
            f"Temperament: {temperament_notes}" if temperament_notes else "",
            f"Power Source: {power_notes}" if power_notes else "",
            f"Signature Gear: {gear_notes}" if gear_notes else "",
            f"Visual Motif: {motif_notes}" if motif_notes else "",
            f"Era Context: {era_notes}" if era_notes else "",
            f"Body Type: {body_notes}" if body_notes else "",
            f"Alignment: {alignment_notes}" if alignment_notes else "",
            f"Team Role: {role_notes}" if role_notes else "",
        ]
        if traits:
            sheet_lines.append("Distinct Traits: " + ", ".join(traits))

        character_sheet = " | ".join(line for line in sheet_lines if line)

        hooks = [
            f"Catchphrase: \"{catchphrase.strip()}\"" if catchphrase.strip() else "",
            f"Signature Move: {signature_move.strip()}" if signature_move.strip() else "",
            f"Team Role: {team_role}" if team_role else "",
            f"Alignment: {alignment}" if alignment else "",
            f"Presence Rating: {presence_rating:.2f} ({presence_descriptor})",
        ]
        if negative_prompt.strip():
            hooks.append("Avoid: " + negative_prompt.strip())
        story_hooks = " | ".join(item for item in hooks if item)

        return (character_prompt, character_sheet, story_hooks, preset_status)

    def _describe_presence(self, value: float) -> str:
        clamped = max(0.0, min(1.0, value))
        if clamped < 0.15:
            return "whisper-soft aura"
        if clamped < 0.35:
            return "subtle undercurrent"
        if clamped < 0.55:
            return "balanced presence"
        if clamped < 0.75:
            return "commanding focus"
        if clamped < 0.9:
            return "formidable charisma"
        return "legendary gravitas"

__all__ = ["NoxPromptCharacterCreator"]
