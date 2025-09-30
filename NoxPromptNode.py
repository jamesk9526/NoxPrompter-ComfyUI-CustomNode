import random
import re


FORMULA_CONFIGS = {
    "Basic Formula": {
        "description": "Subject + Scene + Motion — perfect for ideation and quick inspiration.",
        "structure": ["subject", "scene", "motion"],
    },
    "Advanced Formula": {
        "description": "Subject (desc) + Scene (desc) + Motion (desc) + Aesthetic controls + Stylization.",
        "structure": ["subject", "scene", "motion", "aesthetic", "stylization"],
    },
}
LIGHT_SOURCE_OPTIONS = {
    "None": {"prompt": "", "summary": "No dedicated light source emphasis."},
    "Daylight": {"prompt": "daylight, sunlit ambience, warm highlights, natural light", "summary": "Sunlit scene with warm, natural illumination."},
    "Artificial Light": {"prompt": "artificial lighting, tungsten glow, controlled practicals", "summary": "Moody artificial lighting with cinematic practical sources."},
    "Moonlight": {"prompt": "moonlight, cool lunar glow, silver rim lighting", "summary": "Cool moonlit ambience with gentle highlights."},
    "Practical Light": {"prompt": "practical lighting, lamps, diegetic light sources", "summary": "Scene lit by visible practical fixtures."},
    "Firelight": {"prompt": "firelight, ember glow, flickering warm highlights", "summary": "Flickering firelight with warm dancing shadows."},
    "Fluorescent Light": {"prompt": "fluorescent lighting, clinical glow, cool overhead wash", "summary": "Flat fluorescent illumination with slight green tint."},
    "Overcast Light": {"prompt": "overcast sky, diffuse natural light, soft ambient shadows", "summary": "Soft overcast diffusion with muted contrast."},
    "Mixed Light": {"prompt": "mixed lighting sources, color contrast, layered temperatures", "summary": "Mixed lighting with contrasting color temperatures."},
    "Sunlight": {"prompt": "direct sunlight, high contrast shadows, golden highlights", "summary": "Direct sun with crisp highlights and defined shadows."},
    "Lantern Glow": {"prompt": "lantern-lit ambience, swaying warm pools, intimate highlights", "summary": "Lantern pools of light creating intimate pockets of warmth."},
    "Bioluminescence": {"prompt": "bioluminescent glow, organic shimmer, underwater luminosity", "summary": "Organic bioluminescence casting ethereal aquatic light."},
}


LIGHT_QUALITY_OPTIONS = {
    "None": {"prompt": "", "summary": "No additional light quality emphasis."},
    "Soft Light": {"prompt": "soft light, diffused shadows, gentle transition", "summary": "Soft, diffused lighting with subtle shadow falloff."},
    "Hard Light": {"prompt": "hard light, sharp shadows, chiseled contrast", "summary": "Hard-edged lighting with defined contrast."},
    "Top Light": {"prompt": "top lighting, overhead light source, dramatic downward shadows", "summary": "Top-down lighting with sculpted shadows."},
    "Side Light": {"prompt": "side lighting, directional key light, lateral highlights", "summary": "Side lighting with strong modeling."},
    "Backlight": {"prompt": "backlighting, halo rim, silhouette highlights", "summary": "Backlighting that separates subject from background."},
    "Bottom Light": {"prompt": "uplighting, underlight, theatrical glow", "summary": "Bottom lighting creating dramatic, eerie ambience."},
    "Rim Light": {"prompt": "rim lighting, edge highlight, subject outline glow", "summary": "Highlighted subject edges for separation."},
    "Silhouette": {"prompt": "silhouette lighting, subject in shadow, strong backlight", "summary": "High-contrast silhouette composition."},
    "Low Contrast": {"prompt": "low contrast lighting, gentle tonal range, subtle shadows", "summary": "Low-contrast lighting for a soft palette."},
    "High Contrast": {"prompt": "high contrast lighting, stark shadows, deep blacks", "summary": "High-contrast lighting with dramatic tonality."},
    "Dappled Light": {"prompt": "dappled light, patterned highlights, dancing shade", "summary": "Patterned illumination filtered through foliage or lattice."},
    "Volumetric Rays": {"prompt": "volumetric god rays, particulate beams, dramatic shafts", "summary": "Visible shafts of light carving through atmosphere."},
}


TIME_OF_DAY_OPTIONS = {
    "None": {"prompt": "", "summary": "No specific time-of-day emphasis."},
    "Daytime": {"prompt": "daytime setting, bright ambience", "summary": "Bright daytime environment."},
    "Nighttime": {"prompt": "nighttime scene, deep shadows, artificial accents", "summary": "Nighttime backdrop with dramatic contrast."},
    "Dusk": {"prompt": "dusk, golden hour, lingering warmth", "summary": "Golden hour glow with soft warmth."},
    "Sunset": {"prompt": "sunset sky, saturated horizon, long shadows", "summary": "Sunset palette with vivid horizon."},
    "Dawn": {"prompt": "pre-dawn hues, gentle blue hour, quiet ambience", "summary": "Pre-dawn tones with soft gradients."},
    "Sunrise": {"prompt": "sunrise light, fresh warmth, emerging glow", "summary": "Sunrise optimism with warm highlights."},
    "Midnight": {"prompt": "midnight sky, star-pricked darkness, tranquil hush", "summary": "Deep midnight calm with subtle celestial accents."},
    "Blue Hour": {"prompt": "blue hour tones, twilight glow, cobalt horizon", "summary": "Cool twilight wash bridging night and day."},
}


SHOT_SIZE_OPTIONS = {
    "None": {"prompt": "", "summary": "No shot size emphasis."},
    "Close-up": {"prompt": "close-up shot, intimate framing, facial detail", "summary": "Close-up framing for emotional focus."},
    "Medium Close-up": {"prompt": "medium close-up composition, chest-up framing", "summary": "Medium close-up showcasing shoulders and expression."},
    "Medium Shot": {"prompt": "medium shot, balanced subject framing", "summary": "Medium shot capturing subject and context."},
    "Medium Long Shot": {"prompt": "medium long shot, knees-up framing", "summary": "Medium long shot blending subject and space."},
    "Long Shot": {"prompt": "long shot, full body, environmental scale", "summary": "Long shot emphasizing subject within environment."},
    "Full Shot": {"prompt": "full shot, entire figure, spatial context", "summary": "Full body framing with contextual surroundings."},
    "Wide Angle": {"prompt": "wide angle framing, expansive field of view", "summary": "Wide angle perspective with environmental breadth."},
    "Extreme Close-up": {"prompt": "extreme close-up, micro expression, intimate texture", "summary": "Intense framing that magnifies subtle detail."},
    "Bird's Eye Wide": {"prompt": "bird's-eye master shot, sweeping overhead, geographic context", "summary": "High vantage shot revealing spatial relationships."},
}


COMPOSITION_OPTIONS = {
    "None": {"prompt": "", "summary": "No composition emphasis."},
    "Centered": {"prompt": "centered composition, balanced subject placement", "summary": "Subject centered for symmetry."},
    "Balanced": {"prompt": "balanced framing, visual equilibrium", "summary": "Balanced composition with even weight."},
    "Right-weighted": {"prompt": "right-weighted composition, dynamic off-center balance", "summary": "Subject anchored to the right for motion."},
    "Left-weighted": {"prompt": "left-weighted composition, directional focus", "summary": "Subject anchored to the left for leading motion."},
    "Symmetrical": {"prompt": "symmetrical framing, mirrored balance", "summary": "Symmetrical layout with mirrored elements."},
    "Short-siding": {"prompt": "short-siding composition, open space behind subject", "summary": "Short-siding for tension and anticipation."},
    "Leading Lines": {"prompt": "leading lines composition, guiding geometry, directional flow", "summary": "Structural lines that guide the eye to the subject."},
    "Rule of Thirds": {"prompt": "rule of thirds framing, dynamic balance, offset subject", "summary": "Offset placement using thirds for energetic balance."},
}


LENS_FOCAL_OPTIONS = {
    "None": {"prompt": "", "summary": "No focal length emphasis."},
    "Medium": {"prompt": "medium focal length, natural perspective", "summary": "Medium focal length for balanced view."},
    "Wide Angle": {"prompt": "wide angle lens, expanded perspective, mild distortion", "summary": "Wide angle depth with sweeping environment."},
    "Long": {"prompt": "long lens, compressed background, shallow depth", "summary": "Long lens compression with tight focus."},
    "Telephoto": {"prompt": "telephoto lens, extreme compression, isolated subject", "summary": "Telephoto compression isolating subject."},
    "Fisheye": {"prompt": "fisheye lens, dramatic curvature, immersive distortion", "summary": "Fisheye distortion for stylized wrap."},
    "Ultra Wide": {"prompt": "ultra wide focal length, expansive sweep, dramatic scale", "summary": "Ultra wide view exaggerating space and scope."},
    "Macro": {"prompt": "macro lens, magnified detail, shallow depth of field", "summary": "Macro magnification revealing intricate textures."},
}


