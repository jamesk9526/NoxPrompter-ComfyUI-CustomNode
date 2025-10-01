"""Modular Nox Prompter node package."""

from __future__ import annotations

from . import common as _common
from . import constants as _constants
from .nodes import NODE_CLASSES as _NODE_CLASSES
from .nodes import get_node_classes as _get_node_classes


NODE_CLASSES = tuple(_NODE_CLASSES)
get_node_classes = _get_node_classes

for _helper_name in (
    "PresetManager",
    "PresetMixin",
    "PromptFragmentFilter",
    "_format_notes",
    "_resolve_action_option",
    "_resolve_option",
    "_resolve_with_custom",
    "_split_tokens",
):
    globals()[_helper_name] = getattr(_common, _helper_name)

for _cls in NODE_CLASSES:
    globals()[_cls.__name__] = _cls

for _const_name in dir(_constants):
    if _const_name.isupper():
        globals()[_const_name] = getattr(_constants, _const_name)
