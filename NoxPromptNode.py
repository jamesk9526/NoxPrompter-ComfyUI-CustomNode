"""Legacy aggregator exposing Nox Prompter nodes and shared utilities."""

from __future__ import annotations

from noxprompter import common as _common
from noxprompter import constants as _constants
from noxprompter import nodes as _nodes


PresetManager = _common.PresetManager
PresetMixin = _common.PresetMixin
PromptFragmentFilter = _common.PromptFragmentFilter
_format_notes = _common._format_notes  # noqa: SLF001
_resolve_action_option = _common._resolve_action_option  # noqa: SLF001
_resolve_option = _common._resolve_option  # noqa: SLF001
_resolve_with_custom = _common._resolve_with_custom  # noqa: SLF001
_split_tokens = _common._split_tokens  # noqa: SLF001


NoxPromptUsageGuide = _nodes.NoxPromptUsageGuide
NoxPromptOrganizer = _nodes.NoxPromptOrganizer
NoxPromptEnhancer = _nodes.NoxPromptEnhancer
NoxPromptBuilder = _nodes.NoxPromptBuilder
NoxPromptPaletteMixer = _nodes.NoxPromptPaletteMixer
NoxPromptNarrativeWeaver = _nodes.NoxPromptNarrativeWeaver
NoxPromptCharacterCreator = _nodes.NoxPromptCharacterCreator
NoxPromptHumanDesigner = _nodes.NoxPromptHumanDesigner
NoxPromptWardrobeDesigner = _nodes.NoxPromptWardrobeDesigner
NoxPromptActionDirector = _nodes.NoxPromptActionDirector
NoxPromptNSFWActionDirector = _nodes.NoxPromptNSFWActionDirector
NoxPromptNSFWAIO = _nodes.NoxPromptNSFWAIO
NoxPromptLightingMaster = _nodes.NoxPromptLightingMaster
NoxPromptNSFWDesigner = _nodes.NoxPromptNSFWDesigner
NoxPromptCamz = _nodes.NoxPromptCamz
NoxPromptCombiner = _nodes.NoxPromptCombiner
NoxPromptPipelineCombiner = _nodes.NoxPromptPipelineCombiner
NoxPromptAnalyzer = _nodes.NoxPromptAnalyzer

NODE_CLASSES = tuple(_nodes.NODE_CLASSES)
get_node_classes = _nodes.get_node_classes


_CONSTANT_NAMES = [name for name in dir(_constants) if name.isupper()]

for _const_name in _CONSTANT_NAMES:
    globals()[_const_name] = getattr(_constants, _const_name)

_BASE_EXPORTS = [
    "PresetManager",
    "PresetMixin",
    "PromptFragmentFilter",
    "_format_notes",
    "_resolve_action_option",
    "_resolve_option",
    "_resolve_with_custom",
    "_split_tokens",
    "NoxPromptUsageGuide",
    "NoxPromptOrganizer",
    "NoxPromptEnhancer",
    "NoxPromptBuilder",
    "NoxPromptPaletteMixer",
    "NoxPromptNarrativeWeaver",
    "NoxPromptCharacterCreator",
    "NoxPromptHumanDesigner",
    "NoxPromptWardrobeDesigner",
    "NoxPromptActionDirector",
    "NoxPromptNSFWActionDirector",
    "NoxPromptNSFWAIO",
    "NoxPromptLightingMaster",
    "NoxPromptNSFWDesigner",
    "NoxPromptCamz",
    "NoxPromptCombiner",
    "NoxPromptPipelineCombiner",
    "NoxPromptAnalyzer",
    "NODE_CLASSES",
    "get_node_classes",
]

__all__ = _BASE_EXPORTS + list(_CONSTANT_NAMES)  # type: ignore[assignment]

del _CONSTANT_NAMES