LENS_ANGLE_OPTIONS = {
    "None": {"prompt": "", "summary": "No camera angle emphasis."},
    "Over-the-shoulder": {"prompt": "over-the-shoulder view, subjective framing", "summary": "Over-the-shoulder perspective for dialogue."},
    "High Angle": {"prompt": "high angle shot, elevated vantage", "summary": "High angle perspective for vulnerability."},
    "Low Angle": {"prompt": "low angle shot, heroic scale", "summary": "Low angle for power and grandeur."},
    "Tilted Angle": {"prompt": "dutch angle, tilted horizon, dynamic tension", "summary": "Tilted angle introducing unease."},
    "Aerial Shot": {"prompt": "aerial perspective, sweeping overhead view", "summary": "Aerial viewpoint capturing scale."},
    "Top-down View": {"prompt": "top-down shot, orthographic view, planar composition", "summary": "Top-down vantage for graphic patterns."},
    "Ground Level": {"prompt": "ground-level angle, horizon skimming, towering subject", "summary": "Camera placed at ground height for towering emphasis."},
    "Point-of-View": {"prompt": "first-person POV angle, subjective framing, immersive gaze", "summary": "Immersive first-person angle echoing the character's view."},
}


LENS_TYPE_OPTIONS = {
    "None": {"prompt": "", "summary": "No shot type emphasis."},
    "Single Shot": {"prompt": "single shot focus, solo subject", "summary": "Single shot isolating the hero."},
    "Two Shot": {"prompt": "two shot framing, dual subjects", "summary": "Two shot balancing interactions."},
    "Three Shot": {"prompt": "three shot composition, trio dynamic", "summary": "Three shot capturing group interplay."},
    "Group Shot": {"prompt": "group shot, ensemble framing", "summary": "Group shot highlighting ensemble relationships."},
    "Establishing Shot": {"prompt": "establishing shot, wide context, scene-setting", "summary": "Establishing shot grounding the location."},
    "Insert Shot": {"prompt": "insert shot detail, object emphasis, storytelling prop", "summary": "Tight detail shot spotlighting a crucial element."},
    "Crowd Panorama": {"prompt": "crowd panorama, sweeping ensemble, layered depth", "summary": "Expansive ensemble shot capturing scale and energy."},
}


COLOR_TONE_OPTIONS = {
    "None": {"prompt": "", "summary": "No color tone emphasis."},
    "Warm Tone": {"prompt": "warm color palette, golden hues, inviting saturation", "summary": "Warm palette with golden highlights."},
    "Cool Tone": {"prompt": "cool color palette, blue undertones, serene mood", "summary": "Cool palette with calming tones."},
    "High Saturation": {"prompt": "high saturation, vivid colors, bold intensity", "summary": "Highly saturated color treatment."},
    "Low Saturation": {"prompt": "low saturation, muted palette, cinematic restraint", "summary": "Muted palette with cinematic restraint."},
    "Pastel Tone": {"prompt": "pastel color palette, powdery hues, gentle saturation", "summary": "Soft pastel wash for dreamy, delicate moods."},
    "Neo Noir": {"prompt": "neo-noir palette, electric highlights, deep shadows", "summary": "High-contrast neon noir treatment with moody blacks."},
}


MOTION_TYPE_OPTIONS = {
    "None": {"prompt": "", "summary": "No specific motion descriptor."},
    "Running": {"prompt": "dynamic running motion, explosive sprint, powerful stride", "summary": "High-energy running sequence."},
    "Skateboarding": {"prompt": "skateboarding trick, ollie, urban street energy", "summary": "Skateboarding stunt with street flair."},
    "Soccer": {"prompt": "soccer play, agile footwork, goal attempt", "summary": "Soccer action with athletic control."},
    "Tennis": {"prompt": "tennis rally, racket swing, athletic lunge", "summary": "Tennis motion with decisive swing."},
    "Ping Pong": {"prompt": "table tennis volley, rapid reflexes", "summary": "Ping pong rally with rapid exchanges."},
    "Skiing": {"prompt": "downhill skiing, carving turns, powder spray", "summary": "Skiing descent with dynamic carving."},
    "Basketball": {"prompt": "basketball drive, crossover dribble, slam dunk", "summary": "Basketball highlight moment."},
    "Football": {"prompt": "football play, sprint downfield, defensive pressure", "summary": "Football play with explosive impact."},
    "Bowl Dance": {"prompt": "bowl dance motion, rhythmic choreography", "summary": "Stylized bowl dance movement."},
    "Cartwheel": {"prompt": "cartwheel, acrobatic rotation, graceful motion", "summary": "Cartwheel showcasing athletic grace."},
    "Hovering": {"prompt": "hovering suspension, weightless balance, gentle drift", "summary": "Weightless hover capturing poised suspension."},
    "Freefall": {"prompt": "freefall descent, gravity rush, wind-torn limbs", "summary": "High-velocity drop frozen mid freefall."},
}


EMOTION_OPTIONS = {
    "None": {"prompt": "", "summary": "No explicit emotional cue."},
    "Anger": {"prompt": "fiery anger, clenched expression, intense gaze", "summary": "Emotion of anger and determination."},
    "Fear": {"prompt": "subtle fear, wide eyes, tense posture", "summary": "Emotion of fear and uncertainty."},
    "Joy": {"prompt": "radiant joy, bright smile, delighted energy", "summary": "Joyful optimism."},
    "Sadness": {"prompt": "somber sadness, reflective emotion", "summary": "Quiet sadness and introspection."},
    "Surprise": {"prompt": "surprised reaction, widened expression", "summary": "Emotion of surprise and wonder."},
    "Determination": {"prompt": "steely determination, set jaw, unwavering focus", "summary": "Focused resolve radiating grit and purpose."},
    "Serenity": {"prompt": "calm serenity, relaxed features, centered presence", "summary": "Peaceful composure with gentle poise."},
}


CAMERA_BASIC_OPTIONS = {
    "None": {"prompt": "", "summary": "No basic camera move."},
    "Push-in": {"prompt": "camera push-in, forward dolly, tightening focus", "summary": "Push-in move for increasing intensity."},
    "Pull-out": {"prompt": "camera pull-out, backward dolly, reveal context", "summary": "Pull-out move to reveal context."},
    "Pan Right": {"prompt": "pan right, lateral camera sweep", "summary": "Pan right following subject motion."},
    "Pan Left": {"prompt": "pan left, lateral follow", "summary": "Pan left tracking movement."},
    "Tilt Up": {"prompt": "tilt up, vertical reveal", "summary": "Tilt up uncovering grandeur."},
    "Crane Sweep": {"prompt": "crane sweep, rising arc, cinematic reveal", "summary": "Elevated crane arc that lifts to reveal scope."},
    "Whip Pan": {"prompt": "whip pan, rapid pivot, motion blur streaks", "summary": "Snap pan creating dynamic motion streaks."},
}


CAMERA_ADVANCED_OPTIONS = {
    "None": {"prompt": "", "summary": "No advanced camera move."},
    "Handheld": {"prompt": "handheld camera, organic sway, documentary feel", "summary": "Handheld movement for visceral texture."},
    "Compound": {"prompt": "compound move, layered dolly and pan", "summary": "Compound move blending multiple axes."},
    "Following": {"prompt": "dynamic follow shot, tracking movement", "summary": "Following shot tracking the subject."},
    "Orbit": {"prompt": "orbiting camera, circular move, wraparound view", "summary": "Orbiting move for immersive coverage."},
    "Steadicam Glide": {"prompt": "steadicam glide, fluid tracking, stabilized motion", "summary": "Stabilized glide preserving fluid, anchored movement."},
    "Cable Cam Chase": {"prompt": "cable cam chase, high-speed lateral track, aerial pursuit", "summary": "High-speed cable run carving dynamic parallax."},
}


VISUAL_STYLE_OPTIONS = {
    "None": {"prompt": "", "summary": "No specific visual style."},
    "Felt Style": {"prompt": "felt texture style, handcrafted softness", "summary": "Felt-inspired tactile aesthetic."},
    "3D Cartoon": {"prompt": "3D cartoon aesthetic, stylized characters", "summary": "3D cartoon look with bold forms."},
    "Pixel Art": {"prompt": "pixel art style, retro resolution", "summary": "Pixel art aesthetic with retro charm."},
    "Puppet Animation": {"prompt": "puppet animation style, tangible materials", "summary": "Puppet animation with stop-motion feel."},
    "3D Game": {"prompt": "3D game visuals, real-time rendering", "summary": "3D game engine aesthetic."},
    "Claymation": {"prompt": "claymation style, sculpted forms", "summary": "Claymation stop-motion texture."},
    "Anime": {"prompt": "anime style, crisp linework, expressive shading", "summary": "Anime-inspired illustrative style."},
    "Watercolor": {"prompt": "watercolor wash, fluid pigment, paper texture", "summary": "Watercolor painting feel."},
    "B&W Animation": {"prompt": "black and white animation, noir contrast", "summary": "Monochrome animation aesthetic."},
    "Oil Painting": {"prompt": "oil painting style, rich brushwork", "summary": "Oil painting depth and texture."},
    "Ink Sketch": {"prompt": "ink sketch style, bold linework, crosshatch shading", "summary": "Expressive inked line art with graphic contrast."},
    "Voxel Art": {"prompt": "voxel art style, blocky volumetric pixels, retro 3D", "summary": "Voxel-based 3D aesthetic with chunky forms."},
}


