from __future__ import annotations

from typing import Dict, List

from ..common import PresetMixin, option_keys
from ..constants import (
    CAMERA_TYPES,
    FSTOP_OPTIONS,
    ISO_OPTIONS,
    LENS_FOCAL_LENGTHS,
    SHUTTER_SPEED_OPTIONS,
    WHITE_BALANCE_OPTIONS,
)


class NoxPromptCameraSelector(PresetMixin):
    """Select and combine camera technical settings into a prompt."""

    CATEGORY = "NoxPrompter/Camera"
    FUNCTION = "select_camera"
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("camera_prompt", "preset_status")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "custom_prompt": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                    },
                ),
                "camera_type": (
                    option_keys(CAMERA_TYPES),
                    {"default": "DSLR"},
                ),
            },
            "optional": {
                "iso": (
                    option_keys(ISO_OPTIONS),
                    {"default": "100"},
                ),
                "fstop": (
                    option_keys(FSTOP_OPTIONS),
                    {"default": "f/2.8"},
                ),
                "shutter_speed": (
                    option_keys(SHUTTER_SPEED_OPTIONS),
                    {"default": "1/125"},
                ),
                "lens_focal_length": (
                    option_keys(LENS_FOCAL_LENGTHS),
                    {"default": "50mm"},
                ),
                "white_balance": (
                    option_keys(WHITE_BALANCE_OPTIONS),
                    {"default": "Auto"},
                ),
                "camera_type_custom": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "iso_custom": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "fstop_custom": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "shutter_speed_custom": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "lens_focal_length_custom": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "white_balance_custom": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "preset_action": (
                    ["none", "save", "load", "list"],
                    {"default": "none"},
                ),
                "preset_name": (
                    "STRING",
                    {"default": ""},
                ),
            },
        }

    def select_camera(
        self,
        custom_prompt: str,
        camera_type: str,
        iso: str = "100",
        fstop: str = "f/2.8",
        shutter_speed: str = "1/125",
        lens_focal_length: str = "50mm",
        white_balance: str = "Auto",
        camera_type_custom: str = "",
        iso_custom: str = "",
        fstop_custom: str = "",
        shutter_speed_custom: str = "",
        lens_focal_length_custom: str = "",
        white_balance_custom: str = "",
        preset_action: str = "none",
        preset_name: str = "",
    ):
        config = {
            "custom_prompt": custom_prompt,
            "camera_type": camera_type,
            "iso": iso,
            "fstop": fstop,
            "shutter_speed": shutter_speed,
            "lens_focal_length": lens_focal_length,
            "white_balance": white_balance,
            "camera_type_custom": camera_type_custom,
            "iso_custom": iso_custom,
            "fstop_custom": fstop_custom,
            "shutter_speed_custom": shutter_speed_custom,
            "lens_focal_length_custom": lens_focal_length_custom,
            "white_balance_custom": white_balance_custom,
        }

        config, preset_status = self._apply_preset_action(
            "camera_selector",
            preset_action,
            preset_name,
            config,
        )

        custom_prompt = config.get("custom_prompt", custom_prompt)
        camera_type = config.get("camera_type", camera_type)
        iso = config.get("iso", iso)
        fstop = config.get("fstop", fstop)
        shutter_speed = config.get("shutter_speed", shutter_speed)
        lens_focal_length = config.get("lens_focal_length", lens_focal_length)
        white_balance = config.get("white_balance", white_balance)
        camera_type_custom = config.get("camera_type_custom", camera_type_custom)
        iso_custom = config.get("iso_custom", iso_custom)
        fstop_custom = config.get("fstop_custom", fstop_custom)
        shutter_speed_custom = config.get("shutter_speed_custom", shutter_speed_custom)
        lens_focal_length_custom = config.get("lens_focal_length_custom", lens_focal_length_custom)
        white_balance_custom = config.get("white_balance_custom", white_balance_custom)

        camera_cfg = self._resolve_option(camera_type, camera_type_custom, CAMERA_TYPES)
        iso_cfg = self._resolve_option(iso, iso_custom, ISO_OPTIONS)
        fstop_cfg = self._resolve_option(fstop, fstop_custom, FSTOP_OPTIONS)
        shutter_cfg = self._resolve_option(shutter_speed, shutter_speed_custom, SHUTTER_SPEED_OPTIONS)
        lens_cfg = self._resolve_option(lens_focal_length, lens_focal_length_custom, LENS_FOCAL_LENGTHS)
        wb_cfg = self._resolve_option(white_balance, white_balance_custom, WHITE_BALANCE_OPTIONS)

        prompt_fragments: List[str] = []
        if custom_prompt.strip():
            prompt_fragments.append(custom_prompt.strip())
        if camera_cfg:
            prompt_fragments.append(camera_cfg)
        if iso_cfg:
            prompt_fragments.append(iso_cfg)
        if fstop_cfg:
            prompt_fragments.append(fstop_cfg)
        if shutter_cfg:
            prompt_fragments.append(shutter_cfg)
        if lens_cfg:
            prompt_fragments.append(lens_cfg)
        if wb_cfg:
            prompt_fragments.append(wb_cfg)

        camera_prompt = ", ".join(fragment for fragment in prompt_fragments if fragment)
        if camera_prompt and not camera_prompt.endswith("."):
            camera_prompt += "."

        return camera_prompt, preset_status

    def _resolve_option(self, selection: str, custom: str, options: Dict[str, str]) -> str:
        if selection == "Custom":
            return custom.strip()
        return options.get(selection, "").strip()


__all__ = ["NoxPromptCameraSelector"]