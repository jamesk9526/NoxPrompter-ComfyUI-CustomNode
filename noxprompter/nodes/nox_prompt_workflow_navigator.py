from __future__ import annotations

from textwrap import dedent
from typing import Dict, List, cast


class NoxPromptWorkflowNavigator:
    """Guide users through available nodes and routing options, including NSFW choices."""

    CATEGORY = "NoxPrompter/Guides"
    FUNCTION = "plan"
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = (
        "workflow_summary",
        "recommended_nodes",
        "routing_overview",
        "nsfw_options",
    )

    _GOAL_DATA: Dict[str, Dict[str, object]] = {
        "General Cinematic": {
            "description": (
                "Start with the Builder, enrich with lighting and narrative specialists, "
                "then finalize the master prompt via the Pipeline Combiner."
            ),
            "primary": [
                ("NoxPromptBuilder", "Create the structured cinematic base prompt."),
                (
                    "NoxPromptPaletteMixer",
                    "Define palette overrides that the Builder can ingest directly.",
                ),
                (
                    "NoxPromptLightingMaster",
                    "Dial in mood lighting descriptors and technical notes.",
                ),
                (
                    "NoxPromptNarrativeWeaver",
                    "Layer narrative beats that keep the render cohesive.",
                ),
                ("NoxPromptPipelineCombiner", "Merge all fragments into one master block."),
            ],
            "optional": [
                (
                    "NoxPromptAnalyzer",
                    "Review density, repeated terms, and post-build tweaks.",
                ),
                (
                    "NoxPromptPromptBoard",
                    "Keep alternate ideas ready to swap into the builder inputs.",
                ),
                (
                    "NoxPromptCameraLanguage",
                    "Aggregate shot, move, and rigging notes for Builder and Organizer.",
                ),
            ],
            "routing": [
                "NarrativeWeaver.subject_focus → Builder.subject_focus",
                "NarrativeWeaver.scene_setting → Builder.scene_setting",
                "NarrativeWeaver.motion_arc → Builder.motion_arc",
                "NarrativeWeaver.narrative_hook → Builder.narrative_hook",
                "PaletteMixer.palette_overrides → Builder.palette_overrides",
                "PaletteMixer.custom_keywords → PipelineCombiner.custom_keywords",
                "LightingMaster.lighting_prompt → PipelineCombiner.lighting_prompt",
                "Builder.prompt → PipelineCombiner.core_prompt",
                "Builder.negative_prompt → PipelineCombiner.negative_prompt",
                "CameraLanguage.camera_prompt → Builder.camera_prompt",
                "CameraLanguage.framing_summary → Builder.camera_summary",
                "CameraLanguage.rigging_notes → Builder.camera_notes",
                "CameraLanguage.rigging_notes → PromptOrganizer.camera_notes",
            ],
            "nsfw": [
                "Optional: swap Action Director for NSFW variants if adult motion cues are required.",
            ],
        },
        "Character Showcase": {
            "description": (
                "Focus on character identity first, then lock styling and wardrobe before you build the scene."
            ),
            "primary": [
                (
                    "NoxPromptCharacterCreator",
                    "Establish core traits, proportions, and personality tags.",
                ),
                (
                    "NoxPromptHumanDesigner",
                    "Translate traits into grounded human descriptors.",
                ),
                (
                    "NoxPromptWardrobeDesigner",
                    "Define clothing layers and texture notes.",
                ),
                (
                    "NoxPromptBuilder",
                    "Assemble the hero prompt with the character details pre-seeded.",
                ),
                ("NoxPromptPipelineCombiner", "Merge character, wardrobe, and scene cues."),
            ],
            "optional": [
                (
                    "NoxPromptPaletteMixer",
                    "Keep wardrobe colors and scene palette unified.",
                ),
                (
                    "NoxPromptPromptOrganizer",
                    "List which sections are filled or missing before rendering.",
                ),
            ],
            "routing": [
                "CharacterCreator.character_prompt → Builder.subject_focus",
                "CharacterCreator.character_prompt → PipelineCombiner.character_prompt",
                "HumanDesigner.design_prompt → PipelineCombiner.human_prompt",
                "WardrobeDesigner.wardrobe_prompt → PipelineCombiner.wardrobe_prompt",
                "PaletteMixer.palette_overrides → Builder.palette_overrides",
                "Builder.prompt → PipelineCombiner.core_prompt",
            ],
            "nsfw": [
                "If turning spicy, pair Wardrobe Designer output with NSFW Designer safety toggles.",
            ],
        },
        "Story Sequence": {
            "description": (
                "Build multi-shot narratives by planning the production beats before combining prompts."
            ),
            "primary": [
                (
                    "NoxPromptProductionPlanner",
                    "Outline key scenes, beats, and transition notes.",
                ),
                (
                    "NoxPromptShotlistOrganizer",
                    "Break the plan into shot-by-shot prompt fragments.",
                ),
                (
                    "NoxPromptBuilder",
                    "Author the hero shot prompts using the outline guidance.",
                ),
                (
                    "NoxPromptPipelineCombiner",
                    "Consolidate prompts and negatives for batch rendering.",
                ),
            ],
            "optional": [
                (
                    "NoxPromptLightingMaster",
                    "Maintain lighting continuity across the sequence.",
                ),
                (
                    "NoxPromptAnalyzer",
                    "Double-check for repeated descriptors between shots.",
                ),
            ],
            "routing": [
                "ProductionPlanner.production_checklist → ShotlistOrganizer.prep_notes",
                "ShotlistOrganizer.shotlist → Builder.scene_setting",
                "ShotlistOrganizer.location_summary → PipelineCombiner.sequence_notes",
                "LightingMaster.lighting_prompt → PipelineCombiner.lighting_prompt",
                "Builder.prompt → PipelineCombiner.core_prompt",
            ],
            "nsfw": [
                "Narrative paths that go NSFW should use NSFW AIO to keep beats consistent and safe.",
            ],
        },
        "NSFW Glamour": {
            "description": (
                "Use the NSFW suite to add consent language, tone, and attire guidance while keeping glamour polished."
            ),
            "primary": [
                (
                    "NoxPromptNSFWDesigner",
                    "Blend sensual descriptors with automatic safety phrasing.",
                ),
                (
                    "NoxPromptWardrobeDesigner",
                    "Coordinate lingerie or styling with tasteful modifiers.",
                ),
                (
                    "NoxPromptLightingMaster",
                    "Shape flattering light with emphasis on mood.",
                ),
                (
                    "NoxPromptBuilder",
                    "Merge NSFW and wardrobe cues into the master prompt.",
                ),
                ("NoxPromptPipelineCombiner", "Finalize positives and negatives in one block."),
            ],
            "optional": [
                (
                    "NoxPromptPaletteMixer",
                    "Keep color accents consistent across scenes.",
                ),
                (
                    "NoxPromptEnhancer",
                    "Add high-quality tags while respecting safety language.",
                ),
            ],
            "routing": [
                "NSFWDesigner.prompt → PipelineCombiner.nsfw_prompt",
                "NSFWDesigner.safety_notes → PipelineCombiner.safety_notes",
                "WardrobeDesigner.wardrobe_prompt → PipelineCombiner.wardrobe_prompt",
                "LightingMaster.lighting_prompt → PipelineCombiner.lighting_prompt",
                "Enhancer.enhanced_prompt → PipelineCombiner.enhanced_prompt (optional)",
                "Builder.prompt → PipelineCombiner.core_prompt",
                "Builder.negative_prompt → PipelineCombiner.negative_prompt",
            ],
            "nsfw": [
                "Leave `include_safety_note` enabled and stack with NSFW Action Director if motion cues are needed.",
            ],
        },
        "NSFW Action": {
            "description": (
                "Coordinate dynamic NSFW scenes with explicit motion notes and reinforced consent phrases."
            ),
            "primary": [
                (
                    "NoxPromptNSFWActionDirector",
                    "Define choreography, intensity, and tone with safety defaults.",
                ),
                (
                    "NoxPromptNSFWAIO",
                    "One-stop prompt builder merging action, wardrobe, and compliance.",
                ),
                (
                    "NoxPromptLightingMaster",
                    "Handle atmospheric lighting for dramatic motion.",
                ),
                ("NoxPromptPipelineCombiner", "Combine fragments and generate negatives."),
            ],
            "optional": [
                (
                    "NoxPromptBuilder",
                    "If you prefer manual assembly, feed NSFW outputs into the standard builder.",
                ),
                (
                    "NoxPromptAnalyzer",
                    "Verify consent language and remove repetitive phrasing.",
                ),
            ],
            "routing": [
                "NSFWActionDirector.action_prompt → PipelineCombiner.action_prompt",
                "NSFWActionDirector.safety_notes → PipelineCombiner.safety_notes",
                "NSFWAIO.combined_prompt → PipelineCombiner.core_prompt",
                "NSFWAIO.combined_negative → PipelineCombiner.additional_negative",
                "NSFWAIO.combined_safety → PipelineCombiner.sequence_notes",
                "LightingMaster.lighting_prompt → PipelineCombiner.lighting_prompt",
                "Analyzer.analysis_result → PipelineCombiner.sequence_notes (optional)",
            ],
            "nsfw": [
                "Stack NSFW Designer for wardrobe/pose nuance and let AIO control the final merge.",
            ],
        },
    }

    _GLOBAL_NSFW_OVERVIEW: List[str] = [
        "NSFW Suite Overview",
        "--------------------",
        "• NoxPromptNSFWDesigner – Adds tasteful sensual language plus age-negation safeguards.",
        "• NoxPromptNSFWActionDirector – Maps choreography with consent reminders.",
        "• NoxPromptNSFWAIO – Generates full prompts while enforcing compliance strings.",
        "Mix and match with standard nodes; safety toggles stay enabled unless your studio policy overrides them.",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "goal": (list(cls._GOAL_DATA.keys()), {"default": "General Cinematic"}),
            },
            "optional": {
                "include_optional": ("BOOLEAN", {"default": True}),
                "include_routing": ("BOOLEAN", {"default": True}),
                "include_nsfw": ("BOOLEAN", {"default": True}),
            },
        }

    @classmethod
    def IS_CHANGED(cls, *_args, **_kwargs):  # pragma: no cover - metadata hook
        return True

    def plan(
        self,
        goal: str,
        include_optional: bool = True,
        include_routing: bool = True,
        include_nsfw: bool = True,
    ):
        data = self._GOAL_DATA.get(goal)
        if data is None:
            default_key = "General Cinematic"
            data = self._GOAL_DATA[default_key]
            goal = default_key

        summary_lines = [f"Workflow Focus: {goal}", "", data["description"]]
        workflow_summary = "\n".join(summary_lines).strip()

        def _format_section(title: str, items: List[str]) -> str:
            if not items:
                return ""
            header = f"{title}\n{'-' * len(title)}"
            body = "\n".join(items)
            return f"{header}\n{body}"

        primary_lines = [f"• {name} – {blurb}" for name, blurb in data["primary"]]  # type: ignore[index]

        optional_lines: List[str] = []
        if include_optional:
            optional_pairs = cast(List[tuple[str, str]], data.get("optional", []))
            optional_lines = [f"• {name} – {blurb}" for name, blurb in optional_pairs]

        node_sections = [
            _format_section("Primary Nodes", primary_lines),
        ]
        if include_optional and optional_lines:
            node_sections.append(_format_section("Optional Add-ons", optional_lines))

        recommended_nodes = "\n\n".join(section for section in node_sections if section).strip()

        routing_overview = ""
        if include_routing:
            routing_lines = cast(List[str], data.get("routing", []))
            if routing_lines:
                routing_overview = dedent(
                    "\n".join(
                        [
                            "Output Routing",
                            "--------------",
                            *routing_lines,
                        ]
                    )
                ).strip()

        nsfw_options = ""
        if include_nsfw:
            nsfw_lines = list(self._GLOBAL_NSFW_OVERVIEW)
            goal_specific = cast(List[str], data.get("nsfw", []))
            if goal_specific:
                nsfw_lines.extend(["", *goal_specific])
            nsfw_options = "\n".join(nsfw_lines).strip()

        return workflow_summary, recommended_nodes, routing_overview, nsfw_options


__all__ = ["NoxPromptWorkflowNavigator"]
