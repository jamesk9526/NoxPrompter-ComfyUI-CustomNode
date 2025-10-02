# Example Workflows for ComfyUI Nox Prompter

This directory contains example workflows demonstrating how to use the Nox Prompter nodes effectively.

## Prompt Builder Quick Start

```
Subject Node → Nox Prompt Builder → Text Display / CLIP Text Encode
```

**Setup**:
1. Add a "Nox Prompt Builder" node and select `formula = Advanced Formula`
2. Fill in
     - `subject_focus`: "A brave farmhand hero"
     - `scene_setting`: "Sun-drenched meadow with tall grass"
     - `motion_arc`: "Sprints toward the camera clutching a weathered satchel"
3. (Optional) Add a `narrative_hook`: "Camera orbits to reveal cheering villagers"
4. (Optional) Drop in a "Nox Prompt Lighting Master" node, configure the lighting blueprint you want, then connect `lighting_prompt → lighting_prompt`, `mood_notes → lighting_summary`, and `technical_notes → lighting_technical_notes` on the Builder.
5. (Optional) Add a "Nox Prompt Camera Master" node (alias: Camera Language) and wire `camera_prompt → camera_prompt`, `framing_summary → camera_summary`, and `rigging_notes → camera_notes` on the Builder (and optionally into the Prompt Organizer `camera_notes`).
6. Pick keyword palette options
     - `shot_size`: Medium Close-up · `composition`: Balanced · `lens_angle`: Low Angle
     - `motion_type`: Running · `emotion`: Joy · `camera_basic`: Push-in · `camera_advanced`: Following
     - `visual_style`: Anime · `special_effect`: Tilt-shift
7. Add `custom_keywords`: "heroic energy, epic storytelling" and `extra_descriptors`: "Shot on 85mm, 16fps preview"
8. (Optional) Supply a `negative_prompt` like "blurry, low detail"

**Expected Result**:
A multi-sentence prompt with cinematic palette, motion & camera clause, stylization clause, and appended custom keywords—ready for Wan 2.2.

## Palette Mixer + Narrative Weaver Combo

```
Nox Prompt Narrative Weaver → Nox Prompt Builder
                           ↑
Nox Prompt Palette Mixer -----+
```

**Setup**:
1. Add a "Nox Prompt Narrative Weaver" node
     - `hero_archetype`: "Resolute Protector"
     - `story_tone`: "Brooding Tension"
     - `environment`: "Rain-Soaked Citadel"
     - `set_piece`: "Climactic Duel"
     - `tempo`: "surging"
2. Add a "Nox Prompt Palette Mixer" node
     - `mood_profile`: "Moody Nightfall"
     - `intensity`: `0.7`
     - `include_effects`: `True`
     - Optional `custom_palette`: `camera_basic: Pan Left\nvisual_style: Noir Film`
3. Feed the Weaver outputs (`subject_focus`, `scene_setting`, `motion_arc`, `narrative_hook`, `extra_descriptors`) into the corresponding Builder inputs
4. Send the Palette Mixer `palette_overrides` to the Builder `palette_overrides` input and `custom_keywords` to the Builder `custom_keywords`
5. Enable `randomize_missing` on the Builder with a chosen `random_seed` for reproducible variations

**Expected Result**:
A fully-populated builder with story beats, palette overrides, and keyword clusters generated automatically — perfect for rapid ideation.

## Basic Enhancement Example

```
Input Node (base prompt) → Nox Prompt Enhancer → Text Display
                                    ↓
Input Node (negative) ---------------+
```

**Setup**:
1. Add a "Nox Prompt Enhancer" node
2. Set base_prompt to: "a majestic dragon flying over mountains"
3. Set enhancement_mode to: "fantasy"
4. Set emphasis_strength to: 1.2
5. Enable add_quality_tags: True
6. Connect output to a text display or CLIP Text Encode node

**Expected Result**:
Enhanced prompt with fantasy-style additions and quality tags applied with slight emphasis.

## Multi-Prompt Combination Example

```
Input Node 1 -----→ Nox Prompt Combiner → Text Display
Input Node 2 -----→         ↑
Input Node 3 (opt) ---------+
```

**Setup**:
1. Add a "Nox Prompt Combiner" node
2. Set prompt_1 to: "beautiful sunset"
3. Set prompt_2 to: "over calm ocean waters"
4. Set prompt_3 to: "with seagulls flying"
5. Set combination_mode to: "weighted"
6. Set weight_1 to: 1.5 (emphasis on sunset)
7. Set weight_2 to: 1.0 (normal weight)

