from __future__ import annotations

from ..common import PresetMixin, _resolve_option, option_keys, _split_tokens, _format_notes
from ..constants import (
    WARDROBE_ACCESSORY_OPTIONS,
    WARDROBE_BASE_GARMENT_OPTIONS,
    WARDROBE_COLORWAY_OPTIONS,
    WARDROBE_CULTURE_OPTIONS,
    WARDROBE_FABRIC_OPTIONS,
    WARDROBE_FOOTWEAR_OPTIONS,
    WARDROBE_LAYER_OPTIONS,
    WARDROBE_PATTERN_OPTIONS,
    WARDROBE_SILHOUETTE_OPTIONS,
    WARDROBE_WEAR_STATE_OPTIONS,
)

class NoxPromptWardrobeDesigner(PresetMixin):
    """Generate advanced wardrobe breakdowns with styling guidance."""

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
                "base_garment": (
                    option_keys(WARDROBE_BASE_GARMENT_OPTIONS),
                    {"default": "Battle Dress"},
                ),
                "silhouette": (
                    option_keys(WARDROBE_SILHOUETTE_OPTIONS),
                    {"default": "A-Line"},
                ),
                "colorway": (
                    option_keys(WARDROBE_COLORWAY_OPTIONS),
                    {"default": "Monochrome Obsidian"},
                ),
            },
            "optional": {
                "layering": (
                    option_keys(WARDROBE_LAYER_OPTIONS),
                    {"default": "Armor Plating"},
                ),
                "fabric": (
                    option_keys(WARDROBE_FABRIC_OPTIONS),
                    {"default": "Ballistic Weave"},
                ),
                "pattern": (
                    option_keys(WARDROBE_PATTERN_OPTIONS),
                    {"default": "Fractal"},
                ),
                "wear_state": (
                    option_keys(WARDROBE_WEAR_STATE_OPTIONS),
                    {"default": "Battle-Worn"},
                ),
                "culture_inspiration": (
                    option_keys(WARDROBE_CULTURE_OPTIONS),
                    {"default": "Solar Court"},
                ),
                "footwear": (
                    option_keys(WARDROBE_FOOTWEAR_OPTIONS),
                    {"default": "Combat Boots"},
                ),
                "primary_accessory": (
                    option_keys(WARDROBE_ACCESSORY_OPTIONS),
                    {"default": "Relic Pendant"},
                ),
                "secondary_accessory": (
                    option_keys(WARDROBE_ACCESSORY_OPTIONS),
                    {"default": "Utility Belt"},
                ),
                "functional_focus": ("STRING", {"default": ""}),
                "accent_materials": ("STRING", {"multiline": True, "default": ""}),
                "motion_considerations": ("STRING", {"multiline": True, "default": ""}),
                "finishing_details": ("STRING", {"multiline": True, "default": ""}),
                "additional_accessories": ("STRING", {"multiline": True, "default": ""}),
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
        custom_prompt: str,
        base_garment: str = "Battle Dress",
        silhouette: str = "A-Line",
        colorway: str = "Monochrome Obsidian",
        layering: str = "Armor Plating",
        fabric: str = "Ballistic Weave",
        pattern: str = "Fractal",
        wear_state: str = "Battle-Worn",
        culture_inspiration: str = "Solar Court",
        footwear: str = "Combat Boots",
        primary_accessory: str = "Relic Pendant",
        secondary_accessory: str = "Utility Belt",
        functional_focus: str = "",
        accent_materials: str = "",
        motion_considerations: str = "",
        finishing_details: str = "",
        additional_accessories: str = "",
        preset_action: str = "none",
        preset_name: str = "",
    ):
        config = {
            "custom_prompt": custom_prompt,
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
        }

        config, preset_status = self._apply_preset_action(
            "wardrobe_designer",
            preset_action,
            preset_name,
            config,
        )

        custom_prompt = config.get("custom_prompt", custom_prompt)
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
        base_prompt, base_notes = _resolve_option(base_garment, WARDROBE_BASE_GARMENT_OPTIONS)
        silhouette_prompt, silhouette_notes = _resolve_option(silhouette, WARDROBE_SILHOUETTE_OPTIONS)
        color_prompt, color_notes = _resolve_option(colorway, WARDROBE_COLORWAY_OPTIONS)
        layering_prompt, layering_notes = _resolve_option(layering, WARDROBE_LAYER_OPTIONS)
        fabric_prompt, fabric_notes = _resolve_option(fabric, WARDROBE_FABRIC_OPTIONS)
        pattern_prompt, pattern_notes = _resolve_option(pattern, WARDROBE_PATTERN_OPTIONS)
        wear_prompt, wear_notes = _resolve_option(wear_state, WARDROBE_WEAR_STATE_OPTIONS)
        culture_prompt, culture_notes = _resolve_option(culture_inspiration, WARDROBE_CULTURE_OPTIONS)
        footwear_prompt, footwear_notes = _resolve_option(footwear, WARDROBE_FOOTWEAR_OPTIONS)
        primary_prompt, primary_notes = _resolve_option(primary_accessory, WARDROBE_ACCESSORY_OPTIONS)
        secondary_prompt, secondary_notes = _resolve_option(secondary_accessory, WARDROBE_ACCESSORY_OPTIONS)

        accent_list = _split_tokens(accent_materials)
        motion_list = _split_tokens(motion_considerations)
        finishing_list = _split_tokens(finishing_details)
        extra_accessories = _split_tokens(additional_accessories)

        def _with_fallback(prompt: str, selection: str) -> str:
            cleaned = (prompt or "").strip()
            if cleaned:
                return cleaned
            selection_text = (selection or "").strip()
            if selection_text.lower() == "none":
                return ""
            return selection_text

        base_text = _with_fallback(base_prompt, base_garment)
        silhouette_text = _with_fallback(silhouette_prompt, silhouette)
        fabric_text = _with_fallback(fabric_prompt, fabric)
        layering_text = _with_fallback(layering_prompt, layering)
        color_text = _with_fallback(color_prompt, colorway)
        pattern_text = _with_fallback(pattern_prompt, pattern)
        wear_text = _with_fallback(wear_prompt, wear_state)
        culture_text = _with_fallback(culture_prompt, culture_inspiration)
        footwear_text = _with_fallback(footwear_prompt, footwear)
        primary_text = _with_fallback(primary_prompt, primary_accessory)
        secondary_text = _with_fallback(secondary_prompt, secondary_accessory)

        prompt_fragments = []
        custom_fragment = (custom_prompt or "").strip()
        if custom_fragment:
            prompt_fragments.append(custom_fragment)
        prompt_fragments.extend(
            [
                base_text,
                silhouette_text,
                fabric_text,
                layering_text,
                color_text,
                pattern_text,
                wear_text,
                culture_text,
                footwear_text,
            ]
        )
        if accent_list:
            prompt_fragments.append("accents: " + ", ".join(accent_list))
        if finishing_list:
            prompt_fragments.append("finishing: " + ", ".join(finishing_list))

        wardrobe_prompt = ", ".join(part for part in prompt_fragments if part).strip()
        if wardrobe_prompt and wardrobe_prompt[-1] not in ".!?":
            wardrobe_prompt += "."
        if functional_focus.strip():
            wardrobe_prompt += f" Functional focus: {functional_focus.strip()}."
        if motion_list:
            wardrobe_prompt += f" Movement considerations: {', '.join(motion_list)}."

        styling_segments = [
            _format_notes("Base", base_notes, base_text),
            _format_notes("Silhouette", silhouette_notes, silhouette_text),
            _format_notes("Fabric", fabric_notes, fabric_text),
            _format_notes("Layering", layering_notes, layering_text),
            _format_notes("Colorway", color_notes, color_text),
            _format_notes("Pattern", pattern_notes, pattern_text),
            _format_notes("Wear State", wear_notes, wear_text),
            _format_notes("Culture", culture_notes, culture_text),
            _format_notes("Footwear", footwear_notes, footwear_text),
        ]
        styling_notes = " | ".join(segment for segment in styling_segments if segment)

        accessory_items = []
        if primary_text:
            accessory_items.append(primary_text)
        if secondary_text:
            accessory_items.append(secondary_text)
        accessory_notes = [note for note in [primary_notes, secondary_notes] if note]
        if extra_accessories:
            accessory_items.append("Additional: " + ", ".join(extra_accessories))
        accessory_list = " | ".join(item for item in accessory_items if item)
        if accessory_notes:
            accessory_list += (" | Notes: " + "; ".join(accessory_notes)) if accessory_list else "Notes: " + "; ".join(accessory_notes)

        return (wardrobe_prompt, styling_notes, accessory_list, preset_status)

__all__ = ["NoxPromptWardrobeDesigner"]
