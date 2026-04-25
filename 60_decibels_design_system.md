# 60 Decibels: Design System & Brand Identity

This document serves as a reference for the 60 Decibels design system, visual identity, and brand voice. This is crucial for matching their tone and aesthetic when designing pitches, presentations, or product features tailored to them.

## 1. Brand Tone and Voice
The 60 Decibels brand voice is deeply grounded in human empathy, data rigor, and an approachable, slightly "nerdy" personality.

*   **Empathetic & Human-Centric:** At their core, they emphasize that impact measurement is about real human lives. They use terms like *"Data built by listening,"* and *"Who knows your impact best? The people who experience it."*
*   **Data-Driven but Approachable:** They distill complex statistical methodologies into friendly, easily digestible insights. 
*   **Self-Aware & "Quirky":** They describe their newsletter as *"Quirky, informative, and a little bit nerdy... alongside 11,361 other data geeks."*
*   **Professional Yet Light:** Their careers page epitomizes their culture: *"We take the work seriously, but we take ourselves lightly."*
*   **Honest & Direct:** They use straightforward, fluff-free language. *"Most impact measurement is either too complex to be scalable or too simple to be useful."*

## 2. Typography
Their typographical hierarchy heavily relies on pairing a distinct, modern monospace font for headings with a clean, highly legible sans-serif for body copy.

*   **Primary Font (Headings, Display, Quotes, Numbers):** `Maax` (Monospace)
    *   **Usage:** Used for all `<h1>` through `<h6>` tags, large numerical data visualizations, quotes, and primary buttons/links.
    *   **Characteristics:** Mathematical, structured, gives an analytical "data" feel while remaining highly modern and stylish.
*   **Secondary Font (Body Text, Paragraphs, UI Elements):** `Union` (Sans-Serif)
    *   **Usage:** Standard body paragraphs, sub-text, form labels, and smaller UI read-outs.
    *   **Characteristics:** Clean, highly readable, standard sans-serif that balances the quirky nature of the monospace headings.

## 3. Color Palette
The 60 Decibels color palette is vibrant, warm, and highly distinctive. It avoids generic corporate blues and instead relies on energetic, slightly earthy, and mathematically precise pastel and primary tones.

### Core Background Tones (Neutrals & Pastels)
*   **Off-White / Beige:** `#F3F3EE` / `#FAFAF7` / `#F1F5F0` (Frequently used for page backgrounds, form areas, and embedded blocks).
*   **Soft Mint/Greenish Grey:** `#DEE7DD` (Used for feature block backgrounds).
*   **Soft Lavender/Grey:** `#C6C0CD` (Used to offset map/data visualizations).

### Primary Vibrant Colors (Blocks & Accents)
These colors are used aggressively as full-bleed background colors for different sections on the website, defining distinct chapters of their story.
*   **Coral / Vibrant Red:** `#FF6651` (High-contrast accent color, used for lines, active tabs, and primary emphasis).
*   **Soft Red/Pink:** `#FF8075` (Used for large data-graph blocks, error blocks, and lead sections).
*   **Mustard Yellow / Gold:** `#F4D276` (Used heavily for "Featured", "Social", and "Intro" blocks).
*   **Soft Teal / Cyan:** `#E7F1F2` (Used for chart backgrounds and expertise sections).
*   **Deep Teal / Aquamarine:** `#5FA4A9` (Used for split "What we do" visual blocks).
*   **Sage Green:** `#A1BA9E` (Used for distinct, full-bleed feature blocks).
*   **Dark Navy/Black:** `#1D2B38` / `#000000` (Used for dense text, primary buttons, borders, and footer elements).

## 4. UI/UX and Layout Patterns
*   **Borders and Lines:** They heavily use thin, crisp black borders (`1px solid #000`). Buttons are often "outlined", form fields have hard black borders with slightly rounded corners (`radius: 5px`), and sections are often divided by crisp 1px lines.
*   **Buttons:** 
    *   **Outline Buttons:** Transparent background, `1px solid #000`, turning into solid black background with white text on hover. They also use pill-shaped variants (`border-radius: 45px`).
    *   **Solid Buttons:** Solid `#000` or `#fff` block buttons with strict geometric padding.
*   **Whitespace:** They utilize massive amounts of whitespace. Section paddings are often `60px`, `80px`, or `100px` deep.
*   **Asymmetry & Grid:** They utilize distinct grid columns but often split the screen 50/50 with contrasting background colors (e.g., `#DEE7DD` on the left, `#5FA4A9` on the right) for a modern editorial feel.
*   **Micro-interactions:** Subtle hover states. "Intrinsic images" (images within cards) scale up slightly (`transform: scale(1.05)`) over 600ms on hover. Links often have bottom borders (`border-bottom: 1px solid`) that animate. Data visualizations scale and paths become fully opaque upon interaction.
*   **Iconography:** Uses flat, sharp SVG icons, often encased in a colored circle or standalone. Simple geometry.
