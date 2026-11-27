---
name: Older and Wider
description: The home page as this week's issue of a 1980s British women's weekly, with the two hosts as the cover stars.
colors:
  cover-pink: "#F492BF"
  masthead-red: "#A60201"
  logotype-magenta: "#E8046C"
  paper-white: "#FFFFFF"
  ink: "#1A1A1A"
  coverline-blue: "#6771DD"
  flash-yellow: "#FFD23F"
  ticket-pink: "#FCE4EF"
  studio-grey: "#5E5D60"
typography:
  display:
    fontFamily: "Anton, Barlow Condensed, sans-serif"
    fontSize: "calc(100cqi / 6.45)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Anton, Barlow Condensed, sans-serif"
    fontSize: "4rem"
    fontWeight: 400
    lineHeight: 0.95
  title:
    fontFamily: "Anton, Barlow Condensed, sans-serif"
    fontSize: "1.875rem"
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: "0.005em"
  subhead:
    fontFamily: "Barlow Condensed, Barlow, sans-serif"
    fontSize: "1.625rem"
    fontWeight: 600
    lineHeight: 1.05
  label:
    fontFamily: "Barlow Condensed, Barlow, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: "0.04em"
  body:
    fontFamily: "Barlow, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.55
  body-large:
    fontFamily: "Barlow, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 400
    lineHeight: 1.55
  body-strong:
    fontFamily: "Barlow, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 600
    lineHeight: 1.55
rounded:
  none: "0"
  sm: "0.5rem"
  pill: "999px"
  round: "50%"
spacing:
  gutter: "1rem"
  gutter-wide: "2rem"
  slab-gap: "0.75rem"
  slab-pad: "0.75rem 1rem"
  section: "3.5rem"
  max-width: "80rem"
components:
  nav-strip-link:
    backgroundColor: "{colors.masthead-red}"
    textColor: "{colors.paper-white}"
    typography: "{typography.label}"
    height: "2.75rem"
    padding: "0 0.625rem"
  slab-lead:
    backgroundColor: "{colors.masthead-red}"
    textColor: "{colors.paper-white}"
    typography: "{typography.title}"
    rounded: "{rounded.none}"
    padding: "1rem 1.125rem 1.125rem"
  slab-white:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.ink}"
    typography: "{typography.subhead}"
    rounded: "{rounded.none}"
    padding: "{spacing.slab-pad}"
  slab-magenta:
    backgroundColor: "{colors.logotype-magenta}"
    textColor: "{colors.paper-white}"
    typography: "{typography.subhead}"
    rounded: "{rounded.none}"
    padding: "{spacing.slab-pad}"
  slab-blue:
    backgroundColor: "{colors.coverline-blue}"
    textColor: "{colors.paper-white}"
    typography: "{typography.subhead}"
    rounded: "{rounded.none}"
    padding: "{spacing.slab-pad}"
  flash-roundel:
    backgroundColor: "{colors.flash-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.round}"
    size: "7.75rem"
  play-disc:
    backgroundColor: "{colors.flash-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.round}"
    size: "3rem"
  button-book:
    backgroundColor: "{colors.flash-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    height: "3.75rem"
    padding: "0 1.75rem"
  ticket-paper:
    backgroundColor: "{colors.ticket-pink}"
    textColor: "{colors.masthead-red}"
  ticket-number:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.masthead-red}"
  ticket-number-called:
    backgroundColor: "{colors.logotype-magenta}"
    textColor: "{colors.paper-white}"
  ticket-blank:
    backgroundColor: "{colors.masthead-red}"
---

# Design System: Older and Wider

This document follows ASD-STE100 Simplified Technical English.

## Overview

**Creative North Star: "This Week's Issue"**

The home page is the cover and the contents pages of a 1980s British women's weekly. The two hosts are the cover stars. The masthead fills the full width. Coverlines sit on the cover as solid colour slabs. A yellow flash roundel sells the live tour. Below the cover, the contents pages use full-width colour bands: white for listening, red for the tour, pink for the letter, and ink for the footer.

