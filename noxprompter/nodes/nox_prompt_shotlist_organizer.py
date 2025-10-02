from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


@dataclass
class _ShotEntry:
    index: int
    title: str
    location: str
    description: str
    camera: str
    notes: str

    def is_valid(self) -> bool:
        return any(value.strip() for value in (self.title, self.description, self.location, self.camera, self.notes))

    def display_title(self) -> str:
        if self.title.strip() and self.location.strip():
            return f"{self.title.strip()} — {self.location.strip()}"
        if self.title.strip():
            return self.title.strip()
        return self.location.strip() or f"Untitled shot {self.index}"

    def missing_fields(self) -> List[str]:
        missing: List[str] = []
        if not self.title.strip():
            missing.append("title")
        if not self.description.strip():
            missing.append("description")
        if not self.location.strip():
            missing.append("location")
        return missing


class NoxPromptShotlistOrganizer:
    """Organize shot details into a production-ready shotlist and prep notes."""

    CATEGORY = "NoxPrompter/Organization"
    FUNCTION = "organize"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("shotlist", "location_summary", "prep_notes")

    _ORDER_MODES = (
        "Story Beat (input order)",
        "By Location",
        "By Camera Setup",
    )

    @classmethod
    def INPUT_TYPES(cls):
        required: Dict[str, Tuple[str, Dict[str, object]]] = {
            "project_title": ("STRING", {"default": "Untitled Sequence"}),
        }

        optional: Dict[str, Tuple[Iterable[str] | List[str] | str, Dict[str, object]]] = {
            "shoot_day": ("STRING", {"default": "Day 1"}),
            "ordering_mode": (list(cls._ORDER_MODES), {"default": cls._ORDER_MODES[0]}),
            "include_missing_list": ("BOOLEAN", {"default": True}),
        }

        for idx in range(1, 6):
            optional[f"shot_{idx}_title"] = ("STRING", {"default": ""})
            optional[f"shot_{idx}_location"] = ("STRING", {"default": ""})
            optional[f"shot_{idx}_description"] = ("STRING", {"multiline": True, "default": ""})
            optional[f"shot_{idx}_camera"] = ("STRING", {"default": ""})
            optional[f"shot_{idx}_notes"] = ("STRING", {"multiline": True, "default": ""})

        return {
            "required": required,
            "optional": optional,
        }

    def organize(
        self,
        project_title: str,
        shoot_day: str = "Day 1",
        ordering_mode: str = "Story Beat (input order)",
        include_missing_list: bool = True,
        **kwargs,
    ):
        shots = self._collect_shots(kwargs)
        if not shots:
            return "", "", ""

        ordered_shots = self._order_shots(shots, ordering_mode)

        shot_lines: List[str] = [f"# Shotlist — {project_title.strip() or 'Untitled Sequence'} ({shoot_day.strip() or 'Day 1'})"]
        missing_section: List[str] = []
        prep_notes: List[str] = []
        locations: Dict[str, List[int]] = {}
        camera_setups: Dict[str, List[int]] = {}

        for position, shot in enumerate(ordered_shots, start=1):
            title_line = shot.display_title()
            shot_lines.append(f"{position}. {title_line}")

            if shot.description.strip():
                shot_lines.append(f"   Description: {shot.description.strip()}")
            if shot.camera.strip():
                camera_text = shot.camera.strip()
                shot_lines.append(f"   Camera: {camera_text}")
                camera_setups.setdefault(camera_text.lower(), []).append(position)
            if shot.notes.strip():
                shot_lines.append(f"   Notes: {shot.notes.strip()}")

            key_location = shot.location.strip() or "Unassigned"
            locations.setdefault(key_location, []).append(position)

            if include_missing_list:
                missing_fields = shot.missing_fields()
                if missing_fields:
                    missing_section.append(f"Shot {position} ({title_line}) → missing {', '.join(missing_fields)}")

        location_lines = ["# Locations"]
        for name, indices in sorted(locations.items(), key=lambda item: (item[0].lower(), item[1])):
            index_display = ", ".join(str(i) for i in indices)
            location_lines.append(f"- {name}: shots {index_display}")

        if camera_setups:
            prep_notes.append("Camera setups to prep:")
            for setup, indices in sorted(camera_setups.items(), key=lambda item: (item[0], item[1])):
                label = setup
                if setup == setup.upper():
                    label = setup
                prep_notes.append(f"• {label} → shots {', '.join(str(i) for i in indices)}")

        unique_notes = [shot.notes.strip() for shot in ordered_shots if shot.notes.strip()]
        if unique_notes:
            prep_notes.append("Additional notes:")
            for note in unique_notes:
                prep_notes.append(f"• {note}")

        if include_missing_list and missing_section:
            prep_notes.append("Missing data summary:")
            for line in missing_section:
                prep_notes.append(f"• {line}")

        shotlist_text = "\n".join(shot_lines).strip()
        locations_text = "\n".join(location_lines).strip()
        prep_notes_text = "\n".join(prep_notes).strip()

        return shotlist_text, locations_text, prep_notes_text

    def _collect_shots(self, payload: Dict[str, str]) -> List[_ShotEntry]:
        shots: List[_ShotEntry] = []
        for idx in range(1, 6):
            entry = _ShotEntry(
                index=idx,
                title=payload.get(f"shot_{idx}_title", ""),
                location=payload.get(f"shot_{idx}_location", ""),
                description=payload.get(f"shot_{idx}_description", ""),
                camera=payload.get(f"shot_{idx}_camera", ""),
                notes=payload.get(f"shot_{idx}_notes", ""),
            )
            if entry.is_valid():
                shots.append(entry)
        return shots

    def _order_shots(self, shots: List[_ShotEntry], ordering_mode: str) -> List[_ShotEntry]:
        if ordering_mode == "By Location":
            return sorted(
                shots,
                key=lambda shot: (shot.location.strip().lower() or "zzz", shot.index),
            )
        if ordering_mode == "By Camera Setup":
            return sorted(
                shots,
                key=lambda shot: (shot.camera.strip().lower() or "zzz", shot.index),
            )
        return list(shots)


__all__ = ["NoxPromptShotlistOrganizer"]
