"""Shared constant dictionaries for Nox Prompter nodes."""

from __future__ import annotations

import os

PRESET_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "presets")

CUSTOM_OPTION = "Custom Input"


FORMULA_CONFIGS = {
    "Basic Formula": {
        "description": "Subject + Scene + Motion — perfect for ideation and quick inspiration.",
        "structure": ["subject", "scene", "motion"],
    },
    "Advanced Formula": {
        "description": "Subject (desc) + Scene (desc) + Motion (desc) + Aesthetic controls + Stylization.",
        "structure": ["subject", "scene", "motion", "aesthetic", "stylization"],
    },
    "Story Spotlight": {
        "description": "Focus subject + environmental beat + camera language + emotional tone summary.",
        "structure": ["subject", "scene", "motion", "emotion", "camera"],
    },
    "Trailer Teaser": {
        "description": "Cold open hook + subject descriptor + kinetic beat + stylization tag cloud.",
        "structure": ["scene", "subject", "motion", "stylization"],
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
    "Holographic Panels": {"prompt": "holographic panel lighting, refracted neon, cascading spectrum wash", "summary": "Glitchy holographic panels bathing the scene in shimmering gradients."},
    "Torchline": {"prompt": "torch-lit procession, wavering flame line, ember flicker", "summary": "Row of torches casting rhythmic pulses of warm light."},
    "Neon Billboard": {"prompt": "neon billboard glow, saturated signage wash, flickering letters", "summary": "Vibrant billboard light bathing the scene in rhythmic neon pulses."},
    "Campfire Circle": {"prompt": "campfire circle, ember sparks, storytelling glow", "summary": "Intimate fire pit lighting painting faces with warm flicker."},
    "Stage Spotlight": {"prompt": "stage spotlight beam, hard edge falloff, performer isolation", "summary": "Focused theatrical spotlight carving subject from darkness."},
    "Lightning Storm": {"prompt": "lightning storm bursts, strobing sky flashes, electric contrast", "summary": "Unpredictable lightning bolts freezing action in high contrast."},
    "Volcanic Flow": {"prompt": "volcanic magma glow, molten spill, infernal ambience", "summary": "Seething lava light casting ominous crimson across surfaces."},
    "Candlelit Vigil": {"prompt": "clustered candlelight, fluttering wicks, hushed warmth", "summary": "Sea of candles producing soft, reverent illumination."},
    "Aurora Curtain": {"prompt": "aurora curtain glow, shifting greens and violets, sky drape", "summary": "Northern lights bathing subjects in dreamy celestial hues."},
    "Starlight": {"prompt": "pure starlight, silver speckle, expansive night shimmer", "summary": "Subtle starlit exposure lending gentle highlights to silhouettes."},
    "Underwater Caustics": {"prompt": "underwater caustic light, dancing wave reflections, aquatic shimmer", "summary": "Liquid light patterns rippling across submerged subjects."},
    "Snow Reflection": {"prompt": "snowfield bounce light, diffuse white glow, winter reflection", "summary": "Snow bounce filling shadows with cool diffuse brightness."},
    "Forge Hearth": {"prompt": "forge hearth blaze, iron sparks, molten core", "summary": "Blacksmith forge light casting muscular orange highlights."},
    "Alchemical Vat": {"prompt": "alchemical vat glow, bubbling neon liquids, laboratory luminescence", "summary": "Arcane vats emitting surreal colored glows through mist."},
    "Cyber Street Lamps": {"prompt": "cyberpunk street lamps, holographic ads, saturated sidewalk beams", "summary": "Urban street lamps layering colored pools across rain-slick pavement."},
    "Gaslight Row": {"prompt": "gaslight row glow, amber halos, Victorian haze", "summary": "Historical gas lamps lining the street with soft amber halos."},
    "Lantern Parade": {"prompt": "festival lantern parade, drifting paper lights, communal glow", "summary": "Floating lanterns surrounding characters in celebratory radiance."},
    "Bioreactor": {"prompt": "bioreactor glow, pulsing biofluorescence, vat illumination", "summary": "Contained bioluminescent reactors bathing spaces in organic light."},
    "Laser Grid": {"prompt": "laser grid, intersecting beams, chromatic lattice", "summary": "Precision laser lattice generating futuristic lighting geometry."},
    "Holographic Dome": {"prompt": "holographic dome canopy, rotating gradients, virtual sky", "summary": "Immersive holographic ceiling diffusing programmable spectrum washes."},
    "Meteor Shower": {"prompt": "meteor shower streaks, incandescent trails, cosmic sparks", "summary": "Sky filled with glowing meteors streaking luminous trails downward."},
    "Flare Burst": {"prompt": "signal flare burst, smoke-tinted glow, emergency wash", "summary": "Emergency flare casting dramatic red light through haze."},
    "Oil Lantern": {"prompt": "oil lantern glow, soot-streaked glass, steady warm pool", "summary": "Portable lantern providing steadfast warm illumination."},
    "Arc Welder": {"prompt": "arc welder flash, intense blue-white, showering sparks", "summary": "Industrial arc welding light freezing motion with harsh brilliance."},
    "Citylight Spill": {"prompt": "distant citylight spill, skyline glow, sodium haze", "summary": "Ambient glow from a distant skyline softly filling the frame."},
    "Crystal Chandelier": {"prompt": "crystal chandelier glitter, prismatic sparkle, ballroom glow", "summary": "Opulent chandelier refracting light into glistening shards."},
    "Bonfire Blaze": {"prompt": "towering bonfire blaze, roaring embers, sparks aloft", "summary": "Massive bonfire engulfing the environment in roaring orange light."},
    "Laneway Neon": {"prompt": "laneway neon strips, saturated signage, puddle reflections", "summary": "Tight alley bathed in stacked neon signage reflections."},
    "Bio-Lanterns": {"prompt": "bio-lantern organisms, glowing fauna, natural luminance", "summary": "Living lantern creatures casting organic multi-toned light."},
    "Ice Cavern Crystals": {"prompt": "ice cavern crystals, refracted glimmer, frozen glow", "summary": "Translucent ice crystals bending light through cavern walls."},
    "Plasma Torches": {"prompt": "plasma torch banks, blue-white arcs, industrial intensity", "summary": "Rows of plasma torches bathing subjects in blistering brilliance."},
    "Sunrise Window": {"prompt": "sunrise window beam, golden shafts, dust motes", "summary": "Early sun cascading through windows with painterly rays."},
    "Projector Spill": {"prompt": "film projector spill, dancing shadows, analog flicker", "summary": "Projector light spilling off screen with nostalgic flicker."},
    "Glimmering Reef": {"prompt": "coral reef glow, phosphorescent marine life, tropical illumination", "summary": "Undersea reef emitting soft gradients from luminous coral."},
    "Supernova Remnant": {"prompt": "supernova remnant glow, cosmic dust, radiant nebula", "summary": "Interstellar residue enveloping scene in vibrant nebular light."},
    "Iridescent Canopy": {"prompt": "iridescent canopy panels, shifting oil-slick colors", "summary": "Architectural canopy reflecting iridescent hues onto subjects."},
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
    "Specular Punch": {"prompt": "specular punch lighting, crisp highlights, lacquered sheen", "summary": "High-specular highlights carving glossy definition across surfaces."},
    "Veiled Diffusion": {"prompt": "veiled diffusion, gauzy wrap, mist-filtered glow", "summary": "Soft veil of diffused light for hazy, dreamlike coverage."},
    "Specular Mosaic": {"prompt": "specular mosaic, shattered highlights, jeweled reflections", "summary": "Fragmented highlights breaking across faceted surfaces."},
    "Feathered Rim": {"prompt": "feathered rim lighting, gradual halo, airy separation", "summary": "Gentle rim light with feathery falloff outlining silhouettes."},
    "Split Tone": {"prompt": "split-toned lighting, opposing color temperatures", "summary": "Two-tone lighting dividing the subject into contrasting hues."},
    "Motivated Practical": {"prompt": "motivated practicals, believable diegetic spill", "summary": "Stylized yet grounded lighting justified by on-set fixtures."},
    "Softbox Wrap": {"prompt": "giant softbox wrap, wrapping highlights, creamy falloff", "summary": "Massive soft source hugging the subject with gentle gradient."},
    "Kicker Highlights": {"prompt": "kicker highlights, sharp accent lines, sculpted edges", "summary": "Edge kickers introducing crisp accent streaks."},
    "High Key": {"prompt": "high-key lighting, airy brightness, minimal shadow", "summary": "Bright, buoyant scheme minimizing contrast for cheerful tone."},
    "Low Key": {"prompt": "low-key lighting, deep blacks, selective highlights", "summary": "Moody low-key envelope with pockets of illumination."},
    "Chromatic Spill": {"prompt": "chromatic spill, rainbow edges, spectral fringe", "summary": "Prismatic spill generating colorful haloing around forms."},
    "Firefly Scatter": {"prompt": "firefly scatter, pinpoint twinkles, drifting motes", "summary": "Micro light points swirling through the air like fireflies."},
    "Soft Focus Glow": {"prompt": "soft focus glow, diffusion bloom, romantic haze", "summary": "Dreamy glow softening detail for romantic imagery."},
    "Mirror Bounce": {"prompt": "mirror bounce lighting, crisp reflection, mirrored key", "summary": "Mirrored bounce producing sharp reflected highlights."},
    "Patterned Gobos": {"prompt": "patterned gobo wash, carved shadows, cut shapes", "summary": "Gobo patterns casting intricate silhouettes across surfaces."},
    "Industrial Strip": {"prompt": "industrial strip lighting, linear highlights, warehouse tone", "summary": "Strip fixtures painting parallel lines of illumination."},
    "Dappled Canopy": {"prompt": "dappled canopy light, leafy pattern, natural stipple", "summary": "Filtered sunlight flickering through foliage onto subjects."},
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
    "Golden Hour": {"prompt": "golden hour light, honeyed tones, elongated shadows", "summary": "Golden hour baths everything in soft amber light."},
    "Storm Night": {"prompt": "stormy midnight, lightning flashes, rain-lashed darkness", "summary": "Charged midnight storm with intermittent lightning wash."},
    "Pre-Dawn Blue": {"prompt": "pre-dawn blue hour, hushed gradients, sleeping city", "summary": "Quiet pre-dawn stillness awash in cool blues."},
    "High Noon": {"prompt": "high noon sun, overhead blaze, sharp shadows", "summary": "Unforgiving midday sun casting stark overhead shadows."},
    "Twilight": {"prompt": "twilight blend, fading warmth, encroaching cool", "summary": "Transitional twilight mixing warm and cool tones."},
    "Solar Eclipse": {"prompt": "solar eclipse dimming, surreal twilight, corona rim", "summary": "Eerie eclipse atmosphere with dramatic ambient shift."},
    "Lunar Eclipse": {"prompt": "lunar eclipse glow, copper moon, penumbral hues", "summary": "Earth-shadowed moon painting night with copper undertones."},
    "Rainy Afternoon": {"prompt": "rainy afternoon light, overcast drizzle, reflective streets", "summary": "Soft grey daylight with shimmering rain reflections."},
    "Winter Dawn": {"prompt": "winter dawn, frosted breath, pale sun", "summary": "Chilly dawn with subdued pastel sunlight."},
    "Summer Midnight": {"prompt": "summer midnight twilight, lingering glow, horizon gradients", "summary": "High-latitude midnight where sun barely dips, leaving glow."},
    "Desert High Sun": {"prompt": "desert high sun, heat shimmer, bleached highlights", "summary": "Scorching desert midday flattening contrast under glare."},
    "Golden Dusk": {"prompt": "deep golden dusk, saturated clouds, elongated shadows", "summary": "Late dusk deepening golds and oranges before nightfall."},
    "Aurora Midnight": {"prompt": "aurora midnight, dancing lights, polar night", "summary": "Polar midnight illuminated by auroral ribbons."},
    "Festival Evening": {"prompt": "festival evening glow, lanterns rising, celebratory warmth", "summary": "Community evening with layered practicals and warm ambiance."},
    "Stormy Noon": {"prompt": "stormy noon, bruise-cloud canopy, diffused fury", "summary": "Midday storm muting sun into dramatic diffuse glow."},
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
    "Extreme Wide": {"prompt": "extreme wide vista, monumental scale, tiny subject silhouette", "summary": "Vast scale framing dwarfs the subject within the environment."},
    "Macro Detail": {"prompt": "macro detail insert, texture emphasis, ultra close focus", "summary": "Macro detail shot isolating tactile surfaces and micro storytelling."},
    "Extreme Macro": {"prompt": "extreme macro, microscopic textures, abstract detail", "summary": "Ultra-magnified shot revealing microscopic textures."},
    "Medium Group": {"prompt": "medium group shot, waist-up ensemble, shared frame", "summary": "Medium framing accommodating multiple subjects in balance."},
    "Environmental Portrait": {"prompt": "environmental portrait, subject within meaningful setting", "summary": "Portrait capturing subject alongside context-rich environment."},
    "Architectural Wide": {"prompt": "architectural wide shot, towering structures, spatial clarity", "summary": "Wide framing highlighting grand architectural scale."},
    "Aerial Panorama": {"prompt": "aerial panorama, sweeping vista, expansive scope", "summary": "High-altitude panorama showcasing sprawling landscapes."},
    "Insert Detail": {"prompt": "insert detail shot, key prop close-up", "summary": "Tight insert isolating a crucial storytelling detail."},
    "Hero Medium": {"prompt": "hero medium shot, waist-up heroic framing", "summary": "Classic hero framing balancing intimacy and stature."},
    "Crowd Master": {"prompt": "crowd master shot, large-scale ensemble, layered depth", "summary": "Wide master capturing energetic crowd dynamics."},
    "Tableau": {"prompt": "tableau shot, staged composition, painterly arrangement", "summary": "Static tableau emphasizing composition and collective pose."},
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
    "Radial Burst": {"prompt": "radial burst composition, converging energy, center highlight", "summary": "Radiating lines pull the eye to a powerful center focal point."},
    "Negative Space": {"prompt": "negative space framing, minimal subject occupancy, breathing room", "summary": "Purposeful negative space emphasizing subject isolation."},
    "Golden Spiral": {"prompt": "golden spiral composition, dynamic curve, natural flow", "summary": "Golden spiral guiding viewer eye along elegant arc."},
    "Framed Within": {"prompt": "framed-within composition, doorway framing, nested focus", "summary": "Subject framed by architectural or natural elements for depth."},
    "Leading Curve": {"prompt": "leading curve composition, sweeping arc, graceful guide", "summary": "Curvilinear leading line drawing attention across frame."},
    "Foreground Obscure": {"prompt": "foreground obscure, partial blockage, voyeur framing", "summary": "Foreground elements partially obscuring action for intrigue."},
    "Layered Depth": {"prompt": "layered depth composition, foreground midground background", "summary": "Stacked planes creating rich depth cues."},
    "Diagonal Drive": {"prompt": "diagonal drive composition, kinetic tilt, motion emphasis", "summary": "Dynamic diagonals introducing energy and momentum."},
    "Central Void": {"prompt": "central void composition, subject encircling emptiness", "summary": "Elements arranged around intentional empty core."},
    "Asymmetrical Balance": {"prompt": "asymmetrical balance, weighted contrast, tension harmony", "summary": "Unequal elements balancing through visual weight."},
    "Mirror Symmetry": {"prompt": "mirror symmetry, reflective imagery, cloned halves", "summary": "Mirrored halves creating duality and repetition."},
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
    "Tilt Shift": {"prompt": "tilt-shift focal plane, selective focus, miniature illusion", "summary": "Tilt-shift lens controlling focus plane for miniature effect."},
    "Anamorphic": {"prompt": "anamorphic lens, cinematic squeeze, oval bokeh", "summary": "Anamorphic lensing for widescreen flare and oval bokeh."},
    "Super Telephoto": {"prompt": "super-telephoto lens, extreme reach, compressed horizon", "summary": "Ultra-long focal length flattening space to dramatic effect."},
    "Portrait Prime": {"prompt": "portrait prime lens, creamy bokeh, flattering compression", "summary": "Classic portrait prime emphasizing subject isolation and bokeh."},
    "Vintage Glass": {"prompt": "vintage lens, subtle aberrations, nostalgic softness", "summary": "Retro lens character introducing romantic imperfection."},
    "Soft Focus Lens": {"prompt": "soft focus lens, haloed highlights, blooming edges", "summary": "Specialty lens diffusing focus for dreamy imagery."},
    "Ultra Macro": {"prompt": "ultra macro lens, life-size magnification, shallow plane", "summary": "Macro lens capturing extreme close detail at 1:1 magnification."},
    "Pinhole": {"prompt": "pinhole optics, infinite focus, vignetted edges", "summary": "Pinhole lens aesthetic offering deep focus and organic vignette."},
    "Shift Lens": {"prompt": "shift lens, perspective control, architectural correction", "summary": "Perspective-control lens keeping verticals true."},
    "Catadioptric": {"prompt": "catadioptric mirror lens, donut bokeh, compact telephoto", "summary": "Mirror telephoto lens creating signature donut-shaped bokeh."},
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
    "Drone Chase": {"prompt": "drone chase angle, high-speed pursuit, aerial tracking", "summary": "Fast-moving drone perspective sweeping through the action."},
    "Shoulder Cam": {"prompt": "over-shoulder handheld cam, intimate proximity, reactive framing", "summary": "Shoulder-mounted camera adding immersive immediacy."},
    "Dutch Low": {"prompt": "low dutch angle, canted horizon near ground", "summary": "Low-positioned dutch angle heightening unease and power."},
    "Head-On": {"prompt": "head-on angle, subject facing camera, direct confrontation", "summary": "Direct frontal angle confronting viewer with subject."},
    "Three-Quarter": {"prompt": "three-quarter angle, slight turn, dimensionality", "summary": "Classic three-quarter angle revealing facial depth."},
    "Worm's Eye": {"prompt": "worm's-eye view, extreme upward gaze, towering scale", "summary": "Extreme low angle exaggerating vertical dominance."},
    "Ceiling Mount": {"prompt": "ceiling mounted camera, surveillance vantage", "summary": "High fixed vantage delivering surveillance aesthetic."},
    "Foot-Level": {"prompt": "foot-level angle, grounded perspective, kinetic motion", "summary": "Camera placed at ground level to emphasize motion and speed."},
    "Mirror POV": {"prompt": "mirror point-of-view, reflective perspective, dual framing", "summary": "Angle captured via mirror reflection for dual-layer storytelling."},
    "Drone Descent": {"prompt": "drone descent angle, rapidly dropping aerial", "summary": "Descending aerial angle transitioning from high to mid altitude."},
    "Shoulder Reverse": {"prompt": "reverse over-shoulder, conversational counter", "summary": "Counter-angle OTS capturing opposing subject in dialogue."},
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
    "Overhead Master": {"prompt": "overhead master shot, architectural layout, orchestrated movement", "summary": "High overhead master framing to chart spatial choreography."},
    "Detail Montage": {"prompt": "detail montage series, rapid inserts, sensory collage", "summary": "Montage of detail shots creating rhythmic storytelling."},
    "Reaction Shot": {"prompt": "reaction shot, emotional response focus", "summary": "Shot capturing character reaction for emotional punctuation."},
    "POV Shot": {"prompt": "point-of-view shot, first-person perspective", "summary": "Subjective POV immersing viewer in character perspective."},
    "Montage Sequence": {"prompt": "montage sequence, time compression, rhythmic cuts", "summary": "Collection of shots compressing time through rhythmic editing."},
    "Tracking Shot": {"prompt": "tracking shot, continuous movement, follow focus", "summary": "Shot moving alongside subject to retain consistent framing."},
    "Dialogue Two Shot": {"prompt": "dialogue two shot, conversational framing", "summary": "Balanced two shot highlighting dialogue between characters."},
    "Extreme Long": {"prompt": "extreme long establishing, distant subjects, landscape emphasis", "summary": "Very wide framing situating characters within vast landscape."},
    "Hero Shot": {"prompt": "hero shot, triumphant pose, low angle emphasis", "summary": "Dramatic hero framing underscoring power and victory."},
    "Insert POV": {"prompt": "insert POV shot, detail through character eyes", "summary": "POV insert focusing on critical detail as character sees it."},
    "Crowd Reaction": {"prompt": "crowd reaction shot, ensemble response", "summary": "Group reaction capturing collective emotional beat."},
}


COLOR_TONE_OPTIONS = {
    "None": {"prompt": "", "summary": "No color tone emphasis."},
    "Warm Tone": {"prompt": "warm color palette, golden hues, inviting saturation", "summary": "Warm palette with golden highlights."},
    "Cool Tone": {"prompt": "cool color palette, blue undertones, serene mood", "summary": "Cool palette with calming tones."},
    "High Saturation": {"prompt": "high saturation, vivid colors, bold intensity", "summary": "Highly saturated color treatment."},
    "Low Saturation": {"prompt": "low saturation, muted palette, cinematic restraint", "summary": "Muted palette with cinematic restraint."},
    "Pastel Tone": {"prompt": "pastel color palette, powdery hues, gentle saturation", "summary": "Soft pastel wash for dreamy, delicate moods."},
    "Neo Noir": {"prompt": "neo-noir palette, electric highlights, deep shadows", "summary": "High-contrast neon noir treatment with moody blacks."},
    "Bioluminescent": {"prompt": "bioluminescent palette, teal-magenta glow, organic luminance", "summary": "Bioluminescent-inspired palette with glowing cool hues."},
    "Sepia Film": {"prompt": "sepia-toned film wash, vintage warmth, gentle fade", "summary": "Vintage sepia palette with analog softness."},
    "Teal & Orange": {"prompt": "teal and orange palette, cinematic contrast, blockbuster grade", "summary": "High-contrast teal/orange pairing for cinematic punch."},
    "Muted Pastel": {"prompt": "muted pastel tones, powdery softness, delicate wash", "summary": "Soft pastel palette dialed down for subtle refinement."},
    "Monochrome Steel": {"prompt": "monochrome steel palette, cool grays, industrial vibe", "summary": "Steely monochrome emphasizing industrial mood."},
    "Iridescent": {"prompt": "iridescent color play, oil-slick spectrum, shifting hues", "summary": "Shimmering palette shifting colors with angle."},
    "Sun-Bleached": {"prompt": "sun-bleached palette, desaturated warmth, desert fade", "summary": "Faded warm palette recalling sun-weathered surfaces."},
    "Candy Pop": {"prompt": "candy pop palette, sugary brights, high-gloss saturation", "summary": "Playful high-saturation palette reminiscent of candy wrappers."},
    "Neon Pulse": {"prompt": "neon pulse palette, electric magentas, cyan highlights", "summary": "Glowing neon palette pulsing with nightlife energy."},
    "Mocha": {"prompt": "mocha palette, creamy browns, cozy latte warmth", "summary": "Comforting brown palette echoing café tones."},
    "Frosted Glass": {"prompt": "frosted glass palette, opaque pastels, milky diffusion", "summary": "Milky translucent palette softening contrast with frost-like hues."},
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
    "Parkour": {"prompt": "urban parkour vault, wall run, kinetic agility", "summary": "Parkour motion exploding across rooftops and railings."},
    "Aerial Silk": {"prompt": "aerial silk routine, suspended twirl, fluid acrobatics", "summary": "Aerial silks performance capturing graceful aerial control."},
    "Park Skating": {"prompt": "park skating session, grinding rails, flowing lines", "summary": "Skatepark action blending tricks with fluid movement."},
    "Martial Kata": {"prompt": "martial arts kata, precise forms, disciplined strikes", "summary": "Structured martial sequence emphasizing precision and flow."},
    "Ballet Leap": {"prompt": "grand jeté ballet leap, extended lines, airborne grace", "summary": "Classical ballet leap freezing dancer mid-flight."},
    "Free Diving": {"prompt": "free diving descent, streamlined motion, underwater calm", "summary": "Graceful underwater descent captured mid glide."},
    "Breakdance Spin": {"prompt": "breakdance windmill spin, kinetic sweep, dynamic floorwork", "summary": "Explosive breakdance spin radiating urban energy."},
    "Hoverboard Drift": {"prompt": "hoverboard drift, antigrav carve, futuristic glide", "summary": "Futuristic hoverboard carving arcs through the air."},
    "Park Parade": {"prompt": "parade procession, synchronized steps, celebratory rhythm", "summary": "Processional parade motion with coordinated ensemble."},
    "Sword Duel": {"prompt": "sword duel clash, steel arcs, poised footwork", "summary": "Dramatic swordplay with dynamic lunges and parries."},
    "Mountain Climb": {"prompt": "mountain climb ascent, rope work, vertical challenge", "summary": "Climber scaling sheer rock with dynamic upward movement."},
    "Surf Cutback": {"prompt": "surf cutback maneuver, spray arc, fluid carve", "summary": "Surfer executing stylish cutback with water spray."},
    "Aerial Drone": {"prompt": "drone maneuver, looping flight, agile hover", "summary": "Agile drone weaving loops through obstacles."},
    "Samba Dance": {"prompt": "samba dance rhythm, fast footwork, carnival flair", "summary": "Energetic samba steps pulsing with festive rhythm."},
    "Sprinting Relay": {"prompt": "relay sprint handoff, baton exchange, explosive acceleration", "summary": "Team relay sprint capturing baton handoff intensity."},
}


ACTION_PRIMARY_OPTIONS = {
    "None": {"prompt": "", "summary": "No primary action emphasis."},
    "Heroic Sprint": {"prompt": "explosive sprint, knees driving high, purposeful forward lean", "summary": "Powerful sprinting burst projecting urgency and determination."},
    "Focused Jog": {"prompt": "steady jog, rhythmic breathing, relaxed arm swing", "summary": "Measured jogging pace emphasizing stamina and calm focus."},
    "Casual Walk": {"prompt": "casual walk, easy stride, observant gaze", "summary": "Unhurried walking pace conveying confidence and ease."},
    "Power Stride": {"prompt": "power stride, decisive footfalls, shoulders squared", "summary": "Intentional march underscoring leadership and resolve."},
    "Parade March": {"prompt": "synchronized march, precision cadence, ceremonial posture", "summary": "Disciplined marching cadence suited for procession beats."},
    "Tactical Creep": {"prompt": "controlled prowl, low center of gravity, silent footsteps", "summary": "Slow stealth advance ideal for infiltration storytelling."},
    "Graceful Turn": {"prompt": "graceful pivot, fluid hip rotation, balanced poise", "summary": "Elegant pirouette moment showcasing refined control."},
    "Combat Roll": {"prompt": "combat roll, momentum carry, swift recovery stance", "summary": "Dynamic evasive roll leading into combat readiness."},
    "Acrobatic Flip": {"prompt": "tight aerial flip, tucked knees, precise landing", "summary": "Athletic flip highlighting agility and aerial confidence."},
    "Vault Leap": {"prompt": "vault leap over obstacle, palms planted, legs split", "summary": "Momentum-driven vault clearing barriers with flair."},
    "Wall Run": {"prompt": "wall run, angled sprint, defying gravity", "summary": "Parkour-inspired wall run accentuating daring motion."},
    "Ledge Climb": {"prompt": "vertical climb, fingertips gripping, core engaged", "summary": "Determined ascent capturing grit and physical strength."},
    "Grapple Swing": {"prompt": "grappling swing, cable taut, arc through air", "summary": "Swinging traversal showcasing momentum and heroics."},
    "Hover Drift": {"prompt": "hoverboard drift, counter lean, plasma trail", "summary": "Futuristic glide sequences with dramatic banking."},
    "Aerial Hover": {"prompt": "suspended hover, subtle limb adjustments, anti-grav hum", "summary": "Weightless hover emphasizing controlled stillness."},
    "Sword Combo": {"prompt": "sword combo slash, blade flare, precise follow-through", "summary": "Martial sword sequence brimming with kinetic intent."},
    "Shield Brace": {"prompt": "shield brace, wide stance, impact-ready", "summary": "Protective stance built for blocking heavy blows."},
    "Bow Release": {"prompt": "drawn bow release, focused gaze, taut string snap", "summary": "Archery moment capturing tension and accuracy."},
    "Spell Channel": {"prompt": "channeling spell energy, sigils orbiting, outstretched palm", "summary": "Arcane casting posture radiating cinematic power."},
    "Healing Surge": {"prompt": "healing surge, warm aura, hands hovering over ally", "summary": "Supportive restorative action showcasing compassion."},
    "Tech Interface": {"prompt": "rapid console interface, holographic projections, swift keystrokes", "summary": "High-speed tech interaction driven by intellect."},
    "Drone Pilot": {"prompt": "remote drone coordination, dual sticks, analytical focus", "summary": "Precision drone piloting highlighting dexterity."},
    "Vehicle Drift": {"prompt": "vehicle drift, counter steering, tire smoke curl", "summary": "High-octane driving beat with cinematic drift."},
    "Mech Command": {"prompt": "mech command gestures, haptic controls, cockpit glow", "summary": "Piloting a giant mech with commanding gestures."},
    "Gun Kata": {"prompt": "gun kata flow, synchronized dual pistols, spinning disarm", "summary": "Stylized firearm choreography blending combat and dance."},
    "Cover Slide": {"prompt": "slide into cover, sparks skimming, low ready", "summary": "Tactical slide maneuver transitioning into cover."},
    "Reload Snap": {"prompt": "speed reload snap, magazine swap, decisive click", "summary": "Swift weapon reload underscoring discipline."},
    "Data Hack": {"prompt": "neural hack posture, luminous code stream, intense focus", "summary": "Cyber intrusion beat with immersive hacking visuals."},
    "Creative Sketch": {"prompt": "rapid sketch strokes, charcoal dust, concentrated expression", "summary": "Artistic gesture capturing creativity in motion."},
    "Brush Flourish": {"prompt": "brush flourish across canvas, pigment spray, painterly arc", "summary": "Expressive painting movement bursting with color."},
    "Sculpting Strike": {"prompt": "sculpting chisel strike, stone shards, deliberate rhythm", "summary": "Sculptural carving moment emphasizing craftsmanship."},
    "Conducting Cue": {"prompt": "orchestral conducting cue, baton sweep, poised crescendo", "summary": "Commanding conducting gesture driving musical energy."},
    "Freestyle Dance": {"prompt": "freestyle dance burst, syncopated limbs, playful sync", "summary": "Improvisational dance packed with personality."},
    "Contemporary Flow": {"prompt": "contemporary dance flow, sweeping floor contact, expressive torso", "summary": "Fluid dance sequence mixing control and emotion."},
    "Martial Spar": {"prompt": "martial spar exchange, block and counter, sharpened reflexes", "summary": "Friendly sparring beat balancing offense and defense."},
    "Meditative Breath": {"prompt": "meditative breath cycle, grounded stance, centered palms", "summary": "Stillness-focused breathwork radiating calm strength."},
    "Negotiation Gesture": {"prompt": "open negotiation gesture, hands extended, emphatic cadence", "summary": "Persuasive communication action highlighting diplomacy."},
    "Briefing Command": {"prompt": "mission briefing command stance, holo-map gesture, directive tone", "summary": "Mission leadership beat rallying the team."},
    "Victory Cheer": {"prompt": "victory cheer, arms raised, triumphant shout", "summary": "Celebratory climax conveying success and joy."},
    "Reassuring Embrace": {"prompt": "reassuring embrace, protective posture, supportive warmth", "summary": "Supportive hug emphasizing trust and care."},
    "Rescue Carry": {"prompt": "fireman carry rescue, urgent pace, determined grit", "summary": "Heroic rescue action grounded in strength and urgency."},
    "Scientific Scan": {"prompt": "handheld scanner sweep, sensor readouts, analytical calm", "summary": "Investigative scanning beat revealing discoveries."},
}


ACTION_SECONDARY_OPTIONS = {
    "None": {"prompt": "", "summary": "No secondary beat."},
    "Evasive Sidestep": {"prompt": "evasive sidestep, dust kick, narrow escape", "summary": "Quick lateral dodge threading through danger."},
    "Counter Strike": {"prompt": "counter strike, sudden riposte, momentum reversal", "summary": "Instant retaliation that flips the battlefield tempo."},
    "Guard Break": {"prompt": "guard break shove, stance disruption, advantage claimed", "summary": "Aggressive shove opening defense lines."},
    "Precision Aim": {"prompt": "precision aim, steady breath hold, laser focus", "summary": "Focused targeting moment capturing suspense."},
    "Scan Sweep": {"prompt": "environmental scan sweep, HUD overlay, alerts ping", "summary": "Data-gathering sweep amplifying situational awareness."},
    "Signal Call": {"prompt": "hand signal callout, coordinated motion, squad synch", "summary": "Silent coordination cue enhancing teamwork."},
    "Shield Raise": {"prompt": "shield raise, sparks deflected, resilience flare", "summary": "Defensive beat underlining protection."},
    "Momentum Slide": {"prompt": "momentum slide, low friction drift, sparks trailing", "summary": "Stylized slide maintaining kinetic energy."},
    "Ground Pound": {"prompt": "ground pound impact, shockwave ring, dust burst", "summary": "Impactful finishing beat showcasing raw force."},
    "Air Twist": {"prompt": "aerial twist kick, suspended rotation, dramatic follow-through", "summary": "Signature kick sequence loaded with flair."},
    "Grapple Lock": {"prompt": "grapple lock, leverage shift, controlled takedown", "summary": "Submission-oriented maneuver demonstrating technique."},
    "Companion Assist": {"prompt": "companion assist boost, interlocked hands, cooperative lift", "summary": "Supportive teammate beat accentuating trust."},
    "Barrier Deploy": {"prompt": "deployable barrier throw, emitter unfold, cover established", "summary": "Instant cover creation for tactical repositioning."},
    "Drone Launch": {"prompt": "drone launch flick, rotor ignition, rapid ascent", "summary": "Secondary action launching support drone units."},
    "Med-Pack Toss": {"prompt": "med-pack toss, side-arm throw, lifesaving delivery", "summary": "Supportive aid thrown to allies mid-conflict."},
    "Energy Burst": {"prompt": "energy burst discharge, luminous surge, crackling aftermath", "summary": "Secondary flare of power emphasizing impact."},
    "Telemetry Check": {"prompt": "telemetry check, wrist holo, data validation", "summary": "Brief systems check ensuring mission alignment."},
    "Environmental Interaction": {"prompt": "interactive environment cue, trigger pull, machinery response", "summary": "Action tied to world mechanics and set pieces."},
    "Emotional Accent": {"prompt": "emotional accent glance, micro-expression, character depth", "summary": "Subtle emotional beat layered into action."},
}


ACTION_TEMPO_OPTIONS = {
    "None": {"prompt": "", "summary": "Neutral tempo."},
    "Slow Burn": {"prompt": "slow burn cadence, deliberate pacing, controlled breath", "summary": "Measured tempo suited for stealth or tension building."},
    "Rising Momentum": {"prompt": "rising momentum, energy ramp, quickening steps", "summary": "Tempo increase signaling imminent breakthrough."},
    "Pulse Pounding": {"prompt": "pulse-pounding rhythm, heartbeat percussion, kinetic urgency", "summary": "High-tempo drive keeping adrenaline elevated."},
    "Frantic Rush": {"prompt": "frantic rush, untamed velocity, scattered sparks", "summary": "Chaotic tempo perfect for chase sequences."},
    "Steady Cadence": {"prompt": "steady cadence, balanced breathing, tactical precision", "summary": "Even tempo highlighting discipline and stamina."},
    "Staccato Beats": {"prompt": "staccato beats, rapid-fire cuts, short bursts of motion", "summary": "Choppy tempo ideal for montage or combat edits."},
    "Weightless Drift": {"prompt": "weightless drift tempo, slow-floating beats, elongated frames", "summary": "Dreamlike tempo emphasizing suspended motion."},
    "Heroic Crescendo": {"prompt": "heroic crescendo, swelling momentum, triumphant surge", "summary": "Epic tempo climb culminating in a victorious beat."},
    "Sneaking Pulse": {"prompt": "sneaking pulse, low heart rate, suppressed motion", "summary": "Subtle tempo maintaining stealth tension."},
}


ACTION_INTERACTION_OPTIONS = {
    "None": {"prompt": "", "summary": "Solo focus."},
    "Solo Focus": {"prompt": "solo-focused action, spotlight isolated performer", "summary": "Highlights individual capability without distractions."},
    "Duo Synchrony": {"prompt": "duo synchrony, mirrored movements, interlocking timing", "summary": "Two-person coordination conveying trust and chemistry."},
    "Squad Coordination": {"prompt": "squad coordination, layered formation, call-and-response", "summary": "Team-based action balanced across multiple performers."},
    "Crowd Navigation": {"prompt": "crowd navigation, weaving through onlookers, reactive adjustments", "summary": "Action threaded through dense crowd dynamics."},
    "Rival Showdown": {"prompt": "rival showdown, charged eye-line, matched intensity", "summary": "Dramatic confrontation between evenly matched opponents."},
    "Mentor Guidance": {"prompt": "mentor guidance, supportive coaching, corrective touch", "summary": "Instructional beat where mentor refines protege technique."},
    "Rescue Support": {"prompt": "rescue support, stabilizing assist, collaborative lift", "summary": "Mutual aid moment during high-stakes scenario."},
    "Celebration Group": {"prompt": "celebration group embrace, shared triumph, collective cheer", "summary": "Group celebration amplifying emotional payoff."},
    "Spectator Engagement": {"prompt": "spectator engagement, audience interaction, responsive energy", "summary": "Performer interacting directly with enthusiastic crowd."},
    "Tactical Tandem": {"prompt": "tactical tandem, overlapping cover fire, seamless transitions", "summary": "Combat partnership moving as a unified unit."},
}


NSFW_ACTION_PRIMARY_OPTIONS = {
    "None": {"prompt": "", "summary": "No specific mature action emphasis."},
    "Sensual Caress": {"prompt": "sensual caress, fingertips tracing curves, lingering warmth", "summary": "Tender caress lingering over consenting adult partner."},
    "Slow Undress": {"prompt": "slow undress, deliberate fabric slide, teasing reveal", "summary": "Gradual wardrobe peel emphasizing anticipation."},
    "Passionate Embrace": {"prompt": "passionate embrace, bodies pressed, breath mingling", "summary": "Full-body embrace radiating mutual desire."},
    "Intimate Sway": {"prompt": "intimate sway, hips aligned, subtle grind", "summary": "Synchronized sway capturing shared rhythm."},
    "Seductive Strut": {"prompt": "seductive strut, confident hips, smoldering gaze", "summary": "Confident walk engineered to entice."},
    "Sultry Floorwork": {"prompt": "sultry floorwork, rolling shoulders, arched back", "summary": "Floor routine showcasing curves and fluid control."},
    "Chair Tease": {"prompt": "chair straddle tease, playful lean back, fingertip glide", "summary": "Chair-focused routine blending tease and control."},
    "Lap Dance Flourish": {"prompt": "lap dance flourish, measured grind, eye contact", "summary": "Exploratory lap dance centered on consent and connection."},
    "Wall Pin": {"prompt": "pinned to wall, dominant arm brace, electric tension", "summary": "Consensual wall pin layering controlled dominance."},
    "Silk Rope Display": {"prompt": "silk rope display, decorative binds, supportive suspension", "summary": "Artful rope styling highlighting trust and safety."},
    "Blindfold Reveal": {"prompt": "blindfold reveal, silk slip, heightened senses", "summary": "Playful sensory deprivation moment building anticipation."},
    "Oil Massage": {"prompt": "warm oil massage, glistening skin, affectionate knead", "summary": "Sensual massage exchanging comfort and pleasure."},
    "Body Trace": {"prompt": "body tracing, nails grazing, deliberate pace", "summary": "Slow tracing that savors every contour thoughtfully."},
    "Corset Tighten": {"prompt": "corset tightening, breathy gasp, mirrored gaze", "summary": "Intimate wardrobe cinch celebrating curves."},
    "Stocking Roll": {"prompt": "stocking roll, thigh-high descent, playful smirk", "summary": "Tempting hosiery peel that spotlights legs."},
    "Garter Snap": {"prompt": "garter snap tease, playful sting, laughing eyes", "summary": "Cheeky garter snap punctuating flirtatious energy."},
    "Mirror Worship": {"prompt": "mirror worship pose, self-admiring touch, glossy lighting", "summary": "Self-love moment honoring adult confidence."},
    "Bath Embrace": {"prompt": "shared bubble bath embrace, water shimmer, relaxed smiles", "summary": "Steamy bath cuddle under soft candlelight."},
    "Dominant Command": {"prompt": "dominant command stance, guiding touch, steady gaze", "summary": "Command-driven beat emphasizing trusted leadership."},
    "Submissive Offer": {"prompt": "submissive offer, kneeling poise, open palms", "summary": "Reverent offering posture celebrating mutual trust."},
    "Morning Glow": {"prompt": "morning-after glow, sheet drape, satisfied stretch", "summary": "Post-intimacy glow capturing tenderness and safety."},
}


NSFW_ACTION_SECONDARY_OPTIONS = {
    "None": {"prompt": "", "summary": "No secondary mature beat."},
    "Lip Bite": {"prompt": "soft lip bite, playful tension, smoldering glance", "summary": "Subtle lip bite amplifying chemistry."},
    "Neck Kiss": {"prompt": "neck kiss, lingering breath, gentle tilt", "summary": "Neck kiss moment underscoring intimacy."},
    "Ear Whisper": {"prompt": "ear whisper tease, warm breath, secretive smile", "summary": "Close whisper sharing private promises."},
    "Hair Sweep": {"prompt": "hair sweep aside, revealing collarbone, seductive focus", "summary": "Hair sweep opening the frame to more skin."},
    "Finger Trail": {"prompt": "fingertip trail along spine, shiver ripple", "summary": "Slow finger trail sending shivers down the spine."},
    "Ribbon Tug": {"prompt": "ribbon tug release, fluttering fabric, playful gasp", "summary": "Ribbon pull unlocking the next reveal."},
    "Stocking Adjust": {"prompt": "stocking adjustment, deliberate roll, thigh emphasis", "summary": "Adjusting stockings to heighten leg focus."},
    "Gaze Hold": {"prompt": "gaze lock, dilated pupils, whispered invitation", "summary": "Mutual gaze hold that communicates consent clearly."},
    "Hand Restraint": {"prompt": "gentle wrist restraint, supportive grip, caring check-in", "summary": "Soft restraint paired with constant reassurance."},
    "Body Dip": {"prompt": "dramatic body dip, partner support, arched torso", "summary": "Supported dip highlighting trust and strength."},
    "Hip Grind": {"prompt": "hip grind accent, rolling motion, synchronized breath", "summary": "Rhythmic hip grind deepening sensual flow."},
    "Glove Peel": {"prompt": "glove peel, fingertip tease, slow reveal", "summary": "Slow glove peel coaxing attention to touch."},
    "Perfume Mist": {"prompt": "perfume mist spray, lingering scent, coy smile", "summary": "Scented flourish prepping for closeness."},
    "Velvet Stroke": {"prompt": "velvet glove stroke along torso, indulgent pace", "summary": "Soft fabric glide delighting sensitive skin."},
}


NSFW_ACTION_TEMPO_OPTIONS = {
    "None": {"prompt": "", "summary": "Neutral tempo for mature scene."},
    "Slow Tease": {"prompt": "slow tease tempo, patient pacing, suspended breath", "summary": "Lingering tempo that savors every second."},
    "Languid Flow": {"prompt": "languid flow, fluid transitions, mellow rhythm", "summary": "Relaxed cadence for indulgent sequences."},
    "Measured Build": {"prompt": "measured build, rising heat, controlled escalation", "summary": "Gradual crescendo balancing excitement."},
    "Playful Bounce": {"prompt": "playful bounce, upbeat flirtation, lively pace", "summary": "Light-hearted tempo packed with charm."},
    "Breathless Waves": {"prompt": "breathless wave tempo, rising and crashing energy", "summary": "Repeating waves of intensity and release."},
    "Urgent Clutch": {"prompt": "urgent clutch tempo, hungry pace, desperate energy", "summary": "Fast pace fueled by mutual craving."},
    "Commanded Pace": {"prompt": "commanded pace, deliberate cues, guided rhythm", "summary": "Dominant partner dictating tempo with care."},
    "Hypnotic Loop": {"prompt": "hypnotic loop, repeating pattern, trance-like focus", "summary": "Repetitive motions that mesmerize audience."},
    "Tender Pause": {"prompt": "tender pause beats, held breaths, eye contact linger", "summary": "Strategic pauses that celebrate connection."},
}


CAMZ_PERSONA_OPTIONS = {
    "Soft Glam Muse": {
        "prompt": "soft glam cam performer, luminous skin, encouraging smile, relaxed confidence",
        "notes": "Lean into approachable warmth blended with polished glam cues.",
    },
    "Cyber Starlet": {
        "prompt": "futuristic cyber cam muse, neon accent liner, playful tech accessories",
        "notes": "Pair shimmering highlights with synth-forward ambience for modern edge.",
    },
    "Fitness Tease": {
        "prompt": "athletic cam goddess, toned silhouette, playful flex moments",
        "notes": "Incorporate light workout props and confident body language cues.",
    },
    "Sultry Jazz": {
        "prompt": "jazz lounge cam siren, velvety voice, deliberate slow gestures",
        "notes": "Match low tempo jazz soundtrack with honeyed lighting for intimacy.",
    },
}


CAMZ_STAGE_OPTIONS = {
    "Neon Loft": {
        "prompt": "neon loft backdrop, led strip accents, reflective plexi floor",
        "notes": "Balance saturated highlights with soft fill to flatter skin.",
    },
    "Velvet Boudoir": {
        "prompt": "crimson velvet boudoir set, fairy lights, plush textures",
        "notes": "Layer candles and warm bulbs to deepen romantic ambience.",
    },
    "Glow Studio": {
        "prompt": "glow studio backdrop, gradient colorwash, cloud diffuser panels",
        "notes": "Use color cycling and haze for dreamy, stylized streaming look.",
    },
    "Gamer Den": {
        "prompt": "rgb gamer desk, holographic screens, soft plush seating",
        "notes": "Mix animated overlays with keyboard glow for interactive energy.",
    },
}


CAMZ_CAMERA_OPTIONS = {
    "Intimate Close": {
        "prompt": "intimate close framing, direct lens eye contact, creamy bokeh",
        "notes": "Keep lens near eye level for immediate connection and sparkle.",
    },
    "Desk Peek": {
        "prompt": "desk peek composition, slightly elevated perspective, flattering angle",
        "notes": "Angle camera from high-left to emphasize eyes and decolletage.",
    },
    "Full Body": {
        "prompt": "full body cam frame, full-length mirror, responsive lighting",
        "notes": "Stage lighting evenly to avoid clipping during motion demos.",
    },
    "Dynamic Dolly": {
        "prompt": "slow dolly glide, remote gimbal, smooth parallax",
        "notes": "Automate subtle motion to keep stream kinetic without distraction.",
    },
}


CAMZ_ENERGY_OPTIONS = {
    "Gentle Sway": {
        "prompt": "gentle swaying motion, soft giggles, tender pacing",
        "notes": "Use lingering gestures and ASMR whisper tones for relaxation.",
    },
    "Hype Spark": {
        "prompt": "high-energy bounce, playful chatter, animated laughter",
        "notes": "Cue upbeat playlists and interactive games for tip spikes.",
    },
    "Slow Burn": {
        "prompt": "slow-burn tease, deliberate pauses, smoldering eye contact",
        "notes": "Layer progressive reveals with countdown widgets for tension.",
    },
    "Command Mode": {
        "prompt": "commanding domme cadence, confident directives, teasing coaching",
        "notes": "Balance assertive tone with check-ins on boundaries and comfort.",
    },
}


NSFW_ACTION_INTERACTION_OPTIONS = {
    "None": {"prompt": "", "summary": "Solo highlight by default."},
    "Solo Self-Admiration": {"prompt": "solo self-admiration, mirrored touch, confident posture", "summary": "Spotlights a single adult indulging in self-appreciation."},
    "Mirror Performance": {"prompt": "mirror performance, dual reflections, choreographed tease", "summary": "Performer using mirrors to amplify allure."},
    "Mutual Embrace": {"prompt": "mutual embrace, intertwined limbs, tender reciprocity", "summary": "Two consenting adults wrapped in equal affection."},
    "Dominant Lead": {"prompt": "dominant lead, guiding hand, steady reassurance", "summary": "Confident lead steering an enthusiastic partner."},
    "Submissive Offering": {"prompt": "submissive offering, lowered gaze, trusting openness", "summary": "Trust-forward posture celebrating consensual vulnerability."},
    "Power Switch": {"prompt": "power exchange switch, playful role reversal", "summary": "Partners swapping roles with delighted consent."},
    "Voyeur Tease": {"prompt": "voyeur tease, aware of onlookers, controlled reveal", "summary": "Flirtatious performance directed at an invited audience."},
    "Stage Showcase": {"prompt": "stage showcase, spotlighted solo, theatrical flourish", "summary": "Burlesque-style spotlight designed for adoring fans."},
    "Lap Dance Delivery": {"prompt": "lap dance delivery, partner seated, performer leading", "summary": "Classic lap dance built on clear boundaries."},
    "Sensual Massage Exchange": {"prompt": "mutual massage exchange, alternating focus, satisfied sighs", "summary": "Partners trading soothing touch in balanced turns."},
    "Tandem Pose": {"prompt": "tandem pose alignment, sculpted silhouettes, mutual balance", "summary": "Dual posing moment engineered for visual harmony."},
}

PRESET_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "presets")