**Expected Result**:
Combined prompt with emphasis on the sunset element.

## Analysis and Enhancement Pipeline

```
Input Node → Nox Prompt Analyzer → Text Display (analysis)
     ↓
     → Nox Prompt Enhancer → Text Display (enhanced)
```

**Setup**:
1. Create your base prompt in an input node
2. Connect it to both Analyzer and Enhancer
3. Use Analyzer output to understand prompt characteristics
4. Adjust Enhancer settings based on analysis feedback
5. Use enhanced output for your generation workflow

## Advanced Workflow: Style Transfer

```
Style Prompt ----→ Nox Prompt Enhancer (style=artistic) ----→ Nox Prompt Combiner
Subject Prompt --→ Nox Prompt Enhancer (style=photorealistic) --→         ↑
                                                                 (mode=weighted)
                                                                      ↓
                                                               Final Enhanced Prompt
```

This workflow allows you to combine different styles with different subjects for complex prompt creation.

## Tips for Best Results

1. **Weave + Mix First**: Let the Narrative Weaver and Palette Mixer populate the Builder inputs when you need quick inspiration
2. **Build, Then Enhance**: Generate the core story with the Builder before applying stylistic polish
3. **Analyze First**: Use the Analyzer to understand your prompt before enhancement
4. **Iterate**: Try different enhancement modes and weights to find what works best
5. **Layer Effects**: Chain multiple nodes for complex prompt engineering
6. **Test Negative Prompts**: Use the automatic negative prompt generation for better results

## NSFW Designer Workflow (Mature Projects Only)

```
Concept Inputs → Nox Prompt NSFW Designer → Text Display / Builder / Enhancer
```

**Setup**:
1. Ensure your subject matter complies with local laws and platform policy. Only create adult, consensual scenarios.
2. Drop in a "Nox Prompt NSFW Designer" node.
3. Fill required fields such as:
     - `subject_focus`: "Athletic adult model stretching after a workout"
     - `scene_setting`: "Loft studio with floor-to-ceiling windows"
     - `pose_profile`: `Reclined Elegance`
     - `wardrobe_style`: `Sheer Robe`
     - `tone_profile`: `Soft Intimacy`
4. Adjust optional controls:
     - `lighting_setup`: `Candlelit Warmth`
     - `camera_framing`: `Low Angle Admiration`
     - `explicitness_level`: `Implied Nude`
     - Add `nsfw_tags`: "tasteful, confident, mature"
5. Leave `include_negative_baseline` and `include_safety_note` enabled unless you have advanced compliance tooling downstream.
6. Route the resulting `prompt` into your favorite text display or straight into the builder/enhancer pipeline and keep the generated `safety_notes` handy in your project log.

**Expected Result**:
A curated NSFW prompt assembled with tasteful descriptors, auto-negative baselines filtering out underage or abusive content, plus contextual safety notes summarizing the chosen profiles.

## NSFW Pose Master Workflow (Mature Projects Only)

```
Concept Inputs → Nox Prompt NSFW Pose Master → Text Display / Builder / Combiner
```

**Setup**:
1. Ensure the scene remains within policy-compliant, adult-only boundaries with clear consent language baked in.
2. Drop in a "Nox Prompt NSFW Pose Master" node.
3. Configure the required fields:
     - `subject_focus`: "Empowered adult performer leaning back on a velvet chaise"
     - `pose_profile`: `Reclined Elegance`
     - `camera_framing`: `Low Angle Admiration`
4. Shape the staging with optional modifiers:
     - `lighting_setup`: `Candlelit Warmth`
     - `heat_profile`: `Sensual`
     - `explicitness_level`: `Implied Nude`
     - `pose_intent`: "Highlight graceful posture while keeping tone tasteful and confident"
     - `support_props`: "velvet chaise, crystal coupe"
     - `expression_focus`: "relaxed smile, steady eye contact"
     - `movement_cue`: "slow inhale, gentle arch"
5. Leave the default `include_negative_baseline` and `include_safety_note` toggles enabled so baseline negatives and safety guidance stay attached.
6. Route the `pose_prompt` into Builder/Combiner pipelines, use `pose_negative` for safety filtering, and archive `pose_brief` + `safety_notes` in your production log.

**Expected Result**:
A pose-focused prompt with synchronized camera, lighting, and heat descriptors, an auto-curated negative stack, and a quick-reference brief that reinforces consent and safety reminders.