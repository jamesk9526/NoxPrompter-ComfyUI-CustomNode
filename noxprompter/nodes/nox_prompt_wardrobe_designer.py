from __future__ import annotations

from typing import Any, Dict, List, Tuple
from ..common import PresetMixin, _resolve_with_custom, _split_tokens, _format_notes
from ..constants import *  # noqa: F403

class NoxPromptWardrobeDesigner(PresetMixin):
    """Generate advanced wardrobe breakdowns with styling guidance."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_garment": (list(WARDROBE_BASE_GARMENT_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Battle Dress"}),
                "silhouette": (list(WARDROBE_SILHOUETTE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "A-Line"}),
                "colorway": (list(WARDROBE_COLORWAY_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Monochrome Obsidian"}),
            },
            "optional": {
                "layering": (list(WARDROBE_LAYER_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Armor Plating"}),
                "fabric": (list(WARDROBE_FABRIC_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Ballistic Weave"}),
                "pattern": (list(WARDROBE_PATTERN_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Fractal"}),
                "wear_state": (list(WARDROBE_WEAR_STATE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Battle-Worn"}),
                "culture_inspiration": (list(WARDROBE_CULTURE_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Solar Court"}),
                "footwear": (list(WARDROBE_FOOTWEAR_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Combat Boots"}),
                "primary_accessory": (list(WARDROBE_ACCESSORY_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Relic Pendant"}),
                "secondary_accessory": (list(WARDROBE_ACCESSORY_OPTIONS.keys()) + [CUSTOM_OPTION], {"default": "Utility Belt"}),
                "functional_focus": ("STRING", {"default": ""}),
                "accent_materials": ("STRING", {"multiline": True, "default": ""}),
                "motion_considerations": ("STRING", {"multiline": True, "default": ""}),
                "finishing_details": ("STRING", {"multiline": True, "default": ""}),
                "additional_accessories": ("STRING", {"multiline": True, "default": ""}),
                "base_garment_custom": ("STRING", {"default": ""}),
                "silhouette_custom": ("STRING", {"default": ""}),
                "colorway_custom": ("STRING", {"default": ""}),
                "layering_custom": ("STRING", {"default": ""}),
                "fabric_custom": ("STRING", {"default": ""}),
                "pattern_custom": ("STRING", {"default": ""}),
                "wear_state_custom": ("STRING", {"default": ""}),
                "culture_inspiration_custom": ("STRING", {"default": ""}),
                "footwear_custom": ("STRING", {"default": ""}),
                "primary_accessory_custom": ("STRING", {"default": ""}),
                "secondary_accessory_custom": ("STRING", {"default": ""}),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("wardrobe_prompt", "styling_notes", "accessory_list", "preset_status")
    FUNCTION = "design"
    CATEGORY = "NoxPrompter/Wardrobe"

    def design(
        self,
        base_garment,
        silhouette,
        colorway,
        layering="Armor Plating",
        fabric="Ballistic Weave",
        pattern="Fractal",
        wear_state="Battle-Worn",
        culture_inspiration="Solar Court",
        footwear="Combat Boots",
        primary_accessory="Relic Pendant",
        secondary_accessory="Utility Belt",
        functional_focus="",
        accent_materials="",
        motion_considerations="",
        finishing_details="",
        additional_accessories="",
        base_garment_custom="",
        silhouette_custom="",
        colorway_custom="",
        layering_custom="",
        fabric_custom="",
        pattern_custom="",
        wear_state_custom="",
        culture_inspiration_custom="",
        footwear_custom="",
        primary_accessory_custom="",
        secondary_accessory_custom="",
        preset_action="none",
        preset_name="",
    ):
        config = {
            "base_garment": base_garment,
            "silhouette": silhouette,
            "colorway": colorway,
            "layering": layering,
            "fabric": fabric,
            "pattern": pattern,
            "wear_state": wear_state,
            "culture_inspiration": culture_inspiration,
            "footwear": footwear,
            "primary_accessory": primary_accessory,
            "secondary_accessory": secondary_accessory,
            "functional_focus": functional_focus,
            "accent_materials": accent_materials,
            "motion_considerations": motion_considerations,
            "finishing_details": finishing_details,
            "additional_accessories": additional_accessories,
            "base_garment_custom": base_garment_custom,
            "silhouette_custom": silhouette_custom,
            "colorway_custom": colorway_custom,
            "layering_custom": layering_custom,
            "fabric_custom": fabric_custom,
            "pattern_custom": pattern_custom,
            "wear_state_custom": wear_state_custom,
            "culture_inspiration_custom": culture_inspiration_custom,
            "footwear_custom": footwear_custom,
            "primary_accessory_custom": primary_accessory_custom,
            "secondary_accessory_custom": secondary_accessory_custom,
        }

        config, preset_status = self._apply_preset_action(
            "wardrobe_designer",
            preset_action,
            preset_name,
            config,
        )

        base_garment = config.get("base_garment", base_garment)
        silhouette = config.get("silhouette", silhouette)
        colorway = config.get("colorway", colorway)
        layering = config.get("layering", layering)
        fabric = config.get("fabric", fabric)
        pattern = config.get("pattern", pattern)
        wear_state = config.get("wear_state", wear_state)
        culture_inspiration = config.get("culture_inspiration", culture_inspiration)
        footwear = config.get("footwear", footwear)
        primary_accessory = config.get("primary_accessory", primary_accessory)
        secondary_accessory = config.get("secondary_accessory", secondary_accessory)
        functional_focus = config.get("functional_focus", functional_focus)
        accent_materials = config.get("accent_materials", accent_materials)
        motion_considerations = config.get("motion_considerations", motion_considerations)
        finishing_details = config.get("finishing_details", finishing_details)
        additional_accessories = config.get("additional_accessories", additional_accessories)
        base_garment_custom = config.get("base_garment_custom", base_garment_custom)
        silhouette_custom = config.get("silhouette_custom", silhouette_custom)
        colorway_custom = config.get("colorway_custom", colorway_custom)
        layering_custom = config.get("layering_custom", layering_custom)
        fabric_custom = config.get("fabric_custom", fabric_custom)
        pattern_custom = config.get("pattern_custom", pattern_custom)
        wear_state_custom = config.get("wear_state_custom", wear_state_custom)
        culture_inspiration_custom = config.get("culture_inspiration_custom", culture_inspiration_custom)
        footwear_custom = config.get("footwear_custom", footwear_custom)
        primary_accessory_custom = config.get("primary_accessory_custom", primary_accessory_custom)
        secondary_accessory_custom = config.get("secondary_accessory_custom", secondary_accessory_custom)

        base_prompt, base_notes = _resolve_with_custom(base_garment, base_garment_custom, WARDROBE_BASE_GARMENT_OPTIONS)
        silhouette_prompt, silhouette_notes = _resolve_with_custom(silhouette, silhouette_custom, WARDROBE_SILHOUETTE_OPTIONS)
        color_prompt, color_notes = _resolve_with_custom(colorway, colorway_custom, WARDROBE_COLORWAY_OPTIONS)
        layering_prompt, layering_notes = _resolve_with_custom(layering, layering_custom, WARDROBE_LAYER_OPTIONS)
        fabric_prompt, fabric_notes = _resolve_with_custom(fabric, fabric_custom, WARDROBE_FABRIC_OPTIONS)
        pattern_prompt, pattern_notes = _resolve_with_custom(pattern, pattern_custom, WARDROBE_PATTERN_OPTIONS)
        wear_prompt, wear_notes = _resolve_with_custom(wear_state, wear_state_custom, WARDROBE_WEAR_STATE_OPTIONS)
        culture_prompt, culture_notes = _resolve_with_custom(culture_inspiration, culture_inspiration_custom, WARDROBE_CULTURE_OPTIONS)
        footwear_prompt, footwear_notes = _resolve_with_custom(footwear, footwear_custom, WARDROBE_FOOTWEAR_OPTIONS)
        primary_prompt, primary_notes = _resolve_with_custom(primary_accessory, primary_accessory_custom, WARDROBE_ACCESSORY_OPTIONS)
        secondary_prompt, secondary_notes = _resolve_with_custom(secondary_accessory, secondary_accessory_custom, WARDROBE_ACCESSORY_OPTIONS)

        accent_list = _split_tokens(accent_materials)
        motion_list = _split_tokens(motion_considerations)
        finishing_list = _split_tokens(finishing_details)
        extra_accessories = _split_tokens(additional_accessories)

        wardrobe_prompt_parts = [
            base_prompt,
            silhouette_prompt,
            fabric_prompt,
            layering_prompt,
            color_prompt,
            pattern_prompt,
            wear_prompt,
            culture_prompt,
            footwear_prompt,
        ]
        if accent_list:
            wardrobe_prompt_parts.append("accents: " + ", ".join(accent_list))
        if finishing_list:
            wardrobe_prompt_parts.append("finishing: " + ", ".join(finishing_list))

        wardrobe_prompt = ", ".join(part for part in wardrobe_prompt_parts if part).strip()
        if wardrobe_prompt and wardrobe_prompt[-1] not in ".!?":
            wardrobe_prompt += "."
        if functional_focus.strip():
            wardrobe_prompt += f" Functional focus: {functional_focus.strip()}."
        if motion_list:
            wardrobe_prompt += f" Movement considerations: {', '.join(motion_list)}."

        styling_segments = [
            _format_notes("Base", base_notes, base_prompt),
            _format_notes("Silhouette", silhouette_notes, silhouette_prompt),
            _format_notes("Fabric", fabric_notes, fabric_prompt),
            _format_notes("Layering", layering_notes, layering_prompt),
            _format_notes("Colorway", color_notes, color_prompt),
            _format_notes("Pattern", pattern_notes, pattern_prompt),
            _format_notes("Wear State", wear_notes, wear_prompt),
            _format_notes("Culture", culture_notes, culture_prompt),
            _format_notes("Footwear", footwear_notes, footwear_prompt),
        ]
        styling_notes = " | ".join(segment for segment in styling_segments if segment)

        accessory_items = [
            primary_prompt,
            secondary_prompt if secondary_accessory else "",
        ]
        accessory_notes = [note for note in [primary_notes, secondary_notes] if note]
        if extra_accessories:
            accessory_items.append("Additional: " + ", ".join(extra_accessories))
        accessory_list = " | ".join(item for item in accessory_items if item)
        if accessory_notes:
            accessory_list += (" | Notes: " + "; ".join(accessory_notes)) if accessory_list else "Notes: " + "; ".join(accessory_notes)

        return (wardrobe_prompt, styling_notes, accessory_list, preset_status)

__all__ = ["NoxPromptWardrobeDesigner"]
