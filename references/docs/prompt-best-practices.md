# Prompt Best Practices
Reference guide for crafting generation prompts. Consult this before writing any image or video prompts.

## Nano Banana Pro (Image Generation)

### Core Prompt Structure
Use structured YAML-style fields for consistency and clarity. Every prompt should cover:

| Field | Purpose | Example |
| :--- | :--- | :--- |
| `action` | What the character is doing | `character holds product naturally` |
| `character` | Who - infer from reference or describe | `young woman, 25, casual style` |
| `product` | The product with text accuracy note | `show product with all visible text clear and accurate` |
| `setting` | Where the scene takes place | `kitchen counter, morning light` |
| `camera` | Shot style (always amateur) | `amateur iPhone photo, casual selfie, uneven framing` |
| `style` | Visual feel | `candid UGC look, no filters, imperfections intact` |
| `text_accuracy`| Packaging text preservation | `preserve all visible text exactly as in reference image` |

For simple/undetailed requests, default to: **"put this [product] into the scene with the [character]"**

### Aspect Ratio
- Start every prompt with aspect ratio.
- `2:3` for vertical UGC ads (default).
- `3:2` for horizontal/landscape.
- `9:16` also accepted for vertical.

### Camera & Realism Keywords
Always include casual realism descriptors. Pick 2-3 from this list:
- `unremarkable amateur iPhone photo`
- `reddit image`
- `snapchat photo`
- `casual iPhone selfie`
- `slightly uneven framing`
- `authentic share`
- `slightly blurry`
- `amateur quality phone photo`

### Technical Specifications
- **Camera/Lens**: "Shot on iPhone 15 Pro" or "35mm lens, f/1.8" - forces specific depth-of-field and realism.
- **Lighting**: Be specific - "soft diffused north-facing window light, golden hour warmth" succeeds 95% of the time vs 60% for generic "natural lighting".
- **Skin/Texture**: "natural skin texture with visible pores, subtle grain, not airbrushed" for UGC authenticity.
- **Film Stock (optional)**: "Kodak Portra 400 film" for warm nostalgic look.

### Reference Image Usage
- Mark each input's role explicitly: "Using input image 1 for product identity".
- **Face preservation**: "Keep the facial features exactly consistent with the uploaded image".
- **Reference weighting**: Assign weight values to control how much the reference influences output.
- Supports up to 14 input images in a single composition.
- **Text accuracy is critical**: All visible product text (logos, slogans, packaging claims) must be preserved exactly. Never invent extra claims or numbers.

### UGC Authenticity Checklist
Every image prompt should aim for:
- [ ] Everyday realism with authentic, relatable settings.
- [ ] Amateur-quality iPhone photo style.
- [ ] Slightly imperfect framing and lighting.
- [ ] Candid poses and genuine expressions.
- [ ] Visible imperfections (blemishes, messy hair, uneven skin, texture flaws).
- [ ] Real-world environments left as-is (clutter, busy backgrounds).

### Generating Realistic People
Follow this **element order** when describing a person (each element builds on the last):
1. **Camera Angle**: `front angle`, `45 degree angle to the left`, `top-down overhead shot`.
2. **Character Description**: Age, gender, and **specific physical features**: `a 20-year-old man with a bleached buzzcut hairstyle and freckles`.
3. **Pose + Background**: What they're doing and where: `sitting at a desk in a YouTube studio`.
4. **Outfit**: Specific clothing: `cream oversized tee, straight leg dark denim, clean white minimalist sneakers, simple silver chain`.
5. **Skin Details**: `natural skin texture with visible pores, subtle freckles, fine peach fuzz, not airbrushed`.
6. **Specific Pose/Action**: `resting his hands carefully on the desk looking at the frame`.
7. **Background Details**: `simple aesthetic creator setup, professional YouTube studio lighting`.
8. **Negative Constraints**: `no equipment in the frame, no microphone, no camera visible`.
9. **Style Keywords**: `realism, high detail, skin texture`.

**Key Principles:**
- Be **specific** with physical features - vague descriptions produce generic/plastic results.
- Skin details (pores, freckles, peach fuzz, texture) are what make people look real.

### Character Diversity
- Default age range: **21-38 years old** unless specified otherwise.
- Ensure diversity in gender, ethnicity, and hair color across variations.
- Avoid mentioning copyrighted character names in prompts.

### Negative Constraints
Use these to prevent common issues:
- `no geometric distortion, no extra fingers`
- `no airbrushed skin, no studio backdrop`
- `no text overlays, no watermarks`

### Pro Tips
- Use command-style syntax, not polite phrasing (no "please generate...").
- Avoid double quotes inside prompts (interferes with JSON serialization).
- Specify era aesthetics for mood when relevant.
- **Seed locking**: reuse successful seed values for consistent series generation.
- Prompts with exact lighting terms succeed far more often than vague descriptions.

### BOPA Consistency Framework
When generating multiple images of the same character, use the **BOPA framework** to maintain consistency across generations:
- **B**ACKGROUND: Keep location elements consistent.
- **O**UTFIT: Maintain clothing style and colors.
- **P**OSE: Use logical sequences.
- **A**CTION: Ensure consistent motion cadence.

---

