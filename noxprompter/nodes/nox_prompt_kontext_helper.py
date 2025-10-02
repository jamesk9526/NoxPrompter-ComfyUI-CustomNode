from __future__ import annotations



def _format_section(title: str, lines: list[str]) -> str:
    if not lines:
        return ""
    header = f"{title}\n{'-' * len(title)}"
    body = "\n".join(lines)
    return f"{header}\n{body}"


class NoxPromptKontextHelper:
    """Provide structured FLUX.1 Kontext editing guidance with ready-to-use prompts."""

    CATEGORY = "NoxPrompter/Guides"
    FUNCTION = "build_helper"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("command_reference", "step_plan", "prompt_examples")

    _EDIT_FOCUS_DETAILS = {
        "Modify Object": {
            "verbs": ["Change", "Make", "Transform"],
            "templates": [
                "Change the [object] to [new description]",
                "Make the [object] [updated attribute] while keeping [preserved aspect]",
                "Transform the [object] finish into [style]",
            ],
            "examples": [
                "Change the car to red while keeping the reflections and lighting untouched",
                "Make the building facade brick while preserving the window layout",
            ],
        },
        "Add Element": {
            "verbs": ["Add", "Include", "Put"],
            "templates": [
                "Add [new element] [location/context]",
                "Include [detail] beside the [reference subject]",
                "Put [object] in the [background/foreground]",
            ],
            "examples": [
                "Add sunglasses to the person while maintaining their pose",
                "Put mountains in the background while keeping the city skyline visible",
            ],
        },
        "Remove Element": {
            "verbs": ["Remove", "Delete", "Take away"],
            "templates": [
                "Remove the [unwanted object] from [location]",
                "Delete the [item] while keeping the rest of the scene unchanged",
                "Take away the [element] and keep [context] intact",
            ],
            "examples": [
                "Remove the person in the background while keeping the lighting the same",
                "Delete the text from the sign while preserving the wood texture",
            ],
        },
        "Replace Element": {
            "verbs": ["Replace", "Swap", "Substitute"],
            "templates": [
                "Replace [original] with [new item]",
                "Swap the [element] for [replacement]",
                "Substitute [detail] with [updated detail]",
            ],
            "examples": [
                "Replace 'OPEN' with 'CLOSED' while maintaining the same font style and color",
                "Swap the blue car with a red truck while preserving the parking position",
            ],
        },
        "Reposition": {
            "verbs": ["Move", "Place", "Position"],
            "templates": [
                "Move the [subject] to the [new location]",
                "Place the [object] behind/in front of [reference]",
                "Position the [subject] [spatial instruction]",
            ],
            "examples": [
                "Move the person to the left side while keeping their pose identical",
                "Place a tree behind the house without changing the house scale",
            ],
        },
        "Style Transfer": {
            "verbs": ["Convert", "Transform", "Render"],
            "templates": [
                "Convert to [target style] while maintaining [important feature]",
                "Transform the scene into [style] with [style qualities]",
                "Render as [medium] while preserving [composition/detail]",
            ],
            "examples": [
                "Convert to watercolor while maintaining the composition",
                "Transform to pencil sketch with cross-hatching while keeping facial features crisp",
            ],
        },
        "Text Edit": {
            "verbs": ["Replace", "Update", "Correct"],
            "templates": [
                "Replace \"[old text]\" with \"[new text]\"",
                "Update the sign to read \"[new text]\" while keeping the same font style",
                "Correct the label to \"[new text]\" without changing the layout",
            ],
            "examples": [
                "Replace \"SALE\" with \"SOLD\" while maintaining the same font style and color",
                "Update the marquee to read \"GRAND OPENING\" while keeping the neon glow",
            ],
        },
    }

    _SUPPORTING_TIPS = {
        "Preset": [
            "Start with the most important edit, review the result, then stack the next change.",
            "Use quotation marks around text you want to replace to trigger precise text editing.",
            "Explicitly describe what should remain unchanged, e.g. 'while keeping everything else identical'.",
            "Name the exact visual style rather than using vague words like 'artistic'.",
        ],
        "Context": [
            "Kontext excels at surgical edits—avoid resummarizing the entire scene when you only need a tweak.",
            "For background swaps, mention 'maintain identical subject placement' to anchor the main subject.",
            "When editing characters, identify them with descriptors instead of pronouns.",
            "If identity drifts, reissue the edit with additional facial or clothing markers.",
        ],
    }

    _STEP_SEQUENCES = {
        "Single Edit": [
            "Step 1 — Primary edit: craft a focused instruction using the selected action verbs.",
            "Step 2 — Safeguard context: add clauses like 'while keeping everything else unchanged'.",
            "Step 3 — Review: confirm the target element updated and no unintended changes occurred.",
        ],
        "Two-Step Sequence": [
            "Step 1 — Establish base conditions (e.g. 'Convert to daytime while keeping subject placement identical').",
            "Step 2 — Apply the focal edit with your chosen action (e.g. 'Add string lights above the patio').",
            "Step 3 — Optional refinement: reinforce any styling or text consistency if drift occurred.",
        ],
        "Full Workflow": [
            "Step 1 — Baseline adjustment: fix lighting or time of day if needed before detailed changes.",
            "Step 2 — Subject-specific change: execute the main edit with precise verbs and descriptors.",
            "Step 3 — Environmental support: adjust surrounding elements (backgrounds, props) as separate instructions.",
            "Step 4 — Style harmonization: apply style transfer or finishing touches while preserving composition.",
            "Step 5 — Final pass: issue a protection step such as 'Everything else should remain untouched'.",
        ],
    }

    _TROUBLESHOOTING_LINES = [
        "If Kontext alters unrelated areas, explicitly say 'only modify [target area]' in your prompt.",
        "For stubborn text elements, mention 'maintain the same font style and color' after the replacement instruction.",
        "When adding new props, describe their placement relative to existing subjects to avoid accidental repositioning.",
        "If style changes wipe detail, describe the texture you expect (e.g. 'visible brushstrokes' or 'clean vector lines').",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "edit_focus": (list(cls._EDIT_FOCUS_DETAILS.keys()), {"default": "Modify Object"}),
            },
            "optional": {
                "iteration_depth": (list(cls._STEP_SEQUENCES.keys()), {"default": "Full Workflow"}),
                "preserve_subject": ("BOOLEAN", {"default": True}),
                "include_troubleshooting": ("BOOLEAN", {"default": True}),
                "include_supporting_tips": ("BOOLEAN", {"default": True}),
            },
        }

    @classmethod
    def IS_CHANGED(cls, *_args, **_kwargs):  # pragma: no cover - ComfyUI metadata hook
        return True

    def build_helper(
        self,
        edit_focus: str,
        iteration_depth: str = "Full Workflow",
        preserve_subject: bool = True,
        include_troubleshooting: bool = True,
        include_supporting_tips: bool = True,
    ):
        focus_key = edit_focus if edit_focus in self._EDIT_FOCUS_DETAILS else "Modify Object"
        focus_bundle = self._EDIT_FOCUS_DETAILS[focus_key]

        verb_section = _format_section(
            "Primary Action Verbs",
            [", ".join(focus_bundle["verbs"]), ""],
        )
        template_section = _format_section(
            "Instruction Templates",
            [f"• {template}" for template in focus_bundle["templates"]],
        )

        support_lines: list[str] = []
        if include_supporting_tips:
            support_lines.extend(["• " + tip for tip in self._SUPPORTING_TIPS["Preset"]])
            support_lines.append("")
            support_lines.extend(["• " + tip for tip in self._SUPPORTING_TIPS["Context"]])
        support_section = _format_section("Best Practices", support_lines)

        command_reference_parts = [segment for segment in (verb_section, template_section, support_section) if segment]
        command_reference = "\n\n".join(command_reference_parts)

        steps = self._STEP_SEQUENCES.get(iteration_depth, self._STEP_SEQUENCES["Full Workflow"])
        step_lines = steps.copy()
        if preserve_subject:
            step_lines.append(
                "Reminder: include phrases such as 'maintain identical subject placement and scale' to keep the hero anchored."
            )
        step_plan = _format_section("Kontext Execution Plan", step_lines)

        example_lines = [f"• {example}" for example in focus_bundle["examples"]]
        if preserve_subject and focus_key not in {"Remove Element", "Text Edit"}:
            example_lines.append(
                "• Add 'while maintaining the original pose and lighting' to protect the subject during iterative edits."
            )
        example_section = _format_section("Ready-To-Use Prompts", example_lines)

        troubleshooting_text = ""
        if include_troubleshooting:
            troubleshooting_text = _format_section(
                "Troubleshooting",
                [f"• {line}" for line in self._TROUBLESHOOTING_LINES],
            )

        prompt_examples_parts = [segment for segment in (example_section, troubleshooting_text) if segment]
        prompt_examples = "\n\n".join(prompt_examples_parts)

        return (command_reference, step_plan, prompt_examples)


__all__ = ["NoxPromptKontextHelper"]
