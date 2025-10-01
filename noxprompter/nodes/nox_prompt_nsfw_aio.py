from __future__ import annotations

from typing import List

from ..common import _split_tokens
from ..constants import NSFW_BASELINE_NEGATIVES, NSFW_DEFAULT_SAFETY_NOTE


class NoxPromptNSFWAIO:
    """Combine NSFW designer and action fragments into a single, safety-conscious output."""

    CATEGORY = "NoxPrompter/NSFW"
    FUNCTION = "combine"
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("combined_prompt", "combined_negative", "combined_safety", "fusion_notes")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "designer_prompt": ("STRING", {"multiline": True, "default": ""}),
                "designer_negative": ("STRING", {"multiline": True, "default": ""}),
                "designer_safety": ("STRING", {"multiline": True, "default": ""}),
            },
            "optional": {
                "action_prompt": ("STRING", {"multiline": True, "default": ""}),
                "action_summary": ("STRING", {"multiline": True, "default": ""}),
                "action_safety": ("STRING", {"multiline": True, "default": ""}),
                "camera_notes": ("STRING", {"multiline": True, "default": ""}),
                "extra_positive": ("STRING", {"multiline": True, "default": ""}),
                "extra_negative": ("STRING", {"multiline": True, "default": ""}),
                "extra_safety": ("STRING", {"multiline": True, "default": ""}),
                "include_baseline_negatives": ("BOOLEAN", {"default": True}),
                "include_default_safety": ("BOOLEAN", {"default": True}),
            },
        }

    def combine(
        self,
        designer_prompt: str,
        designer_negative: str,
        designer_safety: str,
        action_prompt: str = "",
        action_summary: str = "",
        action_safety: str = "",
        camera_notes: str = "",
        extra_positive: str = "",
        extra_negative: str = "",
        extra_safety: str = "",
        include_baseline_negatives: bool = True,
        include_default_safety: bool = True,
    ):
        positive_sections = [
            designer_prompt.strip(),
            action_prompt.strip(),
            extra_positive.strip(),
        ]
        combined_prompt = "\n".join([section for section in positive_sections if section]).strip()

        negative_tokens: List[str] = []
        for block in (designer_negative, extra_negative):
            if not block:
                continue
            for token in _split_tokens(block.replace("\n", ",")):
                cleaned = token.strip()
                if cleaned:
                    negative_tokens.append(cleaned)
        if include_baseline_negatives:
            negative_tokens.extend(NSFW_BASELINE_NEGATIVES)
        combined_negative = ", ".join(self._unique_sequence(negative_tokens))

        safety_chunks: List[str] = []
        if include_default_safety:
            safety_chunks.append(NSFW_DEFAULT_SAFETY_NOTE)
        safety_chunks.extend([designer_safety, action_safety, extra_safety])
        combined_safety = "\n".join(self._unique_sequence(self._split_lines(safety_chunks))).strip()

        fusion_lines: List[str] = []
        if action_summary.strip():
            fusion_lines.append(f"Action Summary: {action_summary.strip()}")
        if camera_notes.strip():
            fusion_lines.append(f"Camera Notes: {camera_notes.strip()}")
        if extra_positive.strip():
            fusion_lines.append("Extras merged into prompt body.")
        if extra_negative.strip():
            fusion_lines.append("Extra negative cues merged into combined negatives.")
        fusion_notes = "\n".join(fusion_lines)

        return combined_prompt, combined_negative, combined_safety, fusion_notes

    @staticmethod
    def _split_lines(chunks: List[str]) -> List[str]:
        lines: List[str] = []
        for chunk in chunks:
            if not chunk:
                continue
            for line in chunk.replace("\r", "\n").split("\n"):
                cleaned = line.strip()
                if cleaned:
                    lines.append(cleaned)
        return lines

    @staticmethod
    def _unique_sequence(values: List[str]) -> List[str]:
        seen = set()
        ordered: List[str] = []
        for value in values:
            key = value.lower()
            if key in seen:
                continue
            seen.add(key)
            ordered.append(value)
        return ordered


__all__ = ["NoxPromptNSFWAIO"]