### Example Structured YAML Prompt
```yaml
action: character holds product naturally, showing label to camera
character: young woman, mid-20s, casual loungewear, messy bun, light freckles, natural skin texture
product: show product with all visible text clear and accurate
setting: cozy lived-in apartment, morning light through sheer curtains
camera: amateur iPhone selfie, slightly uneven framing, warm tones
style: candid UGC look, no filters, realism, high detail, skin texture, not airbrushed
text_accuracy: preserve all visible text exactly as in reference image
negative: no studio lighting, no ring light reflection in eyes, no airbrushed skin
```

### Example - Sentence Prompt (Character-First Order)
> 9:16. Front angle. A young woman in her mid-20s with light freckles and a messy bun, wearing casual loungewear. She is naturally holding [product] at chest height in a cozy lived-in apartment with morning light through sheer curtains. Natural skin texture with visible pores, subtle grain, fine peach fuzz. Amateur iPhone selfie, slightly uneven framing, warm golden tones. No studio lighting, no filters. Realism, high detail, skin texture. Using input image 1 for product identity.

---

## Reference Image Analysis
Before generating prompts, analyze reference images to extract:

### For Products
```yaml
brand_name: (visible or inferable brand name)
color_scheme:
  - hex: "#911a1c"
    name: dark red
font_style: sans-serif, bold
visual_description: (1-2 sentences describing the product, ignoring background)
```

### For Characters
```yaml
character_name: (if visible/inferable)
color_scheme:
  - hex: "#911a1c"
    name: dark red
outfit_style: (clothing, accessories, notable features)
visual_description: (1-2 sentences describing appearance, ignoring background)
```

---

## SEALCAM Framework (Cinematic Prompts)
A structured prompting framework for cinematic video and image generation. Use this when you need precise control over every visual element - ideal for hero shots, narrative sequences, and high-production content. Fields must always appear in the exact order: **S, E, A, L, Ca, M**.

### The Six Elements

#### S - Subject
What the camera is optically prioritizing within the frame.
- Use shot-focused terminology: primary subject, secondary subject, foreground element, background element.
- Be specific about the subject's appearance, wardrobe, and placement in frame.

#### E - Environment
The physical or constructed space surrounding the subject.
- Use production terms: location type, set design, spatial depth, background treatment.
- Describe the space as a set designer would: materials, depth, atmosphere.

#### A - Action
Observable motion within the frame, including subject and camera movement.
- Use blocking and motion terms: subject movement, camera movement, environmental motion.
- Separate what the subject does from how the camera responds.

#### L - Lighting
The lighting setup and exposure characteristics shaping the image.
- Use lighting terms only: key light, fill, rim, practicals, contrast ratio, exposure level, color temperature.
- Describe the lighting as a cinematographer would - direction, quality, ratio.

#### Ca - Camera
The capture device, lens choice, framing, angle, and movement strategy.
- **Camera type**: cinema camera or stills camera (e.g., ARRI Alexa, RED, Sony FX series, DSLR).
- **Lens type and focal length**: e.g., 35mm prime, 85mm portrait lens, anamorphic.
- **Framing and angle**: wide, medium, close-up; eye-level, low-angle, high-angle.
- **Camera motion**: locked-off, handheld, dolly, pan, tilt, tracking.

#### M - Metatokens
Technical and stylistic capture cues related to production quality and presentation.
- Realism level, texture and grain, motion cadence (e.g., 24fps cinematic), render or capture quality.

### SEALCAM Example Prompt
> **S**: Primary subject - a woman in her late 20s, linen blouse, holding [product] at chest height, sharp focus on hands and product label. Secondary subject - out-of-focus friend in background frame-right.
> **E**: Sunlit outdoor cafe terrace, wrought-iron table with espresso cups, shallow spatial depth with soft bokeh on tree-lined street behind.
> **A**: Subject lifts product slightly toward camera, gentle head tilt and smile. Camera holds steady then begins slow push-in over 3 seconds. Leaves drift through background.
> **L**: Key light - natural overhead sun diffused by canvas awning, soft and warm (5200K). Fill - ambient bounce from white tablecloth. Rim - subtle hair light from open sky. Contrast ratio 3:1, slightly overexposed highlights.
> **Ca**: ARRI Alexa Mini, 50mm Cooke S4 prime, medium close-up framing at eye-level, locked-off tripod with slow motorized push-in.
> **M**: Photorealistic, fine organic grain matching 800 ISO, 24fps cinematic cadence, shallow depth of field, broadcast-quality finish.

### When to Use SEALCAM vs Standard Prompts
| Use Case | Framework |
| :--- | :--- |
| UGC-style selfie ads (authentic, casual) | Standard UGC structure |
| Cinematic product hero shots | SEALCAM |
| Narrative video sequences | SEALCAM |
| Quick social media content | Standard UGC structure |
| High-production brand films | SEALCAM |

---

## Text & Product Fidelity
Text preservation must be treated as its own explicit directive. When product packaging, logos, or claims are visible in a reference image, call out text fidelity as a **separate concern** in the prompt.

### How to Apply:
- Add a dedicated `text_accuracy` field in structured prompts.
- Reinforce in the instruction layer: *"Make sure the reference image is depicted as ACCURATELY as possible, especially all text"*.
- Never invent extra packaging claims or numbers that aren't visible in the reference.
- If text is partially obscured in the reference, preserve what's visible and don't guess the rest.