The type is loud, condensed and in capitals. Body text is large and calm, for older eyes. Depth is soft and physical. A coverline lifts like a page that a hand picks up. Photos carry a halftone dot screen, as on cheap magazine paper. Back issues sit on a UK bingo ticket.

The world rejects the podcast default: a hero with a player and a row of equal cards.

**Key Characteristics:**
- Pink cover ground with a red and magenta masthead.
- Solid, square coverline slabs in red, white, magenta and blue.
- Display type in Anton capitals. Labels in Barlow Condensed capitals.
- Tonal halftone screen on photos.
- Bingo ticket grid for back issues, with magenta dabs.
- Soft shadows that respond to hover and focus.

## Colors

The palette comes from the 2027 tour poster. It is saturated, warm and printed in flat areas.

### Primary
- **Cover Pink** (cover-pink): The page ground for the cover and the letter band. Ink text sits on it. Use it as the footer logotype colour on ink.
- **Masthead Red** (masthead-red): The masthead words OLDER and WIDER, the nav strip, the lead coverline, the tour band, section titles, episode numbers and the bingo ticket grid.

### Secondary
- **Logotype Magenta** (logotype-magenta): The word AND in the show name. Also the magenta coverline slab and the bingo dab.
- **Coverline Blue** (coverline-blue): One coverline slab (the shop). Use it only with white large text.

### Tertiary
- **Flash Yellow** (flash-yellow): The flash roundel, the play disc, the Book tickets button, the current-page underline in the nav, the text selection colour and the focus ring on red and ink bands. Use ink text on it.

### Neutral
- **Ink** (ink): All body text, rules under titles, the default focus ring and the footer band.
- **Paper White** (paper-white): The listening band, white coverline slabs, the award panel, ticket number cells and text on red, magenta, blue and ink.
- **Ticket Pink** (ticket-pink): The bingo ticket paper, the player placeholder and the scrollbar track.
- **Studio Grey** (studio-grey): The desktop cover panel backdrop. It matches the backdrop of the cover photo. It is not a brand colour.

