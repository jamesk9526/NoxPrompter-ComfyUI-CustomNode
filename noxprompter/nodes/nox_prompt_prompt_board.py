from __future__ import annotations

from typing import Dict, List


class NoxPromptPromptBoard:
    """Gather narrative, visual, and production pillars into a prompt board."""

    CATEGORY = "NoxPrompter/Organization"
    FUNCTION = "assemble"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt_board", "missing_sections", "section_overview")

    _STRUCTURE_MODES: Dict[str, List[str]] = {
        "Story-first": [
            "Story Pillars",
            "Character Focus",
            "Visual Language",
            "Lighting Design",
            "Palette & Texture",
            "Keywords",
            "Risks & Watchouts",
            "Delivery Notes",
        ],
        "Visual-first": [
            "Visual Language",
            "Lighting Design",
            "Palette & Texture",
            "Story Pillars",
            "Character Focus",
            "Keywords",
            "Risks & Watchouts",
            "Delivery Notes",
        ],
        "Client Review": [
            "Delivery Notes",
            "Story Pillars",
            "Character Focus",
            "Visual Language",
            "Lighting Design",
            "Palette & Texture",
            "Risks & Watchouts",
            "Keywords",
        ],
    }

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "board_title": ("STRING", {"default": "Prompt Board"}),
            },
            "optional": {
                "story_pillars": ("STRING", {"multiline": True, "default": ""}),
                "character_focus": ("STRING", {"multiline": True, "default": ""}),
                "visual_language": ("STRING", {"multiline": True, "default": ""}),
                "lighting_design": ("STRING", {"multiline": True, "default": ""}),
                "lighting_camera": ("STRING", {"multiline": True, "default": ""}),
                "camera_language": ("STRING", {"multiline": True, "default": ""}),
                "camera_summary": ("STRING", {"multiline": True, "default": ""}),
                "palette_texture": ("STRING", {"multiline": True, "default": ""}),
                "keywords": ("STRING", {"multiline": True, "default": ""}),
                "risks_watchouts": ("STRING", {"multiline": True, "default": ""}),
                "delivery_notes": ("STRING", {"multiline": True, "default": ""}),
                "structure_mode": (list(cls._STRUCTURE_MODES.keys()), {"default": "Story-first"}),
                "include_missing_list": ("BOOLEAN", {"default": True}),
            },
        }

    def assemble(
        self,
        board_title: str,
        story_pillars: str = "",
        character_focus: str = "",
        visual_language: str = "",
        lighting_design: str = "",
        lighting_camera: str = "",
        camera_language: str = "",
        camera_summary: str = "",
        palette_texture: str = "",
        keywords: str = "",
        risks_watchouts: str = "",
        delivery_notes: str = "",
        structure_mode: str = "Story-first",
        include_missing_list: bool = True,
    ):
        lighting_block = "\n".join(
            part.strip()
            for part in (lighting_design, lighting_camera, camera_language, camera_summary)
            if part and part.strip()
        ).strip()

        section_values: Dict[str, str] = {
            "Story Pillars": story_pillars,
            "Character Focus": character_focus,
            "Visual Language": visual_language,
            "Lighting Design": lighting_block,
            "Palette & Texture": palette_texture,
            "Keywords": keywords,
            "Risks & Watchouts": risks_watchouts,
            "Delivery Notes": delivery_notes,
        }

        structure = self._STRUCTURE_MODES.get(structure_mode, self._STRUCTURE_MODES["Story-first"])

        board_lines: List[str] = [f"# {board_title.strip() or 'Prompt Board'}"]
        overview: List[str] = []
        missing: List[str] = []

        for section in structure:
            value = section_values.get(section, "").strip()
            if value:
                board_lines.append(f"\n## {section}\n{value}")
                overview.append(f"{section} → included")
            else:
                overview.append(f"{section} → missing")
                if include_missing_list:
                    missing.append(section)

        board_text = "\n".join(board_lines).strip()
        missing_text = ", ".join(missing) if missing else ""
        overview_text = "\n".join(overview).strip()

        return board_text, missing_text, overview_text


__all__ = ["NoxPromptPromptBoard"]