SPECIAL_EFFECT_OPTIONS = {
    "None": {"prompt": "", "summary": "No special effect emphasis."},
    "Tilt-shift": {"prompt": "tilt-shift effect, miniature depth of field", "summary": "Tilt-shift miniature illusion."},
    "Time-lapse": {"prompt": "time-lapse effect, accelerated motion", "summary": "Time-lapse acceleration for dynamic pacing."},
    "Light Trails": {"prompt": "long-exposure light trails, kinetic streaks, luminous ribbons", "summary": "Dynamic light streaks painting motion paths."},
    "Chromatic Bloom": {"prompt": "chromatic bloom effect, spectral haze, prismatic fringe", "summary": "Prismatic bloom that radiates color halos."},
}


PALETTE_PROFILES = {
    "Moody Nightfall": {
        "description": "Storm-lashed nocturnal palette with electrified highlights and handheld energy.",
        "overrides": {
            "light_source": ["Moonlight", "Practical Light"],
            "light_quality": ["Soft Light"],
            "time_of_day": ["Nighttime"],
            "color_tone": ["Cool Tone"],
            "camera_advanced": ["Handheld"],
        },
        "intense_overrides": {
            "motion_type": ["Running"],
            "lens_angle": ["Low Angle"],
        },
        "effects": ["Time-lapse"],
        "keywords": [
            "storm-lashed",
            "suspended rain droplets",
            "electric skyline",
            "brooding shadows",
        ],
        "intense_keywords": [
            "staccato lightning bursts",
            "ground-level spray",
        ],
        "effect_keywords": ["temporal smearing"],
    },
    "Action Spotlight": {
        "description": "High-contrast spotlighting that carves out kinetic hero beats on stage-like sets.",
        "overrides": {
            "light_source": ["Artificial Light"],
            "light_quality": ["Hard Light"],
            "time_of_day": ["Daytime"],
            "shot_size": ["Medium Close-up"],
            "composition": ["Right-weighted"],
            "camera_basic": ["Push-in"],
        },
        "intense_overrides": {
            "motion_type": ["Basketball"],
            "camera_advanced": ["Orbit"],
        },
        "effects": ["Tilt-shift"],
        "keywords": [
            "razor-edged highlights",
            "charged air",
            "spotlit sweat sheen",
        ],
        "intense_keywords": ["dynamic crowd blur"],
        "effect_keywords": ["miniature stage illusion"],
    },
    "Dreamscape Glow": {
        "description": "Soft dawn-drenched dreamscape with painterly diffusion and weightless pacing.",
        "overrides": {
            "light_source": ["Daylight"],
            "light_quality": ["Soft Light"],
            "time_of_day": ["Dawn"],
            "color_tone": ["Warm Tone"],
            "visual_style": ["Watercolor"],
            "lens_focal": ["Wide Angle"],
        },
        "intense_overrides": {
            "composition": ["Symmetrical"],
            "special_effect": ["Tilt-shift"],
        },
        "effects": ["Tilt-shift"],
        "keywords": [
            "ethereal mist",
            "periwinkle glow",
            "feathered highlights",
        ],
        "intense_keywords": ["floating pollen shimmer"],
        "effect_keywords": ["miniature haze"],
    },
    "Urban Neon Rush": {
        "description": "High-voltage city palette pulsing with reflected neon and kinetic energy.",
        "overrides": {
            "light_source": ["Artificial Light", "Mixed Light"],
            "light_quality": ["High Contrast"],
            "time_of_day": ["Nighttime"],
            "color_tone": ["High Saturation"],
            "camera_basic": ["Whip Pan"],
        },
        "intense_overrides": {
            "motion_type": ["Running"],
            "camera_advanced": ["Cable Cam Chase"],
        },
        "effects": ["Light Trails"],
        "keywords": [
            "neon signage",
            "slick pavement",
            "electric reflections",
        ],
        "intense_keywords": [
            "crowd rush blur",
            "pulsebeat traffic",
        ],
        "effect_keywords": ["holographic streaks"],
    },
    "Aurora Reverie": {
        "description": "Celestial aurora palette awash with drifting color curtains and tranquil wonder.",
        "overrides": {
            "light_source": ["Moonlight"],
            "light_quality": ["Volumetric Rays"],
            "time_of_day": ["Midnight"],
            "color_tone": ["Cool Tone"],
            "visual_style": ["Watercolor"],
        },
        "intense_overrides": {
            "composition": ["Leading Lines"],
            "lens_angle": ["Ground Level"],
        },
        "effects": ["Chromatic Bloom"],
        "keywords": [
            "dancing aurora",
            "glacial horizon",
            "whispered starlight",
        ],
        "intense_keywords": [
            "skyfire curtains",
            "crystalline hush",
        ],
        "effect_keywords": ["spectral mist"],
    },
}


NARRATIVE_ARCHETYPES = {
    "Resolute Protector": {
        "subject": "Resolute protector clad in weathered armor",
        "keywords": ["steadfast", "guardian", "battle-tempered"],
    },
    "Wandering Visionary": {
        "subject": "Wandering visionary draped in layered fabrics",
        "keywords": ["imaginative", "inventive", "wide-eyed"],
    },
    "Arcane Duelist": {
        "subject": "Arcane duelist wreathed in swirling glyphs",
        "keywords": ["charged sigils", "arc-light", "precision"],
    },
    "Rebel Outrider": {
        "subject": "Rebel outrider astride a dust-scarred hoverbike",
        "keywords": ["maverick", "reckless", "ferocious"],
    },
    "Archivist Seer": {
        "subject": "Archivist seer cocooned in floating tomes and light glyphs",
        "keywords": ["omniscient", "patient", "enigmatic"],
    },
}


NARRATIVE_TONES = {
    "Hopeful Resurgence": {
        "descriptor": "radiating renewed hope",
        "ambience": "glints of light pierce the gloom",
        "hook": "A surge of hope cuts through the collapse.",
        "keywords": ["amber embers", "resilient resolve"],
    },
    "Brooding Tension": {
        "descriptor": "coiled with restrained fury",
        "ambience": "echoing thunder gathers along the horizon",
        "hook": "Tension thickens as the storm converges.",
        "keywords": ["pressure building", "charged silence"],
    },
    "Whimsical Discovery": {
        "descriptor": "buoyed by playful curiosity",
        "ambience": "glowing motes dance in the periphery",
        "hook": "Delight sparks as a hidden wonder unfurls.",
        "keywords": ["gossamer spark", "playful wonder"],
    },
    "Rising Triumph": {
        "descriptor": "charged with impending victory",
        "ambience": "anthemic echoes swell across the horizon",
        "hook": "Momentum crests as destiny crowds the frame.",
        "keywords": ["surging anthem", "victory pulse"],
    },
    "Haunting Echo": {
        "descriptor": "haunted by distant memories",
        "ambience": "soft dirges reverberate through vacant halls",
        "hook": "Silence lingers long after the last note falls.",
        "keywords": ["ghostlight", "murmured lament"],
    },
}


NARRATIVE_ENVIRONMENTS = {
    "Rain-Soaked Citadel": {
        "description": "Rain-soaked citadel ramparts shimmer under guttering torchlight",
        "details": "rain threads off crenellations, puddles mirror the battle-scarred stone",
        "keywords": ["slick masonry", "torchlit haze"],
    },
    "Skybound Orchard": {
        "description": "Skybound orchard terraces float amid drifting cloudbanks",
        "details": "luminous fruit sway on wind-swept branches",
        "keywords": ["weightless terraces", "cloud-sifted light"],
    },
    "Desert Mirage Bazaar": {
        "description": "Sun-baked bazaar shimmers inside a wavering desert mirage",
        "details": "textile canopies ripple above sandstone stalls",
        "keywords": ["heat shimmer", "spice-laden air"],
    },
    "Submerged Temple": {
        "description": "Sunken temple halls glimmer beneath rippling water canopy",
        "details": "shoals of fish weave through mossy columns",
        "keywords": ["refracted light", "ancient murals"],
    },
    "Skyline Rooftops": {
        "description": "Skyline rooftops knit a maze above neon avenues",
        "details": "fluttering tarps snap between antenna arrays",
        "keywords": ["city haze", "wind-sliced banners"],
    },
}


