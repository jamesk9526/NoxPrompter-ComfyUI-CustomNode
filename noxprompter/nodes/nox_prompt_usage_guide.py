from __future__ import annotations

from textwrap import dedent

from .nox_prompt_pipeline_combiner import NoxPromptPipelineCombiner


def _format_section(title: str, lines: list[str]) -> str:
    if not lines:
        return ""
    header = f"{title}\n{'-' * len(title)}"
    body = "\n".join(lines)
    return f"{header}\n{body}"


class NoxPromptUsageGuide:
    """Provide an in-canvas reference explaining how to work with the suite."""

    CATEGORY = "NoxPrompter/Guides"
    FUNCTION = "build_guide"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("guide_text", "pipeline_overview", "safety_highlights")

    _DETAIL_BUNDLES = {
        "Quickstart": [
            "1. Use **NoxPromptBuilder** to assemble the base cinematic prompt.",
            "2. Layer optional specialists (Palette Mixer, Narrative Weaver, Lighting Master) to enrich the builder inputs.",
            "3. Run **NoxPromptEnhancer** for quick polish and quality tags.",
            "4. Feed everything into **NoxPromptPipelineCombiner** to generate the master prompt and negative block.",
        ],
        "Extended": [
            "• Start with the Builder, but pre-seed Character Creator, Human Designer, and Wardrobe Designer to lock identity and styling.",
            "• Action Director + Lighting Master define motion and atmosphere before you finalize palette overrides.",
            "• Use Palette Mixer to create structured overrides that the Builder can ingest (copy the overrides string).",
            "• Analyzer is ideal after Enhancer to review density, key phrases, and make iteration notes.",
        ],
        "Integration": [
            "• Register NODE_CLASSES from `NoxPromptNode` inside ComfyUI; all helpers are exposed there.",
            "• Preset-capable nodes (Builder, Palette Mixer, Character/Human Designer, NSFW variants) save to `custom_nodes/NoxPrompter/presets`.",
            "• Pipeline Combiner accepts raw strings, so you can splice third-party prompts or post-process with samplers easily.",
            "• Each node sticks to standard ComfyUI conventions: `INPUT_TYPES` describe exposed widgets, outputs are plain strings ready for downstream wiring.",
        ],
    }

    _TIP_LINES = [
        "• Pair Character Creator → Human Designer → Wardrobe Designer for a unified hero bible.",
        "• Palette Mixer overrides paste directly into the Builder's palette input block.",
        "• Action Director + NSFW Action Director share option tables—swap between them with the same preset names.",
        "• Lighting Master outputs both prompt text and short technical notes; send the notes into the Pipeline Combiner for reference cards.",
        "• Analyzer helps spot repeated descriptors before the final sampler prompt.",
    ]

    _SAFETY_LINES = [
        "• The NSFW Designer and NSFW Action Director automatically append baseline consent and age-negation phrases.",
        "• Leave `include_safety_note` enabled in NSFW nodes unless you replace it with a studio policy alternative.",
        "• Palette Mixer + Builder share override keys; keep them consistent so lighting or wardrobe selections do not fight each other.",
        "• Final pass: run Pipeline Combiner and scan the Safety & Compliance section before triggering renders.",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "detail_level": (list(cls._DETAIL_BUNDLES.keys()), {"default": "Quickstart"}),
            },
            "optional": {
                "include_pipeline": ("BOOLEAN", {"default": True}),
                "include_safety": ("BOOLEAN", {"default": True}),
                "include_tips": ("BOOLEAN", {"default": True}),
            },
        }

    @classmethod
    def IS_CHANGED(cls, *_args, **_kwargs):  # pragma: no cover - ComfyUI metadata hook
        return True

    def build_guide(
        self,
        detail_level: str,
        include_pipeline: bool = True,
        include_safety: bool = True,
        include_tips: bool = True,
    ):
        detail_key = detail_level if detail_level in self._DETAIL_BUNDLES else "Quickstart"
        intro = _format_section(
            "Nox Prompter Overview",
            [
                "The custom node suite is modular: start from the builder, layer specialists,"
                " and finish with the Pipeline Combiner for a structured master prompt.",
            ],
        )

        detail_section = _format_section(
            f"{detail_key} Workflow",
            self._DETAIL_BUNDLES.get(detail_key, []),
        )

        tip_section = ""
        if include_tips:
            tip_section = _format_section("Suggested Pairings", self._TIP_LINES)

        guide_parts = [segment for segment in (intro, detail_section, tip_section) if segment]
        guide_text = "\n\n".join(guide_parts)

        pipeline_text = ""
        if include_pipeline:
            lines = []
            for index, (description, _keys) in enumerate(NoxPromptPipelineCombiner.PIPELINE_SEQUENCE, start=1):
                token = f"{index}. {description}"
                lines.append(token)
            pipeline_text = dedent(
                "\n".join([
                    "Recommended Pipeline",
                    "--------------------",
                    *lines,
                ])
            ).strip()

        safety_text = ""
        if include_safety:
            safety_text = _format_section("Safety & Consistency", self._SAFETY_LINES)

        return (guide_text, pipeline_text, safety_text)


__all__ = ["NoxPromptUsageGuide"]