CUSTOM_OPTION = "Custom Input"

FORMULA_CONFIGS = {
    "Basic Formula": {
        "description": "Subject + Scene + Motion — perfect for ideation and quick inspiration.",
        "structure": ["subject", "scene", "motion"],
    },
    "Advanced Formula": {
        "description": "Subject (desc) + Scene (desc) + Motion (desc) + Aesthetic controls + Stylization.",
        "structure": ["subject", "scene", "motion", "aesthetic", "stylization"],
    },
    "Story Spotlight": {
        "description": "Focus subject + environmental beat + camera language + emotional tone summary.",
        "structure": ["subject", "scene", "motion", "emotion", "camera"],
    },
    "Trailer Teaser": {
        "description": "Cold open hook + subject descriptor + kinetic beat + stylization tag cloud.",
        "structure": ["scene", "subject", "motion", "stylization"],
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
    "Holographic Panels": {"prompt": "holographic panel lighting, refracted neon, cascading spectrum wash", "summary": "Glitchy holographic panels bathing the scene in shimmering gradients."},
    "Torchline": {"prompt": "torch-lit procession, wavering flame line, ember flicker", "summary": "Row of torches casting rhythmic pulses of warm light."},
    "Neon Billboard": {"prompt": "neon billboard glow, saturated signage wash, flickering letters", "summary": "Vibrant billboard light bathing the scene in rhythmic neon pulses."},
    "Campfire Circle": {"prompt": "campfire circle, ember sparks, storytelling glow", "summary": "Intimate fire pit lighting painting faces with warm flicker."},
    "Stage Spotlight": {"prompt": "stage spotlight beam, hard edge falloff, performer isolation", "summary": "Focused theatrical spotlight carving subject from darkness."},
    "Lightning Storm": {"prompt": "lightning storm bursts, strobing sky flashes, electric contrast", "summary": "Unpredictable lightning bolts freezing action in high contrast."},
    "Volcanic Flow": {"prompt": "volcanic magma glow, molten spill, infernal ambience", "summary": "Seething lava light casting ominous crimson across surfaces."},
    "Candlelit Vigil": {"prompt": "clustered candlelight, fluttering wicks, hushed warmth", "summary": "Sea of candles producing soft, reverent illumination."},
    "Aurora Curtain": {"prompt": "aurora curtain glow, shifting greens and violets, sky drape", "summary": "Northern lights bathing subjects in dreamy celestial hues."},
    "Starlight": {"prompt": "pure starlight, silver speckle, expansive night shimmer", "summary": "Subtle starlit exposure lending gentle highlights to silhouettes."},
    "Underwater Caustics": {"prompt": "underwater caustic light, dancing wave reflections, aquatic shimmer", "summary": "Liquid light patterns rippling across submerged subjects."},
    "Snow Reflection": {"prompt": "snowfield bounce light, diffuse white glow, winter reflection", "summary": "Snow bounce filling shadows with cool diffuse brightness."},
    "Forge Hearth": {"prompt": "forge hearth blaze, iron sparks, molten core", "summary": "Blacksmith forge light casting muscular orange highlights."},
    "Alchemical Vat": {"prompt": "alchemical vat glow, bubbling neon liquids, laboratory luminescence", "summary": "Arcane vats emitting surreal colored glows through mist."},
    "Cyber Street Lamps": {"prompt": "cyberpunk street lamps, holographic ads, saturated sidewalk beams", "summary": "Urban street lamps layering colored pools across rain-slick pavement."},
    "Gaslight Row": {"prompt": "gaslight row glow, amber halos, Victorian haze", "summary": "Historical gas lamps lining the street with soft amber halos."},
    "Lantern Parade": {"prompt": "festival lantern parade, drifting paper lights, communal glow", "summary": "Floating lanterns surrounding characters in celebratory radiance."},
    "Bioreactor": {"prompt": "bioreactor glow, pulsing biofluorescence, vat illumination", "summary": "Contained bioluminescent reactors bathing spaces in organic light."},
    "Laser Grid": {"prompt": "laser grid, intersecting beams, chromatic lattice", "summary": "Precision laser lattice generating futuristic lighting geometry."},
    "Holographic Dome": {"prompt": "holographic dome canopy, rotating gradients, virtual sky", "summary": "Immersive holographic ceiling diffusing programmable spectrum washes."},
    "Meteor Shower": {"prompt": "meteor shower streaks, incandescent trails, cosmic sparks", "summary": "Sky filled with glowing meteors streaking luminous trails downward."},
    "Flare Burst": {"prompt": "signal flare burst, smoke-tinted glow, emergency wash", "summary": "Emergency flare casting dramatic red light through haze."},
    "Oil Lantern": {"prompt": "oil lantern glow, soot-streaked glass, steady warm pool", "summary": "Portable lantern providing steadfast warm illumination."},
    "Arc Welder": {"prompt": "arc welder flash, intense blue-white, showering sparks", "summary": "Industrial arc welding light freezing motion with harsh brilliance."},
    "Citylight Spill": {"prompt": "distant citylight spill, skyline glow, sodium haze", "summary": "Ambient glow from a distant skyline softly filling the frame."},
    "Crystal Chandelier": {"prompt": "crystal chandelier glitter, prismatic sparkle, ballroom glow", "summary": "Opulent chandelier refracting light into glistening shards."},
    "Bonfire Blaze": {"prompt": "towering bonfire blaze, roaring embers, sparks aloft", "summary": "Massive bonfire engulfing the environment in roaring orange light."},
    "Laneway Neon": {"prompt": "laneway neon strips, saturated signage, puddle reflections", "summary": "Tight alley bathed in stacked neon signage reflections."},
    "Bio-Lanterns": {"prompt": "bio-lantern organisms, glowing fauna, natural luminance", "summary": "Living lantern creatures casting organic multi-toned light."},
    "Ice Cavern Crystals": {"prompt": "ice cavern crystals, refracted glimmer, frozen glow", "summary": "Translucent ice crystals bending light through cavern walls."},
    "Plasma Torches": {"prompt": "plasma torch banks, blue-white arcs, industrial intensity", "summary": "Rows of plasma torches bathing subjects in blistering brilliance."},
    "Sunrise Window": {"prompt": "sunrise window beam, golden shafts, dust motes", "summary": "Early sun cascading through windows with painterly rays."},
    "Projector Spill": {"prompt": "film projector spill, dancing shadows, analog flicker", "summary": "Projector light spilling off screen with nostalgic flicker."},
    "Glimmering Reef": {"prompt": "coral reef glow, phosphorescent marine life, tropical illumination", "summary": "Undersea reef emitting soft gradients from luminous coral."},
    "Supernova Remnant": {"prompt": "supernova remnant glow, cosmic dust, radiant nebula", "summary": "Interstellar residue enveloping scene in vibrant nebular light."},
    "Iridescent Canopy": {"prompt": "iridescent canopy panels, shifting oil-slick colors", "summary": "Architectural canopy reflecting iridescent hues onto subjects."},
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
    "Specular Punch": {"prompt": "specular punch lighting, crisp highlights, lacquered sheen", "summary": "High-specular highlights carving glossy definition across surfaces."},
    "Veiled Diffusion": {"prompt": "veiled diffusion, gauzy wrap, mist-filtered glow", "summary": "Soft veil of diffused light for hazy, dreamlike coverage."},
    "Specular Mosaic": {"prompt": "specular mosaic, shattered highlights, jeweled reflections", "summary": "Fragmented highlights breaking across faceted surfaces."},
    "Feathered Rim": {"prompt": "feathered rim lighting, gradual halo, airy separation", "summary": "Gentle rim light with feathery falloff outlining silhouettes."},
    "Split Tone": {"prompt": "split-toned lighting, opposing color temperatures", "summary": "Two-tone lighting dividing the subject into contrasting hues."},
    "Motivated Practical": {"prompt": "motivated practicals, believable diegetic spill", "summary": "Stylized yet grounded lighting justified by on-set fixtures."},
    "Softbox Wrap": {"prompt": "giant softbox wrap, wrapping highlights, creamy falloff", "summary": "Massive soft source hugging the subject with gentle gradient."},
    "Kicker Highlights": {"prompt": "kicker highlights, sharp accent lines, sculpted edges", "summary": "Edge kickers introducing crisp accent streaks."},
    "High Key": {"prompt": "high-key lighting, airy brightness, minimal shadow", "summary": "Bright, buoyant scheme minimizing contrast for cheerful tone."},
    "Low Key": {"prompt": "low-key lighting, deep blacks, selective highlights", "summary": "Moody low-key envelope with pockets of illumination."},
    "Chromatic Spill": {"prompt": "chromatic spill, rainbow edges, spectral fringe", "summary": "Prismatic spill generating colorful haloing around forms."},
    "Firefly Scatter": {"prompt": "firefly scatter, pinpoint twinkles, drifting motes", "summary": "Micro light points swirling through the air like fireflies."},
    "Soft Focus Glow": {"prompt": "soft focus glow, diffusion bloom, romantic haze", "summary": "Dreamy glow softening detail for romantic imagery."},
    "Mirror Bounce": {"prompt": "mirror bounce lighting, crisp reflection, mirrored key", "summary": "Mirrored bounce producing sharp reflected highlights."},
    "Patterned Gobos": {"prompt": "patterned gobo wash, carved shadows, cut shapes", "summary": "Gobo patterns casting intricate silhouettes across surfaces."},
    "Industrial Strip": {"prompt": "industrial strip lighting, linear highlights, warehouse tone", "summary": "Strip fixtures painting parallel lines of illumination."},
    "Dappled Canopy": {"prompt": "dappled canopy light, leafy pattern, natural stipple", "summary": "Filtered sunlight flickering through foliage onto subjects."},
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
    "Golden Hour": {"prompt": "golden hour light, honeyed tones, elongated shadows", "summary": "Golden hour baths everything in soft amber light."},
    "Storm Night": {"prompt": "stormy midnight, lightning flashes, rain-lashed darkness", "summary": "Charged midnight storm with intermittent lightning wash."},
    "Pre-Dawn Blue": {"prompt": "pre-dawn blue hour, hushed gradients, sleeping city", "summary": "Quiet pre-dawn stillness awash in cool blues."},
    "High Noon": {"prompt": "high noon sun, overhead blaze, sharp shadows", "summary": "Unforgiving midday sun casting stark overhead shadows."},
    "Twilight": {"prompt": "twilight blend, fading warmth, encroaching cool", "summary": "Transitional twilight mixing warm and cool tones."},
    "Solar Eclipse": {"prompt": "solar eclipse dimming, surreal twilight, corona rim", "summary": "Eerie eclipse atmosphere with dramatic ambient shift."},
    "Lunar Eclipse": {"prompt": "lunar eclipse glow, copper moon, penumbral hues", "summary": "Earth-shadowed moon painting night with copper undertones."},
    "Rainy Afternoon": {"prompt": "rainy afternoon light, overcast drizzle, reflective streets", "summary": "Soft grey daylight with shimmering rain reflections."},
    "Winter Dawn": {"prompt": "winter dawn, frosted breath, pale sun", "summary": "Chilly dawn with subdued pastel sunlight."},
    "Summer Midnight": {"prompt": "summer midnight twilight, lingering glow, horizon gradients", "summary": "High-latitude midnight where sun barely dips, leaving glow."},
    "Desert High Sun": {"prompt": "desert high sun, heat shimmer, bleached highlights", "summary": "Scorching desert midday flattening contrast under glare."},
    "Golden Dusk": {"prompt": "deep golden dusk, saturated clouds, elongated shadows", "summary": "Late dusk deepening golds and oranges before nightfall."},
    "Aurora Midnight": {"prompt": "aurora midnight, dancing lights, polar night", "summary": "Polar midnight illuminated by auroral ribbons."},
    "Festival Evening": {"prompt": "festival evening glow, lanterns rising, celebratory warmth", "summary": "Community evening with layered practicals and warm ambiance."},
    "Stormy Noon": {"prompt": "stormy noon, bruise-cloud canopy, diffused fury", "summary": "Midday storm muting sun into dramatic diffuse glow."},
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
    "Extreme Wide": {"prompt": "extreme wide vista, monumental scale, tiny subject silhouette", "summary": "Vast scale framing dwarfs the subject within the environment."},
    "Macro Detail": {"prompt": "macro detail insert, texture emphasis, ultra close focus", "summary": "Macro detail shot isolating tactile surfaces and micro storytelling."},
    "Extreme Macro": {"prompt": "extreme macro, microscopic textures, abstract detail", "summary": "Ultra-magnified shot revealing microscopic textures."},
    "Medium Group": {"prompt": "medium group shot, waist-up ensemble, shared frame", "summary": "Medium framing accommodating multiple subjects in balance."},
    "Environmental Portrait": {"prompt": "environmental portrait, subject within meaningful setting", "summary": "Portrait capturing subject alongside context-rich environment."},
    "Architectural Wide": {"prompt": "architectural wide shot, towering structures, spatial clarity", "summary": "Wide framing highlighting grand architectural scale."},
    "Aerial Panorama": {"prompt": "aerial panorama, sweeping vista, expansive scope", "summary": "High-altitude panorama showcasing sprawling landscapes."},
    "Insert Detail": {"prompt": "insert detail shot, key prop close-up", "summary": "Tight insert isolating a crucial storytelling detail."},
    "Hero Medium": {"prompt": "hero medium shot, waist-up heroic framing", "summary": "Classic hero framing balancing intimacy and stature."},
    "Crowd Master": {"prompt": "crowd master shot, large-scale ensemble, layered depth", "summary": "Wide master capturing energetic crowd dynamics."},
    "Tableau": {"prompt": "tableau shot, staged composition, painterly arrangement", "summary": "Static tableau emphasizing composition and collective pose."},
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
    "Radial Burst": {"prompt": "radial burst composition, converging energy, center highlight", "summary": "Radiating lines pull the eye to a powerful center focal point."},
    "Negative Space": {"prompt": "negative space framing, minimal subject occupancy, breathing room", "summary": "Purposeful negative space emphasizing subject isolation."},
    "Golden Spiral": {"prompt": "golden spiral composition, dynamic curve, natural flow", "summary": "Golden spiral guiding viewer eye along elegant arc."},
    "Framed Within": {"prompt": "framed-within composition, doorway framing, nested focus", "summary": "Subject framed by architectural or natural elements for depth."},
    "Leading Curve": {"prompt": "leading curve composition, sweeping arc, graceful guide", "summary": "Curvilinear leading line drawing attention across frame."},
    "Foreground Obscure": {"prompt": "foreground obscure, partial blockage, voyeur framing", "summary": "Foreground elements partially obscuring action for intrigue."},
    "Layered Depth": {"prompt": "layered depth composition, foreground midground background", "summary": "Stacked planes creating rich depth cues."},
    "Diagonal Drive": {"prompt": "diagonal drive composition, kinetic tilt, motion emphasis", "summary": "Dynamic diagonals introducing energy and momentum."},
    "Central Void": {"prompt": "central void composition, subject encircling emptiness", "summary": "Elements arranged around intentional empty core."},
    "Asymmetrical Balance": {"prompt": "asymmetrical balance, weighted contrast, tension harmony", "summary": "Unequal elements balancing through visual weight."},
    "Mirror Symmetry": {"prompt": "mirror symmetry, reflective imagery, cloned halves", "summary": "Mirrored halves creating duality and repetition."},
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
    "Tilt Shift": {"prompt": "tilt-shift focal plane, selective focus, miniature illusion", "summary": "Tilt-shift lens controlling focus plane for miniature effect."},
    "Anamorphic": {"prompt": "anamorphic lens, cinematic squeeze, oval bokeh", "summary": "Anamorphic lensing for widescreen flare and oval bokeh."},
    "Super Telephoto": {"prompt": "super-telephoto lens, extreme reach, compressed horizon", "summary": "Ultra-long focal length flattening space to dramatic effect."},
    "Portrait Prime": {"prompt": "portrait prime lens, creamy bokeh, flattering compression", "summary": "Classic portrait prime emphasizing subject isolation and bokeh."},
    "Vintage Glass": {"prompt": "vintage lens, subtle aberrations, nostalgic softness", "summary": "Retro lens character introducing romantic imperfection."},
    "Soft Focus Lens": {"prompt": "soft focus lens, haloed highlights, blooming edges", "summary": "Specialty lens diffusing focus for dreamy imagery."},
    "Ultra Macro": {"prompt": "ultra macro lens, life-size magnification, shallow plane", "summary": "Macro lens capturing extreme close detail at 1:1 magnification."},
    "Pinhole": {"prompt": "pinhole optics, infinite focus, vignetted edges", "summary": "Pinhole lens aesthetic offering deep focus and organic vignette."},
    "Shift Lens": {"prompt": "shift lens, perspective control, architectural correction", "summary": "Perspective-control lens keeping verticals true."},
    "Catadioptric": {"prompt": "catadioptric mirror lens, donut bokeh, compact telephoto", "summary": "Mirror telephoto lens creating signature donut-shaped bokeh."},
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
    "Drone Chase": {"prompt": "drone chase angle, high-speed pursuit, aerial tracking", "summary": "Fast-moving drone perspective sweeping through the action."},
    "Shoulder Cam": {"prompt": "over-shoulder handheld cam, intimate proximity, reactive framing", "summary": "Shoulder-mounted camera adding immersive immediacy."},
    "Dutch Low": {"prompt": "low dutch angle, canted horizon near ground", "summary": "Low-positioned dutch angle heightening unease and power."},
    "Head-On": {"prompt": "head-on angle, subject facing camera, direct confrontation", "summary": "Direct frontal angle confronting viewer with subject."},
    "Three-Quarter": {"prompt": "three-quarter angle, slight turn, dimensionality", "summary": "Classic three-quarter angle revealing facial depth."},
    "Worm's Eye": {"prompt": "worm's-eye view, extreme upward gaze, towering scale", "summary": "Extreme low angle exaggerating vertical dominance."},
    "Ceiling Mount": {"prompt": "ceiling mounted camera, surveillance vantage", "summary": "High fixed vantage delivering surveillance aesthetic."},
    "Foot-Level": {"prompt": "foot-level angle, grounded perspective, kinetic motion", "summary": "Camera placed at ground level to emphasize motion and speed."},
    "Mirror POV": {"prompt": "mirror point-of-view, reflective perspective, dual framing", "summary": "Angle captured via mirror reflection for dual-layer storytelling."},
    "Drone Descent": {"prompt": "drone descent angle, rapidly dropping aerial", "summary": "Descending aerial angle transitioning from high to mid altitude."},
    "Shoulder Reverse": {"prompt": "reverse over-shoulder, conversational counter", "summary": "Counter-angle OTS capturing opposing subject in dialogue."},
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
    "Overhead Master": {"prompt": "overhead master shot, architectural layout, orchestrated movement", "summary": "High overhead master framing to chart spatial choreography."},
    "Detail Montage": {"prompt": "detail montage series, rapid inserts, sensory collage", "summary": "Montage of detail shots creating rhythmic storytelling."},
    "Reaction Shot": {"prompt": "reaction shot, emotional response focus", "summary": "Shot capturing character reaction for emotional punctuation."},
    "POV Shot": {"prompt": "point-of-view shot, first-person perspective", "summary": "Subjective POV immersing viewer in character perspective."},
    "Montage Sequence": {"prompt": "montage sequence, time compression, rhythmic cuts", "summary": "Collection of shots compressing time through rhythmic editing."},
    "Tracking Shot": {"prompt": "tracking shot, continuous movement, follow focus", "summary": "Shot moving alongside subject to retain consistent framing."},
    "Dialogue Two Shot": {"prompt": "dialogue two shot, conversational framing", "summary": "Balanced two shot highlighting dialogue between characters."},
    "Extreme Long": {"prompt": "extreme long establishing, distant subjects, landscape emphasis", "summary": "Very wide framing situating characters within vast landscape."},
    "Hero Shot": {"prompt": "hero shot, triumphant pose, low angle emphasis", "summary": "Dramatic hero framing underscoring power and victory."},
    "Insert POV": {"prompt": "insert POV shot, detail through character eyes", "summary": "POV insert focusing on critical detail as character sees it."},
    "Crowd Reaction": {"prompt": "crowd reaction shot, ensemble response", "summary": "Group reaction capturing collective emotional beat."},
}

COLOR_TONE_OPTIONS = {
    "None": {"prompt": "", "summary": "No color tone emphasis."},
    "Warm Tone": {"prompt": "warm color palette, golden hues, inviting saturation", "summary": "Warm palette with golden highlights."},
    "Cool Tone": {"prompt": "cool color palette, blue undertones, serene mood", "summary": "Cool palette with calming tones."},
    "High Saturation": {"prompt": "high saturation, vivid colors, bold intensity", "summary": "Highly saturated color treatment."},
    "Low Saturation": {"prompt": "low saturation, muted palette, cinematic restraint", "summary": "Muted palette with cinematic restraint."},
    "Pastel Tone": {"prompt": "pastel color palette, powdery hues, gentle saturation", "summary": "Soft pastel wash for dreamy, delicate moods."},
    "Neo Noir": {"prompt": "neo-noir palette, electric highlights, deep shadows", "summary": "High-contrast neon noir treatment with moody blacks."},
    "Bioluminescent": {"prompt": "bioluminescent palette, teal-magenta glow, organic luminance", "summary": "Bioluminescent-inspired palette with glowing cool hues."},
    "Sepia Film": {"prompt": "sepia-toned film wash, vintage warmth, gentle fade", "summary": "Vintage sepia palette with analog softness."},
    "Teal & Orange": {"prompt": "teal and orange palette, cinematic contrast, blockbuster grade", "summary": "High-contrast teal/orange pairing for cinematic punch."},
    "Muted Pastel": {"prompt": "muted pastel tones, powdery softness, delicate wash", "summary": "Soft pastel palette dialed down for subtle refinement."},
    "Monochrome Steel": {"prompt": "monochrome steel palette, cool grays, industrial vibe", "summary": "Steely monochrome emphasizing industrial mood."},
    "Iridescent": {"prompt": "iridescent color play, oil-slick spectrum, shifting hues", "summary": "Shimmering palette shifting colors with angle."},
    "Sun-Bleached": {"prompt": "sun-bleached palette, desaturated warmth, desert fade", "summary": "Faded warm palette recalling sun-weathered surfaces."},
    "Candy Pop": {"prompt": "candy pop palette, sugary brights, high-gloss saturation", "summary": "Playful high-saturation palette reminiscent of candy wrappers."},
    "Neon Pulse": {"prompt": "neon pulse palette, electric magentas, cyan highlights", "summary": "Glowing neon palette pulsing with nightlife energy."},
    "Mocha": {"prompt": "mocha palette, creamy browns, cozy latte warmth", "summary": "Comforting brown palette echoing café tones."},
    "Frosted Glass": {"prompt": "frosted glass palette, opaque pastels, milky diffusion", "summary": "Milky translucent palette softening contrast with frost-like hues."},
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
    "Parkour": {"prompt": "urban parkour vault, wall run, kinetic agility", "summary": "Parkour motion exploding across rooftops and railings."},
    "Aerial Silk": {"prompt": "aerial silk routine, suspended twirl, fluid acrobatics", "summary": "Aerial silks performance capturing graceful aerial control."},
    "Park Skating": {"prompt": "park skating session, grinding rails, flowing lines", "summary": "Skatepark action blending tricks with fluid movement."},
    "Martial Kata": {"prompt": "martial arts kata, precise forms, disciplined strikes", "summary": "Structured martial sequence emphasizing precision and flow."},
    "Ballet Leap": {"prompt": "grand jeté ballet leap, extended lines, airborne grace", "summary": "Classical ballet leap freezing dancer mid-flight."},
    "Free Diving": {"prompt": "free diving descent, streamlined motion, underwater calm", "summary": "Graceful underwater descent captured mid glide."},
    "Breakdance Spin": {"prompt": "breakdance windmill spin, kinetic sweep, dynamic floorwork", "summary": "Explosive breakdance spin radiating urban energy."},
    "Hoverboard Drift": {"prompt": "hoverboard drift, antigrav carve, futuristic glide", "summary": "Futuristic hoverboard carving arcs through the air."},
    "Park Parade": {"prompt": "parade procession, synchronized steps, celebratory rhythm", "summary": "Processional parade motion with coordinated ensemble."},
    "Sword Duel": {"prompt": "sword duel clash, steel arcs, poised footwork", "summary": "Dramatic swordplay with dynamic lunges and parries."},
    "Mountain Climb": {"prompt": "mountain climb ascent, rope work, vertical challenge", "summary": "Climber scaling sheer rock with dynamic upward movement."},
    "Surf Cutback": {"prompt": "surf cutback maneuver, spray arc, fluid carve", "summary": "Surfer executing stylish cutback with water spray."},
    "Aerial Drone": {"prompt": "drone maneuver, looping flight, agile hover", "summary": "Agile drone weaving loops through obstacles."},
    "Samba Dance": {"prompt": "samba dance rhythm, fast footwork, carnival flair", "summary": "Energetic samba steps pulsing with festive rhythm."},
    "Sprinting Relay": {"prompt": "relay sprint handoff, baton exchange, explosive acceleration", "summary": "Team relay sprint capturing baton handoff intensity."},
}

ACTION_PRIMARY_OPTIONS = {
    "None": {"prompt": "", "summary": "No primary action emphasis."},
    "Heroic Sprint": {"prompt": "explosive sprint, knees driving high, purposeful forward lean", "summary": "Powerful sprinting burst projecting urgency and determination."},
    "Focused Jog": {"prompt": "steady jog, rhythmic breathing, relaxed arm swing", "summary": "Measured jogging pace emphasizing stamina and calm focus."},
    "Casual Walk": {"prompt": "casual walk, easy stride, observant gaze", "summary": "Unhurried walking pace conveying confidence and ease."},
    "Power Stride": {"prompt": "power stride, decisive footfalls, shoulders squared", "summary": "Intentional march underscoring leadership and resolve."},
    "Parade March": {"prompt": "synchronized march, precision cadence, ceremonial posture", "summary": "Disciplined marching cadence suited for procession beats."},
    "Tactical Creep": {"prompt": "controlled prowl, low center of gravity, silent footsteps", "summary": "Slow stealth advance ideal for infiltration storytelling."},
    "Graceful Turn": {"prompt": "graceful pivot, fluid hip rotation, balanced poise", "summary": "Elegant pirouette moment showcasing refined control."},
    "Combat Roll": {"prompt": "combat roll, momentum carry, swift recovery stance", "summary": "Dynamic evasive roll leading into combat readiness."},
    "Acrobatic Flip": {"prompt": "tight aerial flip, tucked knees, precise landing", "summary": "Athletic flip highlighting agility and aerial confidence."},
    "Vault Leap": {"prompt": "vault leap over obstacle, palms planted, legs split", "summary": "Momentum-driven vault clearing barriers with flair."},
    "Wall Run": {"prompt": "wall run, angled sprint, defying gravity", "summary": "Parkour-inspired wall run accentuating daring motion."},
    "Ledge Climb": {"prompt": "vertical climb, fingertips gripping, core engaged", "summary": "Determined ascent capturing grit and physical strength."},
    "Grapple Swing": {"prompt": "grappling swing, cable taut, arc through air", "summary": "Swinging traversal showcasing momentum and heroics."},
    "Hover Drift": {"prompt": "hoverboard drift, counter lean, plasma trail", "summary": "Futuristic glide sequences with dramatic banking."},
    "Aerial Hover": {"prompt": "suspended hover, subtle limb adjustments, anti-grav hum", "summary": "Weightless hover emphasizing controlled stillness."},
    "Sword Combo": {"prompt": "sword combo slash, blade flare, precise follow-through", "summary": "Martial sword sequence brimming with kinetic intent."},
    "Shield Brace": {"prompt": "shield brace, wide stance, impact-ready", "summary": "Protective stance built for blocking heavy blows."},
    "Bow Release": {"prompt": "drawn bow release, focused gaze, taut string snap", "summary": "Archery moment capturing tension and accuracy."},
    "Spell Channel": {"prompt": "channeling spell energy, sigils orbiting, outstretched palm", "summary": "Arcane casting posture radiating cinematic power."},
    "Healing Surge": {"prompt": "healing surge, warm aura, hands hovering over ally", "summary": "Supportive restorative action showcasing compassion."},
    "Tech Interface": {"prompt": "rapid console interface, holographic projections, swift keystrokes", "summary": "High-speed tech interaction driven by intellect."},
    "Drone Pilot": {"prompt": "remote drone coordination, dual sticks, analytical focus", "summary": "Precision drone piloting highlighting dexterity."},
    "Vehicle Drift": {"prompt": "vehicle drift, counter steering, tire smoke curl", "summary": "High-octane driving beat with cinematic drift."},
    "Mech Command": {"prompt": "mech command gestures, haptic controls, cockpit glow", "summary": "Piloting a giant mech with commanding gestures."},
    "Gun Kata": {"prompt": "gun kata flow, synchronized dual pistols, spinning disarm", "summary": "Stylized firearm choreography blending combat and dance."},
    "Cover Slide": {"prompt": "slide into cover, sparks skimming, low ready", "summary": "Tactical slide maneuver transitioning into cover."},
    "Reload Snap": {"prompt": "speed reload snap, magazine swap, decisive click", "summary": "Swift weapon reload underscoring discipline."},
    "Data Hack": {"prompt": "neural hack posture, luminous code stream, intense focus", "summary": "Cyber intrusion beat with immersive hacking visuals."},
    "Creative Sketch": {"prompt": "rapid sketch strokes, charcoal dust, concentrated expression", "summary": "Artistic gesture capturing creativity in motion."},
    "Brush Flourish": {"prompt": "brush flourish across canvas, pigment spray, painterly arc", "summary": "Expressive painting movement bursting with color."},
    "Sculpting Strike": {"prompt": "sculpting chisel strike, stone shards, deliberate rhythm", "summary": "Sculptural carving moment emphasizing craftsmanship."},
    "Conducting Cue": {"prompt": "orchestral conducting cue, baton sweep, poised crescendo", "summary": "Commanding conducting gesture driving musical energy."},
    "Freestyle Dance": {"prompt": "freestyle dance burst, syncopated limbs, playful sync", "summary": "Improvisational dance packed with personality."},
    "Contemporary Flow": {"prompt": "contemporary dance flow, sweeping floor contact, expressive torso", "summary": "Fluid dance sequence mixing control and emotion."},
    "Martial Spar": {"prompt": "martial spar exchange, block and counter, sharpened reflexes", "summary": "Friendly sparring beat balancing offense and defense."},
    "Meditative Breath": {"prompt": "meditative breath cycle, grounded stance, centered palms", "summary": "Stillness-focused breathwork radiating calm strength."},
    "Negotiation Gesture": {"prompt": "open negotiation gesture, hands extended, emphatic cadence", "summary": "Persuasive communication action highlighting diplomacy."},
    "Briefing Command": {"prompt": "mission briefing command stance, holo-map gesture, directive tone", "summary": "Mission leadership beat rallying the team."},
    "Victory Cheer": {"prompt": "victory cheer, arms raised, triumphant shout", "summary": "Celebratory climax conveying success and joy."},
    "Reassuring Embrace": {"prompt": "reassuring embrace, protective posture, supportive warmth", "summary": "Supportive hug emphasizing trust and care."},
    "Rescue Carry": {"prompt": "fireman carry rescue, urgent pace, determined grit", "summary": "Heroic rescue action grounded in strength and urgency."},
    "Scientific Scan": {"prompt": "handheld scanner sweep, sensor readouts, analytical calm", "summary": "Investigative scanning beat revealing discoveries."},
}

ACTION_SECONDARY_OPTIONS = {
    "None": {"prompt": "", "summary": "No secondary beat."},
    "Evasive Sidestep": {"prompt": "evasive sidestep, dust kick, narrow escape", "summary": "Quick lateral dodge threading through danger."},
    "Counter Strike": {"prompt": "counter strike, sudden riposte, momentum reversal", "summary": "Instant retaliation that flips the battlefield tempo."},
    "Guard Break": {"prompt": "guard break shove, stance disruption, advantage claimed", "summary": "Aggressive shove opening defense lines."},
    "Precision Aim": {"prompt": "precision aim, steady breath hold, laser focus", "summary": "Focused targeting moment capturing suspense."},
    "Scan Sweep": {"prompt": "environmental scan sweep, HUD overlay, alerts ping", "summary": "Data-gathering sweep amplifying situational awareness."},
    "Signal Call": {"prompt": "hand signal callout, coordinated motion, squad synch", "summary": "Silent coordination cue enhancing teamwork."},
    "Shield Raise": {"prompt": "shield raise, sparks deflected, resilience flare", "summary": "Defensive beat underlining protection."},
    "Momentum Slide": {"prompt": "momentum slide, low friction drift, sparks trailing", "summary": "Stylized slide maintaining kinetic energy."},
    "Ground Pound": {"prompt": "ground pound impact, shockwave ring, dust burst", "summary": "Impactful finishing beat showcasing raw force."},
    "Air Twist": {"prompt": "aerial twist kick, suspended rotation, dramatic follow-through", "summary": "Signature kick sequence loaded with flair."},
    "Grapple Lock": {"prompt": "grapple lock, leverage shift, controlled takedown", "summary": "Submission-oriented maneuver demonstrating technique."},
    "Companion Assist": {"prompt": "companion assist boost, interlocked hands, cooperative lift", "summary": "Supportive teammate beat accentuating trust."},
    "Barrier Deploy": {"prompt": "deployable barrier throw, emitter unfold, cover established", "summary": "Instant cover creation for tactical repositioning."},
    "Drone Launch": {"prompt": "drone launch flick, rotor ignition, rapid ascent", "summary": "Secondary action launching support drone units."},
    "Med-Pack Toss": {"prompt": "med-pack toss, side-arm throw, lifesaving delivery", "summary": "Supportive aid thrown to allies mid-conflict."},
    "Energy Burst": {"prompt": "energy burst discharge, luminous surge, crackling aftermath", "summary": "Secondary flare of power emphasizing impact."},
    "Telemetry Check": {"prompt": "telemetry check, wrist holo, data validation", "summary": "Brief systems check ensuring mission alignment."},
    "Environmental Interaction": {"prompt": "interactive environment cue, trigger pull, machinery response", "summary": "Action tied to world mechanics and set pieces."},
    "Emotional Accent": {"prompt": "emotional accent glance, micro-expression, character depth", "summary": "Subtle emotional beat layered into action."},
}

ACTION_TEMPO_OPTIONS = {
    "None": {"prompt": "", "summary": "Neutral tempo."},
    "Slow And Steady": {"prompt": "slow and steady tempo, measured steps, deliberate pace", "summary": "Calm, controlled tempo emphasizing precision."},
    "Erotic Pulse": {"prompt": "erotic pulse tempo, sultry sway, rhythmic hips", "summary": "Sensual tempo emphasizing allure and intimacy."},
    "Erotic Flow": {"prompt": "erotic flow tempo, fluid transitions, languid movement", "summary": "Smooth, flowing tempo highlighting sensuality."},
    "Slow Burn": {"prompt": "slow burn cadence, deliberate pacing, controlled breath", "summary": "Measured tempo suited for stealth or tension building."},
    "Rising Momentum": {"prompt": "rising momentum, energy ramp, quickening steps", "summary": "Tempo increase signaling imminent breakthrough."},
    "Pulse Pounding": {"prompt": "pulse-pounding rhythm, heartbeat percussion, kinetic urgency", "summary": "High-tempo drive keeping adrenaline elevated."},
    "Frantic Rush": {"prompt": "frantic rush, untamed velocity, scattered sparks", "summary": "Chaotic tempo perfect for chase sequences."},
    "Steady Cadence": {"prompt": "steady cadence, balanced breathing, tactical precision", "summary": "Even tempo highlighting discipline and stamina."},
    "Staccato Beats": {"prompt": "staccato beats, rapid-fire cuts, short bursts of motion", "summary": "Choppy tempo ideal for montage or combat edits."},
    "Weightless Drift": {"prompt": "weightless drift tempo, slow-floating beats, elongated frames", "summary": "Dreamlike tempo emphasizing suspended motion."},
    "Heroic Crescendo": {"prompt": "heroic crescendo, swelling momentum, triumphant surge", "summary": "Epic tempo climb culminating in a victorious beat."},
    "Sneaking Pulse": {"prompt": "sneaking pulse, low heart rate, suppressed motion", "summary": "Subtle tempo maintaining stealth tension."},
}

ACTION_INTERACTION_OPTIONS = {
    "None": {"prompt": "", "summary": "Solo focus."},
    "Flirty Bounce": {"prompt": "flirty bounce, playful winks, teasing smiles", "summary": "Lighthearted interaction with a playful edge."},
    "Solo Focus": {"prompt": "solo-focused action, spotlight isolated performer", "summary": "Highlights individual capability without distractions."},
    "Duo Synchrony": {"prompt": "duo synchrony, mirrored movements, interlocking timing", "summary": "Two-person coordination conveying trust and chemistry."},
    "Squad Coordination": {"prompt": "squad coordination, layered formation, call-and-response", "summary": "Team-based action balanced across multiple performers."},
    "Crowd Navigation": {"prompt": "crowd navigation, weaving through onlookers, reactive adjustments", "summary": "Action threaded through dense crowd dynamics."},
    "Rival Showdown": {"prompt": "rival showdown, charged eye-line, matched intensity", "summary": "Dramatic confrontation between evenly matched opponents."},
    "Mentor Guidance": {"prompt": "mentor guidance, supportive coaching, corrective touch", "summary": "Instructional beat where mentor refines protege technique."},
    "Rescue Support": {"prompt": "rescue support, stabilizing assist, collaborative lift", "summary": "Mutual aid moment during high-stakes scenario."},
    "Celebration Group": {"prompt": "celebration group embrace, shared triumph, collective cheer", "summary": "Group celebration amplifying emotional payoff."},
    "Spectator Engagement": {"prompt": "spectator engagement, audience interaction, responsive energy", "summary": "Performer interacting directly with enthusiastic crowd."},
    "Tactical Tandem": {"prompt": "tactical tandem, overlapping cover fire, seamless transitions", "summary": "Combat partnership moving as a unified unit."},
}

NSFW_ACTION_PRIMARY_OPTIONS = {
    "None": {"prompt": "", "summary": "No specific mature action emphasis."},
    "sensual_fingering": {"prompt": "sensual_fingering, teasing touch, deliberate pace", "summary": "Slow, teasing finger play emphasizing sensation."},
    "dildoplay": {"prompt": "dildoplay, rhythmic thrusts, focused attention", "summary": "Intentional dildo use highlighting control and pleasure."},
    "dildo plunge": {"prompt": "dildo plunge, deep thrusts, intense focus", "summary": "Deep, purposeful dildo penetration emphasizing intensity."},
    "striptease": {"prompt": "striptease, slow fabric removal, teasing reveal", "summary": "Flirtatious undressing emphasizing anticipation."},
    "Lap Dance On A Pillow": {"prompt": "lap dance on a pillow, sultry grind, intimate proximity", "summary": "Sensual lap dance focusing on close contact."},
    "nipple_play": {"prompt": "nipple play, gentle pinches, teasing twists", "summary": "Delicate nipple stimulation enhancing arousal."},
    "breast_play": {"prompt": "breast play, cupping hands, soft squeezes", "summary": "Tender breast handling emphasizing pleasure."},
    "butt_play": {"prompt": "butt play, firm grabs, playful spanks", "summary": "Cheeky butt interaction blending fun and sensation."},
    "thigh_play": {"prompt": "thigh play, light strokes, teasing caress", "summary": "Sensual thigh touch building anticipation."},
    "intimate_kiss": {"prompt": "intimate kiss, parted lips, lingering tongue", "summary": "Deep, passionate kissing emphasizing connection."},
    "deep_throat": {"prompt": "deep throat, wide gape, focused eye contact", "summary": "Intense oral engagement highlighting depth and control."},
    "oral_tease": {"prompt": "oral tease, soft licks, anticipatory nibbles", "summary": "Playful oral teasing building anticipation."},
    "intimate_dance": {"prompt": "intimate_dance, close body contact, rhythmic sway", "summary": "Close-contact dance highlighting mutual attraction."},
    "tease_undress": {"prompt": "tease undress, fabric slide, playful reveal", "summary": "Flirtatious wardrobe removal emphasizing anticipation."},
    "Sensual Caress": {"prompt": "sensual caress, fingertips tracing curves, lingering warmth", "summary": "Tender caress lingering over consenting adult partner."},
    "Slow Undress": {"prompt": "slow undress, deliberate fabric slide, teasing reveal", "summary": "Gradual wardrobe peel emphasizing anticipation."},
    "Passionate Embrace": {"prompt": "passionate embrace, bodies pressed, breath mingling", "summary": "Full-body embrace radiating mutual desire."},
    "Intimate Sway": {"prompt": "intimate sway, hips aligned, subtle grind", "summary": "Synchronized sway capturing shared rhythm."},
    "Seductive Strut": {"prompt": "seductive strut, confident hips, smoldering gaze", "summary": "Confident walk engineered to entice."},
    "Sultry Floorwork": {"prompt": "sultry floorwork, rolling shoulders, arched back", "summary": "Floor routine showcasing curves and fluid control."},
    "Chair Tease": {"prompt": "chair straddle tease, playful lean back, fingertip glide", "summary": "Chair-focused routine blending tease and control."},
    "Lap Dance Flourish": {"prompt": "lap dance flourish, measured grind, eye contact", "summary": "Exploratory lap dance centered on consent and connection."},
    "Wall Pin": {"prompt": "pinned to wall, dominant arm brace, electric tension", "summary": "Consensual wall pin layering controlled dominance."},
    "Silk Rope Display": {"prompt": "silk rope display, decorative binds, supportive suspension", "summary": "Artful rope styling highlighting trust and safety."},
    "Blindfold Reveal": {"prompt": "blindfold reveal, silk slip, heightened senses", "summary": "Playful sensory deprivation moment building anticipation."},
    "Oil Massage": {"prompt": "warm oil massage, glistening skin, affectionate knead", "summary": "Sensual massage exchanging comfort and pleasure."},
    "Body Trace": {"prompt": "body tracing, nails grazing, deliberate pace", "summary": "Slow tracing that savors every contour thoughtfully."},
    "Corset Tighten": {"prompt": "corset tightening, breathy gasp, mirrored gaze", "summary": "Intimate wardrobe cinch celebrating curves."},
    "Stocking Roll": {"prompt": "stocking roll, thigh-high descent, playful smirk", "summary": "Tempting hosiery peel that spotlights legs."},
    "Garter Snap": {"prompt": "garter snap tease, playful sting, laughing eyes", "summary": "Cheeky garter snap punctuating flirtatious energy."},
    "Mirror Worship": {"prompt": "mirror worship pose, self-admiring touch, glossy lighting", "summary": "Self-love moment honoring adult confidence."},
    "Bath Embrace": {"prompt": "shared bubble bath embrace, water shimmer, relaxed smiles", "summary": "Steamy bath cuddle under soft candlelight."},
    "Dominant Command": {"prompt": "dominant command stance, guiding touch, steady gaze", "summary": "Command-driven beat emphasizing trusted leadership."},
    "Submissive Offer": {"prompt": "submissive offer, kneeling poise, open palms", "summary": "Reverent offering posture celebrating mutual trust."},
    "Morning Glow": {"prompt": "morning-after glow, sheet drape, satisfied stretch", "summary": "Post-intimacy glow capturing tenderness and safety."},
    "rope_bondage": {"prompt": "rope_bondage, intricate knots, secure ties", "summary": "Artful rope bondage emphasizing safety and aesthetics."},
    "Feather Tease": {"prompt": "feather tease, light strokes, playful shivers", "summary": "Delicate feather touch eliciting gentle reactions."},
    "Ice Play": {"prompt": "ice play, cool glide, sharp contrast", "summary": "Icy touch introducing thrilling temperature play."},
    "Candle Drip": {"prompt": "candle wax drip, slow melt, heated skin", "summary": "Sensual wax play balancing warmth and sensation."},
    "Spanking": {"prompt": "spanking rhythm, open palm, playful smirk", "summary": "Consensual spanking beat blending fun and sensation."},
    "Hair Pull": {"prompt": "hair pull tease, gentle tug, sultry glance", "summary": "Controlled hair pull enhancing connection."},
    "Collar Clasp": {"prompt": "collar clasp, firm grip, submissive tilt", "summary": "Symbolic collaring moment underscoring roles."},
    "Cuffs Click": {"prompt": "cuffs click, wrist restraint, daring smile", "summary": "Playful cuffing action highlighting consensual restraint."},

}

NSFW_ACTION_SECONDARY_OPTIONS = {
    "None": {"prompt": "", "summary": "No secondary mature beat."},
    "Touch Genitals": {"prompt": "touching genitals, teasing caress, deliberate pace", "summary": "Focused genital touch emphasizing sensation."},
    "dildoplay": {"prompt": "dildoplay, rhythmic thrusts, focused attention", "summary": "Intentional dildo use highlighting control and pleasure."},
    "dildo plunge": {"prompt": "dildo plunge, deep thrusts, intense focus", "summary": "Deep, purposeful dildo penetration emphasizing intensity."},
    "Body Grind": {"prompt": "body grind, close contact, rhythmic hips", "summary": "Full-body grind highlighting mutual attraction."},
    "Lip Bite": {"prompt": "soft lip bite, playful tension, smoldering glance", "summary": "Subtle lip bite amplifying chemistry."},
    "Neck Kiss": {"prompt": "neck kiss, lingering breath, gentle tilt", "summary": "Neck kiss moment underscoring intimacy."},
    "Ear Whisper": {"prompt": "ear whisper tease, warm breath, secretive smile", "summary": "Close whisper sharing private promises."},
    "Hair Sweep": {"prompt": "hair sweep aside, revealing collarbone, seductive focus", "summary": "Hair sweep opening the frame to more skin."},
    "Finger Trail": {"prompt": "fingertip trail along spine, shiver ripple", "summary": "Slow finger trail sending shivers down the spine."},
    "Ribbon Tug": {"prompt": "ribbon tug release, fluttering fabric, playful gasp", "summary": "Ribbon pull unlocking the next reveal."},
    "Stocking Adjust": {"prompt": "stocking adjustment, deliberate roll, thigh emphasis", "summary": "Adjusting stockings to heighten leg focus."},
    "Gaze Hold": {"prompt": "gaze lock, dilated pupils, whispered invitation", "summary": "Mutual gaze hold that communicates consent clearly."},
    "Hand Restraint": {"prompt": "gentle wrist restraint, supportive grip, caring check-in", "summary": "Soft restraint paired with constant reassurance."},
    "Body Dip": {"prompt": "dramatic body dip, partner support, arched torso", "summary": "Supported dip highlighting trust and strength."},
    "Hip Grind": {"prompt": "hip grind accent, rolling motion, synchronized breath", "summary": "Rhythmic hip grind deepening sensual flow."},
    "Glove Peel": {"prompt": "glove peel, fingertip tease, slow reveal", "summary": "Slow glove peel coaxing attention to touch."},
    "Perfume Mist": {"prompt": "perfume mist spray, lingering scent, coy smile", "summary": "Scented flourish prepping for closeness."},
    "Velvet Stroke": {"prompt": "velvet glove stroke along torso, indulgent pace", "summary": "Soft fabric glide delighting sensitive skin."},
    "Silk Caress": {"prompt": "silk scarf caress, fluid motion, teasing glide", "summary": "Silk touch enhancing tactile sensation."},
    "Body Arch": {"prompt": "body arch, extended lines, breathy moan", "summary": "Full-body arch emphasizing curves and openness."},
    "Thigh Squeeze": {"prompt": "thigh squeeze, firm grip, shared smile", "summary": "Mutual thigh squeeze reinforcing connection."},
    "Knee Spread": {"prompt": "knee spread, grounded base, inviting posture", "summary": "Open knee stance signaling readiness and consent."},
    "Ankle Tie": {"prompt": "ankle tie, secure knot, supportive stance", "summary": "Ankle bondage emphasizing safety and trust."},
    "Body Slide": {"prompt": "body slide, close contact, synchronized rhythm", "summary": "Full-body slide enhancing shared motion."},
    "Teasing Flick": {"prompt": "teasing flick with feather, light touch, playful grin", "summary": "Feather flick eliciting light, pleasurable reactions."},
    "Ice Trace": {"prompt": "ice cube trace along skin, cool contrast, shiver response", "summary": "Icy glide creating thrilling temperature shifts."},
    "Wax Drip": {"prompt": "candle wax drip, slow melt, heated skin", "summary": "Sensual wax drop balancing warmth and sensation."},

}

NSFW_ACTION_TEMPO_OPTIONS = {
    "None": {"prompt": "", "summary": "Neutral tempo for mature scene."},
    "orgasmic_rush": {"prompt": "orgasmic rush tempo, escalating pace, breathless energy", "summary": "Rapid tempo capturing peak intensity."},
    "teasing_tempo": {"prompt": "teasing tempo, slow build, tantalizing rhythm", "summary": "Slow, tantalizing tempo emphasizing anticipation."},

    "Slow Tease": {"prompt": "slow tease tempo, patient pacing, suspended breath", "summary": "Lingering tempo that savors every second."},
    "Languid Flow": {"prompt": "languid flow, fluid transitions, mellow rhythm", "summary": "Relaxed cadence for indulgent sequences."},
    "Measured Build": {"prompt": "measured build, rising heat, controlled escalation", "summary": "Gradual crescendo balancing excitement."},
    "Playful Bounce": {"prompt": "playful bounce, upbeat flirtation, lively pace", "summary": "Light-hearted tempo packed with charm."},
    "Breathless Waves": {"prompt": "breathless wave tempo, rising and crashing energy", "summary": "Repeating waves of intensity and release."},
    "Urgent Clutch": {"prompt": "urgent clutch tempo, hungry pace, desperate energy", "summary": "Fast pace fueled by mutual craving."},
    "Commanded Pace": {"prompt": "commanded pace, deliberate cues, guided rhythm", "summary": "Dominant partner dictating tempo with care."},
    "Hypnotic Loop": {"prompt": "hypnotic loop, repeating pattern, trance-like focus", "summary": "Repetitive motions that mesmerize audience."},
    "Tender Pause": {"prompt": "tender pause beats, held breaths, eye contact linger", "summary": "Strategic pauses that celebrate connection."},
}

CAMZ_PERSONA_OPTIONS = {
    "Soft Glam Muse": {
        "prompt": "soft glam cam performer, luminous skin, encouraging smile, relaxed confidence",
        "notes": "Lean into approachable warmth blended with polished glam cues.",
    },
    "Edgy Vixen": {
        "prompt": "edgy cam vixen, smoky eye makeup, bold lip, provocative poses",
        "notes": "Combine high-contrast lighting with daring wardrobe for impact.",
    },
    "Boho Dreamer": {
        "prompt": "boho cam enchantress, natural makeup, flowing fabrics, earthy tones",
        "notes": "Use soft, diffused light and organic textures to enhance free-spirit vibe.",
    },
    "Nude Preformer": {
        "prompt": "nude cam performer, confident posture, direct eye contact, natural beauty",
        "notes": "Highlight skin tones with warm lighting and minimal distractions.",
    },

    "Nude Lingerie": {
        "prompt": "nude lingerie cam performer, delicate lace, soft lighting, inviting expression",
        "notes": "Blend sensual fabrics with flattering light to enhance allure.",
    },

    "Legs Up": {
        "prompt": "legs up position, open posture, inviting gaze",
        "notes": "Emphasize vulnerability and openness with body language.",
    },  

    "Genital Focus": {
        "prompt": "genital focus, explicit detail, intimate angle",
        "notes": "Use close-up framing and sharp focus to highlight anatomy.",
    },

    "Knee Spread": {
        "prompt": "knee spread position, open posture, inviting gaze",
        "notes": "Emphasize vulnerability and openness with body language.",
    },


    "Gamer Girl": {
        "prompt": "gamer girl cam performer, playful expressions, gaming gear, vibrant colors",
        "notes": "Incorporate RGB lighting and interactive overlays for dynamic energy.",
    },
    
    "Cyber Starlet": {
        "prompt": "futuristic cyber cam muse, neon accent liner, playful tech accessories",
        "notes": "Pair shimmering highlights with synth-forward ambience for modern edge.",
    },
    "Fitness Tease": {
        "prompt": "athletic cam goddess, toned silhouette, playful flex moments",
        "notes": "Incorporate light workout props and confident body language cues.",
    },
    "Sultry Jazz": {
        "prompt": "jazz lounge cam siren, velvety voice, deliberate slow gestures",
        "notes": "Match low tempo jazz soundtrack with honeyed lighting for intimacy.",
    },

    "Classic Burlesque": {
        "prompt": "classic burlesque cam performer, vintage glamour, theatrical poses",
        "notes": "Use spotlighting and rich textures to evoke old-school allure.",
    },
}

CAMZ_STAGE_OPTIONS = {
    "Neon Loft": {
        "prompt": "neon loft backdrop, led strip accents, reflective plexi floor",
        "notes": "Balance saturated highlights with soft fill to flatter skin.",
    },
    "Velvet Boudoir": {
        "prompt": "crimson velvet boudoir set, fairy lights, plush textures",
        "notes": "Layer candles and warm bulbs to deepen romantic ambience.",
    },
    "Glow Studio": {
        "prompt": "glow studio backdrop, gradient colorwash, cloud diffuser panels",
        "notes": "Use color cycling and haze for dreamy, stylized streaming look.",
    },
    "Gamer Den": {
        "prompt": "rgb gamer desk, holographic screens, soft plush seating",
        "notes": "Mix animated overlays with keyboard glow for interactive energy.",
    },
    "Minimalist Chic": {
        "prompt": "minimalist chic set, clean lines, monochrome palette",
        "notes": "Emphasize simplicity and elegance with strategic lighting."
    },
    "Bedroom Retreat": {
        "prompt": "cozy bedroom retreat, soft linens, ambient string lights",
        "notes": "Create a warm, inviting atmosphere with layered textiles and soft lighting.",
    },
    "Outdoor Oasis": {
        "prompt": "lush outdoor oasis, tropical plants, twinkling fairy lights",
        "notes": "Create a serene, nature-inspired backdrop with soft, diffused lighting.",
    },
    "Regular Bedroom": {
        "prompt": "regular bedroom setting, casual decor, natural lighting",
        "notes": "Incorporate personal touches and soft lighting for a lived-in feel.",
    },
    "messy_bedroom": {
        "prompt": "messy bedroom setting, casual decor, natural lighting",
        "notes": "Capture the lived-in feel with unmade beds and personal items.",
    },
    "Gamer Bedroom": {
        "prompt": "gamer bedroom setup, gaming posters, rgb lighting",
        "notes": "Incorporate dynamic lighting and gaming elements for an immersive vibe.",
    },
}


CAMZ_CAMERA_OPTIONS = {
    "Intimate Close": {
        "prompt": "intimate close framing, direct lens eye contact, creamy bokeh",
        "notes": "Keep lens near eye level for immediate connection and sparkle.",
    },
    "Desk Peek": {
        "prompt": "desk peek composition, slightly elevated perspective, flattering angle",
        "notes": "Angle camera from high-left to emphasize eyes and decolletage.",
    },
    "Overhead View": {
        "prompt": "overhead cam angle, top-down view, dynamic foreshortening",
        "notes": "Use wide lens to capture full figure and engaging perspective.",
    },
    "Shoulder Cam": {
        "prompt": "shoulder cam angle, partial profile, soft focus",
        "notes": "Create a dreamy, intimate vibe with gentle focus and framing.",
    },
    "Full Body": {
        "prompt": "full body cam frame, full-length mirror, responsive lighting",
        "notes": "Stage lighting evenly to avoid clipping during motion demos.",
    },
    "Dynamic Dolly": {
        "prompt": "slow dolly glide, remote gimbal, smooth parallax",
        "notes": "Automate subtle motion to keep stream kinetic without distraction.",
    },
}

CAMZ_ENERGY_OPTIONS = {

    "Sexy Bounce": {
        "prompt": "sexy bounce, rhythmic hip sway, playful smiles",
        "notes": "Incorporate playful expressions and dynamic angles for added allure.",
    },

    "Gentle Sway": {
        "prompt": "gentle swaying motion, soft giggles, tender pacing",
        "notes": "Use lingering gestures and ASMR whisper tones for relaxation.",
    },
    "Flirty Bounce": {
        "prompt": "flirty bounce, playful winks, teasing smiles",
        "notes": "Incorporate light, rhythmic music and interactive chat games.",
    },
    "Grind Groove": {
        "prompt": "sensual grind, rhythmic hip sway, sultry eye contact",
        "notes": "Sync movements to mid-tempo beats for hypnotic allure.",
    },
    "To The Music": {
        "prompt": "music-driven moves, beat sync, expressive dance, energetic vibe, hips move to the beat",
        "notes": "Encourage spontaneous movement and playful interaction with the rhythm.",
    },  
    "Hype Spark": {
        "prompt": "high-energy bounce, playful chatter, animated laughter",
        "notes": "Cue upbeat playlists and interactive games for tip spikes.",
    },
    "Slow Burn": {
        "prompt": "slow-burn tease, deliberate pauses, smoldering eye contact",
        "notes": "Layer progressive reveals with countdown widgets for tension.",
    },
    "Command Mode": {
        "prompt": "commanding domme cadence, confident directives, teasing coaching",
        "notes": "Balance assertive tone with check-ins on boundaries and comfort.",
    },
}

NSFW_ACTION_INTERACTION_OPTIONS = {
    "None": {"prompt": "", "summary": "Solo highlight by default."},
    "dildoplay": {"prompt": "dildoplay, rhythmic thrusts, focused attention", "summary": "Intentional dildo use highlighting control and pleasure."},
    "dildo plunge": {"prompt": "dildo plunge, deep thrusts, intense focus", "summary": "Deep, purposeful dildo penetration emphasizing intensity."},
    "Couple's Dance": {"prompt": "couple's dance, synchronized sway, intimate proximity", "summary": "Two-person dance emphasizing connection and chemistry."},
    "Mutual Tease": {"prompt": "mutual tease, playful touches, shared smiles", "summary": "Interactive teasing between consenting adults."},
    "Shared Focus": {"prompt": "shared focus, alternating attention, balanced engagement", "summary": "Equal spotlight on both participants."},
    "Playful Interaction": {"prompt": "playful interaction, light touches, teasing glances", "summary": "Fun, flirtatious exchanges between partners."},
    "Intimate Connection": {"prompt": "intimate connection, close body contact, lingering gazes", "summary": "Deep, affectionate moments highlighting emotional bond."},
    "Consensual Exploration": {"prompt": "consensual exploration, mutual discovery, open communication", "summary": "Partners exploring each other's desires with clear consent."},
    "Teasing Dynamics": {"prompt": "teasing dynamics, push and pull, playful tension", "summary": "Flirtatious back-and-forth emphasizing chemistry."},
    "Sensual Mirror": {"prompt": "sensual mirror play, synchronized movements, reflective allure", "summary": "Partners mirroring each other's sensuality."},
    "Sensual Fingering": {"prompt": "sensual_fingering, teasing touch, 2 fingers inside, deliberate pace", "summary": "Solo finger play emphasizing sensation."},
    "Solo Admiration": {"prompt": "solo admiration, self-touch, reflective gaze", "summary": "Focuses on individual self-appreciation and confidence."},
    "Solo Self-Admiration": {"prompt": "solo self-admiration, mirrored touch, confident posture", "summary": "Spotlights a single adult indulging in self-appreciation."},
    "Mirror Performance": {"prompt": "mirror performance, dual reflections, choreographed tease", "summary": "Performer using mirrors to amplify allure."},
    "Mutual Embrace": {"prompt": "mutual embrace, intertwined limbs, tender reciprocity", "summary": "Two consenting adults wrapped in equal affection."},
    "Dominant Lead": {"prompt": "dominant lead, guiding hand, steady reassurance", "summary": "Confident lead steering an enthusiastic partner."},
    "Submissive Offering": {"prompt": "submissive offering, lowered gaze, trusting openness", "summary": "Trust-forward posture celebrating consensual vulnerability."},
    "Power Switch": {"prompt": "power exchange switch, playful role reversal", "summary": "Partners swapping roles with delighted consent."},
    "Voyeur Tease": {"prompt": "voyeur tease, aware of onlookers, controlled reveal", "summary": "Flirtatious performance directed at an invited audience."},
    "Stage Showcase": {"prompt": "stage showcase, spotlighted solo, theatrical flourish", "summary": "Burlesque-style spotlight designed for adoring fans."},
    "Lap Dance Delivery": {"prompt": "lap dance delivery, partner seated, performer leading", "summary": "Classic lap dance built on clear boundaries."},
    "Sensual Massage Exchange": {"prompt": "mutual massage exchange, alternating focus, satisfied sighs", "summary": "Partners trading soothing touch in balanced turns."},
    "Tandem Pose": {"prompt": "tandem pose alignment, sculpted silhouettes, mutual balance", "summary": "Dual posing moment engineered for visual harmony."},
}

EMOTION_OPTIONS = {
    "None": {"prompt": "", "summary": "No explicit emotional cue."},
    "Anger": {"prompt": "fiery anger, clenched expression, intense gaze", "summary": "Emotion of anger and determination."},
    "Pleasure": {"prompt": "pleasure, satisfied smile, relaxed demeanor", "summary": "Contentment and enjoyment."},
    "Slight sadness": {"prompt": "slight sadness, downturned eyes, soft sigh", "summary": "Subtle sadness with a hint of vulnerability."},
    "A Little Fear": {"prompt": "a little fear, cautious eyes, hesitant posture", "summary": "Mild fear and apprehension."},
    "Fear": {"prompt": "subtle fear, wide eyes, tense posture", "summary": "Emotion of fear and uncertainty."},
    "Joy": {"prompt": "radiant joy, bright smile, delighted energy", "summary": "Joyful optimism."},
    "Sadness": {"prompt": "somber sadness, reflective emotion", "summary": "Quiet sadness and introspection."},
    "Surprise": {"prompt": "surprised reaction, widened expression", "summary": "Emotion of surprise and wonder."},
    "Determination": {"prompt": "steely determination, set jaw, unwavering focus", "summary": "Focused resolve radiating grit and purpose."},
    "Serenity": {"prompt": "calm serenity, relaxed features, centered presence", "summary": "Peaceful composure with gentle poise."},
    "Elation": {"prompt": "bursting elation, effervescent grin, expressive sparkle", "summary": "Effusive elation spilling over with joy."},
    "Stoic Resolve": {"prompt": "stoic resolve, guarded gaze, iron composure", "summary": "Quiet, unshakable resolve under pressure."},
    "Wonder": {"prompt": "awestruck wonder, widened eyes, open breath", "summary": "Fresh awe illuminating expression with curiosity."},
    "Melancholy": {"prompt": "gentle melancholy, softened gaze, reflective sorrow", "summary": "Quiet melancholy with tender introspection."},
    "Euphoria": {"prompt": "surging euphoria, lifted arms, unstoppable joy", "summary": "High-energy euphoria bursting with celebratory glee."},
    "Determined Calm": {"prompt": "determined calm, focused breathing, ready poise", "summary": "Calm exterior masking fierce determination."},
    "Playfulness": {"prompt": "playful mischief, sly smile, twinkling eyes", "summary": "Lighthearted playfulness teasing at spontaneity."},
    "Grief": {"prompt": "profound grief, tear-lined cheeks, trembling lip", "summary": "Visceral grief communicated through fragile posture."},
    "Triumph": {"prompt": "triumphant exhale, victorious grin, fists raised", "summary": "Post-victory triumph radiating unabashed pride."},
    "Suspicion": {"prompt": "suspicious glance, narrowed eyes, tightened posture", "summary": "Guarded suspicion hinting at underlying tension."},
    "Zen": {"prompt": "zen tranquility, serene smile, centered breathing", "summary": "Meditative serenity balancing body and mind."},
    "Frustration": {"prompt": "frustration, clenched jaw, furrowed brow", "summary": "Building frustration conveyed through tense features."},
}

CAMERA_BASIC_OPTIONS = {
    "None": {"prompt": "", "summary": "No basic camera move."},
    "Dolly In": {"prompt": "dolly in, smooth forward track, subject focus", "summary": "Forward dolly move centering subject."},
    "Push-in": {"prompt": "camera push-in, forward dolly, tightening focus", "summary": "Push-in move for increasing intensity."},
    "Pull-out": {"prompt": "camera pull-out, backward dolly, reveal context", "summary": "Pull-out move to reveal context."},
    "Pan Right": {"prompt": "pan right, lateral camera sweep", "summary": "Pan right following subject motion."},
    "Pan Left": {"prompt": "pan left, lateral follow", "summary": "Pan left tracking movement."},
    "Tilt Up": {"prompt": "tilt up, vertical reveal", "summary": "Tilt up uncovering grandeur."},
    "Crane Sweep": {"prompt": "crane sweep, rising arc, cinematic reveal", "summary": "Elevated crane arc that lifts to reveal scope."},
    "Whip Pan": {"prompt": "whip pan, rapid pivot, motion blur streaks", "summary": "Snap pan creating dynamic motion streaks."},
    "Push-Pull": {"prompt": "push-pull dolly zoom, perspective warp, tension swell", "summary": "Push-pull move warping background scale for dramatic tension."},
    "Pedestal Rise": {"prompt": "pedestal rise, vertical travel, unveiling scale", "summary": "Vertical pedestal move revealing layers of the scene."},
    "Pedestal Drop": {"prompt": "pedestal drop, descending move, revealing height", "summary": "Vertical descent revealing elevated vantage down to subject."},
    "Push Tilt": {"prompt": "push-in with tilt, converging axes, dynamic reveal", "summary": "Combined push and tilt creating layered dramatic emphasis."},
    "Dolly Out": {"prompt": "dolly out, expanding context, breath of scale", "summary": "Backward dolly expanding environment around subject."},
    "Arc Sweep": {"prompt": "arc sweep, curved track move, wraparound", "summary": "Semi-circular move hugging subject to show dimensionality."},
    "Static Hold": {"prompt": "static hold, motionless frame, patience", "summary": "Deliberate static shot sustaining tension through stillness."},
    "Push Past": {"prompt": "push past subject, handoff focus, motivated move", "summary": "Camera slides past subject to reveal new focal point."},
    "Rise and Drift": {"prompt": "vertical rise with lateral drift, floating move", "summary": "Combined vertical and lateral move producing gentle drift."},
    "Whip Tilt": {"prompt": "whip tilt, rapid vertical pivot, dynamic smear", "summary": "Fast tilt generating energetic motion blur streaks."},
    "First Person Perspective": {"prompt": "first-person perspective, immersive viewpoint, direct engagement", "summary": "POV angle placing viewer in character's shoes for intimacy."},
}

CAMERA_ADVANCED_OPTIONS = {
    "None": {"prompt": "", "summary": "No advanced camera move."},
    "Handheld": {"prompt": "handheld camera, organic sway, documentary feel", "summary": "Handheld movement for visceral texture."},
    "Compound": {"prompt": "compound move, layered dolly and pan", "summary": "Compound move blending multiple axes."},
    "Following": {"prompt": "dynamic follow shot, tracking movement", "summary": "Following shot tracking the subject."},
    "Orbit": {"prompt": "orbiting camera, circular move, wraparound view", "summary": "Orbiting move for immersive coverage."},
    "Steadicam Glide": {"prompt": "steadicam glide, fluid tracking, stabilized motion", "summary": "Stabilized glide preserving fluid, anchored movement."},
    "Cable Cam Chase": {"prompt": "cable cam chase, high-speed lateral track, aerial pursuit", "summary": "High-speed cable run carving dynamic parallax."},
    "Gimbal Glide": {"prompt": "gimbal glide, balanced footsteps, cinematic float", "summary": "Motorized gimbal smooths footsteps for floating camera energy."},
    "VR Orbit": {"prompt": "immersive vr orbit, spherical capture, wraparound viewpoint", "summary": "VR-ready orbit delivering 360° spatial immersion."},
    "Jib Cascade": {"prompt": "jib cascade, layered vertical arcs, floaty transitions", "summary": "Multi-level jib move creating cascading vertical arcs."},
    "Snorricam": {"prompt": "snorricam mount, subject-locked frame, disorienting world", "summary": "Camera rigidly mounted to subject keeping them static while world moves."},
    "Gimbal Sprint": {"prompt": "gimbal sprint, stabilized run, pursuit energy", "summary": "Stabilized sprint following subject through chaotic motion."},
    "Cable Drop": {"prompt": "cable cam drop, high-to-low plunge, overhead chase", "summary": "Cable cam diving from altitude toward ground-level action."},
    "Drone Orbit": {"prompt": "drone orbit, aerial wrap, wide-scale coverage", "summary": "Drone encircling target for expansive orbital perspective."},
    "Technocrane Lash": {"prompt": "technocrane lash, sweeping extension, cinematic flourish", "summary": "Long reach crane delivering dramatic swoops and lashes."},
    "Handheld Crash": {"prompt": "handheld crash zoom, frenetic push, documentary grit", "summary": "Handheld crash zoom injecting adrenaline and immediacy."},
    "Steadicam Stair": {"prompt": "steadicam stair descent, floating steps, continuous move", "summary": "Steadicam gliding down stairs maintaining smooth coverage."},
    "Robot Arm": {"prompt": "robot arm precision move, programmable path, high-speed control", "summary": "Motion-control robot arm executing precise, repeatable camera paths."},
    "Helmet Cam POV": {"prompt": "helmet-cam first-person view, breath fog, immersive dash", "summary": "Head-mounted POV aligning the viewer with the character's gaze."},
    "Body Cam Pulse": {"prompt": "body-mounted camera POV, chest-level jitter, urgent micro-shake", "summary": "Chest-mounted camera delivering raw first-person immediacy."},
    "Gauntlet POV Sweep": {"prompt": "weapon gauntlet POV, hands in frame, kinetic swings", "summary": "First-person gauntlet view keeping hands and weapon in frame."},
    "Shoulder Rig POV": {"prompt": "shoulder-rig POV, reactive head sway, human-scale perspective", "summary": "Over-shoulder first-person angle balancing stability with intimacy."},
    "Maglev Rail Glide": {"prompt": "maglev rail glide, zero-friction track, hovering sweep", "summary": "Magnetic rail system delivering vibration-free lateral sweeps."},
    "Barrel Roll Orbit": {"prompt": "barrel roll orbit, 360 spin, stabilized center lock", "summary": "Stabilized orbit that rolls around subject while keeping focus pinned."},
    "Spidercam Net": {"prompt": "spidercam cable net, multi-axis chase, rapid altitude shifts", "summary": "Multi-cable spidercam racing across set with agile altitude pivots."},
    "Submersible Pursuit": {"prompt": "submersible pursuit cam, underwater glide, bubble trails", "summary": "Waterproof chase rig gliding beside subjects beneath the surface."},
    "Micro Drone Dash": {"prompt": "micro drone dash, narrow corridor sweep, obstacle dodge", "summary": "Palm-sized drone weaving through tight spaces for kinetic POV."},
    "Holo Stage Orbit": {"prompt": "holo-stage tracked orbit, volumetric capture, light field shimmer", "summary": "Volumetric tracker orbiting holographic performers without parallax drift."},
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
    "Retro Anime": {"prompt": "retro anime cel shading, grainy cels, vintage palette", "summary": "Retro anime throwback with painterly cels and nostalgic hues."},
    "Lofi Vapor": {"prompt": "lofi vapor style, pastel gradients, soft noise texture", "summary": "Lo-fi vapor aesthetic with gentle gradients and analog fuzz."},
    "Synthwave": {"prompt": "synthwave style, neon grids, retro futurism", "summary": "Retro-futuristic synthwave visuals drenched in neon gradients."},
    "Baroque Painting": {"prompt": "baroque oil painting, dramatic chiaroscuro, ornate detail", "summary": "Lavish baroque aesthetic with rich brushwork and contrast."},
    "Cyber Noir": {"prompt": "cyber noir aesthetic, neon noir, rain-soaked streets", "summary": "Futuristic noir blending neon palettes with shadowy grit."},
    "Papercraft": {"prompt": "papercraft collage, layered cutouts, tactile edges", "summary": "Hand-cut paper aesthetic with layered dimensionality."},
    "Editorial Fashion": {"prompt": "editorial fashion photography, high gloss lighting, couture styling", "summary": "Magazine-ready editorial look with glossy polish."},
    "Solarized": {"prompt": "solarized film effect, inverted tones, experimental contrast", "summary": "Solarized treatment flipping tones into psychedelic inversion."},
    "Ink Wash Animation": {"prompt": "ink wash animation, fluid brushstrokes, sumi-e motion", "summary": "Animated ink wash blending flowing brushwork with motion."},
    "Voxel Neon": {"prompt": "voxel neon city, glowing cubes, pixel volumetrics", "summary": "Glowing voxel aesthetic fusing retro pixels with neon depth."},
    "AI Glitch": {"prompt": "AI glitch art, datamosh streaks, corrupted frames", "summary": "Glitch-forward visuals with datamosh artifacts and distortions."},
    "Hyperreal CGI": {"prompt": "hyperreal CGI, physically based shading, immaculate detail", "summary": "Cutting-edge CGI look with immaculate physical accuracy."},
    "Analog Horror": {"prompt": "analog horror aesthetic, VHS static, uncanny grading", "summary": "Grainy analog horror styling with unsettling VHS artifacts."},
    "Water Ink Hybrid": {"prompt": "watercolor ink hybrid, splatter gradients, bleeding pigments", "summary": "Hybrid watercolor and ink aesthetic with bleeding pigments."},
    "Painterly Sci-Fi": {"prompt": "painterly sci-fi, illustrated futurism, saturated scapes", "summary": "Illustrated sci-fi aesthetic with painterly strokes."},
    "Ceramic Render": {"prompt": "ceramic render style, glazed highlights, sculpted forms", "summary": "Rendered ceramics with glossy glaze and sculptural shapes."},
}

SPECIAL_EFFECT_OPTIONS = {
    "None": {"prompt": "", "summary": "No special effect emphasis."},
    "Tilt-shift": {"prompt": "tilt-shift effect, miniature depth of field", "summary": "Tilt-shift miniature illusion."},
    "Time-lapse": {"prompt": "time-lapse effect, accelerated motion", "summary": "Time-lapse acceleration for dynamic pacing."},
    "Light Trails": {"prompt": "long-exposure light trails, kinetic streaks, luminous ribbons", "summary": "Dynamic light streaks painting motion paths."},
    "Chromatic Bloom": {"prompt": "chromatic bloom effect, spectral haze, prismatic fringe", "summary": "Prismatic bloom that radiates color halos."},
    "Particle Swarm": {"prompt": "particle swarm effect, floating embers, suspended motes", "summary": "Particle swarm drifting through the frame for tactile atmosphere."},
    "Holographic Static": {"prompt": "holographic static, glitch shimmer, pixel flutter", "summary": "Glitch-laced holographic static overlays for cybernetic flair."},
    "Fog Burst": {"prompt": "fog burst effect, rolling clouds, atmospheric reveal", "summary": "Timed fog bursts adding dramatic atmospheric volume."},
    "Spark Shower": {"prompt": "spark shower effect, cascading embers, industrial flare", "summary": "Controlled spark cascade igniting kinetic energy."},
    "Rain Simulation": {"prompt": "rain simulation, directional droplets, reflective sheen", "summary": "Simulated rainfall coating scene in reflective droplets."},
    "Particle Glimmer": {"prompt": "particle glimmer effect, floating motes, glitter drift", "summary": "Glittering particles drifting slowly through air."},
    "Light Leak": {"prompt": "film light leak flare, colorful streaks, analog bleed", "summary": "Analog-style light leaks bleeding vibrant streaks across frame."},
    "Speed Ramp": {"prompt": "speed ramp effect, time shift, motion stretch", "summary": "Dynamic speed ramp bending time for emphasis."},
    "Digital Rain": {"prompt": "digital rain code, cascading glyphs, matrix cascade", "summary": "Digital code rain overlay cascading across scene."},
    "Dust Explosion": {"prompt": "dust explosion effect, powder bloom, slow-motion plume", "summary": "Choreographed dust burst expanding in cinematic slow motion."},
    "Energy Ribbons": {"prompt": "energy ribbon trails, luminous arcs, kinetic swirls", "summary": "Luminous energy ribbons weaving through motion path."},
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
    "Crystal Metropolis": {
        "description": "Prismatic mega-city palette where glass towers refract neon pulse and rainfall.",
        "overrides": {
            "light_source": ["Holographic Panels", "Mixed Light"],
            "light_quality": ["Specular Punch"],
            "time_of_day": ["Nighttime"],
            "color_tone": ["Bioluminescent"],
            "visual_style": ["Lofi Vapor"],
            "special_effect": ["Holographic Static"],
        },
        "intense_overrides": {
            "motion_type": ["Parkour"],
            "camera_advanced": ["Gimbal Glide"],
        },
        "effects": ["Light Trails"],
        "keywords": [
            "crystal canopy",
            "rain-slick plazas",
            "neon diffraction",
        ],
        "intense_keywords": [
            "mirror-flare cascades",
            "vertigo sprint",
        ],
        "effect_keywords": ["glitch shimmer"],
    },
    "Mythic Canopy": {
        "description": "Sun-dappled ancient forest palette infused with luminous spores and folklore hush.",
        "overrides": {
            "light_source": ["Overcast Light"],
            "light_quality": ["Veiled Diffusion"],
            "time_of_day": ["Golden Hour"],
            "color_tone": ["Warm Tone"],
            "visual_style": ["Watercolor"],
            "composition": ["Radial Burst"],
        },
        "intense_overrides": {
            "motion_type": ["Aerial Silk"],
            "lens_focal": ["Tilt Shift"],
        },
        "effects": ["Particle Swarm"],
        "keywords": [
            "sunlit spores",
            "ancient canopy",
            "myth-woven moss",
        ],
        "intense_keywords": [
            "floating pollen aurora",
            "silk dancer arc",
        ],
        "effect_keywords": ["ember motes"],
    },
}

CHARACTER_SPECIES_OPTIONS = {
    "Human": {"prompt": "human lineage, adaptable physiology", "notes": "Versatile baseline physiology built for broad storytelling."},
    "Woman": {"prompt": "a woman", "notes": "Baseline human woman—ideal for grounded or genre-flexible prompts."},
    "Man": {"prompt": "a man", "notes": "Baseline human man—works across modern, historical, and speculative settings."},
    "Nonbinary Icon": {"prompt": "a non-binary hero", "notes": "Gender-expansive protagonist centered on confidence and agency."},
    "High Elf": {"prompt": "high elf heritage, luminous eyes, tapered ears", "notes": "Elegant, ageless presence steeped in arcane tradition."},
    "Cyborg": {"prompt": "cybernetic grafts, chrome plating, biomechanical synergy", "notes": "Synthetic augmentation threaded through organic form."},
    "Beastkin": {"prompt": "beastkin traits, digitigrade stance, tufted ears, expressive tail", "notes": "Animal lineage lends primal motion and sensory acuity."},
    "Voidborn": {"prompt": "voidborn aura, astral freckles, gravity-bent silhouette", "notes": "Born in deep space, physics bends gently around them."},
    "Chronomancer": {"prompt": "chronomancer attunement, temporal glyphs inlaid across skin", "notes": "Timeline walker carrying echoes of alternate outcomes."},
    "Draconic Heir": {"prompt": "draconic bloodline, scaled accents, ember glow veins", "notes": "Ancestral dragon heritage radiating latent ferocity."},
    "Aether Construct": {"prompt": "aether-forged shell, floating sigils, hum of resonant crystals", "notes": "Sapient construct suspended by arcane reinforcement fields."},
    "Mycelid": {"prompt": "mycelid collective body, filament hair, luminous spores", "notes": "Fungal network embodied in a collaborative biped form."},
    "Solaris": {"prompt": "solar-charged aura, corona halo, radiant freckles", "notes": "Photosynthetic physiology that stores stellar energy."},
    "Android Emissary": {"prompt": "android emissary, polished synth-skin, bioluminescent joints", "notes": "Diplomatic artificial being fluent in human and machine cultures."},
    "Gene-Spliced": {"prompt": "gene-spliced hybrid, mosaic DNA, adaptive phenotype", "notes": "Experimental hybrid whose form shifts with environmental cues."},
    "Stoneborn": {"prompt": "stoneborn titan, living granite plates, glowing rune veins", "notes": "Earth-wrought giant shaped from enchanted stone."},
    "Celestial Seraph": {"prompt": "celestial seraph, radiant wings, constellation eyes", "notes": "Heaven-forged being channeling starlight through every gesture."},
    "Abyssal Diver": {"prompt": "abyssal diver lineage, bioluminescent markings, pressure-adapted", "notes": "Deep-sea evolved being comfortable in crushing depths."},
    "Chrono Echo": {"prompt": "chrono echo, multiple temporal afterimages, layered timelines", "notes": "Time-split individual existing across overlapping moments."},
    "Glimmer Sprite": {"prompt": "glimmer sprite, crystalline wings, iridescent glow", "notes": "Feykin sprite carried on refractive wings of light."},
    "Terran Ranger": {"prompt": "terra-born ranger, rugged human variant, survival scar", "notes": "Human offshoot adapted for harsh frontier worlds."},
    "Nebula Djinn": {"prompt": "nebula djinn, gaseous limbs, swirling cosmic dust", "notes": "Wish-bending being composed of nebular gases."},
    "Arc Forge": {"prompt": "arc-forged entity, metallic flesh, humming coils", "notes": "Electro-forged lifeform powered by humming arc reactors."},
    "Fungal Scholar": {"prompt": "fungal scholar, mycelial tendrils, spore library", "notes": "Sapient fungus network storing ancestral knowledge."},
    "Solaris Twin": {"prompt": "solar twin pair, bi-phasic body, orbit-linked", "notes": "Twin-bodied organism connected by radiant energy tether."},
    "Glacial Avatar": {"prompt": "glacial avatar, ice-armored skin, frost aura", "notes": "Ice-forged guardian radiating crystalline chill."},
    "Myth-Machine": {"prompt": "myth-machine construct, engraved chassis, story sigils", "notes": "Mechanical being animated by legendary narratives."},
    "Bio-Siren": {"prompt": "bio-siren lineage, harmonic voice, ripple scales", "notes": "Amphibious singer whose tones shape currents and minds."},
    "Shadowweave": {"prompt": "shadowweave entity, semi-corporeal dusk, shifting outline", "notes": "Living shadow capable of phasing through thin light."},
    "Sky Leviathan": {"prompt": "sky leviathan rider lineage, aerodynamic membranes, storm glands", "notes": "Aerial giant evolved to glide on planetary jet streams."},
    "Marrowbound": {"prompt": "marrowbound wanderer, biolattice bones, internal glow", "notes": "Biomechanical nomad whose bones emit soft luminescence."},
    "Quantum Bloom": {"prompt": "quantum bloom organism, petal fractals, probability petals", "notes": "Quantum-born entity blossoming into countless outcomes."},
}

CHARACTER_ARCHETYPE_OPTIONS = {
    "Champion": {"prompt": "heroic champion stance, shield of hope", "notes": "Frontline defender sworn to inspire and protect."},
    "Trickster": {"prompt": "trickster charisma, sly grin, sleight-of-hand readiness", "notes": "Unpredictable agent of chaos and clever subversion."},
    "Scholar": {"prompt": "erudite scholar poise, layered tomes, analytical gaze", "notes": "Driven by curiosity, cataloging the unknown."},
    "Guardian": {"prompt": "guardian vigilance, anchored footing, protective aura", "notes": "Stalwart protector holding the line against threats."},
    "Nomad": {"prompt": "wandering nomad stride, horizon-focused gaze", "notes": "Pathfinder drawn to uncharted horizons and cultural exchange."},
    "Inquisitor": {"prompt": "unyielding inquisitor presence, piercing eyes", "notes": "Relentless truth-seeker weighed down by difficult judgments."},
    "Visionary": {"prompt": "visionary dreamer, star-mapped cloak, prophetic whispers", "notes": "Sees futures yet unwritten, shaping destiny with conviction."},
    "Survivor": {"prompt": "scarred survivor grit, improvised kit", "notes": "Battle-hardened resilience forged through catastrophe."},
    "Diplomat": {"prompt": "compassionate diplomat posture, open palms", "notes": "Bridge-builder skilled in cultural nuance and negotiation."},
    "Warden": {"prompt": "ancient warden gravitas, rooted stance", "notes": "Sworn caretaker of sacred territories and traditions."},
    "Innovator": {"prompt": "visionary innovator, prototype-laden belt, spark of insight", "notes": "Constant tinkerer reshaping the world with daring ideas."},
    "Shadow Broker": {"prompt": "shadow broker, encrypted dossiers, whisper alliances", "notes": "Information powerbroker trading secrets across factions."},
    "Healer": {"prompt": "battlefield healer, luminous salves, steady compassion", "notes": "Medic whose calm precision restores allies under pressure."},
    "Storm Herald": {"prompt": "storm herald, cloak of thunderheads, prophetic warnings", "notes": "Weather-calling herald reading omens in turbulent skies."},
    "Beacon": {"prompt": "living beacon, radiant posture, hope incarnate", "notes": "Symbol of inspiration whose presence uplifts entire movements."},
    "Archivist": {"prompt": "memory archivist, floating data shards, chronicle voice", "notes": "Keeper of histories extracting lessons from layered timelines."},
    "Outlaw Poet": {"prompt": "outlaw poet, handwritten manifestos, rebel charm", "notes": "Romantic renegade weaving revolution through verse."},
    "Voidwalker": {"prompt": "voidwalker stride, starless cloak, planar map", "notes": "Interplanar traveler charting hidden routes between realities."},
    "Caretaker": {"prompt": "gentle caretaker, calming aura, nurturing stance", "notes": "Guardian of communities prioritizing empathy and stability."},
    "Relic Hunter": {"prompt": "relic hunter, artifact harness, keen appraisal", "notes": "Treasure-seeking scholar adept at deciphering ancient wards."},
    "Tactician": {"prompt": "war tactician, strategy lattice, anticipatory gaze", "notes": "Battlefield planner forecasting outcomes with precision."},
    "Dreamweaver": {"prompt": "lucid dreamweaver, shimmering sleep threads, tranquil poise", "notes": "Architect of shared dreams sculpting surreal landscapes."},
    "Firebrand": {"prompt": "street firebrand, megaphone rhetoric, burning conviction", "notes": "Agitator sparking uprisings with bold speeches."},
    "Seer": {"prompt": "veil-wrapped seer, clairvoyant focus, second-sight glow", "notes": "Oracle translating cryptic visions into actionable guidance."},
    "Envoy": {"prompt": "cosmopolitan envoy, emblem sashes, persuasive grace", "notes": "Bridge-builder negotiating peace among rival factions."},
    "Rift Knight": {"prompt": "rift knight, dimensional plate armor, phase-blade", "notes": "Guardian soldier defending portals between worlds."},
    "Songsmith": {"prompt": "battle songsmith, resonant instruments, sonic wards", "notes": "Musical mage channeling melodies into protective sigils."},
    "Lorebreaker": {"prompt": "rule-bending lorebreaker, annotated laws, sly smirk", "notes": "Legal rebel hacking loopholes to reshape society."},
    "Channeler": {"prompt": "elemental channeler, swirling energy conduits, focused stance", "notes": "Conduit for raw natural forces balancing immense power."},
    "Pathfinder": {"prompt": "frontier pathfinder, holographic maps, adaptive gear", "notes": "Explorer leading expeditions through perilous territories."},
    "Sentinel": {"prompt": "midnight sentinel, vigilant guard stance, unwavering gaze", "notes": "Unblinking protector standing between chaos and calm."},
    "Harbinger": {"prompt": "ominous harbinger, windblown heraldry, portentous aura", "notes": "Messenger whose arrival signals profound change."},
    "Artificer": {"prompt": "clockwork artificer, modular gauntlets, analytical eyes", "notes": "Inventor crafting adaptive gadgets under pressure."},
    "Mystic": {"prompt": "hermit mystic, incense haze, layered talismans", "notes": "Spiritual guide searching for enlightenment in silent rituals."},
    "Caretaker AI": {"prompt": "caretaker AI avatar, holographic interface, calming pulse", "notes": "Artificial intelligence embodying empathy as its core directive."},
    "Courier": {"prompt": "sky courier, jet-assisted boots, urgent posture", "notes": "Risk-taking messenger delivering vital packages across hazards."},
    "Saboteur": {"prompt": "precision saboteur, compact charges, disarming wit", "notes": "Expert infiltrator dismantling oppressive infrastructure."},
    "Sage": {"prompt": "wandering sage, humble robes, gentle insight", "notes": "Wisdom keeper gifting balanced counsel to seekers."},
    "Beast Tamer": {"prompt": "stellar beast tamer, companion creature, confident rapport", "notes": "Handler forging bonds with extraordinary fauna."},
    "Soul Forger": {"prompt": "soul forger, radiant anvil, sparks of memory", "notes": "Craftsperson reshaping destinies through metaphysical metallurgy."},
}

CHARACTER_PROFESSION_OPTIONS = {
    "Starship Captain": {"prompt": "starship captain regalia, command epaulettes", "notes": "Seasoned navigator balancing crew morale with tactical foresight."},
    "Shadow Operative": {"prompt": "shadow operative gear, stealth field emitter", "notes": "Specialist in covert insertions armed with cutting-edge espionage tools."},
    "Battle Bard": {"prompt": "battle bard instrument rig, harmonic weaponry", "notes": "Weaves music into battlefield momentum and morale."},
    "Bioengineer": {"prompt": "bioengineer toolkit, gene-etched gloves", "notes": "Cultivates living solutions to impossible problems."},
    "Runesmith": {"prompt": "runesmith hammer, enchanted anvil sparks", "notes": "Artisan forging sigils into resonant artifacts."},
    "Sky Courier": {"prompt": "sky courier harness, aero-satchel", "notes": "Thrill-seeking messenger skimming the jet stream."},
    "Mythic Chef": {"prompt": "culinary alchemist, floating spice jars", "notes": "Chef crafting memory-infused cuisine that shapes emotion."},
    "Chronicle Scribe": {"prompt": "chronicle scribe quills, holographic folios", "notes": "Living historian who witnesses and records pivotal events."},
    "Stormcaller": {"prompt": "stormcaller conduit staff, charged gauntlets", "notes": "Elementalist channeling tempest forces through precise rituals."},
    "Digital Oracle": {"prompt": "digital oracle visor, cascading data-streams", "notes": "Predictive analyst interfaced with sentient archives."},
    "Terraform Architect": {"prompt": "terraform architect console, eco-drone entourage", "notes": "Engineer sculpting habitable worlds from hostile environments."},
    "Rift Cartographer": {"prompt": "rift cartographer holo-astrolabe, dimensional charts", "notes": "Survey specialist mapping unstable planar anomalies."},
    "Plasma Knight": {"prompt": "plasma knight armor, energized lance", "notes": "Elite warrior clad in superheated shielding."},
    "Memory Diver": {"prompt": "memory diver neural rig, mnemonic tether", "notes": "Psychic operative recovering truths buried in minds."},
    "Chrono Prosecutor": {"prompt": "chrono prosecutor robes, temporal evidence glyphs", "notes": "Legal tactician litigating crimes across timefolds."},
    "Skywright": {"prompt": "skywright workshop, levitation tools", "notes": "Artisan crafting airborne vessels and floating habitats."},
    "Pulse DJ": {"prompt": "pulse DJ booth, rhythm gauntlets", "notes": "Sound sculptor remixing reality through bassline manipulation."},
    "Gene Shepherd": {"prompt": "gene shepherd caretaking lab, bio-cradle", "notes": "Caretaker guiding bespoke organisms to maturity."},
    "Quantum Broker": {"prompt": "quantum broker ledger, entangled contracts", "notes": "Negotiator orchestrating probability-weighted deals."},
    "Mythos Curator": {"prompt": "mythos curator reliquary, floating archives", "notes": "Museum steward preserving legendary artifacts."},
    "Flux Gladiator": {"prompt": "flux gladiator arena gear, adaptive plating", "notes": "Arena combatant thriving in transforming battlegrounds."},
    "Aurora Ranger": {"prompt": "aurora ranger scout armor, chromatic cloak", "notes": "Guardian patrolling polar frontiers and lightstorms."},
    "Nanite Surgeon": {"prompt": "nanite surgeon sterile swarm, precision halo", "notes": "Microsurgical expert deploying autonomous healing units."},
    "Dream Cartomancer": {"prompt": "dream cartomancer deck, lucid tarot", "notes": "Sleep-mage reading futures via animated cards."},
    "Ember Smith": {"prompt": "ember smith forge, molten glasswork", "notes": "Artist shaping fire into ornamental weaponry."},
    "Cybernetic Shepherd": {"prompt": "cybernetic shepherd drone-flock, command baton", "notes": "Technician wrangling autonomous machines across fields."},
    "Tidal Envoy": {"prompt": "tidal envoy amphibious gear, water glyph tattoos", "notes": "Diplomat mediating treaties between aquatic nations."},
    "Grav-Law Marshal": {"prompt": "grav-law marshal badge, stabilizer harness", "notes": "Peacekeeper enforcing order in zero-G jurisdictions."},
    "Solar Cantor": {"prompt": "solar cantor choir robe, light harmonics", "notes": "Clerical vocalist channeling solar hymns for healing."},
}

CHARACTER_TEMPERAMENT_OPTIONS = {
    "Stoic": {"prompt": "stoic demeanor, measured breathing", "notes": "Calm exterior shielding unshakeable resolve."},
    "Reckless": {"prompt": "reckless spark, ready grin, forward lean", "notes": "Thrives on risk and improvisational momentum."},
    "Empathic": {"prompt": "empathic warmth, soft cadence, open posture", "notes": "Absorbs emotional atmosphere, reflecting compassion."},
    "Calculating": {"prompt": "calculating gaze, micro-expressions measured", "notes": "Strategist evaluating probabilities before striking."},
    "Haunted": {"prompt": "haunted distance, shadowed eyes", "notes": "Trauma-laden presence haunted by past choices."},
    "Joyous": {"prompt": "joyous energy, kinetic laughter", "notes": "Infectious enthusiasm lifting the spirits of allies."},
    "Obsessive": {"prompt": "obsessive focus, ink-stained fingers", "notes": "Won't rest until every thread of a mystery is resolved."},
    "Serene": {"prompt": "serene center, meditative aura", "notes": "Anchored mindfulness even amid chaos."},
    "Commanding": {"prompt": "commanding cadence, authoritative presence", "notes": "Compels attention with natural leadership."},
    "Unpredictable": {"prompt": "mercurial energy, sudden shifts", "notes": "Volatile impulse shaping chaotic adventures."},
    "Zenith": {"prompt": "zenith poise, radiant calm", "notes": "Steady optimist radiating unwavering positive focus."},
    "Brooding": {"prompt": "brooding quiet, tempest behind eyes", "notes": "Reserved intensity masking deep internal storms."},
    "Mischievous": {"prompt": "mischievous glint, playful tilt", "notes": "Prankster spirit sparking levity amid danger."},
    "Stoic Ember": {"prompt": "stoic ember, quiet burn", "notes": "Outwardly composed yet fueled by simmering drive."},
    "Nurturing": {"prompt": "nurturing warmth, reassuring cadence", "notes": "Care-taker temperament offering continual reassurance."},
    "Relentless": {"prompt": "relentless focus, forward momentum", "notes": "Determination that bulldozes obstacles without hesitation."},
    "Mercurial": {"prompt": "mercurial shift, rapid mood flux", "notes": "Emotion swings fast, channeling creativity and chaos."},
    "Wry": {"prompt": "wry amusement, raised brow", "notes": "Dry-humored commentator defusing tension with wit."},
    "Haute": {"prompt": "haute composure, refined posture", "notes": "Elegant confidence curating every moment with taste."},
}

CHARACTER_POWER_SOURCE_OPTIONS = {
    "Arcane Relic": {"prompt": "arcane relic focus, carved sigils pulsating", "notes": "Ancient artifact channels raw eldritch potency."},
    "Bio-Augment": {"prompt": "bio-augment grafts, living circuitry", "notes": "Symbiotic biotech amplifies physical capabilities."},
    "Symbiotic Spirit": {"prompt": "spirit-bound ally whispering, spectral tether", "notes": "Bonded with an ancestral guardian spirit."},
    "Quantum Reservoir": {"prompt": "quantum reservoir core, probability halos", "notes": "Manipulates chance via micro-singularity core."},
    "Celestial Choir": {"prompt": "celestial choir resonance, harmonized aura", "notes": "Channeling melodies sung beyond mortal perception."},
    "Primeval Blood": {"prompt": "primeval blood surge, pulse-light veins", "notes": "Ancient lineage awakens primal ferocity."},
    "Dreamforge": {"prompt": "dreamforge conduit, lucid shimmer", "notes": "Shapes reality by weaving lucid dream fragments."},
    "Nano Swarm": {"prompt": "nano swarm cloud, adaptive armor", "notes": "Programmable matter responds to instinctive commands."},
    "Shadow Accord": {"prompt": "shadow accord pact, umbral tendrils", "notes": "Dark pact enabling controlled umbral manifestations."},
    "Empyreal Beacon": {"prompt": "empyreal beacon flares, feathered light", "notes": "Holy conduit radiating restorative brilliance."},
    "Bio-Lum Core": {"prompt": "bio-lum core, radiant organ glow", "notes": "Organ grown to store luminescent energy for spells."},
    "Aeon Engine": {"prompt": "aeon engine heart, rotating chronogears", "notes": "Temporal reactor granting longevity and time manipulation."},
    "Starfall Fragment": {"prompt": "starfall fragment shard, cosmic resonance", "notes": "Meteorite shard humming with stellar ferocity."},
    "Echo Choir": {"prompt": "echo choir resonance, harmonic halo", "notes": "Networked voices empowering abilities when harmonized."},
    "Dream Fathom": {"prompt": "dream fathom sigil, lucid tides", "notes": "Draws strength from collective subconscious oceans."},
    "Glyph Circuit": {"prompt": "glyph circuit lattice, rune-lit veins", "notes": "Runic circuitry embedded beneath the skin."},
    "Primal Symbiosis": {"prompt": "primal symbiote companion, entwined motion", "notes": "Living companion organism amplifies raw instincts."},
    "Entropy Well": {"prompt": "entropy well core, orbiting decay motes", "notes": "Harvests decay energy to fuel destructive potential."},
    "Aurora Seed": {"prompt": "aurora seed heart, chromatic bloom", "notes": "Seed of living light blossoming into protective auroras."},
}

CHARACTER_SIGNATURE_GEAR_OPTIONS = {
    "Living Blade": {"prompt": "living blade companion, shifting edge geometry", "notes": "Sentient weapon that adapts to combat rhythm."},
    "Modular Gauntlet": {"prompt": "modular gauntlet, deployable tools", "notes": "Swiss-army gauntlet that reconfigures for any task."},
    "Archivist Drone": {"prompt": "archivist drone orbiting, holo-scribe projectors", "notes": "Floating aide capturing and projecting key intel."},
    "Aether Cloak": {"prompt": "aether cloak, phase-shifting weave", "notes": "Cloak that slips between visibility bands to protect the wearer."},
    "Phoenix Sigil": {"prompt": "phoenix sigil brooch, ember trails", "notes": "Symbol igniting morale and triggering regenerative surges."},
    "Gravity Boots": {"prompt": "gravity boots, thruster vents, magnetic soles", "notes": "Footwear manipulating gravity wells for agile traversal."},
    "Warden Shield": {"prompt": "warden shield, etched wardlines", "notes": "Monolithic shield storing protective ward glyphs."},
    "Chrono Dice": {"prompt": "chrono dice reliquary, suspended numbers", "notes": "Randomizer glimpsing potential futures to adjust tactics."},
    "Liminal Loom": {"prompt": "liminal loom toolkit, reality-thread spindles", "notes": "Portable loom stitching scenario-specific disguises."},
    "Mycelial Satchel": {"prompt": "mycelial satchel, cultivated spores", "notes": "Organic pack sprouting bespoke remedies on demand."},
    "Echo Bow": {"prompt": "echo bow, resonance arrows", "notes": "Bow that replicates shots across parallel timelines."},
    "Solar Bracers": {"prompt": "solar bracers, photon vents", "notes": "Gauntlets storing sunlight for explosive discharges."},
    "Grav Whip": {"prompt": "gravity whip, collapsing nodes", "notes": "Whip manipulating localized gravity wells mid-strike."},
    "Chrono Compass": {"prompt": "chrono compass, spinning epochs", "notes": "Navigational relic pointing toward optimal futures."},
    "Nimbus Kite": {"prompt": "nimbus kite familiar, tethered cloud", "notes": "Weather-bound companion providing lift and surveillance."},
    "Quantum Satchel": {"prompt": "quantum satchel, nested storage fields", "notes": "Bag storing entire arsenals within compressed dimensions."},
    "Runebound Mask": {"prompt": "runebound mask, animated etchings", "notes": "Mask that shifts identities through carved sigils."},
    "Pulse Hammer": {"prompt": "pulse hammer, shockwave coils", "notes": "Weapon releasing seismic bursts on impact."},
    "Lullaby Harp": {"prompt": "lullaby harp, starlit strings", "notes": "Instrument weaving calming enchantments mid-conflict."},
}

CHARACTER_VISUAL_MOTIF_OPTIONS = {
    "Solar Flare": {"prompt": "solar flare motifs, golden filigree", "notes": "Radiant motifs framing them in warm celestial geometry."},
    "Glacial Facets": {"prompt": "glacial facet accents, refracted highlights", "notes": "Crystalline textures evoking frozen elegance."},
    "Verdant Bloom": {"prompt": "verdant bloom vines, botanical flourish", "notes": "Living flora that responds to their emotional cadence."},
    "Neon Glyphs": {"prompt": "neon glyph tattoos, animated circuitry", "notes": "Luminous glyphwork channeling cybernetic runes."},
    "Ink Wash": {"prompt": "ink wash gradients, sumi-e splashes", "notes": "Brushstroke aesthetics trailing each movement."},
    "Storm Wreath": {"prompt": "storm wreath corona, static arcs", "notes": "Micro-lightning dances around their silhouette."},
    "Mirror Shards": {"prompt": "mirror shard fragments, reflective armor", "notes": "Fragmented reflections distorting perception."},
    "Bone Filigree": {"prompt": "ivory bone filigree, ancestral carvings", "notes": "Ornate osteal motifs honoring ancient lineage."},
    "Lunar Petals": {"prompt": "lunar petal embroidery, silver sheen", "notes": "Delicate moonlit blossoms drifting in their wake."},
    "Aurora Stream": {"prompt": "aurora stream ribbons, chromatic trails", "notes": "Flowing gradients reminiscent of polar skies."},
    "Obsidian Fractals": {"prompt": "obsidian fractal veins, dark sheen", "notes": "Geometric void patterns refracting shadow light."},
    "Circuit Lace": {"prompt": "circuit lace filaments, glowing traces", "notes": "Delicate techno-filagree tracing along fabrics."},
    "Celestial Manuscript": {"prompt": "celestial manuscript constellations, inked nebulae", "notes": "Scripted galaxies arcing across garments."},
    "Tidal Plumes": {"prompt": "tidal plume motifs, misted gradients", "notes": "Ocean-swept vapor ribbons swirling around them."},
    "Floral Geodes": {"prompt": "floral geode facets, blooming crystals", "notes": "Gemstone blossoms bursting through attire."},
    "Sonic Waves": {"prompt": "sonic wave glyphs, rippling rings", "notes": "Resonant patterns oscillating with each step."},
    "Origami Armor": {"prompt": "origami armor plates, fold-shift edges", "notes": "Artful folds rearranging protective layers in motion."},
    "Ink Nebula": {"prompt": "ink nebula swirls, gaseous gradients", "notes": "Liquid galaxy motifs pooling into nocturnal clouds."},
    "Feather Storm": {"prompt": "feather storm cascade, drifting barbs", "notes": "Swirling plumage orbiting in controlled spirals."},
}

CHARACTER_ERA_OPTIONS = {
    "Mythic Age": {"prompt": "mythic age setting, legendary sagas", "notes": "Epic era of gods, titans, and heroic epics."},
    "Clockwork Renaissance": {"prompt": "clockwork renaissance metropolis, brasswork skyline", "notes": "Mechanical rebirth blending artistry and automation."},
    "Cyberpunk Dawn": {"prompt": "neon-drenched cyberpunk dawn, megacity sprawl", "notes": "Edge-of-revolt techno metropolis soaked in neon fog."},
    "Frontier Colony": {"prompt": "frontier colony outpost, terraforming rigs", "notes": "Newly settled world balancing survival and exploration."},
    "Magepunk Capital": {"prompt": "magepunk capital spires, arcano-engineered transit", "notes": "City powered by spellwork woven into infrastructure."},
    "Post-Singularity": {"prompt": "post-singularity skylines, post-human society", "notes": "Society navigates coexistence with transcendent AI."},
    "Solar Kingdom": {"prompt": "solar kingdom citadel, mirrored battlements", "notes": "Sun-worshiping empire shimmering with mirrored stone."},
    "Deep Time Ruins": {"prompt": "deep time ruins, subsumed by bioluminescent jungle", "notes": "Fallen civilization enveloped by luminous overgrowth."},
    "Floating Archipelago": {"prompt": "floating archipelago isles, gravitic bridges", "notes": "Linked sky islands anchored by ancient runes."},
    "Quantum Bazaar": {"prompt": "quantum bazaar interdimensional market", "notes": "Marketplace perched between layered realities."},
    "Crystal Regency": {"prompt": "crystal regency court, prismatic halls", "notes": "Opulent monarchy thriving on gemstone alchemy."},
    "Afterlight Reclamation": {"prompt": "afterlight reclamation camps, biolum salvage", "notes": "Post-cataclysm rebuilding focused on sustainable tech."},
    "Aether Age": {"prompt": "aether age dirigibles, brass conduits", "notes": "Era of pseudo-science airships and arcane industry."},
    "Galactic Commons": {"prompt": "galactic commons hub, multicultural convergence", "notes": "Peace-period fostering shared interstellar culture."},
    "Shadow Dominion": {"prompt": "shadow dominion citadels, midnight governance", "notes": "Age where darkness-ruled empires sculpt society."},
    "Eco Renaissance": {"prompt": "eco renaissance arcologies, lush rooftops", "notes": "Green-forward rebirth harmonizing architecture with nature."},
    "Neon Restoration": {"prompt": "neon restoration alleys, vibrant murals", "notes": "Rebuilding dystopian streets with art activism."},
    "Chronicle Epoch": {"prompt": "chronicle epoch archives, time-locked vaults", "notes": "Era dedicated to preserving histories across timelines."},
    "Stellar Crusade": {"prompt": "stellar crusade fleets, radiant armadas", "notes": "Interstellar holy wars shaping galactic borders."},
}

CHARACTER_BODY_TYPE_OPTIONS = {
    "Athletic": {"prompt": "athletic build, balanced musculature", "notes": "Functional physique tuned for mobility and strength."},
    "Slender": {"prompt": "slender frame, poised elegance", "notes": "Graceful lines emphasizing finesse."},
    "Compact": {"prompt": "compact stature, coiled energy", "notes": "Dense power focused in a smaller frame."},
    "Towering": {"prompt": "towering height, elongated proportions", "notes": "Commanding presence with sweeping reach."},
    "Curved": {"prompt": "curved silhouette, soft strength", "notes": "Embraces fullness with confident poise."},
    "Augmented": {"prompt": "augmented bodywork, reinforced plating", "notes": "Engineered enhancements broadening capability."},
    "Aerodynamic": {"prompt": "streamlined physique, aerodynamic contours", "notes": "Built for velocity with minimal drag."},
    "Ethereal": {"prompt": "ethereal weightlessness, semi-translucent form", "notes": "Lightfooted, almost intangible presence."},
    "Stalwart": {"prompt": "stalwart frame, fortress-like build", "notes": "Broad, enduring structure anchored in resilience."},
    "Adaptive": {"prompt": "adaptive biomorph body, shifting contours", "notes": "Morphing physique responding to situational demands."},
    "Willowy": {"prompt": "willowy silhouette, elongated grace", "notes": "Delicate length balanced with flexible poise."},
    "Titanic": {"prompt": "titanic frame, colossal scale", "notes": "Monumental proportions towering above companions."},
    "Featherlight": {"prompt": "featherlight carriage, airy steps", "notes": "Almost weightless movement, hovering transitions."},
    "Stonecarved": {"prompt": "stonecarved musculature, chiseled lines", "notes": "Hard-edged build reminiscent of sculpted statues."},
    "Gossamer": {"prompt": "gossamer ethereality, translucent limbs", "notes": "Fine, delicate structure with subtle translucence."},
    "Cyclonic": {"prompt": "cyclonic spin, coiled torque", "notes": "Body primed for rotational force and sudden action."},
    "Nebulous": {"prompt": "nebulous outline, diffuse limbs", "notes": "Semi-fluid form shifting like condensed mist."},
    "Anchored": {"prompt": "anchored stance, low center", "notes": "Grounded build exuding steadfast stability."},
    "Hybridized": {"prompt": "hybridized morphology, contrasting halves", "notes": "Body blending dual species traits in symmetrical harmony."},
}

CHARACTER_ALIGNMENT_OPTIONS = {
    "Lawful Good": {"prompt": "lawful good code, honorable aura", "notes": "Upholds justice with unwavering ethics."},
    "Neutral Good": {"prompt": "neutral good compassion, balanced heart", "notes": "Helps others guided by empathy over law."},
    "Chaotic Good": {"prompt": "chaotic good rebellion, liberating spark", "notes": "Breaks rules for the greater good."},
    "Lawful Neutral": {"prompt": "lawful neutral discipline, ritual precision", "notes": "Follows codes and hierarchies to the letter."},
    "True Neutral": {"prompt": "true neutral equilibrium, contemplative restraint", "notes": "Seeks balance over allegiance."},
    "Chaotic Neutral": {"prompt": "chaotic neutral unpredictability, personal freedom", "notes": "Acts on instinct, answerable to no one."},
    "Lawful Evil": {"prompt": "lawful evil supremacy, cold authority", "notes": "Twists legal structures for personal gain."},
    "Neutral Evil": {"prompt": "neutral evil opportunism, quiet menace", "notes": "Self-serving tactician with ruthless pragmatism."},
    "Chaotic Evil": {"prompt": "chaotic evil cataclysm, feral grin", "notes": "Unleashes mayhem purely for domination."},
    "Reformed": {"prompt": "reformed antagonist, redemption arc", "notes": "Clawing back toward the light after dark deeds."},
    "Apathetic": {"prompt": "apathetic drift, muted aura", "notes": "Detached from moral stakes, acting only when forced."},
    "Paragon": {"prompt": "paragon brilliance, unwavering ethics", "notes": "Elevated idealist constantly striving for exemplary conduct."},
    "Anarch Idealist": {"prompt": "anarch idealist blaze, banner of autonomy", "notes": "Rejects authority while protecting community freedom."},
    "Pragmatic": {"prompt": "pragmatic balance, evaluating scales", "notes": "Focuses on outcomes over ideology, flexible morality."},
    "Ruthless": {"prompt": "ruthless precision, chill resolve", "notes": "Will sacrifice anything for objectives without remorse."},
    "Devoted": {"prompt": "devoted loyalty, sworn oath light", "notes": "Anchored to vows that guide every decision."},
    "Contrite": {"prompt": "contrite humility, penitent aura", "notes": "Driven by guilt to make amends through action."},
}

CHARACTER_ROLE_OPTIONS = {
    "Party Leader": {"prompt": "party leader coordination, tactical bark", "notes": "Coordinates allies with decisive clarity."},
    "Scout": {"prompt": "pathfinder scout awareness, quiet tread", "notes": "Hunts for vantage and hidden threats."},
    "Support": {"prompt": "support specialist aura, restorative gestures", "notes": "Bolsters allies through buffs and morale."},
    "Artillery": {"prompt": "arcane artillery stance, wide-range focus", "notes": "Rains devastation from a distance."},
    "Face": {"prompt": "party face charm, negotiation toolkit", "notes": "First to speak in courts and bazaars alike."},
    "Infiltrator": {"prompt": "infiltrator shadow-step, code-break tools", "notes": "Silently cracks defenses from within."},
    "Tank": {"prompt": "frontline bulwark posture, threat magnet", "notes": "Soaks enemy focus while allies execute."},
    "Controller": {"prompt": "battlefield controller gestures, zone manipulation", "notes": "Shapes spaces to restrict foes."},
    "Summoner": {"prompt": "summoner sigils, conjured allies", "notes": "Commands linked entities for versatile tactics."},
    "Icon": {"prompt": "cultural icon presence, symbolic costumes", "notes": "Embodies a movement bigger than themselves."},
    "Tactician": {"prompt": "party tactician, battlefield schematics", "notes": "Coordinates formations and counters mid-battle."},
    "Healer": {"prompt": "dedicated healer focus, restorative glow", "notes": "Keeps allies standing through triage and magic."},
    "Saboteur": {"prompt": "behind-the-lines saboteur, trap rig", "notes": "Destroys enemy capabilities before conflicts erupt."},
    "Lorekeeper": {"prompt": "lorekeeper recitation, living archive", "notes": "Supplies critical intel and historical context."},
    "Logistician": {"prompt": "logistician organizer, supply drones", "notes": "Ensures resources and contingency plans never run dry."},
    "Champion": {"prompt": "dueling champion stance, challenge token", "notes": "Takes on the strongest foes in honorable combat."},
    "Handler": {"prompt": "handler coordination, companion command", "notes": "Directs allied creatures or constructs in battle."},
    "Oracle": {"prompt": "battle oracle trance, foresight glow", "notes": "Provides prophetic positions and warnings in real time."},
    "Envoy": {"prompt": "diplomatic envoy, crisis mediation kit", "notes": "Soothes tensions and secures alliances under duress."},
}

WARDROBE_BASE_GARMENT_OPTIONS = {
    "Battle Dress": {"prompt": "battle dress core, reinforced bodice, articulated plating", "notes": "Armor-meets-fashion silhouette balancing protection and movement."},
    "yoga Pants & Tank": {"prompt": "stretch-fit yoga pants paired with breathable tank top", "notes": "Flexible activewear for dynamic poses and fluid motion."},
    "Evening Suit": {"prompt": "sleek evening suit, tailored fit", " notes": "Sophisticated formalwear with sharp lines and classic elegance."},
    "jogging Suit": {"prompt": "lightweight jogging suit, moisture-wicking fabric", "notes": "Sporty ensemble designed for high-energy activity."},
    "Casual Dress": {"prompt": "flowy casual dress, soft fabric", "notes": "Relaxed yet stylish dress perfect for everyday wear."},
    "Formal Gown": {"prompt": "elegant formal gown, intricate detailing", "notes": "Luxurious gown designed for high-society events."},
    "Leather Jacket & Pants": {"prompt": "fitted leather jacket with matching pants", "notes": "Edgy ensemble combining rugged textures with sleek tailoring."},
    "Evening Dress": {"prompt": "glamorous evening dress, sequined accents", "notes": "Dazzling dress ideal for red carpet appearances."},
    "Athletic Shorts & Top": {"prompt": "performance athletic shorts with a supportive top", "notes": "Sport-focused outfit for training and competition."},
    "Combat Gear": {"prompt": "tactical combat gear, reinforced vest, cargo pants", "notes": "Durable outfit built for high-intensity scenarios."},
    "booty Shorts & Crop Top": {"prompt": "casual booty shorts paired with a trendy crop top", "notes": "Playful summer outfit perfect for warm weather."},
    "Evening Jumpsuit": {"prompt": "chic evening jumpsuit, sleek silhouette", "notes": "Modern alternative to traditional gowns for formal occasions."},

    "Tactical Suit": {"prompt": "nano-fiber tactical suit, segmented plating", "notes": "Flexible tactical suit layered with modular attachment points."},
    "Gala Gown": {"prompt": "cascade gala gown, luminescent panels", "notes": "Statement gown engineered for spotlight drama."},
    "Streetwear Ensemble": {"prompt": "layered streetwear ensemble, asymmetric drape", "notes": "Urban streetwear mixing comfort with avant-garde tailoring."},
    "T-Shirt & Jeans": {"prompt": "soft cotton t-shirt paired with lived-in denim jeans", "notes": "Approachable everyday combo for grounded, contemporary storytelling."},
    "Button-Down & Slacks": {"prompt": "crisp button-down shirt with tailored slacks", "notes": "Smart casual office-ready base with clean lines."},
    "Hoodie & Joggers": {"prompt": "cozy hoodie layered over tapered joggers", "notes": "Comfort-forward athleisure ideal for relaxed scenes."},
    "Summer Sundress": {"prompt": "lightweight summer sundress, breezy hem", "notes": "Sun-ready silhouette perfect for daytime leisure moments."},
    "Business Suit": {"prompt": "structured business suit, sharp lapels", "notes": "Professional ensemble projecting confidence and polish."},
    "Casual Shorts Set": {"prompt": "relaxed tee with cuffed shorts", "notes": "Warm-weather casual look for carefree outings."},
    "Athletic Leggings Set": {"prompt": "moisture-wicking athletic tank with compression leggings", "notes": "Performance activewear tuned for training and dynamic motion."},
    "Classic Sweater & Skirt": {"prompt": "chunky knit sweater tucked into pleated skirt", "notes": "Cozy layered look balancing texture and movement."},
    "Bikini Set": {"prompt": "two-piece bikini with supportive top and high-cut bottoms", "notes": "Swim-ready ensemble for poolside or beach visuals."},
    "Swim Trunks": {"prompt": "quick-dry swim trunks with elastic waistband", "notes": "Casual swimwear for aquatic adventures."},
    "Aviator Uniform": {"prompt": "retro aviator uniform, bomber jacket, harnessed straps", "notes": "Flight-ready uniform with nostalgic military cues."},
    "Monastic Robes": {"prompt": "monastic robes, incense-scented fabric, hand-stitched trim", "notes": "Spiritual vestments woven with ceremonial symbolism."},
    "Void Suit": {"prompt": "void-rated suit, thermal seals, reflective plating", "notes": "Spacefaring ensemble engineered for vacuum resilience."},
    "Ranger Leathers": {"prompt": "weathered ranger leathers, botanical embossing", "notes": "Travel-ready leatherwork infused with natural motifs."},
    "Cyber Kimono": {"prompt": "cyber kimono, fiber-optic seams, programmable patterns", "notes": "Traditional silhouette fused with luminous smart textiles."},
    "Mage Tunic": {"prompt": "arcane mage tunic, rune-stitched layers", "notes": "Spellcaster attire optimized for ceremonial focus flows."},
    "Pilot Flight Suit": {"prompt": "pilot flight suit, sealed seams, mission patches", "notes": "All-purpose flight uniform with vacuum-rated protections."},
    "Desert Wraps": {"prompt": "desert nomad wraps, sun-bleached layers", "notes": "Breathable, protective layers designed for arid climates."},
    "Stealth Bodysuit": {"prompt": "stealth bodysuit, adaptive camouflage", "notes": "Low-profile stealth suit with active concealment."},
    "Festival Jumpsuit": {"prompt": "festival jumpsuit, holographic tassels", "notes": "Party-ready jumpsuit with playful color-reactive accents."},
    "Vintage Suit Dress": {"prompt": "mid-century suit dress, cinched waist", "notes": "Retro formalwear channeling classic silhouettes."},
    "Street Armor": {"prompt": "street armor jacket, panel plating", "notes": "Urban battle jacket blending style and protection."},
    "Battle Kimono": {"prompt": "battle kimono, reinforced sleeves, tactical obi", "notes": "War-ready robes designed for martial arts agility."},
    "Synthwave Tracksuit": {"prompt": "synthwave tracksuit, neon piping", "notes": "80s-inspired athletic suit glowing with retro flair."},
    "Explorer Coveralls": {"prompt": "explorer coveralls, tool loops", "notes": "Rugged field suit loaded with expedition-friendly pockets."},
    "Monarch Regalia": {"prompt": "monarch regalia, gem-set bodice", "notes": "Ceremonial finery befitting a ruling sovereign."},
    "Artisan Apron": {"prompt": "artisan apron, paint-splattered", "notes": "Studio-ready layers adorned with creative wear."},
    "Holographic Dress": {"prompt": "holographic dinner dress, shimmering panels", "notes": "Eveningwear projecting shifting light displays."},
    "Mech Pilot Rig": {"prompt": "mech pilot rig, reinforced joints", "notes": "Exosuit-compatible base layer for mechanized combat."},
    "Glacial Parka": {"prompt": "glacial expedition parka, fur-lined hood", "notes": "Insulated outerwear made for frozen vistas."},
    "Operatic Costume": {"prompt": "operatic costume, dramatic farthingale", "notes": "Stage costume bursting with theatrical grandeur."},
    "Biohazard Suit": {"prompt": "biohazard suit, sealed visors", "notes": "Containment gear for hazardous environments."},
    "Lab Coat Set": {"prompt": "tailored lab coat, utility pockets", "notes": "Professional scientific ensemble with clean precision."},
    "Nomad Armor": {"prompt": "nomad armor, scavenged plates", "notes": "Reclaimed armor pieces assembled for wasteland survival."},
    "Ceremonial Hanfu": {"prompt": "ceremonial hanfu, sweeping sleeves", "notes": "Traditional attire layered with historical elegance."},
}

WARDROBE_LAYER_OPTIONS = {
    "Base Layer": {"prompt": "form-fitting base layer, moisture-wicking", "notes": "Second skin layer enhancing mobility and comfort."},
    "Wet Cloth": {"prompt": "wet cloth wrap, clingy texture", "notes": "Damp fabric adding realism to aquatic scenes."},
    "Tactical Vest": {"prompt": "tactical vest, modular pouches", "notes": "Utility vest designed for quick access to gear."},

    "Armor Plating": {"prompt": "layered armor plating, reactive segments", "notes": "Deployable plating that stiffens on impact."},
    "Sheer Overlay": {"prompt": "sheer organza overlay, cascading transparency", "notes": "Gossamer layer that refracts stage lighting."},
    "Draped Cape": {"prompt": "floor-length draped cape, weighted hem", "notes": "Dramatic cloak engineered to billow with motion."},
    "Harness Rig": {"prompt": "utility harness rig, quick-release clasps", "notes": "Functional harness ready for gear clips and tether lines."},
    "Layered Sash": {"prompt": "layered sash bundle, symbolic knots", "notes": "Sashes encoded with cultural symbology and achievements."},
    "Feather Mantle": {"prompt": "feather mantle, iridescent plumage", "notes": "Plumage mantle rippling with chromatic sheen."},
    "Hooded Shawl": {"prompt": "hooded shawl, quieted interior", "notes": "Noise-dampening hood for stealth and focus."},
    "Holster Web": {"prompt": "holster webbing, magnetized docks", "notes": "Holster network distributing signature tools."},
    "Scale Veil": {"prompt": "scale veil drape, metallic tessellation", "notes": "Articulated scales shimmering like liquid metal."},
    "Thermal Cloak": {"prompt": "thermal cloak, heating filaments", "notes": "Climate-responsive cloak shielding from extremes."},
    "Denim Jacket": {"prompt": "faded denim jacket, lived-in creases", "notes": "Casual layer adding texture to modern outfits."},
    "Cardigan": {"prompt": "soft knit cardigan, open front drape", "notes": "Comfortable knit layer ideal for cozy scenes."},
    "Tailored Blazer": {"prompt": "tailored blazer, structured shoulders", "notes": "Polished layer dialing up professional energy."},
    "Raincoat": {"prompt": "lightweight raincoat, snap closures", "notes": "Weather-ready shell keeping things practical."},
    "Fur Stole": {"prompt": "luxury fur stole, draped shoulders", "notes": "Plush accent layer radiating classic glamour."},
    "Holo Poncho": {"prompt": "holo poncho, refractive fringe", "notes": "Digital poncho projecting responsive patterns."},
    "Battle Tabard": {"prompt": "house tabard, banner insignia", "notes": "Battlefield garment emblazoned with heraldry."},
    "Utility Shrug": {"prompt": "utility shrug, magnetic closures", "notes": "Compact shrug integrating quick-access compartments."},
    "Chain Mantle": {"prompt": "chain mantle, draped links", "notes": "Heavy chains draping the shoulders in metallic arcs."},
    "Solar Shawl": {"prompt": "solar shawl, light-absorbing fibers", "notes": "Sun-charged wrap emitting gentle warmth at night."},
    "Wing Harness": {"prompt": "wing harness, kinetic joints", "notes": "Support rig for detachable wings or gliders."},
    "Sequin Bolero": {"prompt": "sequin bolero, cropped sparkle", "notes": "Showpiece bolero packed with glittering sequins."},
    "Tech Gilet": {"prompt": "tech gilet, embedded processors", "notes": "Sleeveless interface layer managing wearable hardware."},
}

WARDROBE_FABRIC_OPTIONS = {
    "Velvet": {"prompt": "plush velvet, deep pile sheen", "notes": "Luxurious velvet catching soft highlights."},
    "Ballistic Weave": {"prompt": "ballistic weave textile, abrasion guard", "notes": "Impact-resistant weave favored by tactical crews."},
    "Silk Brocade": {"prompt": "silk brocade, gold-thread relief", "notes": "Opulent brocade shimmering with embroidered relief."},
    "Smartfabric": {"prompt": "adaptive smartfabric, mood-responsive pigments", "notes": "Interactive textile shifting hue with biometrics."},
    "Holo Mesh": {"prompt": "holographic mesh, prismatic sheen", "notes": "Spectral mesh projecting animated motifs."},
    "Leather": {"prompt": "supple oil-tanned leather, weathered patina", "notes": "Durable leather aged by countless journeys."},
    "Linen": {"prompt": "breathable linen, handloom weave", "notes": "Natural linen lending breathable ease."},
    "Chainmail Lace": {"prompt": "chainmail lace, interlinked micro rings", "notes": "Metallic lacework balancing defense and grace."},
    "Chitin Laminate": {"prompt": "chitin laminate plates, biopolymer sheen", "notes": "Organic exoshell laminate reinforcing structure."},
    "Plasma Gauze": {"prompt": "plasma-reactive gauze, ghostlight shimmer", "notes": "Gauze that glows softly when energized."},
    "Cotton": {"prompt": "soft combed cotton, breathable comfort", "notes": "Everyday cotton knit suited for relaxed wear."},
    "Denim": {"prompt": "sturdy denim twill, indigo wash", "notes": "Classic denim texture adding casual grit."},
    "Fleece": {"prompt": "plush fleece interior, cozy warmth", "notes": "Fleece lining delivering soft insulation."},
    "Jersey Knit": {"prompt": "stretch jersey knit, fluid drape", "notes": "Flexible knit fabric following natural movement."},
    "Neoprene": {"prompt": "sleek neoprene, smooth wetsuit sheen", "notes": "Water-friendly neoprene perfect for swim silhouettes."},
    "SeaSilk": {"prompt": "seasilk fibers, pearl sheen", "notes": "Rare ocean-spun fabric shimmering with aquatic gloss."},
    "Aerogel Weave": {"prompt": "aerogel weave, translucent insulation", "notes": "Ultra-light material offering vacuum-grade insulation."},
    "Reactive Latex": {"prompt": "reactive latex panels, liquid gloss", "notes": "High-shine polymer shifting texture with temperature."},
    "Feather Felt": {"prompt": "feather felt layers, downy softness", "notes": "Feather-compacted textile balancing warmth and lightness."},
    "Nano Knit": {"prompt": "nano-knit fibers, self-healing stitches", "notes": "Microbots continually repair the fabric's surface."},
    "Solar Mesh": {"prompt": "solar mesh filaments, photovoltaic strands", "notes": "Energy-harvesting mesh powering embedded devices."},
    "Crystalline Tulle": {"prompt": "crystalline tulle, glittering nodes", "notes": "Filmy net accented with suspended gemstones."},
    "Biolume Silk": {"prompt": "biolume silk, glowing threads", "notes": "Living silk colony generating soft ambient light."},
    "Memory Denim": {"prompt": "memory denim, shapeshift seams", "notes": "Denim that memorizes personal fits and reshapes as needed."},
}

WARDROBE_ACCESSORY_OPTIONS = {
    "necklace": {"prompt": "ornate necklace, layered chains", "notes": "Statement piece drawing attention to the neckline."},
    "visor": {"prompt": "high-tech visor, HUD display", "notes": "Futuristic eyewear projecting augmented reality."},
    "sunglasses": {"prompt": "sleek sunglasses, tinted lenses", "notes": "Modern shades adding an air of mystery."},
    "bracelets": {"prompt": "stacked bracelets, mixed metals", "notes": "Arm adornments clinking with movement."},
    "Relic Pendant": {"prompt": "relic pendant, memory-locked gem", "notes": "Pendant storing ancestral recordings."},
    "Utility Belt": {"prompt": "utility belt, compartmentalized pouches", "notes": "Belt organizing mission-critical tools."},
    "Quantum Bracelets": {"prompt": "quantum-entangled bracelets, flickering runes", "notes": "Linked bracelets enabling instant communication."},
    "Feathered Circlet": {"prompt": "feathered circlet, iridescent quills", "notes": "Headpiece crowned with skyborn plumage."},
    "Aether Earrings": {"prompt": "aether earrings, suspended crystals", "notes": "Earrings humming with harmonic resonance."},
    "Tactical Visor": {"prompt": "tactical visor, augmented reality HUD", "notes": "Visor projecting real-time battlefield overlays."},
    "Potion Bandolier": {"prompt": "potion bandolier, alchemical vials", "notes": "Bandolier stocked with quick-access elixirs."},
    "Charm Bangles": {"prompt": "charm bangles, layered talismans", "notes": "Bracelets jingling with protective charms."},
    "Void Gloves": {"prompt": "void-channeling gloves, fingerless design", "notes": "Gloves designed to safely redirect cosmic currents."},
    "Monocle Display": {"prompt": "monocle display, rotating data readouts", "notes": "Augmented monocle feeding curated intel."},
    "Baseball Cap": {"prompt": "soft baseball cap, curved brim", "notes": "Casual cap that instantly relaxes a look."},
    "Sunglasses": {"prompt": "sleek sunglasses, tinted lenses", "notes": "Shades that add modern swagger and sun protection."},
    "Tote Bag": {"prompt": "canvas tote bag, printed graphic", "notes": "Everyday carryall keeping essentials close."},
    "Data Sash": {"prompt": "data sash holsters, scrolling LEDs", "notes": "Sash storing encrypted data strips for quick reference."},
    "Storm Umbrella": {"prompt": "storm umbrella, lightning rod spine", "notes": "Weatherproof parasol doubling as electro-shield."},
    "Astrolabe Brooch": {"prompt": "astrolabe brooch, rotating rings", "notes": "Pin that charts stellar alignments in real time."},
    "Pulse Anklets": {"prompt": "pulse anklets, kinetic lights", "notes": "Anklets emitting rhythmic glows synchronized with movement."},
    "Holster Purse": {"prompt": "holster purse, tactical compartments", "notes": "Crossover bag balancing style and functionality."},
    "Glyph Gloves": {"prompt": "glyph gloves, glowing sigils", "notes": "Gloves projecting spell matrices during gestures."},
    "Rebreather Necklace": {"prompt": "rebreather necklace, collapsible mouthpiece", "notes": "Emergency respirator disguised as elegant jewelry."},
    "Signal Fan": {"prompt": "signal fan, colored transmitters", "notes": "Fan that conveys covert signals via shifting hues."},
    "Chrono Cuff": {"prompt": "chrono cuff, time-stop dial", "notes": "Temporal cuff offering short-duration field slowdowns."},
}

WARDROBE_FOOTWEAR_OPTIONS = {
    "tennis Shoes": {"prompt": "tennis shoes, cushioned sole", "notes": "Sporty footwear built for agility and comfort."},
    "no shoes": {"prompt": "bare feet, natural stance", "notes": "Unshod feet connecting directly with the ground."},
    "Dress Shoes": {"prompt": "polished dress shoes, leather finish", "notes": "Classic formal footwear elevating any outfit."},
    "Sneakers": {"prompt": "casual sneakers, breathable mesh", "notes": "Comfortable shoes for everyday wear."},
    "Slip-Ons": {"prompt": "casual slip-ons, elastic side panels", "notes": "Easy-wear shoes for laid-back days."},
    "Combat Boots": {"prompt": "combat boots, reinforced toe, shock absorbers", "notes": "Mil-spec boots tuned for stability."},
    "Hover Heels": {"prompt": "hover heels, anti-grav emitters", "notes": "Levitation-boosted footwear gliding with each step."},
    "Barefoot Wraps": {"prompt": "barefoot wraps, pressure-mapped grip", "notes": "Foot wraps enabling silent movement."},
    "Ceremonial Sandals": {"prompt": "ceremonial sandals, gilt straps", "notes": "Ritual sandals echoing ancient rites."},
    "Tactical Greaves": {"prompt": "tactical greaves, knee articulation", "notes": "Armored greaves safeguarding lower limbs."},
    "Riding Boots": {"prompt": "knee-high riding boots, polished leather", "notes": "Equestrian boots suited for long journeys."},
    "Mag Boots": {"prompt": "magnetic mag boots, hull-walk capable", "notes": "Zero-g rated boots anchoring to metallic surfaces."},
    "Pulse Sneakers": {"prompt": "pulse sneakers, energy return midsole", "notes": "Athletic footwear with reactive cushioning."},
    "Gilded Slippers": {"prompt": "gilded slippers, opaline finish", "notes": "Luxury slippers radiating opulent charm."},
    "Gecko Pads": {"prompt": "gecko grip pads, wall-scaling microfibers", "notes": "Microfiber pads adhering to vertical terrain."},
    "Classic Sneakers": {"prompt": "classic lace-up sneakers, rubber sole", "notes": "Everyday sneakers built for all-day comfort."},
    "Leather Loafers": {"prompt": "polished leather loafers, stacked heel", "notes": "Smart slip-on footwear for business casual looks."},
    "Strappy Sandals": {"prompt": "strappy leather sandals, cork footbed", "notes": "Warm-weather sandals perfect for beach scenes."},
    "Flip Flops": {"prompt": "foam flip flops, casual beachwear", "notes": "Simple beach footwear for relaxed narratives."},
    "Heeled Ankle Boots": {"prompt": "heeled ankle boots, suede finish", "notes": "Versatile heeled boots adding height and style."},
    "Crystal Heels": {"prompt": "crystal heels, prismatic lift", "notes": "Faceted heels refracting light trails with each step."},
    "Sandwalkers": {"prompt": "sandwalker boots, dune grip", "notes": "Desert-adapted boots dispersing heat and sand."},
    "Storm Galoshes": {"prompt": "storm galoshes, insulating seal", "notes": "Weather armor boots built for torrential conditions."},
    "Kinetic Skates": {"prompt": "kinetic skates, retractable wheels", "notes": "Footwear switching between high-speed glide and stable stance."},
    "Forest Claspers": {"prompt": "forest clasper boots, root hooks", "notes": "Tree-climbing boots with adaptive grip tendrils."},
    "Exo Talons": {"prompt": "exo talon greaves, clawed toes", "notes": "Augmented talons for vertical scaling in heavy armor."},
    "Ceremonial Geta": {"prompt": "ceremonial geta, lacquered platforms", "notes": "Traditional elevated sandals adorned with painted motifs."},
    "Void Slippers": {"prompt": "void slippers, anti-sound lining", "notes": "Silent slippers favored by stealth operatives."},
    "Solar Trainers": {"prompt": "solar trainers, lightstrip soles", "notes": "Footwear powered by sunlight to enhance sprinting bursts."},
}

HUMAN_DESIGN_GENDER_OPTIONS = {
    "Adult Woman": {
        "prompt": "adult woman",
        "notes": "Explicitly 18+ feminine presentation with mature proportions.",
    },
    "Adult Man": {
        "prompt": "adult man",
        "notes": "Explicitly 18+ masculine presentation with mature stature.",
    },
    "Adult Female": {
        "prompt": "adult female body",
        "notes": "Female anatomy described with respectful, adult-focused language.",
    },
    "Adult Male": {
        "prompt": "adult male body",
        "notes": "Male anatomy described with respectful, adult-focused language.",
    },
    "Adult Androgynous": {
        "prompt": "adult androgynous figure",
        "notes": "Elegant, mature androgyny blending traditionally masculine and feminine cues.",
    },

}

HUMAN_DESIGN_HEIGHT_OPTIONS = {
    "Super Short": {
        "prompt": "super short height around 4'6\" / 137 cm",
        "notes": "Very short stature with a compact frame.",
    },
    "Super petite": {
        "prompt": "super petite stature around 5'0\" / 152 cm",
        "notes": "Very short stature with a compact frame.",
    },
    "Petite": {
        "prompt": "petite stature around 5'2\" / 157 cm",
        "notes": "Compact height with graceful proportions.",
    },
    "Average": {
        "prompt": "average height near 5'7\" / 170 cm",
        "notes": "Balanced height typical for adult humans.",
    },
    "Curvy": {
        "prompt": "curvy frame around 5'5\" / 165 cm",
        "notes": "Softly rounded proportions with an emphasis on curves.",
    },

    "Base Male" : {
        "prompt": "average male height around 5'9\" / 175 cm",
        "notes": "Standard male proportions with a balanced silhouette.",
    },


    "Tall": {
        "prompt": "tall frame around 6'1\" / 185 cm",
        "notes": "Notably tall presence with extended reach.",
    },
    "Towering": {
        "prompt": "towering height near 6'6\" / 198 cm",
        "notes": "Commanding height that stands out immediately.",
    },
    "Diminutive": {
        "prompt": "diminutive height around 4'11\" / 150 cm",
        "notes": "Very short adult frame with agile stature.",
    },
    "Statuesque": {
        "prompt": "statuesque height near 5'11\" / 180 cm",
        "notes": "Gracefully tall proportions ideal for striking silhouettes.",
    },
    "Colossal": {
        "prompt": "colossal height approaching 7'2\" / 218 cm",
        "notes": "Extraordinary height suited to mythical or augmented figures.",
    },
    "Average Tall": {
        "prompt": "above-average height near 5'9\" / 175 cm",
        "notes": "Subtly tall without feeling out of place in everyday scenes.",
    },
    "Average Short": {
        "prompt": "below-average height near 5'4\" / 163 cm",
        "notes": "Slightly short adult presence balancing reach and comfort.",
    },
}

HUMAN_DESIGN_FACE_OPTIONS = {
    "Oval": {
        "prompt": "oval face, gently tapered jawline",
        "notes": "Balanced proportions with softly rounded features.",
    },
    "Heart": {
        "prompt": "heart-shaped face, prominent cheekbones, tapered chin",
        "notes": "Expressive cheek structure with a delicate chin.",
    },
    "Angular": {
        "prompt": "angular face, sharp jawline, defined cheek planes",
        "notes": "Sculpted geometry lending dramatic presence.",
    },
    "Round": {
        "prompt": "round face, full cheeks, soft jawline",
        "notes": "Youthful softness paired with smooth contours.",
    },
    "Diamond": {
        "prompt": "diamond face, high cheekbones, narrow forehead and chin",
        "notes": "Faceted elegance with striking cheek definition.",
    },
    "Square": {
        "prompt": "square face, broad jawline, even forehead width",
        "notes": "Defined angles conveying strength and confidence.",
    },
    "Triangular": {
        "prompt": "triangular face, tapered forehead, wider jaw",
        "notes": "Foundation-heavy shape grounded by solid jawlines.",
    },
    "Oblong": {
        "prompt": "oblong face, elongated proportions, gentle angles",
        "notes": "Extended vertical lines with refined slender elegance.",
    },
    "Heart-Soft": {
        "prompt": "soft heart face, rounded hairline, subtle chin",
        "notes": "Heart-shaped nuance softened by gentle contours.",
    },
}

HUMAN_DESIGN_BODY_TYPE_OPTIONS = {
    "Athletic": {
        "prompt": "athletic muscle tone, defined limbs",
        "notes": "Functional strength with evident conditioning.",
    },
    "Soft Curvy": {
        "prompt": "soft curvy build with gentle lines",
        "notes": "Supple silhouette favoring plush contours.",
    },
    "Lean": {
        "prompt": "lean physique, long lines",
        "notes": "Slender frame emphasizing graceful length.",
    },
    "Stocky": {
        "prompt": "stocky build, dense musculature",
        "notes": "Compact power with grounded stance.",
    },
    "Plus Size": {
        "prompt": "plus-size figure with full curves",
        "notes": "Celebrates abundant curves with confident posture.",
    },
    "Muscular": {
        "prompt": "muscular build with pronounced definition",
        "notes": "Gym-honed physique showcasing sculpted muscle groups.",
    },
    "Willowy": {
        "prompt": "willowy frame, delicate limbs",
        "notes": "Graceful slenderness paired with airy posture.",
    },
    "Broad": {
        "prompt": "broad build, expanded shoulders",
        "notes": "Wide frame projecting steadfast presence.",
    },
    "Average": {
        "prompt": "average build, balanced proportions",
        "notes": "Everyday physique offering versatile styling.",
    },
}

HUMAN_DESIGN_BODY_SHAPE_OPTIONS = {
    "Hourglass": {
        "prompt": "hourglass proportions, balanced bust and hips, defined waist",
        "notes": "Classic hourglass balance with prominent waist definition.",
    },
    "Super Model": {
        "prompt": "super model proportions, tall and slender with long limbs",
        "notes": "Exaggerated height and length creating a striking silhouette.",
    },

    "Rectangle": {
        "prompt": "rectangular proportions, parallel lines from shoulders to hips",
        "notes": "Athletic straight silhouette with minimal taper.",
    },
    "Pear": {
        "prompt": "pear shape, narrower shoulders, fuller hips and thighs",
        "notes": "Lower-body emphasis creating grounded elegance.",
    },
    "Inverted Triangle": {
        "prompt": "inverted triangle shape, broad shoulders, tapered hips",
        "notes": "Upper-body strength tapering to lean hips.",
    },
    "Apple": {
        "prompt": "apple shape, fuller midsection with rounded torso",
        "notes": "Central softness complemented by smooth limbs.",
    },
    "Athletic V": {
        "prompt": "athletic V shape, sculpted shoulders tapering waist",
        "notes": "Sport-driven silhouette defined by upper-body strength.",
    },
    "Diamond": {
        "prompt": "diamond shape, fuller midsection and shoulders, narrow hips",
        "notes": "Eye-catching mid-body emphasis with tapered hip line.",
    },
    "Oval": {
        "prompt": "oval shape, soft curve distribution",
        "notes": "Gentle fullness evenly wrapped around torso.",
    },
    "Straight": {
        "prompt": "straight column shape, minimal waist definition",
        "notes": "Clean linear silhouette ideal for draped garments.",
    },
}

HUMAN_DESIGN_HAIR_LENGTH_OPTIONS = {

    "Short": {
        "prompt": "short hair, just above the shoulders",
        "notes": "Chic and easy-to-maintain length with versatile styling options.",
    },

    "Medium": {
        "prompt": "medium-length hair, grazing the collarbone",
        "notes": "Versatile length allowing for various styling options.",
    },

    "Pixie": {
        "prompt": "pixie-length hair cropped close to the scalp",
        "notes": "Playful short crop attracting focus to facial structure.",
    },
    "Chin": {
        "prompt": "chin-length hair framing the jaw",
        "notes": "Tailored bob emphasizing jawline definition.",
    },
    "Shoulder": {
        "prompt": "shoulder-length hair resting on the collarbones",
        "notes": "Versatile medium length suited for numerous styles.",
    },
    "Mid-back": {
        "prompt": "mid-back length hair with flowing strands",
        "notes": "Luxurious length that sways with movement.",
    },
    "Floor": {
        "prompt": "dramatically long hair trailing toward the floor",
        "notes": "Fantastical length creating ethereal motion.",
    },
    "Buzz": {
        "prompt": "buzz-cut hair, ultra-short stubble",
        "notes": "Crisp close shave showcasing head shape.",
    },
    "Ear": {
        "prompt": "ear-length crop, playful bounce",
        "notes": "Short cut brushing the ears for lively motion.",
    },
    "Waist": {
        "prompt": "waist-length hair, heavy braid potential",
        "notes": "Sweeping length ideal for intricate styling.",
    },
    "Cascading": {
        "prompt": "cascading layered hair, mid-waist flow",
        "notes": "Layered lengths adding dynamic movement.",
    },
}

HUMAN_DESIGN_HAIR_COLOR_OPTIONS = {
    "Deep Brunette": {
        "prompt": "deep brunette hair with espresso undertones",
        "notes": "Rich brown palette catching warm highlights.",
    },
    "Chestnut Brown": {
        "prompt": "chestnut brown hair with auburn hints",
        "notes": "Warm brown tones enriched with subtle red undertones.",
    },
    "Bimbo Blonde"  : {
        "prompt": "bimbo blonde hair, bright and eye-catching",
        "notes": "Vibrant platinum shades with high shine.",
    },
    "Ash Brown": {
        "prompt": "ash brown hair with cool undertones",
        "notes": "Muted brown spectrum with smoky highlights.",
    },
    "Jet Black": {
        "prompt": "jet black hair, deep and glossy",
        "notes": "Intense black hue reflecting light beautifully.",
    },
    "Golden Blonde": {
        "prompt": "golden blonde hair with sunlit glow",
        "notes": "Radiant blonde gradients with bright sheen.",
    },
    "Copper Red": {
        "prompt": "copper red hair with fiery vibrance",
        "notes": "Spirited red spectrum glowing under light.",
    },
    "Midnight Black": {
        "prompt": "midnight black hair, mirror-gloss finish",
        "notes": "Inky black hair delivering striking contrast.",
    },
    "Silver": {
        "prompt": "silver hair with metallic shimmer",
        "notes": "Cool silver tones hinting at ethereal maturity.",
    },
    "Fantasy Pastel": {
        "prompt": "pastel fantasy hair blending cotton-candy hues",
        "notes": "Playful colorway spanning lilac, teal, and blush.",
    },
    "Icy Platinum": {
        "prompt": "icy platinum hair, frosted sheen",
        "notes": "Bleached platinum with glacial sparkle.",
    },
    "Rose Gold": {
        "prompt": "rose gold hair, metallic blush",
        "notes": "Warm rosy metallic tones shimmering softly.",
    },
    "Emerald Green": {
        "prompt": "emerald green hair, jewel-toned depth",
        "notes": "Vibrant green cascade reminiscent of enchanted forests.",
    },
    "Midnight Blue": {
        "prompt": "midnight blue hair, cosmic lowlights",
        "notes": "Deep indigo hue echoing star-streaked skies.",
    },
}

HUMAN_DESIGN_HAIR_STYLE_OPTIONS = {
    "Sleek Straight": {
        "prompt": "sleek straight hair, smooth and polished",
        "notes": "Glass-like finish with disciplined alignment.",
    },
    "Loose Waves": {
        "prompt": "loose waves cascading with gentle movement",
        "notes": "Relaxed wave pattern suggesting soft motion.",
    },
    "Defined Curls": {
        "prompt": "defined curls spiraling with springy volume",
        "notes": "Structured curls amplifying texture and bounce.",
    },
    "Braided Crown": {
        "prompt": "braided crown wrapping the head",
        "notes": "Intricate braiding delivering regal symmetry.",
    },
    "Locs": {
        "prompt": "shoulder-length locs with neat sectioning",
        "notes": "Textured locs celebrating cultural heritage.",
    },
    "Shaved Fade": {
        "prompt": "shaved sides with tapered fade and longer top",
        "notes": "Bold undercut combining edge with styling versatility.",
    },
    "High Ponytail": {
        "prompt": "high ponytail swept upward, dynamic lift",
        "notes": "Energetic style emphasizing motion and confidence.",
    },
    "Space Buns": {
        "prompt": "double space buns perched atop the head",
        "notes": "Playful style balancing symmetry and whimsy.",
    },
    "Fishtail Braid": {
        "prompt": "fishtail braid draping over one shoulder",
        "notes": "Detailed plait showcasing craftsmanship and texture.",
    },
    "Afro": {
        "prompt": "rounded afro halo, voluminous coils",
        "notes": "Proud natural coil shape radiating strength.",
    },
    "Vintage Rolls": {
        "prompt": "vintage victory rolls framing the crown",
        "notes": "Retro glam styling channeling mid-century flair.",
    },
}

HUMAN_DESIGN_GENITAL_OPTIONS = {
    "Vulva Regular": {
        "prompt": "adult vulva anatomy with soft natural contours",
        "notes": "18+ only: describe consensual feminine anatomy respectfully.",
    },
    "Vulva Detailed": {
        "prompt": "detailed adult vulva anatomy with realistic texture",
        "notes": "18+ only: provide anatomically accurate feminine detail with care.",
    },
    "Vulva Detailed Innie"  : {
        "prompt": "detailed adult vulva anatomy with pronounced inner labia",
        "notes": "18+ only: focus on inner labial detail with respectful language.",
    },
    "Vulva Detailed Outie": {
        "prompt": "detailed adult vulva anatomy with pronounced outer labia",
        "notes": "18+ only: focus on outer labial detail with respectful language.",
    },
    "Vulva Covered": {
        "prompt": "covered adult vulva beneath garments",   
        "notes": "18+ only: indirect reference emphasizing modest coverage.",
    },
    "Vulva Regular": {
        "prompt": "adult vulva anatomy with soft natural contours",
        "notes": "18+ only: describe consensual feminine anatomy respectfully.",
    },
    "Highly Detailed Vulva Close Up" : {
        "prompt": "highly detailed adult vulva anatomy with intricate texture and shading,  Vulva detail close-up",
        "notes": "18+ only: provide anatomically accurate feminine detail with care.",
    },
    "Highly Detailed Vulva": {
        "prompt": "highly detailed adult vulva anatomy with intricate texture and shading",
        "notes": "18+ only: provide anatomically accurate feminine detail with care.",
    },
    "Penis": {
        "prompt": "adult penis anatomy with mature proportion",
        "notes": "18+ only: describe consensual masculine anatomy respectfully.",
    }, 

    "Discrete": {
        "prompt": "discreet reference to adult anatomy without explicit detail",
        "notes": "18+ only: suggest presence subtly, prioritizing tasteful framing.",
    },
    "Covered": {
        "prompt": "covered adult anatomy beneath garments",
        "notes": "18+ only: indirect reference emphasizing modest coverage.",
    },
}

HUMAN_DESIGN_EYE_DETAIL_OPTIONS = {
    "Almond Focus": {
        "prompt": "almond-shaped eyes with soft outer taper",
        "notes": "Balanced eye shape conveying attentive, relaxed focus.",
    },
    "Round Radiance": {
        "prompt": "round eyes with luminous openness",
        "notes": "Rounded eyes projecting curiosity and emotive clarity.",
    },
    "Monolid Grace": {
        "prompt": "sleek monolid eyes with gentle fold",
        "notes": "Elegant monolid structure celebrated with respect.",
    },
    "Hooded Mystery": {
        "prompt": "hooded eyes with soft upper lid shadow",
        "notes": "Naturally shaded lids that accentuate subtle expressions.",
    },
    "Upturned Spark": {
        "prompt": "upturned eyes with lifted outer corners",
        "notes": "Playful uplift adding lively charm to the gaze.",
    },
    "Downturned Poise": {
        "prompt": "downturned eyes with thoughtful softness",
        "notes": "Gentle downward tilt evoking contemplative serenity.",
    },
}

HUMAN_DESIGN_EYE_COLOR_OPTIONS = {
    "Amber Luminescence": {
        "prompt": "amber eyes with sunlit flecks",
        "notes": "Warm golden irises catching honeyed highlights.",
    },
    "Brown Earth": {
        "prompt": "rich brown eyes with chocolate depth",
        "notes": "Deep brown irises exuding grounded warmth.",
    },
    "Hazel Glow": {
        "prompt": "hazel eyes with flecks of green and gold",
        "notes": "Dynamic hazel tones shifting with light.",
    },
    "Grey Mist": {
        "prompt": "grey eyes with silvery undertones",
        "notes": "Cool grey irises reflecting soft metallic hues.",
    },
    "Ocean Blue": {
        "prompt": "ocean blue eyes with mirrored sheen",
        "notes": "Vivid blue irises reflecting cool maritime depth.",
    },
    "Verdant Green": {
        "prompt": "emerald green eyes with jewel clarity",
        "notes": "Brilliant green gaze reminiscent of forest light.",
    },
    "Smoky Hazel": {
        "prompt": "smoky hazel eyes with amber halo",
        "notes": "Hazel irises blending brown and gold undertones.",
    },
    "Warm Brown": {
        "prompt": "warm brown eyes with soft chestnut depth",
        "notes": "Comforting brunette hues radiating grounded warmth.",
    },
    "Silver Grey": {
        "prompt": "silver grey eyes with crystal shimmer",
        "notes": "Cool grey irises catching metallic highlights.",
    },
    "Violet Aura": {
        "prompt": "violet eyes with rare amethyst glow",
        "notes": "Distinctive violet tint lending dreamlike allure.",
    },
}

HUMAN_DESIGN_SKIN_TONE_OPTIONS = {
    "Porcelain Dawn": {
        "prompt": "porcelain skin with peach undertone",
        "notes": "Luminous fair complexion carrying gentle warmth.",
    },
    "Warm Honey": {
        "prompt": "warm honey skin with golden undertone",
        "notes": "Sun-touched glow radiating healthy vibrance.",
    },
    "Golden Olive": {
        "prompt": "golden olive skin with sunlit depth",
        "notes": "Mediterranean-inspired tones balancing green-gold undertones.",
    },
    "Copper Ember": {
        "prompt": "copper skin with burnished highlights",
        "notes": "Rich copper warmth reflecting fiery brilliance.",
    },
    "Rich Umber": {
        "prompt": "rich umber skin with velvety depth",
        "notes": "Deep brown complexion glowing with lowlight sheen.",
    },
    "Espresso Luxe": {
        "prompt": "espresso skin with satin finish",
        "notes": "Inky deep complexion accented by subtle sheen.",
    },
    "Rosy Beige": {
        "prompt": "rosy beige skin with flushed highlights",
        "notes": "Neutral beige infused with natural rosy bloom.",
    },
    "Cool Mocha": {
        "prompt": "cool mocha skin with muted undertone",
        "notes": "Balanced cool-toned brown offering refined softness.",
    },
    "Alabaster Glow": {
        "prompt": "alabaster skin with icy undertone",
        "notes": "Very fair complexion with cool, ethereal highlights.",
    },
    "Deep Ebony": {
        "prompt": "deep ebony skin with rich undertone",
        "notes": "Luxurious dark complexion exuding radiant depth.",
    },
    "Caramel Bronze": {
        "prompt": "caramel bronze skin with sun-kissed warmth",
        "notes": "Medium bronze tone glowing with golden highlights.",
    },
    "Sandy Taupe": {
        "prompt": "sandy taupe skin with neutral balance",
        "notes": "Light brown complexion with balanced warm-cool undertones.",
    },
    "Mahogany Rich": {
        "prompt": "mahogany skin with deep reddish undertone",
        "notes": "Dark brown complexion enriched with warm red hues.",
    },
    "Ivory Silk": {
        "prompt": "ivory skin with soft peach undertone",
        "notes": "Light complexion with a hint of warm blush.",
    },
    "Bronze Glow": {
        "prompt": "bronze skin with radiant warmth",
        "notes": "Medium-dark complexion shimmering with golden highlights.",
    },
}

HUMAN_DESIGN_SKIN_DETAIL_OPTIONS = {
    "Soft Glow": {
        "prompt": "skin softly luminous with dewy finish",
        "notes": "Hydrated complexion with ambient light reflection.",
    },
    "Realsitic" : {
        "prompt": "realistic skin with natural texture and pores",
        "notes": "Authentic skin detail showcasing natural imperfections.",
    },
    "Velvet Matte": {
        "prompt": "skin with velvet matte texture",
        "notes": "Powdery matte finish highlighting contour definition.",
    },
    "Sun-Kissed Freckles": {
        "prompt": "sun-kissed freckles dusted across cheeks",
        "notes": "Sprinkled freckles celebrating authentic outdoor life.",
    },
    "Glazed Highlight": {
        "prompt": "glazed highpoints catching radiant sheen",
        "notes": "Glassy highlights accenting cheekbones and brow ridge.",
    },
    "Marble Smooth": {
        "prompt": "marble-smooth skin with refined pores",
        "notes": "Even texture delivering polished elegance.",
    },
    "Lived-In Realism": {
        "prompt": "lived-in skin with subtle lines and warmth",
        "notes": "Mature complexion honoring natural texture and history.",
    },
    "Studio Gloss": {
        "prompt": "studio-lit skin with editorial gloss",
        "notes": "High-fashion sheen ideal for dramatic lighting.",
    },
}

HUMAN_DESIGN_BEAUTY_MARK_OPTIONS = {
    "Bare": {
        "prompt": "",
        "notes": "Natural canvas without notable beauty marks.",
    },
    "Cheek Spot": {
        "prompt": "distinct beauty mark on the cheek",
        "notes": "Classic facial mark adding character and charm.",
    },
    "Neck Accent": {
        "prompt": "subtle beauty mark on the neck",
        "notes": "Delicate mark enhancing neckline allure.",
    },
    "Shoulder Fleck": {
        "prompt": "small fleck on the shoulder",
        "notes": "Understated mark adding unique detail.",
    },
    "Shoulder Star": {
        "prompt": "beauty mark shaped like a star on the shoulder",
        "notes": "Celestial-inspired mark adding whimsical touch.",
    },
    "Back Dimple": {
        "prompt": "tiny dimple beauty mark on the upper back",
        "notes": "Subtle back detail enhancing skin texture.",
    },
    "Cheek Constellation": {
        "prompt": "cluster of freckles across cheeks",
        "notes": "Freckle constellation adding playful charm.",
    },
    "Upper Lip Signature": {
        "prompt": "signature beauty mark above the lip",
        "notes": "Classic beauty mark evoking vintage glamour.",
    },
    "Collarbone Accent": {
        "prompt": "beauty mark resting at the collarbone",
        "notes": "Subtle mark drawing attention to neckline.",
    },
    "Eye Corner Fleck": {
        "prompt": "tiny fleck near the outer eye corner",
        "notes": "Delicate mark accentuating expressive gaze.",
    },
    "Shoulder Star": {
        "prompt": "freckle cluster along the shoulder",
        "notes": "Sun-kissed marks emphasizing lived-in warmth.",
    },
    "Hip Muse": {
        "prompt": "beauty mark along the hip curve",
        "notes": "Intimate placement adding bespoke allure.",
    },
}

WARDROBE_COLORWAY_OPTIONS = {
    "Monochrome Obsidian": {"prompt": "monochrome obsidian palette, layered blacks, matte to gloss", "notes": "Black-on-black layering emphasizing texture over hue."},
    "Solar Burst": {"prompt": "solar burst gradient, saffron to rose gold", "notes": "Sunrise gradient igniting dramatic silhouettes."},
    "Moonlit Pastel": {"prompt": "moonlit pastel wash, lavender mist, silver trims", "notes": "Soft pastels cooled by moonlit silver accents."},
    "Aqua Neon": {"prompt": "aqua neon spectrum, cyan energy veins", "notes": "Vibrant teal with electric highlights."},
    "Autumn Ember": {"prompt": "autumn ember palette, russet, ember orange", "notes": "Warm autumn hues echoing fallen leaves."},
    "Verdigris": {"prompt": "verdigris patina, weathered copper tones", "notes": "Aged metal palette blending green and bronze."},
    "Storm Prism": {"prompt": "storm prism palette, slate blues, lightning white", "notes": "Storm-swept palette with flashes of brilliance."},
    "Ivory & Ink": {"prompt": "ivory and ink contrast, sharp monochrome", "notes": "High contrast interplay of pale and dark surfaces."},
    "Sunset Hologram": {"prompt": "sunset hologram iridescence, shifting magenta gold", "notes": "Angle-dependent holographic sunset sheen."},
    "Toxic Bloom": {"prompt": "toxic bloom palette, biohazard lime, ultraviolet trim", "notes": "Bold palette evoking bioluminescent flora."},
    "Classic Black": {"prompt": "classic black palette, matte and satin blacks", "notes": "Monochrome black styling for timeless minimalism."},
    "Soft Pastels": {"prompt": "soft pastel palette, powder pink, sky blue, mint", "notes": "Gentle candy hues perfect for casual looks."},
    "Earthy Neutrals": {"prompt": "earthy neutrals, warm beige, olive, terracotta", "notes": "Natural neutral mix for grounded realism."},
    "Primary Pop": {"prompt": "primary color pop, bold red, cobalt, sunshine yellow", "notes": "High-energy palette with graphic clarity."},
    "Denim Blues": {"prompt": "denim blue gradient, indigo to faded sky", "notes": "Layered denim-inspired blues for casual wear."},
    "Beach Brights": {"prompt": "beach brights, coral, seafoam, sunbleached white", "notes": "Vibrant beach palette tailored for swim looks."},
    "Arcane Jewel": {"prompt": "arcane jewel tones, amethyst, sapphire, emerald", "notes": "Opulent jewel palette tuned for mage aesthetics."},
    "Cyber Chrome": {"prompt": "cyber chrome palette, silver, electric teal", "notes": "High-gloss metallics paired with neon accents."},
    "Forest Canopy": {"prompt": "forest canopy palette, moss, pine, bark", "notes": "Layered greens capturing woodland depth."},
    "Ember Noir": {"prompt": "ember noir palette, charcoal with ember highlights", "notes": "Smoldering interplay of blackened reds and smoke."},
    "Polar Shift": {"prompt": "polar shift palette, glacier blue, aurora mint", "notes": "Arctic cool palette with luminous ice highlights."},
    "Desert Dusk": {"prompt": "desert dusk palette, mauve sand, twilight purple", "notes": "Muted desert sunset blending warmth and cool."},
    "Vintage Sepia": {"prompt": "vintage sepia wash, parchment tan, faded brown", "notes": "Retro palette invoking aged photographs."},
    "Candy Pop": {"prompt": "candy pop palette, bubblegum pink, lemon fizz", "notes": "Sugary high-saturation palette for playful styling."},
    "Industrial Rust": {"prompt": "industrial rust palette, oxidized orange, iron", "notes": "Weathered industrial hues suggesting grit and age."},
}

WARDROBE_PATTERN_OPTIONS = {
    "Fractal": {"prompt": "fractal tessellation pattern, recursive geometry", "notes": "Endless fractal motif that feels otherworldly."},
    "Constellation": {"prompt": "constellation embroidery, starlit map", "notes": "Star chart motifs mapping ancestral skies."},
    "Circuitry": {"prompt": "circuit board etching, luminous trace", "notes": "Printed circuits glowing with micro current."},
    "Runic": {"prompt": "runic etching, glowing sigils", "notes": "Glyph script broadcasting protective wards."},
    "Botanical": {"prompt": "botanical prints, climbing vines", "notes": "Organic floral motifs wrapping the silhouette."},
    "Animalistic": {"prompt": "animalistic spotting, gradient stripes", "notes": "Predatory patterns referencing apex creatures."},
    "Plaid": {"prompt": "precision plaid, woven geometry", "notes": "Classic plaid reinterpreted in modern textiles."},
    "Iridescent Marbling": {"prompt": "iridescent marbling, fluid swirls", "notes": "Liquid marble finish shimmering with color shifts."},
    "Sacred Geometry": {"prompt": "sacred geometry lattice, balanced symmetry", "notes": "Meditative geometry aligning chakral flow."},
    "Microtext": {"prompt": "microtext inscriptions, hidden messages", "notes": "Tiny script carrying encoded lore."},
    "Solid": {"prompt": "solid color finish, clean tone", "notes": "Simple solid base letting silhouette shine."},
    "Stripes": {"prompt": "striped pattern, alternating bands", "notes": "Classic stripes adding rhythm and direction."},
    "Polka Dot": {"prompt": "polka dot scatter, playful speckles", "notes": "Cheerful polka dots injecting retro charm."},
    "Chevron": {"prompt": "chevron zigzag, bold angles", "notes": "Dynamic zigzag adding directional energy."},
    "Paisley": {"prompt": "paisley swirls, ornate teardrops", "notes": "Intricate paisley pattern steeped in tradition."},
    "Digital Camo": {"prompt": "digital camouflage pixels, urban fade", "notes": "Pixelated camo bridging tactical and streetwear."},
    "Houndstooth": {"prompt": "houndstooth tessellation, monochrome bite", "notes": "Classic jagged motif reinvented for modern cuts."},
    "Galaxy Print": {"prompt": "galaxy print nebulas, star clusters", "notes": "Cosmic imagery swirling across fabric expanse."},
    "Plaque Lace": {"prompt": "lace overlay, translucent floral", "notes": "Delicate lace overlay adding romantic texture."},
    "Binary Code": {"prompt": "binary code columns, scrolling digits", "notes": "Tech-forward print broadcasting data streams."},
    "Graffiti": {"prompt": "graffiti spray layers, vibrant tags", "notes": "Street art energy splashed across the garment."},
    "Quilt Patchwork": {"prompt": "quilt patchwork panels, mismatched fabrics", "notes": "Upcycled patchwork celebrating eclectic heritage."},
}

WARDROBE_WEAR_STATE_OPTIONS = {
    "Pristine": {"prompt": "meticulously pristine finish, crisp seams", "notes": "Fresh-from-workshop immaculate condition."},
    "Battle-Worn": {"prompt": "battle-worn scarring, carbon scoring", "notes": "Visible wear narrating countless encounters."},
    "Patched": {"prompt": "hand-patched patches, mismatched thread", "notes": "Resourceful repairs showcasing journey history."},
    "Aged Artisan": {"prompt": "artfully aged patina, curated distress", "notes": "Intentional weathering for heirloom authenticity."},
    "Rain-Slick": {"prompt": "rain-slick sheen, water-bead texture", "notes": "Freshly soaked finish glistening with droplets."},
    "Dusted": {"prompt": "desert dust coating, sun-bleached edges", "notes": "Dry, windworn finish rooted in arid expeditions."},
    "Icy Frost": {"prompt": "frost-rimed edging, crystalline glaze", "notes": "Frozen overcoat capturing winter chill."},
    "Gala Ready": {"prompt": "spotlight-ready polish, no visible seams", "notes": "Perfect presentation for regal events."},
    "Lab-Stained": {"prompt": "alchemical staining, reactive splashes", "notes": "Scientific pigment mapping failed experiments."},
    "Scorched": {"prompt": "heat-scorched panels, ember glow edges", "notes": "Charred accents telling of close calls with fire."},
    "Everyday Fresh": {"prompt": "freshly laundered finish, crisp press", "notes": "Clean ready-to-wear condition for daily life."},
    "Gently Worn": {"prompt": "gently worn patina, soft creases", "notes": "Light lived-in cues suggesting authenticity."},
    "Festival Paint": {"prompt": "festival paint splatter, neon remnants", "notes": "Bright paint streaks leftover from celebratory revelry."},
    "Snow Dusted": {"prompt": "snow-dusted trim, crystalline specks", "notes": "Fresh snowfall collecting along hems and shoulders."},
    "Oil-Stained": {"prompt": "oil-stained smears, mechanic residue", "notes": "Grease and oil marks telling a hands-on story."},
    "Shadow Patina": {"prompt": "shadow patina, subtle soot glow", "notes": "Smoky residue imparting a mysterious aura."},
    "Sun-Faded": {"prompt": "sun-faded gradient, washed pigments", "notes": "Color gently bleached by prolonged sunlight."},
    "Rain-Patched": {"prompt": "rain-patched repairs, waxed overlays", "notes": "Waterproof patches applied after storms."},
    "Field-Tested": {"prompt": "field-tested wear, scuffed plating", "notes": "Function-first condition showing rigorous deployment."},
    "Laboratory Sterile": {"prompt": "sterile lab press, anti-static clean", "notes": "Meticulous sterilization leaving crisp finish."},
    "Ceremonial Shine": {"prompt": "ceremonial high-polish, gleaming highlights", "notes": "Polished to mirror sheen for ritual importance."},
}

WARDROBE_SILHOUETTE_OPTIONS = {
    "A-Line": {"prompt": "a-line silhouette, flared hem", "notes": "Classic A-line offering graceful flow."},
    "Mermaid": {"prompt": "mermaid silhouette, sculpted curve", "notes": "Tailored to flare dramatically at the calves."},
    "Duster": {"prompt": "duster length, elongated lines", "notes": "Sweeping length amplifying movements."},
    "Armored Bulk": {"prompt": "armored bulk profile, imposing mass", "notes": "Intimidating bulk emphasizing defensive power."},
    "Corseted": {"prompt": "corseted waist, cinched shaping", "notes": "Structured waist crafting hourglass emphasis."},
    "Layercake": {"prompt": "multi-tiered layers, cascading volume", "notes": "Stacked layers creating kinetic volume."},
    "Sleeveless Column": {"prompt": "sleeveless column profile, streamlined line", "notes": "Minimalist column silhouette for sleek modernity."},
    "Crop & Drop": {"prompt": "cropped top with drop panels, dynamic reveals", "notes": "Cropped upper matched with dramatic lower panels."},
    "Flight Ready": {"prompt": "flight-ready tapered silhouette, aerodynamic", "notes": "Aerodynamic tailoring reducing drag mid-air."},
    "Battle Cloak": {"prompt": "battle cloak silhouette, sweeping guards", "notes": "Layered cloak lines designed to intimidate."},
    "Straight Leg": {"prompt": "straight leg silhouette, relaxed drape", "notes": "Classic straight fit for jeans or trousers."},
    "Boxy Crop": {"prompt": "boxy cropped silhouette, squared volume", "notes": "Modern cropped profile balancing relaxed structure."},
    "Relaxed Fit": {"prompt": "relaxed fit silhouette, easy ease", "notes": "Laid-back fit emphasizing comfort and movement."},
    "Empire": {"prompt": "empire waist silhouette, elevated waistline", "notes": "High waist seam creating flowing lines below the bust."},
    "Peplum": {"prompt": "peplum flare silhouette, flounced waist", "notes": "Waist flare adding playful structured volume."},
    "Cocoon": {"prompt": "cocoon silhouette, rounded envelope", "notes": "Protective oval contour wrapping the body."},
    "High-Low": {"prompt": "high-low hem silhouette, cascading back", "notes": "Asymmetric hem creating dramatic trailing movement."},
    "Column Armor": {"prompt": "column armor silhouette, vertical plates", "notes": "Rigid vertical lines reinforcing imposing presence."},
    "Skater": {"prompt": "skater silhouette, fitted bodice, flared skirt", "notes": "Energetic flare ideal for motion-heavy scenes."},
    "Oversized": {"prompt": "oversized silhouette, exaggerated volume", "notes": "Deliberate volume cultivating avant-garde shapes."},
    "Tech Shell": {"prompt": "tech shell silhouette, modular panels", "notes": "Futuristic segmented layering with sleek contour."},
    "Draped Column": {"prompt": "draped column silhouette, fluid vertical folds", "notes": "Elegant draped lines hugging the figure softly."},
}

WARDROBE_CULTURE_OPTIONS = {
    "Solar Court": {"prompt": "solar court heritage, sunburst sigils", "notes": "Regal culture venerating solar cycles."},
    "Glacier Nomads": {"prompt": "glacier nomad traditions, fur trims, ice beads", "notes": "Cold-adapted culture celebrating endurance."},
    "Desert Caravan": {"prompt": "desert caravan dyes, desert-bleached fabrics", "notes": "Dust-filtering fabrics patterned with trade route maps."},
    "Sky Temple": {"prompt": "sky temple robes, levitation-ready accents", "notes": "Soaring monasteries that blend flight and faith."},
    "Neon Syndicate": {"prompt": "neon syndicate emblem, rebellious graffiti stitches", "notes": "Counterculture collective glowing in neon defiance."},
    "Oceanic Sovereign": {"prompt": "oceanic sovereign regalwear, shell filigree", "notes": "Sea-born royalty with tidal embellishment."},
    "Starborn Dynasty": {"prompt": "starborn dynasty embroideries, constellation pearls", "notes": "Interstellar noble house mapping constellations into garments."},
    "Terracotta Order": {"prompt": "terracotta order armor, kiln-fired plates", "notes": "Ceramic armor steeped in ancient ritual."},
    "Verdant Commune": {"prompt": "verdant commune weaving, living vines", "notes": "Eco-society cultivating garments that grow with the wearer."},
    "Quantum Atelier": {"prompt": "quantum atelier craftsmanship, uncertainty patterns", "notes": "Avant-garde designers manipulating probability fabrics."},
    "Crystal Nomads": {"prompt": "crystal nomad caravans, prism charms", "notes": "Migratory artisans trading faceted crystal ornaments."},
    "Sky Dancers": {"prompt": "sky dancer clans, ribbonstream regalia", "notes": "Aerial performers weaving silk ribbons mid-flight."},
    "Deep Current": {"prompt": "deep current kingdom, biolum armor", "notes": "Undersea civilization plating garments with glowing reefs."},
    "Chronicle Keepers": {"prompt": "chronicle keeper archives, inked robes", "notes": "Historians inscribing outfits with living chronicle text."},
    "Volcanic Forge": {"prompt": "volcanic forge guild, ember-treated hides", "notes": "Smithing culture tempering textiles in molten vents."},
    "Aurora Court": {"prompt": "aurora court finery, polar light trims", "notes": "Courtly attire inspired by shimmering polar skies."},
    "Jungle Kin": {"prompt": "jungle kin tribe, woven lianas", "notes": "Rainforest collective crafting garments from living vines."},
    "Data Monks": {"prompt": "data monk monasteries, fiberoptic prayer beads", "notes": "Ascetics weaving illuminated code prayers into robes."},
    "Obsidian Guild": {"prompt": "obsidian guildtailors, volcanic glass mosaics", "notes": "Crafters inlaying volcanic glass across ceremonial plates."},
}

LIGHTING_BLUEPRINT_OPTIONS = {
    "None": {"prompt": "", "notes": "No lighting blueprint emphasis."},
    "Three-Point": {"prompt": "three-point lighting setup, key fill back", "notes": "Classic key, fill, and backlight arrangement for balanced subjects."},
    "Rembrandt": {"prompt": "rembrandt key triangle, dramatic portrait shadows", "notes": "Portrait-ready triangular patch of light under the eye."},
    "Split": {"prompt": "split lighting, hard key from side", "notes": "Half the face lit, half in shadow for tension."},
    "Clamshell": {"prompt": "clamshell lighting, beauty dish above, reflector below", "notes": "Soft glamour lighting emphasizing smooth highlights."},
    "High Key": {"prompt": "high key flood, minimal shadows", "notes": "Bright, low-contrast illumination conveying upbeat energy."},
    "Low Key": {"prompt": "low key sculpture, dominant shadow play", "notes": "Moody, high-contrast lighting sculpting form."},
    "Silhouette": {"prompt": "silhouette blueprint, backlight dominant", "notes": "Backlit figure with minimal front fill."},
    "Blade Light": {"prompt": "blade light ribbon, thin slit illumination", "notes": "Precision ribbon of light slicing across the subject."},
    "Ring": {"prompt": "ring light halo, catchlight circle", "notes": "Even frontal illumination with circular catchlights."},
    "Stage Cross": {"prompt": "stage cross lighting, opposing spot beams", "notes": "Concert-style crisscross beams framing the subject."},
}

LIGHTING_KEY_STYLE_OPTIONS = {
    "None": {"prompt": "", "notes": "No specific key light emphasis."},
    "Softbox Key": {"prompt": "softbox key light, creamy diffusion", "notes": "Large diffused key wrapping the subject in gentle gradients."},
    "Hard Spot": {"prompt": "hard spotlight key, crisp specular", "notes": "Focused key delivering sharp contrast."},
    "Fresnel": {"prompt": "fresnel focus key, cinematic carve", "notes": "Classic fresnel throw with controllable spill."},
    "Sunbeam": {"prompt": "sunbeam key shaft, natural brilliance", "notes": "Simulated sunlight streaming through set architecture."},
    "Lantern": {"prompt": "paper lantern key, omnidirectional glow", "notes": "Ambient lantern source ideal for ensemble coverage."},
    "Neon Strip": {"prompt": "neon strip key, colored edge light", "notes": "Linear neon bar painting chromatic edges."},
    "Volumetric Projector": {"prompt": "volumetric projector, patterned gobo wash", "notes": "Projector key layering complex shape patterns."},
    "Laser Curtain": {"prompt": "laser curtain key, micron-thin beams", "notes": "High-tech curtain of laser filaments slicing space."},
    "Bounce Key": {"prompt": "bounce card key, indirect spill", "notes": "Indirect bounce key for soft natural wrap."},
    "Specular Mirror": {"prompt": "specular mirror key, mirror bounce highlights", "notes": "Mirror-bounced key introducing intense highlights."},
}

LIGHTING_FILL_STYLE_OPTIONS = {
    "None": {"prompt": "", "notes": "No additional fill style."},
    "Negative Fill": {"prompt": "negative fill flags, shadow deepen", "notes": "Flags absorbing spill to intensify contrast."},
    "Soft Fill": {"prompt": "soft fill reflector, gentle shadow lift", "notes": "Subtle fill lifting shadows while preserving shape."},
    "Bounce Wall": {"prompt": "bounce wall fill, large white surface", "notes": "Broad bounce creating even secondary illumination."},
    "RGB Ambient": {"prompt": "rgb ambient fill, color cycling", "notes": "Programmable ambient fill painting ambient gradients."},
    "Prism Scatter": {"prompt": "prism scatter fill, refracted spectrum", "notes": "Fill light pushed through prisms for chromatic edges."},
    "Firelight": {"prompt": "firelight fill, flicker simulation", "notes": "Dynamic flicker emulating open flame."},
    "Moon Bounce": {"prompt": "moonlight bounce, pale blue lift", "notes": "Cool-toned fill replicating moonlight reflection."},
    "Fog Diffuse": {"prompt": "fog diffuse fill, volumetric scatter", "notes": "Fog-charged fill softening transitions."},
    "Screen Panel": {"prompt": "led screen panel fill, texture playback", "notes": "LED panel looping environment for diegetic fill."},
    "Mirror Pool": {"prompt": "mirror pool bounce, watery shimmer", "notes": "Fill reflecting off shallow water to add shimmer."},
}

LIGHTING_BACKLIGHT_OPTIONS = {
    "None": {"prompt": "", "notes": "No backlight emphasis."},
    "Rim Strip": {"prompt": "rim strip backlight, edge separation", "notes": "Thin strip lighting carving out silhouette."},
    "Hair Light": {"prompt": "hair light kicker, top-back sparkle", "notes": "Dedicated hair light adding crown highlights."},
    "Halo Arc": {"prompt": "halo arc backlight, 180-degree sweep", "notes": "Arcing backlight sculpting a halo edge."},
    "Laser Back": {"prompt": "laser backlight, volumetric shafts", "notes": "Laser back beams cutting through atmosphere."},
    "Bioluminescent": {"prompt": "bioluminescent backlight, organic glow", "notes": "Organic luminescence emanating from set pieces."},
    "Spark Shower": {"prompt": "spark shower backlight, metal grind", "notes": "Industrial sparks raining behind the subject."},
    "Sunset Flair": {"prompt": "sunset backlight, warm flare", "notes": "Backlit warmth mimicking golden hour edge light."},
    "Neon Halo": {"prompt": "neon halo hoop, saturated rim", "notes": "Neon hoop encircling the subject with color."},
    "Lightning Rig": {"prompt": "lightning rig arcs, strobing bolts", "notes": "Simulated lightning arcs pulsing behind."},
    "Hazer Beam": {"prompt": "hazer-enhanced beam, particulate sparkle", "notes": "Backlight combined with haze for sparkling particles."},
}

LIGHTING_PRACTICAL_OPTIONS = {
    "None": {"prompt": "", "notes": "No practical lighting additions."},
    "Lantern Cluster": {"prompt": "lantern cluster practicals, hanging lantern glow", "notes": "Cluster of lanterns layering warm diegetic light."},
    "Holo Billboards": {"prompt": "holographic billboard spill, animated adverts", "notes": "Holographic signage bathing scene in neon adverts."},
    "Candle Field": {"prompt": "candle field practicals, dozens of flames", "notes": "Dense arrangement of candles for romantic shimmer."},
    "Arc Reactors": {"prompt": "arc reactor pedestals, blue-white pulses", "notes": "Industrial energy cores pulsing with raw power."},
    "Fiber Nebula": {"prompt": "fiber optic nebula strands, suspended constellations", "notes": "Fiber strands weaving starfield practicals."},
    "Alchemy Vats": {"prompt": "alchemy vats practical, bubbling glow", "notes": "Chemical vats radiating eerie internal light."},
    "City Windows": {"prompt": "tower window grid, staggered luminance", "notes": "Skyscraper windows creating urban texture."},
    "Campfire": {"prompt": "campfire practical, ember crackle", "notes": "Open flame grounding scene in nomadic warmth."},
    "Festival Lanterns": {"prompt": "festival ribbon lanterns, color wash", "notes": "Festival lantern strings enriching cultural mood."},
    "Emergency Strobes": {"prompt": "emergency strobes, red-blue oscillation", "notes": "Emergency lights cycling urgent color beats."},
}

LIGHTING_ATMOSPHERE_OPTIONS = {
    "None": {"prompt": "", "notes": "No added atmospheric effect."},
    "Haze": {"prompt": "thin haze layer, volumetric definition", "notes": "Mild haze clarifying beams and depth."},
    "Fog Bank": {"prompt": "rolling fog bank, floor-level drift", "notes": "Dense fog hugging ground for mystery."},
    "Snowfall": {"prompt": "slow snowfall, glittering flakes", "notes": "Snow catching light for ethereal sparkle."},
    "Sand Drift": {"prompt": "desert sand drift, suspended grains", "notes": "Wind-blown sands creating scorched ambience."},
    "Ash Fall": {"prompt": "ash fall atmosphere, ember flecks", "notes": "Ash particles narrating a recent blaze."},
    "Petal Storm": {"prompt": "petal storm, floating blossoms", "notes": "Petals swirling for poetic motion."},
    "Electrical Mist": {"prompt": "ionized mist, static crackle", "notes": "Charged mist emitting faint lightning crackle."},
    "Bubble Field": {"prompt": "bubble field, refractive spheres", "notes": "Clusters of bubbles refracting rainbow highlights."},
    "Glitter Rain": {"prompt": "glitter rain fall, sparkling cascade", "notes": "Glitter-laced precipitation glinting in light."},
    "Aurora Veil": {"prompt": "aurora veil atmosphere, spectral curtain", "notes": "Auroral curtain draping across the sky."},
}

LIGHTING_COLOR_GEL_OPTIONS = {
    "None": {"prompt": "", "notes": "No color gel adjustments."},
    "Teal & Orange": {"prompt": "teal and orange color contrast", "notes": "Cinematic complementary color pairing."},
    "Magenta Cyan": {"prompt": "magenta cyan split tone", "notes": "Vibrant chromatic opposition energizing midtones."},
    "Royal Purple": {"prompt": "royal purple gel wash", "notes": "Luxurious purple saturating highlights."},
    "Emerald": {"prompt": "emerald gel, deep verdant hues", "notes": "Green gel invoking enchanted forest tones."},
    "Amber Glow": {"prompt": "amber glow gel, warm embrace", "notes": "Soft amber warming skin tones elegantly."},
    "Ice Blue": {"prompt": "ice blue gel, crisp chill", "notes": "Cool blue casting a fresh, nocturnal feel."},
    "Infrared": {"prompt": "infrared gel, edge-spectrum tint", "notes": "Infrared filter for surreal color separation."},
    "Grunge Mix": {"prompt": "grunge gel mix, dirty sodium vapor", "notes": "Sodium-esque grime for dystopian scenes."},
    "Neon Pop": {"prompt": "neon pop gel, high saturation", "notes": "High-energy neon saturations for cyberpunk vibes."},
    "Pastel Bloom": {"prompt": "pastel bloom gel, gentle gradient", "notes": "Pastel gradient softening transitions."},
}

LIGHTING_CAM_SETTINGS = {
    "None": {"prompt": "", "notes": "No camera setting adjustments."},
    "Cinematic": {"prompt": "cinematic exposure, shutter 1/48, iso 400", "notes": "Filmic settings for motion blur authenticity."},
    "Noir": {"prompt": "noir exposure, deep blacks, high contrast", "notes": "High contrast exposure chasing noir shadows."},
    "Documentary": {"prompt": "documentary settings, handheld realism", "notes": "Naturalistic exposure with slight grain."},
    "Hyperreal": {"prompt": "hyperreal hdr settings, crisp micro-detail", "notes": "HDR tuned for extraordinary clarity."},
    "Dreamscape": {"prompt": "dreamscape exposure, bloom-heavy", "notes": "Soft bloom with lifted blacks for dreamy feel."},
    "Retro Film": {"prompt": "retro film stock, iso 200, warm bias", "notes": "Vintage film simulation with warm bias."},
    "Action Sports": {"prompt": "action sports shutter 1/2000, frozen motion", "notes": "Fast shutter freezing explosive action."},
    "Long Exposure": {"prompt": "long exposure trails, tripod stability", "notes": "Intentional motion blur capturing light trails."},
    "Low Light": {"prompt": "low light push, iso 3200, noise texture", "notes": "Low light push processing embracing grain."},
    "Event Stage": {"prompt": "event stage metering, skin priority", "notes": "Spot metering tuned for stage performance."},
}

LIGHTING_SPECIAL_TECHNIQUES = {
    "None": {"prompt": "", "notes": "No special lighting technique."},
    "Shutter Drag": {"prompt": "shutter drag blur, staccato flash freeze", "notes": "Flash plus slow shutter smearing ambient movement."},
    "Light Painting": {"prompt": "light painting streaks, handheld torch", "notes": "Painterly streaks drawn during long exposure."},
    "Projection Mapping": {"prompt": "projection mapped visuals, surface wrap", "notes": "Animated visuals mapped onto set geometry."},
    "Gobo Patterns": {"prompt": "gobo pattern washes, carved shadows", "notes": "Patterned gobos carving kinetic shadows."},
    "Lens Flares": {"prompt": "intentional lens flares, anamorphic streaks", "notes": "Controlled flares adding cinematic polish."},
    "Strobe Pulse": {"prompt": "strobe pulse bursts, rhythmic flash", "notes": "Timed strobes freezing micro-moments."},
    "Double Exposure": {"prompt": "double exposure in-camera blend", "notes": "Layered exposures blending scenes."},
    "Underlight": {"prompt": "underlighting practical, theatrical creep", "notes": "Upward lighting for eerie, dramatic mood."},
    "Soft Wrap": {"prompt": "soft wrap diffusion, bounce from multiple angles", "notes": "Multiple soft sources wrapping subject completely."},
    "Back Projection": {"prompt": "back projection plate, retro technique", "notes": "Vintage rear-projection mixing live and plate."},
}

LIGHTING_ENERGY_LEVEL_OPTIONS = {
    "None": {"prompt": "", "notes": "No lighting energy emphasis."},
    "Serene": {"prompt": "serene luminance, gentle gradients", "notes": "Calm lighting with slow falloffs."},
    "Romantic": {"prompt": "romantic warmth, flickering softness", "notes": "Warm, intimate glow suited to close moments."},
    "Dynamic": {"prompt": "dynamic staccato pulses, sharp ratios", "notes": "Energetic lighting fueling action beats."},
    "Sinister": {"prompt": "sinister chiaroscuro, crawling shadows", "notes": "Menacing interplay of darkness and slit light."},
    "Triumphant": {"prompt": "triumphant brilliance, radiant beams", "notes": "Victorious glow drenching subject in light."},
    "Mystic": {"prompt": "mystic iridescence, unpredictable bloom", "notes": "Arcane lighting shimmering with spectral hues."},
    "Industrial": {"prompt": "industrial sodium vapor, gritty ambiance", "notes": "Utility lighting humming with mechanical hum."},
    "Apocalyptic": {"prompt": "apocalyptic firelight, ash-choked glow", "notes": "Harsh lighting referencing catastrophic aftermath."},
    "Celebratory": {"prompt": "celebratory confetti sparkle, multi-color wash", "notes": "Party-ready mix bursting with excitement."},
    "Sci-Fi Clinical": {"prompt": "clinical white glow, sterile gradient", "notes": "Lab-grade illumination crisp and clean."},
}

LIGHTING_SAFETY_NOTES = {
    "Pyro": "Coordinate with pyro technician, clear safety perimeter.",
    "Laser": "Use eye-safe laser modules and avoid reflective surfaces.",
    "Water": "Isolate electrical gear from water effects, use GFCI protection.",
    "Crowded Set": "Mark cable runs and secure fixtures overhead for extras.",
    "Strobe": "Warn crew about strobing to protect those with sensitivities.",
    "Fog": "Ventilate space and monitor particulate exposure for crew.",
    "Heights": "Harness operators working on elevated lighting truss.",
    "Heat": "Insulate fixtures and schedule cooldown windows.",
    "Animals": "Acclimate animals to lighting cues gradually.",
    "Children": "Soften light intensity and minimize high-heat fixtures around minors.",
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
    "Skyline Courier": {
        "subject": "Skyline courier weaving between skyscrapers with thruster skates",
        "keywords": ["fleet-footed", "aerial", "deadline-driven"],
    },
    "Bio-Sculptor": {
        "subject": "Bio-sculptor artisan coaxing living flora sculptures from luminous resin",
        "keywords": ["organic craft", "bioluminescent", "delicate"],
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
    "Electric Rebellion": {
        "descriptor": "charged by uprising sparks",
        "ambience": "holographic flyers pulse across rain-slick streets",
        "hook": "Every footstep feeds the citywide surge of defiance.",
        "keywords": ["neon defiance", "street anthem"],
    },
    "Quiet Reckoning": {
        "descriptor": "weighted with soft resolve",
        "ambience": "low thunder rumbles beneath hushed breaths",
        "hook": "Stillness marks the moment before balance is restored.",
        "keywords": ["held breath", "measured justice"],
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
    "Luminal Skyway": {
        "description": "Glass skyways thread between levitating transit hubs",
        "details": "hovercraft blur through light curtains and transit glyphs",
        "keywords": ["altitude lanes", "transit glow"],
    },
    "Subterranean Grotto": {
        "description": "Bioluminescent grotto carved below cascading waterfalls",
        "details": "glowing lichens trace the cavern walls and mirrored pools",
        "keywords": ["glowstone", "echoing drip"],
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
    "Skyway Escape": {
        "motion": "sprints across translucent skyways as drones weave in pursuit",
        "hook": "Every leap risks a plunge through rain-streaked neon abyss.",
        "keywords": ["thruster sparks", "altitude slip"],
    },
    "Ritual Awakening": {
        "motion": "raises a relic as luminous glyphs spiral outward in slow bloom",
        "hook": "The chamber hums as ancient power unfurls from the circle.",
        "keywords": ["sigil bloom", "resonant chime"],
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
    "thunder build": {
        "motion_prefix": "On a rumbling build,",
        "motion_suffix": "as rolling thunder stacks beneath each beat",
        "hook_suffix": "Pressure mounts until the sky itself is ready to split.",
        "subject_accent": "braced against incoming storm",
        "keywords": ["gathering charge", "storm cadence"],
    },
    "weightless drift": {
        "motion_prefix": "In a weightless drift,",
        "motion_suffix": "letting gravity pause while motion hangs suspended",
        "hook_suffix": "A silent float suspends the story between inhale and exhale.",
        "subject_accent": "buoyed by gentle momentum",
        "keywords": ["hover pulse", "airy sway"],
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
    "Suspended Silk": {
        "prompt": "suspended silk inversion, toes pointed, ribbon wrap",
        "notes": "Ideal for aerial rigs—spotter safety and secure tie-offs are essential.",
    },
    "XXX Wall Brace": {
        "prompt": "braced against wall, arched back, dramatic leg extension",
        "notes": "Stage explicit power poses—align lighting to sculpt athletic definition.",
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
    "Casual": {
        "prompt": "comfortable casual wear, soft fabrics, relaxed fit",
        "notes": "Emphasize comfort and ease of movement.",
    },
    "Nude": {
        "prompt": "bare skin, natural beauty, soft lighting",
        "notes": "Celebrate the human form with tasteful nudity.",
    },
    "Lace Lingerie": {
        "prompt": "delicate lace lingerie set, intricate patterns, sheer panels",
        "notes": "Highlight femininity and elegance through intricate lace details.",
    },
    "Torn Yoga Pants": {
        "prompt": "torn yoga pants, torn crotch, snug fit, athletic vibe",
        "notes": "Combine comfort with a hint of edginess.",
    },
    "Torn Jeans": {
        "prompt": "ripped denim jeans, distressed details, casual cool",
        "notes": "Embrace a laid-back vibe with edgy denim.",
    },
    "Bra And Panties": {
        "prompt": "coordinated bra and panties set, soft fabrics, flattering fit",
        "notes": "Focus on color coordination and fabric texture for a polished look.",
    },

    "Bikini": {
        "prompt": "stylish bikini set, vibrant colors, beach-ready",
        "notes": "Perfect for sun-soaked shoots with a playful vibe.",
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
    "Body Paint Couture": {
        "prompt": "hand-painted body art, shimmering pigments, gradient coverage",
        "notes": "Coordinate palette with lighting to keep body paint vibrant and respectful.",
    },
    "XXX Mesh Harness": {
        "prompt": "transparent mesh harness, chrome rings, high-shine thigh straps",
        "notes": "High-voltage fetish styling—maintain empowered stance and clear consent messaging.",
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
    "Erotic" : {
        "prompt": "sensual erotic vibe, smoldering gaze, intimate setting",
        "notes": "Emphasize connection and allure through body language.",
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
    "Heated Performance": {
        "prompt": "stage-heated charisma, performer flair, crowd-responsive energy",
        "notes": "Great for live-show vibes where confidence is spotlighted.",
    },
    "XXX Outrageous": {
        "prompt": "outrageous adult spectacle, unapologetic flair, spotlight fever",
        "notes": "Max intensity energy—underscore agency and consent cues.",
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
    "Led Light Panels": {
        "prompt": "LED light panels, adjustable color temp, soft diffusion",
        "notes": "Versatile lighting for various moods—experiment with colors.",
    },

"softbox Glow": {
        "prompt": "large softbox, even wraparound light, minimal shadows",
        "notes": "Ideal for beauty and fashion shoots requiring flattering illumination.",
    },

    "Side light Drama": {
        "prompt": "strong side light, deep shadows, high contrast",
        "notes": "Creates a dramatic, moody atmosphere—great for storytelling.",
    },

    "Flatering Ring Light": {
        "prompt": "ring light, circular catchlights, even facial illumination",
        "notes": "Perfect for close-up glamour shots emphasizing facial features.",
    },

    "Warm Side Light": {
        "prompt": "warm side light, golden hour mimicry, soft shadow gradients",
        "notes": "Use for a natural, inviting glow that enhances skin tones.",
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
    "Projection Mapping": {
        "prompt": "projection-mapped patterns, evolving textures, responsive light",
        "notes": "Project visuals that complement body contours for artistic storytelling.",
    },
    "XXX Laser Grid": {
        "prompt": "laser grid lighting, intersecting beams, electric pulse",
        "notes": "High-voltage adult club vibe—mind safety and avoid direct eye exposure.",
    },
    "Custom": {
        "prompt": "",
        "notes": "Use the custom lighting prompt input to detail bespoke setups.",
    },

"XXX Nightlife": {
        "prompt": "nightlife-inspired lighting, vibrant gels, dynamic contrasts",
        "notes": "Capture the energy and excitement of nightlife with bold colors and dramatic shadows.",
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

NSFW_SET_DESIGNS = {
    "None": {
        "prompt": "",
        "notes": "No dedicated set dressing emphasis.",
    },
    "Sensual Lounge": {
        "prompt": "Velvet chaise draped with ambient fabric, clustered candles, and soft-focus drapery staging",
        "notes": "Layer deep cushions and candle groupings for an intimate lounge vignette.",
    },
    "Velvet Lounge": {
        "prompt": "velvet lounge set, jewel-toned drapery, plush seating tiers",
        "notes": "Classic boudoir lounge ideal for editorial glamour.",
    },
    "Cabaret Stage": {
        "prompt": "cabaret stage with velvet curtains, luminous footlights, polished hardwood",
        "notes": "Perfect for theatrical burlesque-inspired showcases.",
    },
    "Futuristic Capsule": {
        "prompt": "futuristic capsule suite, curved glass, ambient neon striping",
        "notes": "Great for sci-fi erotica with clean architectural lines.",
    },
    "Neon Skyline Suite": {
        "prompt": "penthouse skyline suite, floor-to-ceiling glass, holographic signage glow",
        "notes": "Pair with reflective materials to amplify urban glamour.",
    },
    "Private Dressing Room": {
        "prompt": "private dressing room set, marquee bulbs, wardrobe racks",
        "notes": "Backstage energy with intimate performer preparation cues.",
    },
    "Rope Studio Loft": {
        "prompt": "industrial loft rigged with suspension points, coiled ropes, and padded mats",
        "notes": "Ensure experienced riggers supervise and prioritize safety briefings.",
    },
    "Spa Retreat": {
        "prompt": "steam spa retreat, billowing mist, warm cedar benches",
        "notes": "Soft spa atmosphere suited for serene sensuality.",
    },
    "XXX Champagne Stage": {
        "prompt": "champagne stage, mirrored runway, confetti shimmer",
        "notes": "High-energy adult stage experience with luxe finishes.",
    },
    "XXX Neon Tunnel": {
        "prompt": "pulsing neon gauntlet of arches, mirrored floor, bass-thumping fog bursts",
        "notes": "Lean into electrified runway energy with confident choreography.",
    },
    "XXX Industrial Cage": {
        "prompt": "industrial cage set, gridded shadows, steel spotlight",
        "notes": "Edgy adult setting—pair with empowering posing.",
    },
    "XXX Ritual Chamber": {
        "prompt": "ritual chamber with flickering sconces, carved stone plinths, incense haze",
        "notes": "Apply consent-forward framing when invoking power-play aesthetics.",
    },
    "Custom": {
        "prompt": "",
        "notes": "Use the custom set prompt input to describe bespoke set pieces.",
    },
    "XXX Custom": {
        "prompt": "",
        "notes": "Use the custom set prompt input for adult-stage set designs.",
    },
}

NSFW_HEAT_LEVELS = {
    "None": {
        "prompt": "",
        "notes": "No additional heat descriptors applied.",
        "negative": "",
    },
    "Subtle": {
        "prompt": "subtle allure, whispered tension, restrained tease",
        "notes": "Ideal for low-intensity boudoir and soft editorial scenarios.",
        "negative": "overt explicit acts, graphic focus",
    },
    "Sensual": {
        "prompt": "sensual cadence, warm magnetism, intimate pace",
        "notes": "Balanced sensuality that stays refined and inviting.",
        "negative": "aggressive explicit behavior, harsh fetish framing",
    },
    "Slow Burn": {
        "prompt": "slow-burning heat, patient glances, lingering contact",
        "notes": "Great for storytelling arcs that crescendo gradually.",
        "negative": "sudden explicit jumps, hard-cut transitions",
    },
    "Bold": {
        "prompt": "bold seduction, confident heat, commanding gaze",
        "notes": "Turn up intensity while celebrating empowered presence.",
        "negative": "demeaning scenarios, non-consensual direction",
    },

    "Solo XXX": {
        "prompt": "solo xxx energy, unapologetic self-expression, empowered allure, sensual_fingering,",
        "notes": "Celebrate solo adult confidence with clear agency messaging.",
        "negative": "non-consensual themes, degrading scenarios",
    },

    "XXX Heatwave": {
        "prompt": "scorching club frenzy, relentless rhythm, unapologetic showmanship",
        "notes": "Maximize adult spectacle with emphasis on mutual enthusiasm.",
        "negative": "shaming language, non-consensual escalation",
    },
    "XXX Fever": {
        "prompt": "xxx feverish energy, charged teasing, spotlight hunger",
        "notes": "Maximal adult heat—pair with strong agency messaging.",
        "negative": "violent explicit content, bodily fluids, humiliation themes",
    },
    "Custom": {
        "prompt": "",
        "notes": "Use the custom heat prompt input to define bespoke heat language.",
        "negative": "",
    },
    "XXX Custom": {
        "prompt": "",
        "notes": "Use the custom heat prompt input for adult-only heat descriptors.",
        "negative": "",
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

    "Fully Adult Nude": {
        "prompt": "fully adult nude, explicit anatomy, highly detailed Skin, confident exposure", 
        "negative": "underage, fetish extremes, non-consensual themes, violence",
    },
    "Nude" : {
        "prompt": "full nudity, explicit anatomy, detailed skin texture, confident pose",
        "negative": "underage, fetish extremes, non-consensual themes, violence",
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
    "degrading",
    "humiliation",
    "excrement",
    
]

NSFW_DEFAULT_SAFETY_NOTE = (
    "For mature audiences only. Confirm all depicted subjects are consenting adults and comply with platform policies."
)


PROMPT_CONTRADICTION_RULES = [
    {
        "label": "Time of Day",
        "hint": "Align time-of-day cues across narrative, lighting, and palette selections.",
        "groups": {
            "day": [
                "daytime",
                "day-lit",
                "sunlit",
                "bright daylight",
                "midday",
                "high noon",
                "noonday",
            ],
            "night": [
                "night",
                "nighttime",
                "midnight",
                "moonlit",
                "nocturnal",
                "after-hours",
            ],
            "dawn": ["dawn", "sunrise", "first light"],
            "dusk": ["dusk", "sunset", "twilight", "golden hour"],
        },
    },
    {
        "label": "Lighting Temperature",
        "hint": "Keep lighting descriptors centered on either warm or cool styling for clarity.",
        "groups": {
            "warm": [
                "warm tone",
                "warm color palette",
                "golden hue",
                "amber glow",
                "ember glow",
                "sunset glow",
                "firelight",
                "sun-bathed",
            ],
            "cool": [
                "cool tone",
                "cool color palette",
                "icy",
                "frosted",
                "blue undertones",
                "silver rim",
                "moonlit",
                "glacial",
            ],
        },
    },
    {
        "label": "Weather Mood",
        "hint": "Conflicting weather cues can confuse render context—choose a single atmosphere.",
        "groups": {
            "clear": ["clear skies", "sun-drenched", "sunny", "cloudless"],
            "storm": [
                "storm",
                "lightning",
                "downpour",
                "rain-soaked",
                "rainfall",
                "tempest",
            ],
            "snow": ["snow", "snowfall", "blizzard", "frost", "snowstorm"],
        },
    },
]

