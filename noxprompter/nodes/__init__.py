"""Node modules for the modular Nox Prompter package."""

from __future__ import annotations

from .nox_prompt_action_director import NoxPromptActionDirector
from .nox_prompt_analyzer import NoxPromptAnalyzer
from .nox_prompt_builder import NoxPromptBuilder
from .nox_prompt_camz import NoxPromptCamz
from .nox_prompt_camera_language import NoxPromptCameraMaster, NoxPromptCameraLanguage
from .nox_prompt_character_creator import NoxPromptCharacterCreator
from .nox_prompt_combiner import NoxPromptCombiner
from .nox_prompt_enhancer import NoxPromptEnhancer
from .nox_prompt_human_designer import NoxPromptHumanDesigner
from .nox_prompt_lighting_master import NoxPromptLightingMaster
from .nox_prompt_narrative_weaver import NoxPromptNarrativeWeaver
from .nox_prompt_nsfw_action_director import NoxPromptNSFWActionDirector
from .nox_prompt_nsfw_designer import NoxPromptNSFWDesigner
from .nox_prompt_nsfw_pose_master import NoxPromptNSFWPoseMaster
from .nox_prompt_pose_master import NoxPromptPoseMaster
from .nox_prompt_palette_mixer import NoxPromptPaletteMixer
from .nox_prompt_pipeline_combiner import NoxPromptPipelineCombiner
from .nox_prompt_wardrobe_designer import NoxPromptWardrobeDesigner
from .nox_prompt_usage_guide import NoxPromptUsageGuide
from .nox_prompt_workflow_navigator import NoxPromptWorkflowNavigator
from .nox_prompt_kontext_helper import NoxPromptKontextHelper
from .nox_prompt_prompt_organizer import NoxPromptOrganizer
from .nox_prompt_prompt_board import NoxPromptPromptBoard
from .nox_prompt_shotlist_organizer import NoxPromptShotlistOrganizer
from .nox_prompt_production_planner import NoxPromptProductionPlanner
from .nox_prompt_nsfw_aio import NoxPromptNSFWAIO

_NODE_CLASSES = (
    NoxPromptUsageGuide,
    NoxPromptWorkflowNavigator,
    NoxPromptKontextHelper,
    NoxPromptOrganizer,
    NoxPromptPromptBoard,
    NoxPromptShotlistOrganizer,
    NoxPromptProductionPlanner,
    NoxPromptEnhancer,
    NoxPromptBuilder,
    NoxPromptPaletteMixer,
    NoxPromptNarrativeWeaver,
    NoxPromptCharacterCreator,
    NoxPromptHumanDesigner,
    NoxPromptWardrobeDesigner,
    NoxPromptActionDirector,
    NoxPromptPoseMaster,
    NoxPromptNSFWActionDirector,
    NoxPromptNSFWAIO,
    NoxPromptLightingMaster,
    NoxPromptCameraMaster,
    NoxPromptNSFWDesigner,
    NoxPromptNSFWPoseMaster,
    NoxPromptCamz,
    NoxPromptCombiner,
    NoxPromptPipelineCombiner,
    NoxPromptAnalyzer,
)

NODE_CLASSES = _NODE_CLASSES


def get_node_classes():
    """Return all node classes defined in the modular package."""

    return NODE_CLASSES


__all__ = [
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