NARRATIVE_SETPIECES = {
    "Climactic Duel": {
        "motion": "locks blades with an adversary as sparks cascade in slow arcs",
        "hook": "Every strike echoes like a bell tolling fate.",
        "keywords": ["arc of sparks", "ringing steel"],
    },
    "Heist Dash": {
        "motion": "vaults through market stalls clutching luminous artifacts",
        "hook": "The chase snaps into sharp focus as alarms flare.",
        "keywords": ["darting silhouettes", "flashing sirens"],
    },
    "Revelation Stillness": {
        "motion": "stands suspended as constellations form sigils around them",
        "hook": "Silence blooms before the cosmos whispers the truth.",
        "keywords": ["starlit hush", "sigil glow"],
    },
    "Rescue Descent": {
        "motion": "rappels through fractured skylights to lift allies from danger",
        "hook": "The drop becomes a lifeline threading hope through chaos.",
        "keywords": ["tensioned cable", "shattered glass"],
    },
    "Diplomatic Standoff": {
        "motion": "circles the negotiation table as tempers simmer just below the surface",
        "hook": "Every measured word teeters between alliance and collapse.",
        "keywords": ["clenched fists", "shifting glances"],
    },
}


TEMPO_PROFILES = {
    "slow burn": {
        "motion_prefix": "With deliberate poise,",
        "motion_suffix": "drawing out each telling beat",
        "hook_suffix": "The moment lingers, heavy with intent.",
        "subject_accent": "poised in measured control",
        "keywords": ["elongated cadence", "measured breaths"],
    },
    "measured build": {
        "motion_prefix": "In a building rhythm,",
        "motion_suffix": "stacking momentum with purpose",
        "hook_suffix": "Anticipation climbs like a drumline swell.",
        "subject_accent": "centered and ready",
        "keywords": ["tight rhythm", "rising tempo"],
    },
    "surging": {
        "motion_prefix": "With a sudden surge,",
        "motion_suffix": "as the surrounding world blurs",
        "hook_suffix": "The scene ignites in a flash of motion.",
        "subject_accent": "caught mid-action",
        "keywords": ["accelerated blur", "kinetic rush"],
    },
    "frantic": {
        "motion_prefix": "In a frantic burst,",
        "motion_suffix": "leaving streaks of energy hanging in the air",
        "hook_suffix": "Heartbeat percussion rattles every frame.",
        "subject_accent": "fractured by adrenaline",
        "keywords": ["ragged tempo", "stuttered focus"],
    },
    "syncopated pulse": {
        "motion_prefix": "On a syncopated pulse,",
        "motion_suffix": "as tension snaps between staggered beats",
        "hook_suffix": "Rhythmic jolts keep the narrative out of step just enough to thrill.",
        "subject_accent": "moving on off-beat pivots",
        "keywords": ["stammered rhythm", "counter tempo"],
    },
    "glacial stillness": {
        "motion_prefix": "Within glacial stillness,",
        "motion_suffix": "each breath crystallizes before the next",
        "hook_suffix": "Time stretches thin enough to hear the quiet turn.",
        "subject_accent": "enveloped in frozen composure",
        "keywords": ["suspended hush", "slow tide"],
    },
}


NSFW_POSE_PROFILES = {
    "None": {
        "prompt": "",
        "notes": "No specific pose emphasis.",
    },
    "Suggestive Pinup": {
        "prompt": "suggestive pinup pose, playful hip tilt, confident eye contact",
        "notes": "Keep the focus on charisma and silhouette rather than explicit detail.",
    },
    "Reclined Elegance": {
        "prompt": "reclined pose on plush surface, soft arm drape, languid posture",
        "notes": "Use graceful lines and relaxed body language for a calm mood.",
    },
    "Backlit Silhouette": {
        "prompt": "backlit silhouette pose, curves defined through rim light, raised arms framing the body",
        "notes": "Let light shape the figure while facial expression carries the emotion.",
    },
    "Arching Stretch": {
        "prompt": "arching stretch pose, elongated spine, fingertips brushing hair",
        "notes": "Emphasize athletic grace and tension without revealing more than intended.",
    },
    "Window Lean": {
        "prompt": "window sill lean, soft shoulder drop, contemplative outward gaze",
        "notes": "Use architecture and reflections to frame a quiet, alluring moment.",
    },
    "S-Curve Stand": {
        "prompt": "standing s-curve pose, hip popped, graceful arm framing",
        "notes": "Classic glamour stance that accentuates silhouette without explicit focus.",
    },
    "Floorline Spotlight": {
        "prompt": "floorline pose, one leg extended, torso propped on forearms, spotlight emphasis",
        "notes": "Great for stage-style shoots with dramatic uplight.",
    },
    "Barstool Tease": {
        "prompt": "perched on barstool, crossed legs, arched shoulders, playful lean",
        "notes": "Combine confident posture with relaxed, social energy.",
    },
    "Over-Shoulder Glance": {
        "prompt": "over-shoulder glance, back arched, coy smile, hair tossed",
        "notes": "Highlights back definition and adds flirtatious storytelling.",
    },
    "XXX Stage Strut": {
        "prompt": "bold stage strut, hips leading, spotlight-followed, sultry focus",
        "notes": "High-energy adult stage choreography—keep movement confident and empowered.",
    },
    "XXX Lounge Arch": {
        "prompt": "provocative lounge arch, chest lifted, legs draped over chair edge",
        "notes": "Editorial-level eroticism; frame to celebrate form without explicit exposure.",
    },
    "Custom": {
        "prompt": "",
        "notes": "Use the custom pose prompt input to describe a bespoke stance.",
    },
    "XXX Custom": {
        "prompt": "",
        "notes": "Use the custom pose prompt input for high-heat adult staging while staying policy compliant.",
    },
}


NSFW_WARDROBE_STYLES = {
    "None": {
        "prompt": "",
        "notes": "No wardrobe styling adjustments.",
    },
    "Silk Lingerie": {
        "prompt": "luxurious silk lingerie set, delicate lace trim, coordinated stockings",
        "notes": "Highlight texture and craftsmanship for an elevated aesthetic.",
    },
    "Sheer Robe": {
        "prompt": "sheer chiffon robe tied at the waist, glimpses of toned figure",
        "notes": "Let fabric layers provide implied coverage with elegant motion.",
    },
    "Artistic Drapery": {
        "prompt": "artistic fabric drape, classical fine art styling, implied coverage",
        "notes": "Reference fine art photography to keep the composition tasteful.",
    },
    "Latex Couture": {
        "prompt": "sleek latex couture ensemble, high-shine finish, sculpted fit",
        "notes": "Balance bold materials with confident posture for empowered vibes.",
    },
    "Velvet Bodysuit": {
        "prompt": "plush velvet bodysuit, deep jewel tones, subtle sheen",
        "notes": "Use rich lighting to bring out the texture without overpowering skin tones.",
    },
    "Corseted Ensemble": {
        "prompt": "structured corseted set, ribbon lacing, sculpted hourglass silhouette",
        "notes": "Keep posture elongated to emphasize tailoring and refined glamour.",
    },
    "Crystal Bikini": {
        "prompt": "sparkling crystal bikini set, reflective rhinestone accents, gleaming straps",
        "notes": "Ideal for showgirl aesthetics—watch for specular blowouts in lighting.",
    },
    "Leather Harness": {
        "prompt": "sleek leather harness layering, adjustable straps, metallic buckles",
        "notes": "Edgy styling that pairs well with dramatic lighting and strong poses.",
    },
    "Body Chain Highlight": {
        "prompt": "delicate body chains draped across torso, shimmering highlights",
        "notes": "Use focused light to let jewelry catch attention over skin.",
    },
    "XXX Latex Catsuit": {
        "prompt": "second-skin latex catsuit, high-gloss finish, contour-tracing seams",
        "notes": "Channel fetish couture while keeping framing artistic and celebratory.",
    },
    "XXX Micro Lingerie": {
        "prompt": "ultra-minimal lingerie set, strappy cutouts, bold adult-mag styling",
        "notes": "Reserve for explicit glamour contexts; ensure confident expression and agency.",
    },
    "Custom": {
        "prompt": "",
        "notes": "Use the custom wardrobe prompt input to define bespoke styling.",
    },
    "XXX Custom": {
        "prompt": "",
        "notes": "Use the custom wardrobe prompt input for adult-oriented wardrobe design.",
    },
}


