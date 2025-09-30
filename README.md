# ComfyUI Nox Prompter

A powerful collection of custom nodes for ComfyUI that enhance prompt handling, manipulation, and analysis for better AI image generation results.

## 🌟 Features

- **Formula-driven Prompt Builder**: Assemble cinematic Wan 2.2 prompts with guided subject, scene, motion, aesthetic, and style controls
- **Palette + Narrative Companions**: Use the Palette Mixer and Narrative Weaver to seed builder inputs with curated palettes and story scaffolding
- **Prompt Enhancement**: Automatically enhance prompts with style-specific additions and quality tags
- **Prompt Combination**: Combine multiple prompts using various blending modes
- **Prompt Analysis**: Analyze prompt characteristics, complexity, and style detection
- **Emphasis Control**: Apply emphasis and de-emphasis to prompts using weights
- **Curated Keyword Palettes**: Built-in lighting, camera, motion, emotion, and stylization vocabularies for rapid iteration
- **Adaptive Keyword Controls**: Switch between auto, inline, or compact keyword formatting, randomize missing selections with seeds, and override palettes inline
- **NSFW Prompt Designer**: Assemble mature-oriented prompts with curated safeguards, automatic baselines, and safety guidance

<img width="805" height="798" alt="image" src="https://github.com/user-attachments/assets/480a1bbc-fa04-4722-80bc-88f3ccc4918f" />


## 📦 Installation

### Method 1: Git Clone (Recommended)
1. Navigate to your ComfyUI `custom_nodes` directory
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ComfyNoxPrompter.git
   ```
3. Restart ComfyUI

### Method 2: Manual Installation
1. Download the repository as a ZIP file
2. Extract it to your ComfyUI `custom_nodes` directory
3. Ensure the folder is named `ComfyNoxPrompter`
4. Restart ComfyUI

## 🎯 Node Overview

### 1. Nox Prompt Builder
**Category**: `NoxPrompter/Builders`

Build cinematic Wan 2.2 prompts by mixing formulas with curated lighting, camera, motion, emotion, and stylization vocabularies.

**Guiding formulas**
- `Basic Formula` — Subject + Scene + Motion for fast ideation.
- `Advanced Formula` — Subject (desc) + Scene (desc) + Motion (desc) + Aesthetic controls + Stylization for production-ready prompts.

**Core inputs**
- `formula` (DROPDOWN): Choose Basic or Advanced structure
- `subject_focus`, `scene_setting`, `motion_arc` (STRING): Rich natural-language descriptions
- `narrative_hook`, `model_emphasis` (STRING, Optional): Extra beats or feature emphasis
- `keyword_style` (auto, inline, compact): Control how curated keywords appear in the assembled prompt
- `randomize_missing` + `random_seed`: Auto-fill "None" selections with curated palette picks
- `palette_overrides`: Inline overrides (e.g. `light_source: Moonlight, Firelight`) that merge with dropdown selections
- `extra_descriptors`, `custom_keywords`, `prompt_prefix`, `prompt_suffix` (STRING, Optional)
- `negative_prompt` (STRING, Optional): Direct output channel for Wan 2.2 negatives

**Keyword palettes**
- *Aesthetic controls*: Light Source, Light Quality, Time of Day, Shot Size, Composition, Lens Focal Length, Lens Angle, Lens Shot Type, Color Tone
- *Dynamics*: Motion Type (running, skateboarding, soccer, tennis, ping pong, skiing, basketball, football, bowl dance, cartwheel), Emotion (anger, fear, joy, sadness, surprise), Camera Moves (push-in, pull-out, pan left/right, tilt up, handheld, compound, following, orbit)
- *Stylization*: Visual Styles (felt style, 3D cartoon, pixel art, puppet animation, 3D game, claymation, anime, watercolor, B&W animation, oil painting) and Special Effects (tilt-shift, time-lapse)
- *Overrides & extras*: Merge additional palette lines (`lens_angle: Low Angle | Tilted Angle`) and append bespoke keyword clusters without losing dropdown state

**Outputs**
- `prompt`: Fully assembled prompt following the selected formula
- `negative_prompt`: Pass-through of the user-provided negative list
- `aesthetic_notes`: Summaries of the chosen lighting, camera, and color selections
- `dynamic_notes`: Summaries of motion, emotion, and camera move selections

**Example (Advanced Formula)**
```
Prefix: "Wan 2.2 cinematic prompt"
Subject: "Battle-hardened warrior drenched in rain, leather armor and fur"
Scene: "Muddy battlefield at night, lightning on the horizon"
Motion: "Charges forward roaring, blade swings in slow-motion crash zoom"
Aesthetic Picks: Daylight · Soft Light · Dusk · Medium Close-up · Balanced · Medium focal · Low angle · Single shot · Warm tone
Dynamics: Running · Anger · Push-in · Orbit
Stylization: Anime · Tilt-shift
Custom Keywords: "heroic energy, epic storytelling"