Green (#01A05F) is in the brand list from the tour poster. The build does not use it. Do not add it to a surface before you add it to this file.

### Contrast pairs
- White on Masthead Red: 7.98. Use at all sizes.
- Ink on Cover Pink: 8.05. Use at all sizes.
- Ink on Flash Yellow: 12.05. Use at all sizes.
- Masthead Red on Paper White: 7.98. Use at all sizes.
- Masthead Red on Ticket Pink: 6.65. Use at all sizes.
- Masthead Red on Cover Pink: 3.69. Use for large text only.
- White on Logotype Magenta: 4.50. Use for large text only.
- White on Coverline Blue: 4.21. Use for large text only.
- Logotype Magenta on Cover Pink: 2.08. This pair fails. Use it only for the logotype.
- White on Cover Pink: 2.16. This pair fails. Do not use it.

Large text is 24px or more at weight 400, or 18.66px or more at weight 600 or more.

### Named Rules
**The Logotype Exception Rule.** Set the word AND in Logotype Magenta in the show name. This pair is exempt from contrast rules. The exemption applies only to the show name in display lettering.

**The Name Rule.** Write the show name as "Older and Wider". Spell out "and". Do not use an ampersand.

**The Studio Grey Rule.** Use Studio Grey only as the cover panel backdrop, and always under the halftone screen. Do not use it for text, borders or other surfaces.

**The Large Text Only Rule.** Use Masthead Red on Cover Pink, white on Logotype Magenta and white on Coverline Blue only for large text.

## Typography

**Display Font:** Anton (with Barlow Condensed, sans-serif)
**Label Font:** Barlow Condensed 600 (with Barlow, sans-serif)
**Body Font:** Barlow 400 and 600 (with sans-serif)

**Character:** Anton is the shout of a magazine cover. Barlow Condensed is the voice of the coverlines and the labels. Barlow is a clear, friendly text face at a large size.

### Hierarchy
- **Display** (Anton 400, fills the cover width, line height 0.9): The masthead only. The size follows the container width so the name always fits on one line.
- **Headline** (Anton 400, 4rem on phones, 5rem from 48rem, 6rem from 64rem, line height 0.95): Section titles in the tour and the letter bands. The listening title is 3.5rem, then 4.5rem.
- **Title** (Anton 400, 1.875rem, line height 1.08): The lead coverline, the flash roundel top line and the Book tickets button (1.75rem).
- **Subhead** (Barlow Condensed 600, 1.25rem to 1.75rem, line height 1.05 to 1.2): Coverlines, episode titles, tour subtitle, sign-off and sub-section titles.
- **Label** (Barlow Condensed 600, 1rem to 1.125rem, letter spacing 0.04em to 0.12em): Nav links, the issue line, table headings, the ticket serial and short labels.
- **Body** (Barlow 400, 1.125rem, line height 1.55): All running text. Keep lines to 34rem to 36rem, or 52ch.
- **Body Large** (Barlow 400, 1.25rem): The letter.
- **Numerals**: Anton for episode numbers (2.5rem to 4rem) and ticket numbers. Use tabular figures for times, dates and ticket numbers.

### Named Rules
**The Capitals Rule.** Set Anton and Barlow Condensed in capitals with `text-transform`. Write the source text in sentence case.

**The No Serif Rule.** Do not use a serif face. Use only Anton, Barlow Condensed and Barlow.

**The Balance Rule.** Apply balanced wrapping to display, headline, title and subhead text.

## Layout

The page is a vertical stack of full-width colour bands. Content in each band sits in a column of 80rem maximum width. The side gutter is 1rem on phones and 2rem from 48rem.

Breakpoints:
- 48rem (tablet): wider gutter, issue line shows the hosts, larger section titles.
- 64rem (desktop): the cover becomes a three-column panel (19rem, flexible, 19rem). The photo sits at the bottom centre, no wider than 44rem. Coverlines sit on the grey at each side.

On phones the cover photo is full bleed. Coverlines stack under the photo with a 0.75rem gap. The flash roundel hangs over the top right corner of the photo.

Contents bands use 3rem to 3.5rem of vertical space. Desktop grids split the listening band 1.4 to 1, the tour band 1 to 1.25 and the letter band 1 to 1.4. The four "Last called" episodes sit in four columns on desktop and in one column on phones.

Every touch target is 2.75rem high or more.

## Elevation & Depth

The system uses soft, ambient shadows and physical lift. Surfaces are flat colour. Shadows show paper that sits on paper. Hover and focus lift a coverline and turn it a little.

### Shadow Vocabulary
- **Rest** (`0 0.125rem 0.375rem rgba(26, 26, 26, 0.18)`): Coverline slabs and the flash roundel at rest.
- **Lift** (`0 1rem 1.75rem -0.5rem rgba(26, 26, 26, 0.38)`): Coverline slabs and the flash roundel on hover and focus.
- **Button** (`0 0.5rem 1rem -0.25rem rgba(26, 26, 26, 0.4)`): The Book tickets button.
- **Ticket** (`drop-shadow(0 0.625rem 0.875rem rgba(120, 0, 40, 0.24))`): The bingo ticket paper. A drop shadow follows the scalloped edges.

### Halftone screen
Photos carry a tonal halftone dot screen. The dot pitch is 5px. Dots grow in the darker areas of the photo. A grey copy of the photo multiplies with a soft dot pattern, then a high contrast filter makes hard dots. The screen sits over the colour photo at 0.26 opacity with a multiply blend.

On desktop one screen covers the full grey panel. The grey and the photo pass through the same dots, so the photo edge disappears. Coverlines and the roundel sit above the screen.

### Named Rules
**The Page Lift Rule.** Lift a coverline on hover and focus by 0.375rem and turn it by -0.6deg, with the Lift shadow. Use the out-expo curve over 0.45s.

**The Halftone Rule.** Put the halftone screen on cover photos. Remove the screen under `prefers-contrast: more`.

**The Soft Shadow Rule.** Use only blurred shadows. Do not use hard offset shadows.

## Shapes

Coverline slabs, bands, the award panel and ticket cells have square corners. Round forms are for the yellow items: the flash roundel and the play disc are circles, and the Book tickets button is a pill. The player frame has a 0.5rem radius.

Rules are print rules: a 3px ink rule under section titles and above the issue line, and 1px rules elsewhere. The bingo ticket has scalloped tear-off edges at the top and bottom, and a dotted perforation under its serial line. Bingo dabs are irregular blots with a different corner shape on every second number.

## Components

### Nav strip
- **Style:** A slim red strip above the masthead. Links are white Label type, centred.
- **States:** Hover adds an underline. The current page has a thick Flash Yellow underline and `aria-current="page"`.
- **Focus:** The focus ring is Flash Yellow on the red strip.

### Masthead and issue line
- **Masthead:** Display type in Masthead Red across the full width. The word AND is Logotype Magenta.
- **Issue line:** Label type between a 3px ink rule and a 1px ink rule. It shows the issue number and the date at the left, and the hosts at the right from 48rem.

### Coverline slabs
- **Shape:** Square corners. Rest shadow.
- **Lead:** Masthead Red with white Title type, a yellow play disc, the action text and the episode time.
- **White, magenta, blue:** Subhead type. The main line is 1.625rem (1.75rem on magenta and blue). An optional second line is 1.25rem.
- **Hover / Focus:** The Page Lift Rule applies. Hover underlines the main line.

### Flash roundel
- **Style:** A Flash Yellow circle, turned -8deg, with an Anton top line and a Barlow Condensed bottom line in ink.
- **Size:** 7.75rem by default, 6rem on the phone photo corner, 10rem on desktop.
- **Hover / Focus:** It lifts and turns to -10deg.

### Book tickets button
- **Shape:** Pill. 3.75rem high.
- **Style:** Flash Yellow with ink Anton text and a ticket icon. Button shadow.
- **Hover:** Underline.

### Bingo ticket (signature component)
- **Grid:** 9 columns by 3 rows. Each row has 5 numbers and 4 blanks. The grid lines are Masthead Red.
- **Paper:** Ticket Pink with scalloped edges, a Ticket shadow and a red serial line ("Older and Wider", "Ticket" plus the issue number).
- **Number:** Masthead Red Anton numerals on white cells.
- **Blank:** A solid Masthead Red square inside a white border.
- **Dab:** A solid Logotype Magenta blot at full opacity. Do not make the dab translucent. The number turns white. White on solid magenta is 4.5:1, so the pair passes at all text sizes. The four most recent episodes show the dab at rest. Hover, focus and active show the dab on every number.
- **Focus:** A 4px ink ring inside the cell.

### Episode list ("Last called")
- **Style:** An Anton red number at the left, a Subhead title and a Body line with the date and time. A light ink rule under each item.
- **Hover:** Underline on the title.

### Tour dates table
- **Style:** White text on red. Label headings above a 3px white rule. Rows have 1px white rules at 45% opacity. The date column uses Barlow Condensed 600.

## Do's and Don'ts

### Do:
- **Do** write the show name as "Older and Wider", with AND in Logotype Magenta in display lettering.
- **Do** set display, subhead, label, nav and button text in capitals.
- **Do** use the contrast pairs in the Colors section, and keep the large-text-only pairs at large sizes.
- **Do** put the halftone screen on cover photos, and remove it under `prefers-contrast: more`.
- **Do** remove the lift and the turn under `prefers-reduced-motion: reduce`.
- **Do** keep every touch target 2.75rem high or more.
- **Do** keep all style rules in the stylesheet and all tokens as custom properties on `:root`.

### Don't:
- **Don't** use an ampersand in the show name.
- **Don't** use Studio Grey outside the cover panel.
- **Don't** put white or Logotype Magenta text on Cover Pink, except the logotype.
- **Don't** use em dashes.
- **Don't** use eyebrow text above headings.
- **Don't** number sections.
- **Don't** use gradient text.
- **Don't** use hard offset shadows.
- **Don't** use inline styles or inline scripts.
- **Don't** use a serif face.
