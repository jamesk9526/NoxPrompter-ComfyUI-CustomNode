from __future__ import annotations

import re
from typing import Any, Dict, List, Tuple
from ..common import PresetMixin
from ..constants import *  # noqa: F403

class NoxPromptEnhancer(PresetMixin):
    """
    A custom ComfyUI node for enhancing and manipulating text prompts.
    Provides various prompt enhancement features including style application,
    keyword emphasis, and prompt combination.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {
                    "multiline": True,
                    "default": "a beautiful landscape"
                }),
                "enhancement_mode": (["none", "artistic", "photorealistic", "cinematic", "fantasy", "sci-fi", "portrait"], {
                    "default": "none"
                }),
                "emphasis_strength": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 2.0,
                    "step": 0.1
                }),
                "add_quality_tags": ("BOOLEAN", {"default": True}),
            },
            "optional": {
                "secondary_prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "negative_prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "custom_style": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "preset_action": (["none", "save", "load", "list"], {"default": "none"}),
                "preset_name": ("STRING", {"default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("enhanced_prompt", "negative_prompt", "preset_status")
    FUNCTION = "enhance_prompt"
    CATEGORY = "NoxPrompter/Text"
    
    def enhance_prompt(self, base_prompt, enhancement_mode, emphasis_strength, add_quality_tags, 
                      secondary_prompt="", negative_prompt="", custom_style="",
                      preset_action="none", preset_name=""):
        """
        Enhance the input prompt based on the selected parameters.
        """

        config = {
            "base_prompt": base_prompt,
            "enhancement_mode": enhancement_mode,
            "emphasis_strength": emphasis_strength,
            "add_quality_tags": add_quality_tags,
            "secondary_prompt": secondary_prompt,
            "negative_prompt": negative_prompt,
            "custom_style": custom_style,
        }

        config, preset_status = self._apply_preset_action(
            "prompt_enhancer",
            preset_action,
            preset_name,
            config,
        )

        base_prompt = config["base_prompt"]
        enhancement_mode = config["enhancement_mode"]
        emphasis_strength = float(config["emphasis_strength"])
        add_quality_tags = bool(config["add_quality_tags"])
        secondary_prompt = config.get("secondary_prompt", "")
        negative_prompt = config.get("negative_prompt", "")
        custom_style = config.get("custom_style", "")
        
        # Start with the base prompt
        enhanced_prompt = base_prompt.strip()
        
        # Apply emphasis strength if greater than 1.0
        if emphasis_strength > 1.0:
            # Add parentheses for emphasis (ComfyUI/Stable Diffusion syntax)
            emphasis_level = int((emphasis_strength - 1.0) * 10)
            emphasis_chars = "(" * min(emphasis_level, 5)  # Cap at 5 levels
            closing_chars = ")" * len(emphasis_chars)
            enhanced_prompt = f"{emphasis_chars}{enhanced_prompt}{closing_chars}"
        
        # Apply enhancement mode styles
        style_additions = self._get_style_additions(enhancement_mode)
        if style_additions:
            enhanced_prompt = f"{enhanced_prompt}, {style_additions}"
        
        # Add custom style if provided
        if custom_style.strip():
            enhanced_prompt = f"{enhanced_prompt}, {custom_style.strip()}"
        
        # Combine with secondary prompt if provided
        if secondary_prompt.strip():
            enhanced_prompt = f"{enhanced_prompt}, {secondary_prompt.strip()}"
        
        # Add quality tags if enabled
        if add_quality_tags:
            quality_tags = self._get_quality_tags(enhancement_mode)
            enhanced_prompt = f"{enhanced_prompt}, {quality_tags}"
        
        # Process negative prompt
        processed_negative = self._process_negative_prompt(negative_prompt, enhancement_mode)
        
        # Clean up the final prompt
        enhanced_prompt = self._clean_prompt(enhanced_prompt)

        return (enhanced_prompt, processed_negative, preset_status)
    
    def _get_style_additions(self, mode):
        """Get style-specific prompt additions based on enhancement mode."""
        styles = {
            "artistic": "artistic, painterly, expressive brushstrokes, vibrant colors",
            "photorealistic": "photorealistic, highly detailed, sharp focus, professional photography",
            "cinematic": "cinematic lighting, dramatic composition, film grain, movie still",
            "fantasy": "fantasy art, magical atmosphere, ethereal lighting, mystical",
            "sci-fi": "sci-fi, futuristic, high-tech, neon lighting, cyberpunk aesthetic",
            "portrait": "portrait photography, professional lighting, shallow depth of field, bokeh"
        }
        return styles.get(mode, "")
    
    def _get_quality_tags(self, mode):
        """Get quality enhancement tags based on the mode."""
        base_quality = "high quality, detailed, masterpiece"
        
        mode_specific = {
            "artistic": "8k resolution, trending on artstation",
            "photorealistic": "8k uhd, dslr, soft lighting, high quality",
            "cinematic": "4k, imax, film photography",
            "fantasy": "concept art, digital painting, trending on artstation",
            "sci-fi": "concept art, digital art, trending on artstation",
            "portrait": "professional photography, studio lighting"
        }
        
        specific_tags = mode_specific.get(mode, "best quality")
        return f"{base_quality}, {specific_tags}"
    
    def _process_negative_prompt(self, negative_prompt, mode):
        """Process and enhance the negative prompt based on mode."""
        base_negative = negative_prompt.strip() if negative_prompt.strip() else ""
        
        # Add common negative prompts based on mode
        mode_negatives = {
            "photorealistic": "cartoon, anime, painting, drawing, illustration",
            "artistic": "photograph, photo, realistic",
            "cinematic": "amateur, low quality, blurry",
            "fantasy": "modern, contemporary, realistic photography",
            "sci-fi": "medieval, ancient, primitive",
            "portrait": "full body, landscape, multiple people"
        }
        
        mode_specific = mode_negatives.get(mode, "")
        
        # Combine negatives
        if base_negative and mode_specific:
            return f"{base_negative}, {mode_specific}"
        elif mode_specific:
            return mode_specific
        else:
            return base_negative
    
    def _clean_prompt(self, prompt):
        """Clean up the prompt by removing duplicate commas and extra spaces."""
    # Remove multiple consecutive commas
        prompt = re.sub(r',\s*,', ',', prompt)
        # Remove spaces before commas
        prompt = re.sub(r'\s+,', ',', prompt)
        # Remove multiple consecutive spaces
        prompt = re.sub(r'\s+', ' ', prompt)
        # Add space after commas if missing
        prompt = re.sub(r',([^\s])', r', \1', prompt)
        return prompt.strip()

__all__ = ["NoxPromptEnhancer"]