Result → A multi-sentence prompt with labeled cinematic palette, motion & camera clause, stylization clause, keyword styling control, and appended custom keywords — ready to paste into Wan 2.2.

### 2. Nox Prompt Palette Mixer
**Category**: `NoxPrompter/Companions`

Curate palette overrides and keyword clusters without touching spreadsheets. Pick a cinematic mood, dial intensity, and optionally add your own override lines — the mixer outputs ready-to-paste builder overrides and matching keyword suggestions.

**Inputs**
- `mood_profile`: Curated looks (Moody Nightfall, Action Spotlight, Dreamscape Glow)
- `intensity`: Blends in advanced overrides and keywords when pushed above 0.6
- `include_effects`: Toggle built-in special effects additions
- `custom_palette`: Extra override lines or keywords that merge with the result

**Outputs**
- `palette_overrides`: Multi-line text (e.g. `light_source: Moonlight, Practical Light`)
- `custom_keywords`: Comma-separated keywords to feed into the builder
- `notes`: Helpful summary of the chosen profile, intensity, and effects

### 3. Nox Prompt Narrative Weaver
**Category**: `NoxPrompter/Companions`

Generate narrative scaffolding — subject focus, scene setting, motion arc, narrative hook, and extra descriptors — from cinematic archetypes, tones, environments, set pieces, and tempo profiles.

**Inputs**
- `hero_archetype`: e.g. Resolute Protector, Wandering Visionary, Arcane Duelist
- `story_tone`: e.g. Hopeful Resurgence, Brooding Tension, Whimsical Discovery
- `environment`: e.g. Rain-Soaked Citadel, Skybound Orchard, Desert Mirage Bazaar
- `set_piece`: Action beats such as Climactic Duel, Heist Dash, Revelation Stillness
- `tempo`: Motion cadence presets (slow burn, measured build, surging, frantic)
- `focus_detail`: Extra keywords folded into the descriptor stack

**Outputs**
- `subject_focus`, `scene_setting`, `motion_arc`, `narrative_hook`, `extra_descriptors` — each aligns directly with builder inputs
```

### 4. Nox Prompt Enhancer
**Category**: `NoxPrompter/Text`

Enhances your base prompt with style-specific additions, quality tags, and emphasis control.

**Inputs**:
- `base_prompt` (STRING): Your main prompt text
- `enhancement_mode` (DROPDOWN): Choose from artistic, photorealistic, cinematic, fantasy, sci-fi, portrait, or none
- `emphasis_strength` (FLOAT 0.0-2.0): Control emphasis level using parentheses syntax
- `add_quality_tags` (BOOLEAN): Automatically add quality enhancement tags
- `secondary_prompt` (STRING, Optional): Additional prompt to combine
- `negative_prompt` (STRING, Optional): Negative prompt input
- `custom_style` (STRING, Optional): Your own custom style additions

**Outputs**:
- `enhanced_prompt` (STRING): The enhanced version of your prompt
- `negative_prompt` (STRING): Processed negative prompt

**Example Usage**:
```
Input: "a cat sitting on a chair"
Enhancement Mode: "photorealistic"
Emphasis Strength: 1.3
Add Quality Tags: True

