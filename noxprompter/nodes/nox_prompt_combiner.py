from __future__ import annotations

from ..constants import *  # noqa: F403

class NoxPromptCombiner:
    """
    A node for combining multiple prompts with different blending modes.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt_1": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "prompt_2": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "combination_mode": (["concatenate", "blend", "alternate", "weighted"], {
                    "default": "concatenate"
                }),
                "weight_1": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 2.0,
                    "step": 0.1
                }),
                "weight_2": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 2.0,
                    "step": 0.1
                }),
            },
            "optional": {
                "prompt_3": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "separator": ("STRING", {
                    "default": ", "
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("combined_prompt",)
    FUNCTION = "combine_prompts"
    CATEGORY = "NoxPrompter/Text"
    
    def combine_prompts(self, prompt_1, prompt_2, combination_mode, weight_1, weight_2, 
                       prompt_3="", separator=", "):
        """
        Combine prompts using different combination modes.
        """
        
        prompts = [p.strip() for p in [prompt_1, prompt_2, prompt_3] if p.strip()]
        
        if not prompts:
            return ("",)
        
        if len(prompts) == 1:
            return (prompts[0],)
        
        if combination_mode == "concatenate":
            return (separator.join(prompts),)
        
        elif combination_mode == "blend":
            # Simple blending - interleave words
            words = []
            all_words = [p.split() for p in prompts]
            max_len = max(len(w) for w in all_words)
            
            for i in range(max_len):
                for word_list in all_words:
                    if i < len(word_list):
                        words.append(word_list[i])
            
            return (" ".join(words),)
        
        elif combination_mode == "alternate":
            # Alternate between prompts sentence by sentence
            sentences = []
            for i, prompt in enumerate(prompts):
                prompt_sentences = [s.strip() for s in prompt.split('.') if s.strip()]
                for j, sentence in enumerate(prompt_sentences):
                    if (i + j) % len(prompts) == 0:
                        sentences.append(sentence)
            
            return (". ".join(sentences) + ".",)
        
        elif combination_mode == "weighted":
            # Apply weights using parentheses
            weighted_prompts = []
            weights = [weight_1, weight_2, 1.0]  # Default weight for prompt_3
            
            for prompt, weight in zip(prompts, weights[:len(prompts)]):
                if weight > 1.0:
                    emphasis_level = int((weight - 1.0) * 10)
                    emphasis_chars = "(" * min(emphasis_level, 5)
                    closing_chars = ")" * len(emphasis_chars)
                    weighted_prompts.append(f"{emphasis_chars}{prompt}{closing_chars}")
                elif weight < 1.0:
                    # Use square brackets for de-emphasis
                    deemphasis_level = int((1.0 - weight) * 10)
                    deemphasis_chars = "[" * min(deemphasis_level, 5)
                    closing_chars = "]" * len(deemphasis_chars)
                    weighted_prompts.append(f"{deemphasis_chars}{prompt}{closing_chars}")
                else:
                    weighted_prompts.append(prompt)
            
            return (separator.join(weighted_prompts),)
        
        return (separator.join(prompts),)

__all__ = ["NoxPromptCombiner"]
