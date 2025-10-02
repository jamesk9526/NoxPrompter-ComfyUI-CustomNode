from __future__ import annotations

from typing import Dict, List, Tuple


class NoxPromptProductionPlanner:
    """Collect departmental notes into a structured production checklist."""

    CATEGORY = "NoxPrompter/Organization"
    FUNCTION = "plan"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("production_checklist", "missing_departments", "callouts")

    _DEPARTMENTS: Tuple[str, ...] = (
        "Direction",
        "Camera",
        "Lighting",
        "Grip",
        "Sound",
        "Wardrobe",
        "Makeup",
        "Props",
        "VFX",
        "Safety",
        "Logistics",
        "Post",
    )

    @classmethod
    def INPUT_TYPES(cls):
        optional: Dict[str, Tuple[str, Dict[str, object]]] = {
            "shoot_day": ("STRING", {"default": "Day 1"}),
            "location": ("STRING", {"default": "Main Stage"}),
            "call_time": ("STRING", {"default": "08:00"}),
            "wrap_target": ("STRING", {"default": "18:30"}),
            "include_missing_list": ("BOOLEAN", {"default": True}),
            "priority_notes": ("STRING", {"multiline": True, "default": ""}),
            "risks": ("STRING", {"multiline": True, "default": ""}),
        }

        for department in cls._DEPARTMENTS:
            key = f"{department.lower()}_notes".replace(" ", "_")
            optional[key] = ("STRING", {"multiline": True, "default": ""})

        return {
            "required": {
                "project_title": ("STRING", {"default": "Untitled Production"}),
            },
            "optional": optional,
        }

    def plan(
        self,
        project_title: str,
        shoot_day: str = "Day 1",
        location: str = "Main Stage",
        call_time: str = "08:00",
        wrap_target: str = "18:30",
        include_missing_list: bool = True,
        priority_notes: str = "",
        risks: str = "",
        **kwargs,
    ):
        header = self._build_header(project_title, shoot_day, location, call_time, wrap_target)

        department_sections: List[str] = []
        missing_departments: List[str] = []
        callout_lines: List[str] = []

        for department in self._DEPARTMENTS:
            key = f"{department.lower()}_notes".replace(" ", "_")
            notes = kwargs.get(key, "").strip()
            if notes:
                department_sections.append(f"## {department}\n{notes}")
                callout_lines.append(f"{department}: ready")
            else:
                callout_lines.append(f"{department}: needs details")
                if include_missing_list:
                    missing_departments.append(department)

        if priority_notes.strip():
            department_sections.insert(0, f"## Priority Focus\n{priority_notes.strip()}")
            callout_lines.insert(0, "Priority: see checklist header")

        if risks.strip():
            department_sections.append(f"## Risks & Mitigations\n{risks.strip()}")
            callout_lines.append("Risks: mitigation plan documented")

        checklist_body = "\n\n".join(section for section in department_sections if section.strip())
        checklist_text = f"{header}\n\n{checklist_body}".strip()

        missing_text = ", ".join(missing_departments) if missing_departments else ""
        callouts_text = "\n".join(callout_lines).strip()

        return checklist_text, missing_text, callouts_text

    def _build_header(self, project_title: str, shoot_day: str, location: str, call_time: str, wrap_target: str) -> str:
        title = project_title.strip() or "Untitled Production"
        day = shoot_day.strip() or "Day 1"
        loc = location.strip() or "Main Stage"
        call = call_time.strip() or "08:00"
        wrap = wrap_target.strip() or "18:30"

        lines = [
            f"# Production Checklist — {title}",
            f"• {day} @ {loc}",
            f"• Call: {call} | Target wrap: {wrap}",
        ]
        return "\n".join(lines)


__all__ = ["NoxPromptProductionPlanner"]
