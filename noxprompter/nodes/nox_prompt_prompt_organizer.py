from __future__ import annotations

from typing import Dict, List


class NoxPromptOrganizer:
    """Collect prompt fragments and present them in a consistent, readable order."""

    CATEGORY = "NoxPrompter/Utility"
    FUNCTION = "organize"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("organized_prompt", "missing_sections", "section_overview")

    _STRUCTURE_MODES: Dict[str, List[str]] = {
        "Builder-first": [
            "Core Prompt",
            "Character",
            "Wardrobe",
            "Action",
            "Lighting",
            "Camera",
            "Palette",
            "Extra",
        ],
        "Narrative-first": [
            "Narrative",
            "Character",
            "Action",
            "Wardrobe",
            "Lighting",
            "Camera",
            "Palette",
            "Core Prompt",
            "Extra",
        ],
        "Lighting-first": [
            "Lighting",
            "Camera",
            "Action",
            "Character",
            "Wardrobe",
            "Core Prompt",
            "Palette",
            "Extra",
        ],
    }

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "core_prompt": ("STRING", {"multiline": True, "default": ""}),
            },
            "optional": {
                "character_prompt": ("STRING", {"multiline": True, "default": ""}),
                "narrative_notes": ("STRING", {"multiline": True, "default": ""}),
                "wardrobe_prompt": ("STRING", {"multiline": True, "default": ""}),
                "action_prompt": ("STRING", {"multiline": True, "default": ""}),
                "lighting_prompt": ("STRING", {"multiline": True, "default": ""}),
                "camera_notes": ("STRING", {"multiline": True, "default": ""}),
                "palette_overrides": ("STRING", {"multiline": True, "default": ""}),
                "extra_descriptors": ("STRING", {"multiline": True, "default": ""}),
                "structure_mode": (list(cls._STRUCTURE_MODES.keys()), {"default": "Builder-first"}),
                "include_missing_list": ("BOOLEAN", {"default": True}),
            },
        }

    def organize(
        self,
        core_prompt: str,
        character_prompt: str = "",
        narrative_notes: str = "",
        wardrobe_prompt: str = "",
        action_prompt: str = "",
        lighting_prompt: str = "",
        camera_notes: str = "",
        palette_overrides: str = "",
        extra_descriptors: str = "",
        structure_mode: str = "Builder-first",
        include_missing_list: bool = True,
    ):
        structure = self._STRUCTURE_MODES.get(structure_mode, self._STRUCTURE_MODES["Builder-first"])

        section_values: Dict[str, str] = {
            "Core Prompt": core_prompt,
            "Narrative": narrative_notes,
            "Character": character_prompt,
            "Wardrobe": wardrobe_prompt,
            "Action": action_prompt,
            "Lighting": lighting_prompt,
            "Camera": camera_notes,
            "Palette": palette_overrides,
            "Extra": extra_descriptors,
        }

        ordered_lines: List[str] = []
        missing: List[str] = []
        overview: List[str] = []

        for section in structure:
            content = section_values.get(section, "").strip()
            if content:
                ordered_lines.append(f"{section}: {content}")
                overview.append(f"{section} → included")
            else:
                overview.append(f"{section} → missing")
                missing.append(section)

        # Append any additional sections that were populated but not present in the structure definition
        for section, value in section_values.items():
            if section in structure:
                continue
            content = value.strip()
            if content:
                ordered_lines.append(f"{section}: {content}")
                overview.append(f"{section} → included (appended)")

        organized_prompt = "\n".join(ordered_lines).strip()

        missing_sections = ""
        if include_missing_list and missing:
            missing_sections = ", ".join(missing)

        section_overview = "\n".join(overview).strip()

        return organized_prompt, missing_sections, section_overview


__all__ = ["NoxPromptOrganizer"]
