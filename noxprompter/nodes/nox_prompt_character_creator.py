from __future__ import annotations

from ..common import PresetMixin, _resolve_option, option_keys, _split_tokens
from ..constants import (
    CHARACTER_ALIGNMENT_OPTIONS,
    CHARACTER_ARCHETYPE_OPTIONS,
    CHARACTER_BODY_TYPE_OPTIONS,
    CHARACTER_ERA_OPTIONS,
    CHARACTER_POWER_SOURCE_OPTIONS,
    CHARACTER_PROFESSION_OPTIONS,
    CHARACTER_ROLE_OPTIONS,
    CHARACTER_SIGNATURE_GEAR_OPTIONS,
    CHARACTER_SPECIES_OPTIONS,
    CHARACTER_TEMPERAMENT_OPTIONS,
    CHARACTER_VISUAL_MOTIF_OPTIONS,
)

class NoxPromptCharacterCreator(PresetMixin):
    """Build richly-detailed character prompts and quick-reference sheets."""

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
                "species": (
                    option_keys(CHARACTER_SPECIES_OPTIONS),
                    {"default": "Human"},
                ),
                "archetype": (
                    option_keys(CHARACTER_ARCHETYPE_OPTIONS),
                    {"default": "Champion"},
                ),
                "profession": (
                    option_keys(CHARACTER_PROFESSION_OPTIONS),
                    {"default": "Starship Captain"},
                ),
            },
            "optional": {
                "temperament": (
                    option_keys(CHARACTER_TEMPERAMENT_OPTIONS),
                    {"default": "Stoic"},
                ),
                "power_source": (
                    option_keys(CHARACTER_POWER_SOURCE_OPTIONS),
                    {"default": "Arcane Relic"},
                ),
                "signature_gear": (
                    option_keys(CHARACTER_SIGNATURE_GEAR_OPTIONS),
                    {"default": "Living Blade"},
                ),
                "visual_motif": (
                    option_keys(CHARACTER_VISUAL_MOTIF_OPTIONS),
                    {"default": "Solar Flare"},
                ),
                "era": (
                    option_keys(CHARACTER_ERA_OPTIONS),
                    {"default": "Mythic Age"},
                ),
                "body_type": (
                    option_keys(CHARACTER_BODY_TYPE_OPTIONS),
                    {"default": "Athletic"},
                ),
                "alignment": (
                    option_keys(CHARACTER_ALIGNMENT_OPTIONS),
                    {"default": "Lawful Good"},
                ),
                "team_role": (
                    option_keys(CHARACTER_ROLE_OPTIONS),
                    {"default": "Party Leader"},
                ),
                "catchphrase": ("STRING", {"default": ""}),
                "signature_move": ("STRING", {"default": ""}),
                "backstory_snippet": ("STRING", {"multiline": True, "default": ""}),
                "custom_traits": ("STRING", {"multiline": True, "default": ""}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                "presence_rating": ("FLOAT", {"default": 0.75, "min": 0.0, "max": 1.0, "step": 0.05}),
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
        custom_prompt: str = "",
        species: str = "Human",
        archetype: str = "Champion",
        profession: str = "Starship Captain",
        temperament: str = "Stoic",
        power_source: str = "Arcane Relic",
        signature_gear: str = "Living Blade",
        visual_motif: str = "Solar Flare",
        era: str = "Mythic Age",
        body_type: str = "Athletic",
        alignment: str = "Lawful Good",
        team_role: str = "Party Leader",
        catchphrase: str = "",
        signature_move: str = "",
        backstory_snippet: str = "",
        custom_traits: str = "",
        negative_prompt: str = "",
        presence_rating: float = 0.75,
        preset_action: str = "none",
        preset_name: str = "",
    ):
        config = {
            "custom_prompt": custom_prompt,
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

        custom_prompt = config.get("custom_prompt", custom_prompt)
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
        catchphrase = config.get("catchphrase", catchphrase)
        signature_move = config.get("signature_move", signature_move)
        backstory_snippet = config.get("backstory_snippet", backstory_snippet)
        custom_traits = config.get("custom_traits", custom_traits)
        negative_prompt = config.get("negative_prompt", negative_prompt)
        presence_rating = float(config.get("presence_rating", presence_rating))
        species_prompt, species_notes = _resolve_option(species, CHARACTER_SPECIES_OPTIONS)
        archetype_prompt, archetype_notes = _resolve_option(archetype, CHARACTER_ARCHETYPE_OPTIONS)
        profession_prompt, profession_notes = _resolve_option(profession, CHARACTER_PROFESSION_OPTIONS)
        temperament_prompt, temperament_notes = _resolve_option(temperament, CHARACTER_TEMPERAMENT_OPTIONS)
        power_prompt, power_notes = _resolve_option(power_source, CHARACTER_POWER_SOURCE_OPTIONS)
        gear_prompt, gear_notes = _resolve_option(signature_gear, CHARACTER_SIGNATURE_GEAR_OPTIONS)
        motif_prompt, motif_notes = _resolve_option(visual_motif, CHARACTER_VISUAL_MOTIF_OPTIONS)
        era_prompt, era_notes = _resolve_option(era, CHARACTER_ERA_OPTIONS)
        body_prompt, body_notes = _resolve_option(body_type, CHARACTER_BODY_TYPE_OPTIONS)
        alignment_prompt, alignment_notes = _resolve_option(alignment, CHARACTER_ALIGNMENT_OPTIONS)
        role_prompt, role_notes = _resolve_option(team_role, CHARACTER_ROLE_OPTIONS)

        def _fallback(selection: str, prompt: str) -> str:
            cleaned_prompt = (prompt or "").strip()
            if cleaned_prompt:
                return cleaned_prompt
            selection_text = (selection or "").strip()
            if selection_text.lower() == "none":
                return ""
            return selection_text

        species_text = _fallback(species, species_prompt)
        archetype_text = _fallback(archetype, archetype_prompt)
        profession_text = _fallback(profession, profession_prompt)
        temperament_text = _fallback(temperament, temperament_prompt)
        power_text = _fallback(power_source, power_prompt)
        gear_text = _fallback(signature_gear, gear_prompt)
        motif_text = _fallback(visual_motif, motif_prompt)
        era_text = _fallback(era, era_prompt)
        body_text = _fallback(body_type, body_prompt)
        alignment_text = _fallback(alignment, alignment_prompt)
        role_text = _fallback(team_role, role_prompt)

        traits = _split_tokens(custom_traits)
        trait_prompt = ", ".join(traits)

        presence_descriptor = self._describe_presence(presence_rating)

        custom_fragment = (custom_prompt or "").strip()

        prompt_parts = [custom_fragment] if custom_fragment else []
        prompt_parts.extend(
            [
                species_text,
                body_text,
                archetype_text,
                profession_text,
                temperament_text,
                power_text,
                motif_text,
                gear_text,
                alignment_text,
                role_text,
            ]
        )
        prompt_parts.extend(
            [
                f"signature move: {signature_move.strip()}" if signature_move.strip() else "",
                f"operates during {era_text}" if era_text else "",
                trait_prompt,
                f"presence reads as {presence_descriptor}",
            ]
        )

        character_prompt = ", ".join(part for part in prompt_parts if part).strip()
        if backstory_snippet.strip():
            character_prompt = f"{character_prompt}. {backstory_snippet.strip()}" if character_prompt else backstory_snippet.strip()
        if character_prompt and character_prompt[-1] not in ".!?":
            character_prompt += "."

        sheet_lines = [
            f"Species Notes: {species_notes}" if species_notes else (f"Species: {species_text}" if species_text else ""),
            f"Archetype Notes: {archetype_notes}" if archetype_notes else (f"Archetype: {archetype_text}" if archetype_text else ""),
            f"Profession Notes: {profession_notes}" if profession_notes else (f"Profession: {profession_text}" if profession_text else ""),
            f"Temperament: {temperament_notes}" if temperament_notes else (f"Temperament: {temperament_text}" if temperament_text else ""),
            f"Power Source: {power_notes}" if power_notes else (f"Power Source: {power_text}" if power_text else ""),
            f"Signature Gear: {gear_notes}" if gear_notes else (f"Signature Gear: {gear_text}" if gear_text else ""),
            f"Visual Motif: {motif_notes}" if motif_notes else (f"Visual Motif: {motif_text}" if motif_text else ""),
            f"Era Context: {era_notes}" if era_notes else (f"Era: {era_text}" if era_text else ""),
            f"Body Type: {body_notes}" if body_notes else (f"Body Type: {body_text}" if body_text else ""),
            f"Alignment: {alignment_notes}" if alignment_notes else (f"Alignment: {alignment_text}" if alignment_text else ""),
            f"Team Role: {role_notes}" if role_notes else (f"Team Role: {role_text}" if role_text else ""),
        ]
        if traits:
            sheet_lines.append("Distinct Traits: " + ", ".join(traits))

        character_sheet = " | ".join(line for line in sheet_lines if line)

        hooks = [
            f"Catchphrase: \"{catchphrase.strip()}\"" if catchphrase.strip() else "",
            f"Signature Move: {signature_move.strip()}" if signature_move.strip() else "",
            f"Team Role: {role_text}" if role_text else "",
            f"Alignment: {alignment_text}" if alignment_text else "",
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