Output: "((a cat sitting on a chair)), photorealistic, highly detailed, sharp focus, professional photography, high quality, detailed, masterpiece, 8k uhd, dslr, soft lighting, high quality"
```

### 5. Nox Prompt Combiner
**Category**: `NoxPrompter/Text`

Combines multiple prompts using different blending strategies.

**Inputs**:
- `prompt_1` (STRING): First prompt
- `prompt_2` (STRING): Second prompt
- `combination_mode` (DROPDOWN): concatenate, blend, alternate, or weighted
- `weight_1` (FLOAT 0.0-2.0): Weight for first prompt (in weighted mode)
- `weight_2` (FLOAT 0.0-2.0): Weight for second prompt (in weighted mode)
- `prompt_3` (STRING, Optional): Third prompt
- `separator` (STRING, Optional): Custom separator (default: ", ")

**Outputs**:
- `combined_prompt` (STRING): The combined result

**Combination Modes**:
- **Concatenate**: Simple joining with separator
- **Blend**: Interleave words from different prompts
- **Alternate**: Alternate sentences between prompts
- **Weighted**: Apply emphasis/de-emphasis based on weights

### 6. Nox Prompt Analyzer
**Category**: `NoxPrompter/Analysis`

Analyzes prompt characteristics and provides detailed feedback.

**Inputs**:
- `prompt` (STRING): Prompt to analyze
- `analysis_type` (DROPDOWN): word_count, complexity, style_detection, or full_analysis

**Outputs**:
- `analysis_result` (STRING): Detailed analysis text
- `word_count` (INT): Number of words in the prompt
- `complexity_score` (FLOAT): Complexity rating (0-10)

**Analysis Features**:
- Word count and length categorization
- Complexity scoring based on vocabulary and uniqueness
- Style detection (photorealistic, artistic, anime, cinematic, etc.)
- Sentiment analysis (positive, negative, neutral)

### 7. Nox Prompt NSFW Designer
**Category**: `NoxPrompter/NSFW`

Crafts mature-oriented prompts with curated tone, wardrobe, and safety guards. The node blends tasteful descriptors with required baselines so you can focus on creative direction while staying compliant.

**Inputs**
- `subject_focus`, `scene_setting` (STRING): Core concept and environment
- `pose_profile`, `wardrobe_style`, `tone_profile` (DROPDOWN): Curated NSFW personas and moods
- `lighting_setup`, `camera_framing`, `explicitness_level` (DROPDOWN, Optional): Fine-tune lighting, lensing, and intensity while auto-managing negatives
- `detail_accent`, `nsfw_tags` (STRING, Optional): Extra descriptors and keyword clusters
- `negative_prompt` (STRING, Optional): Merge your own negatives with the safeguarded baseline
- `include_negative_baseline`, `include_safety_note` (BOOLEAN): Toggle the automatic guardrails

**Outputs**
- `prompt`: Fully assembled NSFW-ready prompt with pose, wardrobe, lighting, and framing
- `negative_prompt`: Combined baseline+user list that filters underage, violent, or explicit anatomical extremes
- `safety_notes`: Quick reminders sourced from the chosen profiles plus a compliance headline

**Safety Features**
- Baseline negatives covering underage, coercive, or graphic subject matter
- Explicitness-level aware negatives to keep anatomy references tasteful
- Contextual notes explaining how to keep the scene respectful and compliant

## 🎨 Style Presets

### Enhancement Modes Available:
- **Artistic**: Adds painterly, expressive elements
- **Photorealistic**: Focuses on realistic photography terms
- **Cinematic**: Movie and film-style enhancements
- **Fantasy**: Magical and mystical elements
- **Sci-Fi**: Futuristic and technological terms
- **Portrait**: Professional portrait photography focus

## 💡 Usage Tips

1. **Pick the formula first**: Choose Basic for brainstorming or Advanced for full cinematic structure
2. **Seed with companions**: Use the Narrative Weaver and Palette Mixer to generate builder-ready inputs in seconds
3. **Tune keyword style**: Swap between auto, inline, or compact keyword presentation depending on downstream needs
4. **Randomize wisely**: Enable `randomize_missing` with a fixed seed to explore alternates while staying reproducible
5. **Layer keyword palettes**: Mix lighting, camera, motion, emotion, and style options to rapidly explore looks
6. **Layered Enhancement**: Feed the builder output into the Prompt Enhancer for stylistic polish
7. **Analysis Feedback**: Use the Analyzer to understand your prompt characteristics before enhancement
8. **Weight Control**: In the Combiner, weights > 1.0 add emphasis while < 1.0 reduce it
9. **Negative Prompts**: Both the Builder and Enhancer accept negative prompts so you can enforce consistency
10. **Custom Styles**: Use `custom_keywords`, `extra_descriptors`, or the Enhancer `custom_style` input to inject project-specific flavor
11. **Guard NSFW work**: Route mature concepts through the NSFW Designer to leverage curated baselines, safety notes, and explicitness controls before sharing outputs

## 🔧 Technical Details

### File Structure:
```
ComfyNoxPrompter/
├── __init__.py                 # Node registration
├── NoxPromptNode.py           # Main node implementations (builder, NSFW designer, palette mixer, narrative weaver, enhancer, combiner, analyzer)
├── README.md                  # This documentation
├── INSTALLATION.md            # Quick install reference
├── test_nodes.py              # Offline sanity tests for each node
├── examples/                  # Example workflows
└── LICENSE                    # License file
```

### Dependencies:
- ComfyUI (obviously!)
- Python 3.7+
- No additional packages required - uses only Python standard library

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- ComfyUI community for the excellent framework
- Inspired by the guide from traugdor90 on creating custom nodes
- All the prompt engineering enthusiasts who make AI art better

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/ComfyNoxPrompter/issues) page
2. Create a new issue with detailed information about your problem
3. Include your ComfyUI version and any error messages

---

**Happy Prompting! 🎨✨**
