from __future__ import annotations

from ..constants import *  # noqa: F403

class NoxPromptAnalyzer:
    """
    A node for analyzing prompt characteristics and providing feedback.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "analysis_type": (["word_count", "complexity", "style_detection", "full_analysis"], {
                    "default": "full_analysis"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING", "INT", "FLOAT")
    RETURN_NAMES = ("analysis_result", "word_count", "complexity_score")
    FUNCTION = "analyze_prompt"
    CATEGORY = "NoxPrompter/Analysis"
    
    def analyze_prompt(self, prompt, analysis_type):
        """
        Analyze the prompt and return various metrics.
        """
        
        if not prompt.strip():
            return ("Empty prompt", 0, 0.0)
        
        words = prompt.split()
        word_count = len(words)
        
        # Calculate complexity score
        complexity_score = self._calculate_complexity(prompt)
        
        if analysis_type == "word_count":
            result = f"Word count: {word_count}"
        
        elif analysis_type == "complexity":
            result = f"Complexity score: {complexity_score:.2f}"
        
        elif analysis_type == "style_detection":
            detected_style = self._detect_style(prompt)
            result = f"Detected style: {detected_style}"
        
        else:  # full_analysis
            detected_style = self._detect_style(prompt)
            sentiment = self._analyze_sentiment(prompt)
            result = f"""Prompt Analysis:
Word Count: {word_count}
Complexity Score: {complexity_score:.2f}
Detected Style: {detected_style}
Sentiment: {sentiment}
Length: {'Short' if word_count < 10 else 'Medium' if word_count < 25 else 'Long'}"""
        
        return (result, word_count, complexity_score)
    
    def _calculate_complexity(self, prompt):
        """Calculate a complexity score for the prompt."""
        words = prompt.split()
        if not words:
            return 0.0
        
        # Factors that increase complexity
        avg_word_length = sum(len(word) for word in words) / len(words)
        unique_words = len(set(words))
        uniqueness_ratio = unique_words / len(words)
        
        # Look for artistic/technical terms
        artistic_terms = ['masterpiece', 'detailed', 'artstation', 'concept', 'digital', 'painting']
        artistic_score = sum(1 for term in artistic_terms if term.lower() in prompt.lower())
        
        complexity = (avg_word_length * 0.3 + uniqueness_ratio * 0.4 + artistic_score * 0.3)
        return min(complexity, 10.0)  # Cap at 10
    
    def _detect_style(self, prompt):
        """Detect the likely style of the prompt."""
        prompt_lower = prompt.lower()
        
        style_keywords = {
            'photorealistic': ['photo', 'realistic', 'photography', 'dslr', 'camera'],
            'artistic': ['painting', 'art', 'artistic', 'canvas', 'brushstroke'],
            'anime': ['anime', 'manga', 'kawaii', 'chibi'],
            'cinematic': ['cinematic', 'movie', 'film', 'dramatic'],
            'fantasy': ['fantasy', 'magical', 'mystical', 'dragon', 'wizard'],
            'sci-fi': ['sci-fi', 'futuristic', 'cyberpunk', 'robot', 'space'],
            'abstract': ['abstract', 'surreal', 'experimental']
        }
        
        style_scores = {}
        for style, keywords in style_keywords.items():
            score = sum(1 for keyword in keywords if keyword in prompt_lower)
            if score > 0:
                style_scores[style] = score
        
        if style_scores:
            # Find the style with the highest score
            best_style = None
            best_score = 0
            for style, score in style_scores.items():
                if score > best_score:
                    best_score = score
                    best_style = style
            return best_style
        return "general"
    
    def _analyze_sentiment(self, prompt):
        """Basic sentiment analysis of the prompt."""
        positive_words = ['beautiful', 'amazing', 'stunning', 'gorgeous', 'magnificent', 'wonderful']
        negative_words = ['dark', 'scary', 'horror', 'grim', 'sinister', 'evil']
        
        prompt_lower = prompt.lower()
        positive_count = sum(1 for word in positive_words if word in prompt_lower)
        negative_count = sum(1 for word in negative_words if word in prompt_lower)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"

__all__ = ["NoxPromptAnalyzer"]
