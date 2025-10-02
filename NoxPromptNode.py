"""Legacy aggregator exposing Nox Prompter nodes and shared utilities."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path


def _load_module(module: str):
    """Import module preferring relative package path, then absolute."""

    package_prefix = f"{__package__}." if __package__ else ""
    candidates = [f"{package_prefix}{module}"] if package_prefix else []
    candidates.append(module)

    last_error: ModuleNotFoundError | None = None

    for candidate in candidates:
        try:
            return importlib.import_module(candidate)
        except ModuleNotFoundError as exc:
            last_error = exc

    # If both relative and absolute lookups failed, inject the plugin root into sys.path.
    plugin_root = Path(__file__).resolve().parent
    if str(plugin_root) not in sys.path:
        sys.path.insert(0, str(plugin_root))
        try:
            return importlib.import_module(module)
        except ModuleNotFoundError:  # pragma: no cover - will re-raise original error
            pass

    if last_error is None:  # pragma: no cover - defensive guard
        raise ModuleNotFoundError(module)

    raise last_error


_common = _load_module("noxprompter.common")
_constants = _load_module("noxprompter.constants")
_nodes = _load_module("noxprompter.nodes")


PresetManager = _common.PresetManager
PresetMixin = _common.PresetMixin
PromptFragmentFilter = _common.PromptFragmentFilter
_format_notes = getattr(_common, "_format_notes")
_resolve_action_option = getattr(_common, "_resolve_action_option")
_resolve_option = getattr(_common, "_resolve_option")
_resolve_with_custom = getattr(_common, "_resolve_with_custom")
_split_tokens = getattr(_common, "_split_tokens")


NoxPromptUsageGuide = _nodes.NoxPromptUsageGuide
NoxPromptWorkflowNavigator = _nodes.NoxPromptWorkflowNavigator
NoxPromptKontextHelper = _nodes.NoxPromptKontextHelper
NoxPromptOrganizer = _nodes.NoxPromptOrganizer
NoxPromptPromptBoard = _nodes.NoxPromptPromptBoard
NoxPromptShotlistOrganizer = _nodes.NoxPromptShotlistOrganizer
NoxPromptProductionPlanner = _nodes.NoxPromptProductionPlanner
NoxPromptEnhancer = _nodes.NoxPromptEnhancer
NoxPromptBuilder = _nodes.NoxPromptBuilder
NoxPromptPaletteMixer = _nodes.NoxPromptPaletteMixer
NoxPromptNarrativeWeaver = _nodes.NoxPromptNarrativeWeaver
NoxPromptCharacterCreator = _nodes.NoxPromptCharacterCreator
NoxPromptHumanDesigner = _nodes.NoxPromptHumanDesigner
NoxPromptWardrobeDesigner = _nodes.NoxPromptWardrobeDesigner
NoxPromptActionDirector = _nodes.NoxPromptActionDirector
NoxPromptPoseMaster = _nodes.NoxPromptPoseMaster
NoxPromptNSFWActionDirector = _nodes.NoxPromptNSFWActionDirector
NoxPromptNSFWAIO = _nodes.NoxPromptNSFWAIO
NoxPromptLightingMaster = _nodes.NoxPromptLightingMaster
NoxPromptCameraMaster = _nodes.NoxPromptCameraMaster
NoxPromptCameraLanguage = _nodes.NoxPromptCameraLanguage
NoxPromptNSFWDesigner = _nodes.NoxPromptNSFWDesigner
NoxPromptNSFWPoseMaster = _nodes.NoxPromptNSFWPoseMaster
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
    "NoxPromptWorkflowNavigator",
    "NoxPromptKontextHelper",
    "NoxPromptOrganizer",
    "NoxPromptPromptBoard",
    "NoxPromptShotlistOrganizer",
    "NoxPromptProductionPlanner",
    "NoxPromptEnhancer",
    "NoxPromptBuilder",
    "NoxPromptPaletteMixer",
    "NoxPromptNarrativeWeaver",
    "NoxPromptCharacterCreator",
    "NoxPromptHumanDesigner",
    "NoxPromptWardrobeDesigner",
    "NoxPromptActionDirector",
    "NoxPromptPoseMaster",
    "NoxPromptNSFWActionDirector",
    "NoxPromptNSFWAIO",
    "NoxPromptLightingMaster",
    "NoxPromptCameraMaster",
    "NoxPromptCameraLanguage",
    "NoxPromptNSFWDesigner",
    "NoxPromptNSFWPoseMaster",
    "NoxPromptCamz",
    "NoxPromptCombiner",
    "NoxPromptPipelineCombiner",
    "NoxPromptAnalyzer",
    "NODE_CLASSES",
    "get_node_classes",
]

__all__ = _BASE_EXPORTS + list(_CONSTANT_NAMES)  # type: ignore[assignment]

del _CONSTANT_NAMES
