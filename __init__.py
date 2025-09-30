"""
ComfyUI Nox Prompter - Custom Prompt Enhancement Nodes

A collection of custom nodes for ComfyUI that enhance prompt handling and manipulation.
Includes nodes for prompt enhancement, combination, and analysis.
"""

from .NoxPromptNode import (
    NoxPromptEnhancer,
    NoxPromptBuilder,
    NoxPromptPaletteMixer,
    NoxPromptNarrativeWeaver,
    NoxPromptNSFWDesigner,
    NoxPromptCombiner,
    NoxPromptAnalyzer,
)

# Register all the custom nodes with ComfyUI
NODE_CLASS_MAPPINGS = {
    "NoxPromptEnhancer": NoxPromptEnhancer,
    "NoxPromptBuilder": NoxPromptBuilder,
    "NoxPromptPaletteMixer": NoxPromptPaletteMixer,
    "NoxPromptNarrativeWeaver": NoxPromptNarrativeWeaver,
    "NoxPromptNSFWDesigner": NoxPromptNSFWDesigner,
    "NoxPromptCombiner": NoxPromptCombiner,
    "NoxPromptAnalyzer": NoxPromptAnalyzer,
}

# Display names that appear in the ComfyUI interface
NODE_DISPLAY_NAME_MAPPINGS = {
    "NoxPromptEnhancer": "Nox Prompt Enhancer",
    "NoxPromptBuilder": "Nox Prompt Builder",
    "NoxPromptPaletteMixer": "Nox Prompt Palette Mixer",
    "NoxPromptNarrativeWeaver": "Nox Prompt Narrative Weaver",
    "NoxPromptNSFWDesigner": "Nox Prompt NSFW Designer",
    "NoxPromptCombiner": "Nox Prompt Combiner", 
    "NoxPromptAnalyzer": "Nox Prompt Analyzer",
}

# Export the mappings for ComfyUI to discover
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# Version information
__version__ = "1.4.0"
__author__ = "NoxPrompter"
__description__ = "Custom prompt enhancement nodes for ComfyUI"