NSFW_TONE_MOODS = {
    "None": {
        "prompt": "",
        "notes": "No additional mood guidance.",
    },
    "Glamorous Editorial": {
        "prompt": "glamorous editorial energy, polished makeup, confident gaze",
        "notes": "Channel high-fashion storytelling with poised expression.",
    },
    "Sensual Noir": {
        "prompt": "noir inspired mood, smoky atmosphere, mysterious expression",
        "notes": "Lean into shadow play and narrative intrigue.",
    },
    "Soft Intimacy": {
        "prompt": "soft intimate atmosphere, gentle smile, inviting warmth",
        "notes": "Keep gestures small and welcoming for a romantic tone.",
    },
    "Artistic Nude": {
        "prompt": "fine art nude photography approach, focus on form and composition",
        "notes": "Treat the body as sculpture, emphasizing respect and artistry.",
    },
    "Sultry Twilight": {
        "prompt": "dusky twilight mood, amber window light, languid expression",
        "notes": "Balance warmth and shadow to create a quiet, smoldering vibe.",
    },
    "Playful Tease": {
        "prompt": "playful teasing energy, coy glance over shoulder, bright pops of color",
        "notes": "Keep body language energetic and lighthearted to avoid overt intensity.",
    },
    "Opulent Burlesque": {
        "prompt": "burlesque stage mood, velvet curtains, theatrical wink",
        "notes": "Dial up opulence and showmanship with articulate gestures.",
    },
    "Magenta Heat": {
        "prompt": "electric magenta nightclub glow, pulsing beat, charged allure",
        "notes": "Pair with neon or gel lighting for high-energy atmospherics.",
    },
    "Sensory Overdrive": {
        "prompt": "sensory overdrive mood, pounding bass, adrenaline sparkle",
        "notes": "Great for festival or rave-inspired adult sets.",
    },
    "XXX After Hours": {
        "prompt": "after-hours adult lounge vibe, smoky haze, unabashed swagger",
        "notes": "Acknowledge adult-only context while keeping tone empowered.",
    },
    "XXX Seductive Drama": {
        "prompt": "high-drama erotic tension, intense eye contact, charged pauses",
        "notes": "Amplify emotional stakes without shifting into explicit action.",
    },
    "Custom": {
        "prompt": "",
        "notes": "Use the custom tone prompt input to define bespoke mood cues.",
    },
    "XXX Custom": {
        "prompt": "",
        "notes": "Use the custom tone prompt input for adult-only mood or storytelling.",
    },
}


NSFW_LIGHTING_SETUPS = {
    "None": {
        "prompt": "",
        "notes": "No special lighting setup.",
    },
    "Candlelit Warmth": {
        "prompt": "candlelit glow, warm highlights, gentle falloff across skin",
        "notes": "Use clustered light sources to emphasize depth and comfort.",
    },
    "Neon Accent": {
        "prompt": "neon accent lighting, complementary color contrast, reflective sheen",
        "notes": "Pick two bold hues to accentuate mood without washing out tones.",
    },
    "Moody Spotlight": {
        "prompt": "single spotlight, sculpted shadows, dramatic contrast",
        "notes": "Frame the subject with shadow for a theatrical focal point.",
    },
    "Window Backlight": {
        "prompt": "soft window backlight, translucent curtains, haloed edges",
        "notes": "Let natural spill wrap the figure while keeping front fill minimal.",
    },
    "Colored Gel Duo": {
        "prompt": "split lighting with complementary gels, gradient washes across skin",
        "notes": "Blend opposing hues to carve shape while preserving complexion.",
    },
    "Striplight Sculpt": {
        "prompt": "studio striplights skimming curves, controlled edge highlights",
        "notes": "Ideal for glamour sets that crave clean separation from backdrop.",
    },
    "Mirror Bounce": {
        "prompt": "mirror bounce lighting, reflective panels amplifying shimmer",
        "notes": "Leverage reflective surfaces for layered specular detail.",
    },
    "Holographic Wash": {
        "prompt": "holographic prism wash, iridescent color shifts, futuristic sheen",
        "notes": "Pairs with metallic wardrobe and modern editorial staging.",
    },
    "XXX Club Strobe": {
        "prompt": "club strobe pulses, alternating gel colors, rapid highlights",
        "notes": "Simulate adult club energy—capture motion trails responsibly.",
    },
    "XXX Champagne Glow": {
        "prompt": "champagne bottle glints, gold bounce fill, indulgent sparkle",
        "notes": "Adds decadent adult-party flair with luxurious reflections.",
    },
    "Custom": {
        "prompt": "",
        "notes": "Use the custom lighting prompt input to detail bespoke setups.",
    },
    "XXX Custom": {
        "prompt": "",
        "notes": "Use the custom lighting prompt input for explicit nightlife scenarios.",
    },
}


NSFW_CAMERA_FRAMING = {
    "None": {
        "prompt": "",
        "notes": "No specific framing guidance.",
    },
    "Intimate Portrait": {
        "prompt": "intimate portrait framing, medium close-up, shallow depth of field",
        "notes": "Highlight eyes and expression to carry the story.",
    },
    "Full-Length Showcase": {
        "prompt": "full-length framing, elongated lines, elegant posture",
        "notes": "Ensure the pose reads clearly from head to toe.",
    },
    "Low Angle Admiration": {
        "prompt": "low angle lens, empowering perspective, upward gaze",
        "notes": "Use perspective to emphasize confidence and strength.",
    },
    "Overhead Curve Highlight": {
        "prompt": "overhead shot, graceful curvature emphasized, symmetrical layout",
        "notes": "Mind the set dressing so shapes remain readable from above.",
    },
    "Mirror Reflection": {
        "prompt": "mirror reflection framing, doubled imagery, blurred foreground glass",
        "notes": "Use the mirror to hint at form while keeping direct exposure restrained.",
    },
    "Profile Silhouette": {
        "prompt": "profile silhouette framing, edge lighting tracing contours, negative space",
        "notes": "Let rim light outline the figure, preserving mystery and mood.",
    },
    "Dutch Glamour": {
        "prompt": "dutch angle glamour framing, diagonal energy, kinetic composition",
        "notes": "Adds motion and drama while centering the subject's presence.",
    },
    "Split Focus Mirror": {
        "prompt": "split focus with mirrored panels, layered depth cues",
        "notes": "Great for editorial concepts mixing reflection and direct gaze.",
    },
    "XXX Runway POV": {
        "prompt": "runway pov framing, direct eye-line, confident strut captured mid-step",
        "notes": "Channels adult runway shows—keep perspective empowering.",
    },
    "XXX Close Intimacy": {
        "prompt": "hyper-close framing on lips and neckline, shimmering highlights",
        "notes": "Use shallow focus to maintain artistry in explicit glamour shots.",
    },
    "Custom": {
        "prompt": "",
        "notes": "Use the custom camera prompt input to define bespoke framing.",
    },
    "XXX Custom": {
        "prompt": "",
        "notes": "Use the custom camera prompt input for adult-centric framing approaches.",
    },
}


NSFW_EXPLICITNESS_LEVELS = {
    "None": {
        "prompt": "",
        "negative": "",
    },
    "Soft Suggestive": {
        "prompt": "tasteful suggestive tone, emphasis on attitude over exposure",
        "negative": "graphic nudity, explicit anatomy, pornographic framing",
    },
    "Implied Nude": {
        "prompt": "implied nudity, strategic coverage, focus on silhouette and light",
        "negative": "fully exposed genitals, spread legs, explicit close-ups",
    },
    "Artistic Nude": {
        "prompt": "fine art nude composition, respect for subject, sculptural lighting",
        "negative": "pornographic framing, fetish extremes, explicit anatomical detail",
    },
    "Bold Glamour": {
        "prompt": "bold glamour styling, confident pose, editorial polish",
        "negative": "hardcore explicit acts, fetish content, degrading scenarios",
    },
    "XXX Glamour": {
        "prompt": "xxx glamour focus, unapologetic skin-forward posing, adult magazine energy",
        "negative": "explicit sexual acts, penetration, fetish violence, non-consensual themes",
    },
    "XXX Showcase": {
        "prompt": "erotic showcase, full nude confidence, provocative glimmer lighting",
        "negative": "pornographic close-ups, bodily fluids, explicit intercourse depiction",
    },
    "XXX Performance": {
        "prompt": "adult-stage performance vibe, theatrical erotica, high-voltage seduction",
        "negative": "graphic sexual acts, fetish degradation, non-consensual scenarios",
    },
    "Custom": {
        "prompt": "",
        "negative": "",
    },
    "XXX Custom": {
        "prompt": "",
        "negative": "",
    },
}


NSFW_BASELINE_NEGATIVES = [
    "child",
    "teen",
    "minor",
    "underage",
    "youth",
    "loli",
    "shota",
    "young-looking",
    "non-consensual",
    "abuse",
    "violence",
    "blood",
    "gore",
    "injury",
    "body horror",
    "incest",
    "bestiality",
    "rape",
    "drugged",
    "sleeping partner",
    "unconscious",
]


NSFW_DEFAULT_SAFETY_NOTE = (
    "For mature audiences only. Confirm all depicted subjects are consenting adults and comply with platform policies."
)

class NoxPromptEnhancer:
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
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("enhanced_prompt", "negative_prompt")
    FUNCTION = "enhance_prompt"
    CATEGORY = "NoxPrompter/Text"
    
    def enhance_prompt(self, base_prompt, enhancement_mode, emphasis_strength, add_quality_tags, 
                      secondary_prompt="", negative_prompt="", custom_style=""):
        """
        Enhance the input prompt based on the selected parameters.
        """
        
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
        
        return (enhanced_prompt, processed_negative)
    
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


class NoxPromptBuilder:
    """Construct prompts using formulas and curated keyword palettes."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "formula": (list(FORMULA_CONFIGS.keys()), {"default": "Advanced Formula"}),
                "subject_focus": ("STRING", {"multiline": True, "default": "Battle-hardened warrior drenched in rain, wearing leather armor and fur"}),
                "scene_setting": ("STRING", {"multiline": True, "default": "Muddy battlefield at night, lightning in the distance, flames flickering"}),
                "motion_arc": ("STRING", {"multiline": True, "default": "Charges forward roaring, swings blade in a slow-motion crash zoom"}),
            },
            "optional": {
                "narrative_hook": ("STRING", {"multiline": True, "default": "Camera locks onto her determined eyes as thunder cracks overhead"}),
                "model_emphasis": ("STRING", {"multiline": True, "default": "Cinematic aesthetic control, precise semantic adherence"}),
                "light_source": (list(LIGHT_SOURCE_OPTIONS.keys()), {"default": "Daylight"}),
                "light_quality": (list(LIGHT_QUALITY_OPTIONS.keys()), {"default": "Soft Light"}),
                "time_of_day": (list(TIME_OF_DAY_OPTIONS.keys()), {"default": "Dusk"}),
                "shot_size": (list(SHOT_SIZE_OPTIONS.keys()), {"default": "Medium Close-up"}),
                "composition": (list(COMPOSITION_OPTIONS.keys()), {"default": "Balanced"}),
                "lens_focal": (list(LENS_FOCAL_OPTIONS.keys()), {"default": "Medium"}),
                "lens_angle": (list(LENS_ANGLE_OPTIONS.keys()), {"default": "None"}),
                "lens_type": (list(LENS_TYPE_OPTIONS.keys()), {"default": "Single Shot"}),
                "color_tone": (list(COLOR_TONE_OPTIONS.keys()), {"default": "Warm Tone"}),
                "motion_type": (list(MOTION_TYPE_OPTIONS.keys()), {"default": "Running"}),
                "emotion": (list(EMOTION_OPTIONS.keys()), {"default": "Joy"}),
                "camera_basic": (list(CAMERA_BASIC_OPTIONS.keys()), {"default": "Push-in"}),
                "camera_advanced": (list(CAMERA_ADVANCED_OPTIONS.keys()), {"default": "Handheld"}),
                "visual_style": (list(VISUAL_STYLE_OPTIONS.keys()), {"default": "Anime"}),
                "special_effect": (list(SPECIAL_EFFECT_OPTIONS.keys()), {"default": "None"}),
                "keyword_style": (["auto", "inline", "compact"], {"default": "auto"}),
                "randomize_missing": ("BOOLEAN", {"default": False}),
                "random_seed": ("INT", {"default": 0, "min": 0, "max": 1_000_000, "step": 1}),
                "palette_overrides": ("STRING", {"multiline": True, "default": ""}),
                "extra_descriptors": ("STRING", {"multiline": True, "default": "Model feature emphasis: complex & dynamic motion"}),
                "custom_keywords": ("STRING", {"multiline": True, "default": ""}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                "prompt_prefix": ("STRING", {"default": ""}),
                "prompt_suffix": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt", "negative_prompt", "aesthetic_notes", "dynamic_notes")
    FUNCTION = "build_prompt"
    CATEGORY = "NoxPrompter/Builders"

    def build_prompt(
        self,
        formula,
        subject_focus,
        scene_setting,
        motion_arc,
        narrative_hook="",
        model_emphasis="",
        light_source="Daylight",
        light_quality="Soft Light",
        time_of_day="Dusk",
        shot_size="Medium Close-up",
        composition="Balanced",
        lens_focal="Medium",
        lens_angle="None",
        lens_type="Single Shot",
        color_tone="Warm Tone",
        motion_type="Running",
        emotion="Joy",
        camera_basic="Push-in",
        camera_advanced="Handheld",
        visual_style="Anime",
        special_effect="None",
        keyword_style="auto",
        randomize_missing=False,
        random_seed=0,
        palette_overrides="",
        extra_descriptors="",
        custom_keywords="",
        negative_prompt="",
        prompt_prefix="",
        prompt_suffix="",
    ):
        formula_config = FORMULA_CONFIGS.get(formula, next(iter(FORMULA_CONFIGS.values())))
        overrides_map, override_custom = self._parse_palette_overrides(palette_overrides)
        rng = random.Random(random_seed) if randomize_missing else None

        prompt_fragments = []

        if prompt_prefix.strip():
            prompt_fragments.append(prompt_prefix.strip())

        subject_clause = subject_focus.strip()
        if model_emphasis.strip():
            emphasis = model_emphasis.strip()
            subject_clause = f"{subject_clause}, {emphasis}" if subject_clause else emphasis
        if subject_clause:
            prompt_fragments.append(subject_clause)

        if scene_setting.strip():
            prompt_fragments.append(scene_setting.strip())

        if motion_arc.strip():
            prompt_fragments.append(motion_arc.strip())

        if narrative_hook.strip():
            prompt_fragments.append(narrative_hook.strip())

        if extra_descriptors.strip():
            prompt_fragments.append(extra_descriptors.strip())

        aesthetic_prompts, aesthetic_summaries = self._collect_category_details(
            [
                ("light_source", light_source, LIGHT_SOURCE_OPTIONS),
                ("light_quality", light_quality, LIGHT_QUALITY_OPTIONS),
                ("time_of_day", time_of_day, TIME_OF_DAY_OPTIONS),
                ("shot_size", shot_size, SHOT_SIZE_OPTIONS),
                ("composition", composition, COMPOSITION_OPTIONS),
                ("lens_focal", lens_focal, LENS_FOCAL_OPTIONS),
                ("lens_angle", lens_angle, LENS_ANGLE_OPTIONS),
                ("lens_type", lens_type, LENS_TYPE_OPTIONS),
                ("color_tone", color_tone, COLOR_TONE_OPTIONS),
            ],
            overrides_map,
            rng=rng,
            randomize_missing=randomize_missing,
        )

        dynamic_prompts, dynamic_summaries = self._collect_category_details(
            [
                ("motion_type", motion_type, MOTION_TYPE_OPTIONS),
                ("emotion", emotion, EMOTION_OPTIONS),
                ("camera_basic", camera_basic, CAMERA_BASIC_OPTIONS),
                ("camera_advanced", camera_advanced, CAMERA_ADVANCED_OPTIONS),
            ],
            overrides_map,
            rng=rng,
            randomize_missing=randomize_missing,
        )

        style_prompts, style_summaries = self._collect_category_details(
            [
                ("visual_style", visual_style, VISUAL_STYLE_OPTIONS),
                ("special_effect", special_effect, SPECIAL_EFFECT_OPTIONS),
            ],
            overrides_map,
            rng=rng,
            randomize_missing=randomize_missing,
        )

        keyword_mode = (keyword_style or "auto").lower()
        structure = formula_config.get("structure", [])

        if keyword_mode == "compact":
            combined_keywords = aesthetic_prompts + dynamic_prompts + style_prompts
            if combined_keywords:
                prompt_fragments.append(f"Keywords: {', '.join(combined_keywords)}")
        elif keyword_mode == "inline":
            for chunk in aesthetic_prompts + dynamic_prompts + style_prompts:
                prompt_fragments.append(chunk)
        else:
            if "aesthetic" in structure and aesthetic_prompts:
                prompt_fragments.append(f"Cinematic palette: {', '.join(aesthetic_prompts)}")
            elif aesthetic_prompts:
                prompt_fragments.extend(aesthetic_prompts)

            if dynamic_prompts:
                prompt_fragments.append(f"Motion & camera: {', '.join(dynamic_prompts)}")

            if "stylization" in structure and style_prompts:
                prompt_fragments.append(f"Stylization: {', '.join(style_prompts)}")
            elif style_prompts:
                prompt_fragments.extend(style_prompts)

        combined_custom = self._split_keywords(custom_keywords)
        if override_custom:
            combined_custom.extend(override_custom)
        if combined_custom:
            combined_custom = list(dict.fromkeys(filter(None, (item.strip() for item in combined_custom))))
            if combined_custom:
                prompt_fragments.append(", ".join(combined_custom))

        if prompt_suffix.strip():
            prompt_fragments.append(prompt_suffix.strip())

        prompt_text = self._assemble_prompt(prompt_fragments)
        neg_text = negative_prompt.strip()

        aesthetic_notes = " | ".join(filter(None, aesthetic_summaries + style_summaries))
        dynamic_notes = " | ".join(filter(None, dynamic_summaries))

        return (prompt_text, neg_text, aesthetic_notes, dynamic_notes)

    def _collect_category_details(self, selections, overrides, rng=None, randomize_missing=False):
        prompts = []
        summaries = []
        overrides = overrides or {}
        for key, label, options in selections:
            tokens = self._expand_selection(label)
            override_tokens = overrides.get(key, [])
            if override_tokens:
                tokens.extend(override_tokens)
            if not tokens:
                tokens.append(label)

            for token in tokens:
                option = self._resolve_option(token, options, rng=rng, randomize_missing=randomize_missing)
                prompt_text = option.get("prompt", "").strip()
                summary_text = option.get("summary", "").strip()
                if prompt_text:
                    prompts.append(prompt_text)
                if summary_text:
                    summaries.append(summary_text)

        prompts = list(dict.fromkeys(filter(None, prompts)))
        summaries = list(dict.fromkeys(filter(None, summaries)))
        return prompts, summaries

    def _resolve_option(self, label, options, rng=None, randomize_missing=False):
        normalized = (label or "").strip()
        if normalized:
            if normalized.lower() == "none":
                normalized = ""
            else:
                lower_map = {name.lower(): name for name in options.keys()}
                lookup = lower_map.get(normalized.lower())
                if lookup:
                    return options.get(lookup, options.get("None", {"prompt": "", "summary": ""}))
        if randomize_missing and rng:
            candidates = [name for name in options if name.lower() != "none" and options[name].get("prompt")]
            if candidates:
                choice = rng.choice(candidates)
                return options[choice]
        return options.get("None", {"prompt": "", "summary": ""})

    def _expand_selection(self, value):
        if not value:
            return []
        tokens = [token.strip() for token in re.split(r'[|/,]', value) if token.strip()]
        return tokens

    def _parse_palette_overrides(self, text):
        if not text or not text.strip():
            return {}, []

        overrides = {}
        custom_chunks = []
        mapping = self._palette_alias_map()

        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            if ":" in line:
                key_part, values_part = line.split(":", 1)
                canonical = mapping.get(self._normalize_token(key_part))
                values = self._split_keywords(values_part)
                if canonical and values:
                    overrides.setdefault(canonical, []).extend(values)
                elif values:
                    custom_chunks.extend(values)
            else:
                custom_chunks.extend(self._split_keywords(line))

        for key in list(overrides.keys()):
            overrides[key] = list(dict.fromkeys(overrides[key]))

        custom_chunks = list(dict.fromkeys(custom_chunks))
        return overrides, custom_chunks

    def _palette_alias_map(self):
        return {
            "light source": "light_source",
            "light sources": "light_source",
            "lighting": "light_source",
            "light quality": "light_quality",
            "light qualities": "light_quality",
            "time of day": "time_of_day",
            "time": "time_of_day",
            "shot size": "shot_size",
            "composition": "composition",
            "lens focal": "lens_focal",
            "focal length": "lens_focal",
            "lens angle": "lens_angle",
            "camera angle": "lens_angle",
            "lens type": "lens_type",
            "shot type": "lens_type",
            "color tone": "color_tone",
            "color": "color_tone",
            "motion type": "motion_type",
            "motion": "motion_type",
            "emotion": "emotion",
            "camera basic": "camera_basic",
            "camera move": "camera_basic",
            "basic move": "camera_basic",
            "camera advanced": "camera_advanced",
            "advanced move": "camera_advanced",
            "visual style": "visual_style",
            "style": "visual_style",
            "special effect": "special_effect",
            "effects": "special_effect",
        }

    def _normalize_token(self, token):
        return token.strip().lower().replace("_", " ")

    def _split_keywords(self, text):
        if not text:
            return []
        separators = [",", "\n", ";"]
        tokens = [text]
        for sep in separators:
            temp = []
            for token in tokens:
                temp.extend(token.split(sep))
            tokens = temp
        return [token.strip() for token in tokens if token.strip()]

    def _assemble_prompt(self, fragments):
        cleaned = []
        for fragment in fragments:
            segment = fragment.strip()
            if not segment:
                continue
            if segment[-1] not in ".!?":
                segment = f"{segment}."
            cleaned.append(segment)
        return " ".join(cleaned)


class NoxPromptPaletteMixer:
    """Generate palette overrides and keyword clusters for the builder."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mood_profile": (list(PALETTE_PROFILES.keys()), {"default": "Moody Nightfall"}),
                "intensity": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.05}),
            },
            "optional": {
                "include_effects": ("BOOLEAN", {"default": True}),
                "custom_palette": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("palette_overrides", "custom_keywords", "notes")
    FUNCTION = "mix_palette"
    CATEGORY = "NoxPrompter/Companions"

    def mix_palette(self, mood_profile, intensity, include_effects=True, custom_palette=""):
        profile = PALETTE_PROFILES.get(mood_profile)
        if not profile:
            overrides_text = custom_palette.strip()
            custom_keywords = ", ".join(self._split_keywords(custom_palette))
            notes = "Custom palette applied. Profile not found."
            return (overrides_text, custom_keywords, notes)

        overrides = {key: list(values) for key, values in profile.get("overrides", {}).items()}

        if intensity >= 0.6:
            for key, values in profile.get("intense_overrides", {}).items():
                overrides.setdefault(key, []).extend(values)

        if include_effects and profile.get("effects"):
            overrides.setdefault("special_effect", []).extend(profile["effects"])

        override_lines = []
        for key, values in overrides.items():
            deduped = list(dict.fromkeys(value for value in values if value))
            if deduped:
                override_lines.append(f"{key}: {', '.join(deduped)}")

        if custom_palette.strip():
            override_lines.append(custom_palette.strip())

        overrides_text = "\n".join(override_lines).strip()

        keywords = list(profile.get("keywords", []))
        if intensity >= 0.6:
            keywords.extend(profile.get("intense_keywords", []))
        if include_effects:
            keywords.extend(profile.get("effect_keywords", []))
        if custom_palette.strip():
            keywords.extend(self._split_keywords(custom_palette))

        keywords = list(dict.fromkeys(kw.strip() for kw in keywords if kw and kw.strip()))
        custom_keywords = ", ".join(keywords)

        notes_parts = [profile.get("description", mood_profile)]
        notes_parts.append(f"Intensity: {intensity:.2f}")
        if include_effects and profile.get("effects"):
            notes_parts.append("Special effects included: " + ", ".join(profile["effects"]))
        if keywords:
            notes_parts.append("Keywords curated for emphasis.")

        return (overrides_text, custom_keywords, " | ".join(notes_parts))

    def _split_keywords(self, text):
        if not text:
            return []
        separators = [",", "\n", ";"]
        tokens = [text]
        for sep in separators:
            temp = []
            for token in tokens:
                temp.extend(token.split(sep))
            tokens = temp
        return [token.strip() for token in tokens if token.strip()]


class NoxPromptNarrativeWeaver:
    """Craft narrative scaffolding for the prompt builder."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "hero_archetype": (list(NARRATIVE_ARCHETYPES.keys()), {"default": "Resolute Protector"}),
                "story_tone": (list(NARRATIVE_TONES.keys()), {"default": "Hopeful Resurgence"}),
                "environment": (list(NARRATIVE_ENVIRONMENTS.keys()), {"default": "Rain-Soaked Citadel"}),
            },
            "optional": {
                "set_piece": (list(NARRATIVE_SETPIECES.keys()), {"default": "Climactic Duel"}),
                "tempo": (list(TEMPO_PROFILES.keys()), {"default": "surging"}),
                "focus_detail": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = (
        "subject_focus",
        "scene_setting",
        "motion_arc",
        "narrative_hook",
        "extra_descriptors",
    )
    FUNCTION = "weave"
    CATEGORY = "NoxPrompter/Companions"

    def weave(
        self,
        hero_archetype,
        story_tone,
        environment,
        set_piece="Climactic Duel",
        tempo="surging",
        focus_detail="",
    ):
        archetype = NARRATIVE_ARCHETYPES.get(hero_archetype, {"subject": hero_archetype, "keywords": []})
        tone = NARRATIVE_TONES.get(story_tone, {"descriptor": story_tone, "ambience": "", "hook": "", "keywords": []})
        env = NARRATIVE_ENVIRONMENTS.get(environment, {"description": environment, "details": "", "keywords": []})
        setpiece = NARRATIVE_SETPIECES.get(set_piece, {"motion": set_piece, "hook": "", "keywords": []})
        tempo_cfg = TEMPO_PROFILES.get(tempo, TEMPO_PROFILES["measured build"])

        subject_parts = [archetype.get("subject", "")]
        if tempo_cfg.get("subject_accent"):
            subject_parts.append(tempo_cfg["subject_accent"])
        if tone.get("descriptor"):
            subject_parts.append(tone["descriptor"])
        subject_focus = ", ".join(part for part in subject_parts if part).strip(", ")

        scene_parts = [env.get("description", ""), env.get("details", ""), tone.get("ambience", "")]
        scene_setting = ", ".join(part for part in scene_parts if part).strip(", ")

        motion_parts = [tempo_cfg.get("motion_prefix"), setpiece.get("motion"), tempo_cfg.get("motion_suffix")]
        motion_arc = " ".join(part.strip() for part in motion_parts if part and part.strip())

        hook_parts = [tone.get("hook"), setpiece.get("hook"), tempo_cfg.get("hook_suffix")]
        narrative_hook = " ".join(part.strip() for part in hook_parts if part and part.strip())

        descriptor_sources = [
            archetype.get("keywords", []),
            tone.get("keywords", []),
            env.get("keywords", []),
            setpiece.get("keywords", []),
            tempo_cfg.get("keywords", []),
        ]
        if focus_detail.strip():
            descriptor_sources.append(self._split_keywords(focus_detail))

        descriptors = []
        for source in descriptor_sources:
            descriptors.extend(source)
        descriptors = list(dict.fromkeys(desc.strip() for desc in descriptors if desc and desc.strip()))
        extra_descriptors = ", ".join(descriptors)

        return (
            subject_focus,
            scene_setting,
            motion_arc,
            narrative_hook,
            extra_descriptors,
        )

    def _split_keywords(self, text):
        if not text:
            return []
        separators = [",", "\n", ";"]
        tokens = [text]
        for sep in separators:
            temp = []
            for token in tokens:
                temp.extend(token.split(sep))
            tokens = temp
        return [token.strip() for token in tokens if token.strip()]


class NoxPromptNSFWDesigner:
    """Assemble mature-oriented prompts with responsible defaults and safeguards."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject_focus": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "Confident adult model with poised expression",
                    },
                ),
                "scene_setting": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "Softly lit studio lounge accented with plush textures",
                    },
                ),
                "pose_profile": (list(NSFW_POSE_PROFILES.keys()), {"default": "Suggestive Pinup"}),
                "wardrobe_style": (
                    list(NSFW_WARDROBE_STYLES.keys()),
                    {"default": "Silk Lingerie"},
                ),
                "tone_profile": (list(NSFW_TONE_MOODS.keys()), {"default": "Glamorous Editorial"}),
            },
            "optional": {
                "lighting_setup": (
                    list(NSFW_LIGHTING_SETUPS.keys()),
                    {"default": "Candlelit Warmth"},
                ),
                "camera_framing": (
                    list(NSFW_CAMERA_FRAMING.keys()),
                    {"default": "Intimate Portrait"},
                ),
                "explicitness_level": (
                    list(NSFW_EXPLICITNESS_LEVELS.keys()),
                    {"default": "Implied Nude"},
                ),
                "custom_pose_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_pose_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_wardrobe_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_wardrobe_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_tone_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_tone_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_lighting_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_lighting_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_camera_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_camera_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_explicitness_prompt": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_explicitness_negative": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "custom_explicitness_notes": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
                "detail_accent": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "soft blemish-free skin, natural curves, respectful staging",
                    },
                ),
                "nsfw_tags": ("STRING", {"multiline": True, "default": "tasteful, mature, confident"}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                "include_negative_baseline": ("BOOLEAN", {"default": True}),
                "include_safety_note": ("BOOLEAN", {"default": True}),
                "custom_safety_note": (
                    "STRING",
                    {"multiline": True, "default": ""},
                ),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt", "negative_prompt", "safety_notes")
    FUNCTION = "design_prompt"
    CATEGORY = "NoxPrompter/NSFW"

    def design_prompt(
        self,
        subject_focus,
        scene_setting,
        pose_profile,
        wardrobe_style,
        tone_profile,
        lighting_setup="Candlelit Warmth",
        camera_framing="Intimate Portrait",
        explicitness_level="Implied Nude",
        detail_accent="",
        nsfw_tags="",
        negative_prompt="",
        include_negative_baseline=True,
        include_safety_note=True,
        custom_pose_prompt="",
        custom_pose_notes="",
        custom_wardrobe_prompt="",
        custom_wardrobe_notes="",
        custom_tone_prompt="",
        custom_tone_notes="",
        custom_lighting_prompt="",
        custom_lighting_notes="",
        custom_camera_prompt="",
        custom_camera_notes="",
        custom_explicitness_prompt="",
        custom_explicitness_negative="",
        custom_explicitness_notes="",
        custom_safety_note="",
    ):
        pose_cfg = self._resolve_nsfw_option(
            pose_profile,
            NSFW_POSE_PROFILES,
            custom_prompt=custom_pose_prompt,
            custom_notes=custom_pose_notes,
        )
        wardrobe_cfg = self._resolve_nsfw_option(
            wardrobe_style,
            NSFW_WARDROBE_STYLES,
            custom_prompt=custom_wardrobe_prompt,
            custom_notes=custom_wardrobe_notes,
        )
        tone_cfg = self._resolve_nsfw_option(
            tone_profile,
            NSFW_TONE_MOODS,
            custom_prompt=custom_tone_prompt,
            custom_notes=custom_tone_notes,
        )
        lighting_cfg = self._resolve_nsfw_option(
            lighting_setup,
            NSFW_LIGHTING_SETUPS,
            custom_prompt=custom_lighting_prompt,
            custom_notes=custom_lighting_notes,
        )
        camera_cfg = self._resolve_nsfw_option(
            camera_framing,
            NSFW_CAMERA_FRAMING,
            custom_prompt=custom_camera_prompt,
            custom_notes=custom_camera_notes,
        )
        explicit_cfg = self._resolve_nsfw_option(
            explicitness_level,
            NSFW_EXPLICITNESS_LEVELS,
            custom_prompt=custom_explicitness_prompt,
            custom_notes=custom_explicitness_notes,
            custom_negative=custom_explicitness_negative,
        )

        fragments = []

        subject_clause_parts = [subject_focus.strip()]
        if tone_cfg.get("prompt"):
            subject_clause_parts.append(tone_cfg["prompt"])
        if explicit_cfg.get("prompt"):
            subject_clause_parts.append(explicit_cfg["prompt"])
        subject_clause = ", ".join(part for part in subject_clause_parts if part)
        if subject_clause:
            fragments.append(subject_clause)

        if scene_setting.strip():
            fragments.append(scene_setting.strip())

        descriptive_chunks = [
            pose_cfg.get("prompt", ""),
            wardrobe_cfg.get("prompt", ""),
            lighting_cfg.get("prompt", ""),
            camera_cfg.get("prompt", ""),
        ]
        if detail_accent.strip():
            descriptive_chunks.append(detail_accent.strip())
        descriptive_line = ", ".join(chunk for chunk in descriptive_chunks if chunk)
        if descriptive_line:
            fragments.append(descriptive_line)

        tag_list = self._split_keywords(nsfw_tags)
        if tag_list:
            fragments.append(f"Keywords: {', '.join(tag_list)}")

        prompt_text = self._assemble_sentences(fragments)

        negative_terms = []
        if include_negative_baseline:
            negative_terms.extend(NSFW_BASELINE_NEGATIVES)
        explicit_negative = self._split_keywords(explicit_cfg.get("negative", ""))
        negative_terms.extend(explicit_negative)
        negative_terms.extend(self._split_keywords(negative_prompt))
        negative_terms = list(dict.fromkeys(term.strip() for term in negative_terms if term.strip()))
        negative_text = ", ".join(negative_terms)

        safety_parts = []
        if include_safety_note:
            safety_parts.append(NSFW_DEFAULT_SAFETY_NOTE)
        notes_sources = [
            pose_cfg.get("notes"),
            wardrobe_cfg.get("notes"),
            tone_cfg.get("notes"),
            lighting_cfg.get("notes"),
            camera_cfg.get("notes"),
            explicit_cfg.get("notes"),
        ]
        curated_notes = [note for note in notes_sources if note]
        if curated_notes:
            safety_parts.extend(list(dict.fromkeys(curated_notes)))
        if custom_safety_note.strip():
            safety_parts.append(custom_safety_note.strip())
        safety_notes = " | ".join(part for part in safety_parts if part)

        return (prompt_text, negative_text, safety_notes)

    def _assemble_sentences(self, fragments):
        sentences = []
        for fragment in fragments:
            segment = fragment.strip()
            if not segment:
                continue
            if segment[-1] not in ".!?":
                segment = f"{segment}."
            sentences.append(segment)
        return " ".join(sentences)

    def _split_keywords(self, text):
        if not text:
            return []
        separators = [",", "\n", ";"]
        tokens = [text]
        for sep in separators:
            expanded = []
            for token in tokens:
                expanded.extend(token.split(sep))
            tokens = expanded
        return [token.strip() for token in tokens if token.strip()]

    def _resolve_nsfw_option(
        self,
        selection,
        options,
        *,
        custom_prompt="",
        custom_notes="",
        custom_negative=None,
    ):
        key = self._match_option_key(selection, options)
        fallback_key = "None" if "None" in options else next(iter(options))
        source_key = key or fallback_key
        base = dict(options.get(source_key, {}))

        prompt_parts = [part.strip() for part in [base.get("prompt", ""), custom_prompt] if part and part.strip()]
        base["prompt"] = ", ".join(dict.fromkeys(prompt_parts)) if prompt_parts else ""

        notes_parts = [part.strip() for part in [base.get("notes", ""), custom_notes] if part and part.strip()]
        if notes_parts:
            base["notes"] = " | ".join(dict.fromkeys(notes_parts))
        elif "notes" in base:
            base["notes"] = base.get("notes", "")

        if custom_negative is not None:
            negative_parts = [part.strip() for part in [base.get("negative", ""), custom_negative] if part and part.strip()]
            base["negative"] = ", ".join(dict.fromkeys(negative_parts)) if negative_parts else ""

        return base

    def _match_option_key(self, selection, options):
        normalized = (selection or "").strip()
        if not normalized:
            return None
        lookup = normalized.lower()
        for key in options.keys():
            if key.lower() == lookup:
                return key
        return None


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