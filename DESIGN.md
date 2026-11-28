---
name: Older and Wider
description: The site as this week's issue of a 1980s British women's weekly. The home page is the cover. The other pages are inside pages.
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
  feature-band-pink:
    backgroundColor: "{colors.cover-pink}"
    textColor: "{colors.ink}"
  feature-band-white:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.ink}"
  feature-title:
    textColor: "{colors.masthead-red}"
    typography: "{typography.headline}"
  standfirst:
    textColor: "{colors.ink}"
    typography: "{typography.body-strong}"
    width: "32ch"
  second-print:
    backgroundColor: "{colors.paper-white}"
    padding: "0.625rem 0.625rem 0.75rem"
    width: "20rem"
  contact-sheet:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper-white}"
    padding: "1.5rem 1rem 1.75rem"
  hear-band:
    backgroundColor: "{colors.masthead-red}"
    textColor: "{colors.paper-white}"
    typography: "{typography.headline}"
  board-slab:
    backgroundColor: "{colors.masthead-red}"
    textColor: "{colors.paper-white}"
    typography: "{typography.title}"
    rounded: "{rounded.none}"
    padding: "1.25rem 1.25rem 1.375rem"
  board-slab-icon:
    backgroundColor: "{colors.flash-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.round}"
    size: "3.5rem"
  board-print:
    backgroundColor: "{colors.paper-white}"
    padding: "0.625rem 0.625rem 0.75rem"
    width: "34rem"
  board-flash:
    backgroundColor: "{colors.flash-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.round}"
    size: "6.5rem"
  board-load:
    backgroundColor: "{colors.masthead-red}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.none}"
    height: "3.25rem"
    padding: "0.75rem 1.25rem"
  post-letter:
    backgroundColor: "{colors.ticket-pink}"
    textColor: "{colors.masthead-red}"
  post-red:
    backgroundColor: "{colors.masthead-red}"
    textColor: "{colors.paper-white}"
  post-white:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.masthead-red}"
  post-pin:
    backgroundColor: "{colors.flash-yellow}"
    rounded: "{rounded.round}"
    size: "1.125rem"
  err-print:
    backgroundColor: "{colors.paper-white}"
    width: "22rem"
  err-flash:
    backgroundColor: "{colors.flash-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.round}"
    size: "7.75rem"
---

# Design System: Older and Wider

This document follows ASD-STE100 Simplified Technical English.

## Overview

**Creative North Star: "This Week's Issue"**

The home page is the cover and the contents pages of a 1980s British women's weekly. The two hosts are the cover stars. The masthead fills the full width. Coverlines sit on the cover as solid colour slabs. A yellow flash roundel sells the live tour. Below the cover, the contents pages use full-width colour bands: white for listening, red for the tour, pink for the letter, and ink for the footer.

The type is loud, condensed and in capitals. Body text is large and calm, for older eyes. Depth is soft and physical. A coverline lifts like a page that a hand picks up. Photos carry a halftone dot screen, as on cheap magazine paper. Back issues sit on a UK bingo ticket.

The other pages are inside pages of the same issue:
- The About page is a feature interview spread, with one profile for each host.
- The Message Board page is the readers' page. Posts show as letters and prints pinned to a wall.
- The 404 page is an error in print. The missing page "went to press missing".

The world rejects the podcast default: a hero with a player and a row of equal cards.

**Key Characteristics:**
- Pink cover ground with a red and magenta masthead.
- Solid, square coverline slabs in red, white, magenta and blue.
- Display type in Anton capitals. Labels in Barlow Condensed capitals.
- Tonal halftone screen on photos.
- Bingo ticket grid for back issues, with magenta dabs.
- Soft shadows that respond to hover and focus.
- Host photos as white-bordered prints, laid on the page at a small angle.
- A pinned post wall in three paper stocks, with a yellow pin on each post.

## Colors

The palette comes from the 2027 tour poster. It is saturated, warm and printed in flat areas.

### Primary
- **Cover Pink** (cover-pink): The page ground for the cover, the letter band, the About intro band, the Jenny profile band and the Message Board intro band. Ink text sits on it. Use it for the word AND in the footer logotype on ink.
- **Masthead Red** (masthead-red): The colour of these items:
  - The masthead words OLDER and WIDER, and the nav strip.
  - The lead coverline, the follow slab and the load button.
  - Section titles, feature titles, page titles and drop caps.
  - The tour band and the "Hear them for yourself" band.
  - Episode numbers, the bingo ticket grid and the red post stock.

### Secondary
- **Logotype Magenta** (logotype-magenta): The word AND in the show name on pink. In the footer on ink, OLDER and WIDER are magenta and AND is pink, so that the big words stay darker than AND. In the masthead and the footer mark, AND is 0.75 of the size of OLDER and WIDER, as on the merchandise. In the About title, AND is the same size as the other words, in magenta. In the favicon, AND is smaller again, so that it fits on its own line. Also the magenta coverline slab and the bingo dab.
- **Coverline Blue** (coverline-blue): One coverline slab (the shop). Use it only with white large text.

### Tertiary
- **Flash Yellow** (flash-yellow): The colour of these items. Use ink text on it.
  - The flash roundels (the cover, the "Hello" roundel and the 404 roundel).
  - The play disc, the Instagram icon disc and the post pin.
  - The Book tickets button and the current-page underline in the nav.
  - The text selection colour.
  - The focus ring on red and ink bands.

### Neutral
- **Ink** (ink): All body text, rules under titles, the default focus ring, the contact sheet and the footer band.
- **Paper White** (paper-white): The listening band, the Judith profile band, the posts band, white coverline slabs, the award panel, ticket number cells, print borders, the white post stock and text on red, magenta, blue and ink.
- **Ticket Pink** (ticket-pink): The bingo ticket paper, the pink letter post stock, the player placeholder and the scrollbar track. In the CSS it is `--pink-soft`.
- **Studio Grey** (studio-grey): The desktop cover panel backdrop. It matches the backdrop of the cover photo. It is not a brand colour.

Green (#01A05F) is in the brand list from the tour poster. The build does not use it. Do not add it to a surface before you add it to this file.

### Contrast pairs
- White on Masthead Red: 7.98. Use at all sizes.
- Ink on Cover Pink: 8.05. Use at all sizes.
- Ink on Flash Yellow: 12.05. Use at all sizes.
- Masthead Red on Paper White: 7.98. Use at all sizes.
- Masthead Red on Ticket Pink: 6.65. Use at all sizes.
- Ink on Ticket Pink: 14.49. Use at all sizes.
- White on Ink: 17.40. Use at all sizes.
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
- **Headline** (Anton 400, 4rem on phones, 5rem from 48rem, 6rem from 64rem, line height 0.95): Section titles in the tour and the letter bands, the Message Board title and the 404 title. Other sizes:
  - The listening title is 3.5rem, then 4.5rem.
  - The About feature titles are 3.25rem, then 4.5rem from 48rem, then 6rem from 64rem.
  - The "Hear them for yourself" title is 3.5rem, then 4.5rem, then 5rem.
- **Title** (Anton 400, 1.875rem, line height 1.08): The lead coverline, the flash roundel top line and the Book tickets button (1.75rem).
- **Subhead** (Barlow Condensed 600, 1.25rem to 1.75rem, line height 1.05 to 1.2): Coverlines, episode titles, tour subtitle, sign-off and sub-section titles.
- **Label** (Barlow Condensed 600, 1rem to 1.125rem, letter spacing 0.04em to 0.12em): Nav links, the issue line, table headings, the ticket serial and short labels.
- **Body** (Barlow 400, 1.125rem, line height 1.55): All running text. Keep lines to 34rem to 36rem, or 52ch.
- **Body Large** (Barlow 400, 1.25rem): The letter, the Message Board lead and the 404 lead.
- **Standfirst** (Barlow 600, 1.5rem, then 2rem from 48rem, then 2.25rem from 64rem, line height 1.25): The opening line of a feature. Maximum width 32ch.
- **Drop cap** (Anton 400, 4.25em, line height 0.8, Masthead Red): The first letter of the first paragraph in each host profile (`.opener`).
- **Post text** (Barlow Condensed 600, 1.75rem, line height 1.08, capitals): The words of a post on the wall. The first post is 2.25rem from 48rem.
- **Feature body** (Barlow 400, 1.1875rem from 48rem): The About page columns. Maximum width 70ch.
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

### Pages
The site has five pages. Each page has the same nav strip and the same footer.
- `index.html`: the cover and the contents pages.
- `about.html`: the feature spread.
- `message-board.html`: the readers' page.
- `404.html`: the error in print.
- `privacy.html`: the privacy notice.

The nav strip has three links: Home, About, Message Board. The privacy page has no link in the nav strip. The footer links to it.

These pages are deleted. Do not link to them:
- `contact.html`
- `contact-completion.html`
- `mailing-list-completion.html`

Their images (`contact-completion.webp` and `mailing-list-completion.webp`) are also deleted. The old stylesheet `styles.css` is deleted. All pages use `assets/css/main.css`.

No page has a meta refresh. The 404 page has `<meta name="robots" content="noindex">`.

### About page layout
- Bands: the intro on Cover Pink, the Judith profile on Paper White, the Jenny profile on Cover Pink, then the red "Hear them for yourself" band.
- Each band uses `.about-inner`: maximum width 80rem, padding 3rem at the top and 3.5rem at the bottom. From 64rem the padding is 3.5rem and 4rem.
- On phones the feature photo is full bleed and the body sits under it.
- From 64rem the feature is two columns: the photo at 36rem maximum, and the body. The Jenny profile flips the columns (`.feature-flip`), so the photo is at the right.
- The contact sheet shows two frames in a row on phones and four frames from 48rem.
- From 64rem the hear band is two columns: the title, and the links at the right.

### Message Board layout
- The intro band is on Cover Pink. From 64rem it is two columns at 1.3 to 1: the text, and the print.
- The posts band is on Paper White.
- On phones the wall is one column. Each post has its own width (84% to 100%) and alignment (start, centre or end).
- From 48rem the wall is a six-column grid. The posts span 4, 2, 3, 3, 2 and 4 columns. Some posts start lower, by 1rem to 2rem.
- When Instagram loads, the wall becomes an even grid (see the Loaded post wall component).

### 404 page layout
- On phones the text sits above the print.
- From 64rem the page is two columns at 1.5 to 1, centred on the vertical axis.

## Elevation & Depth

The system uses soft, ambient shadows and physical lift. Surfaces are flat colour. Shadows show paper that sits on paper. Hover and focus lift a coverline and turn it a little.

### Shadow Vocabulary
- **Rest** (`0 0.125rem 0.375rem rgba(26, 26, 26, 0.18)`): Coverline slabs and the flash roundel at rest.
- **Lift** (`0 1rem 1.75rem -0.5rem rgba(26, 26, 26, 0.38)`): Coverline slabs and the flash roundel on hover and focus.
- **Button** (`0 0.5rem 1rem -0.25rem rgba(26, 26, 26, 0.4)`): The Book tickets button.
- **Ticket** (`drop-shadow(0 0.625rem 0.875rem rgba(120, 0, 40, 0.24))`): The bingo ticket paper. A drop shadow follows the scalloped edges.
- **Print** (`0 0.625rem 1.25rem -0.375rem rgba(26, 26, 26, 0.35)`): The second photo in each profile and the Message Board print.
- **Post** (`0 0.625rem 1.25rem -0.375rem rgba(26, 26, 26, 0.3)`): Each post on the wall at rest. A post uses the Lift shadow on hover and focus.
- **Pin** (`0 0.1875rem 0.25rem rgba(26, 26, 26, 0.35)`): The yellow pin on each post.

The 404 print uses the Lift shadow at rest.

### Halftone screen
Photos carry a tonal halftone dot screen. The dot pitch is 5px. Dots grow in the darker areas of the photo. A grey copy of the photo multiplies with a soft dot pattern, then a high contrast filter makes hard dots. The screen sits over the colour photo at 0.26 opacity with a multiply blend.

On desktop one screen covers the full grey panel. The grey and the photo pass through the same dots, so the photo edge disappears. Coverlines and the roundel sit above the screen.

The screen also covers these photos. Each one sets `--screen-photo` to its own image, with the same `--dot`, `--screen-lift` and `--screen-ink` values.
- The three large About photos (`.photo-frame`: `.photo-team`, `.photo-judith`, `.photo-jenny`).
- The Message Board print (`.board-print-photo`).
- The 404 print (`.err-photo`).

The second photos and the contact sheet frames also carry the screen. Their dot layer uses the 256 pixel copy of each photo.

### Named Rules
**The Page Lift Rule.** Lift a coverline on hover and focus by 0.375rem and turn it by -0.6deg, with the Lift shadow. Use the out-expo curve over 0.45s.

**The Halftone Rule.** Put the halftone screen on every photo. Remove the screen under `prefers-contrast: more`.

**The Laid Print Rule.** Show a loose photo as a print on the page. Give it a white border and a soft shadow. Turn it between 1.5deg and 2deg.

**The Straight Embed Rule.** Remove the tilt from a post when Instagram loads it. A live embed sits straight in an even grid.

**The Soft Shadow Rule.** Use only blurred shadows. Do not use hard offset shadows.

## Shapes

Coverline slabs, bands, the award panel and ticket cells have square corners. Round forms are for the yellow items: the flash roundel and the play disc are circles, and the Book tickets button is a pill. The player frame has a 0.5rem radius.

Prints have a white border. The second photo and the Message Board print have 0.625rem of white padding (0.75rem at the bottom). The 404 print has a 0.625rem white border. The post pin is a circle.

Rules are print rules: a 3px ink rule under section titles, feature titles and the Message Board title, and above the issue line. Rules elsewhere are 1px. The post meta line has a 1px rule in the text colour.

The contact sheet is a strip of film. White sprocket holes run along the top and the bottom edge. Each hole is a solid white 1rem square, on a 2.5rem pitch.

Prints and posts are turned a little. The values are:
- Second photos: -1.5deg (Jenny) and 1.5deg (Judith).
- Message Board print: 1.5deg.
- 404 print: 2deg.
- Posts 1 to 6: -1deg, 1.2deg, -0.6deg, 1.4deg, -1.3deg and 0.5deg. Each post sets `--tilt`.

The bingo ticket has scalloped tear-off edges at the top and bottom, and a dotted perforation under its serial line. Bingo dabs are irregular blots with a different corner shape on every second number.

## Components

### Nav strip
- **Style:** A slim red strip above the masthead. Links are white Label type, centred.
- **Links:** Home, About, Message Board. The strip is the same on every page.
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

### Feature spread (About)
- **Title:** `.about-title` and `.profile-title`. Headline type in Masthead Red, with a 3px ink rule under it. The word AND in the page title is Logotype Magenta (`.masthead-and`).
- **Standfirst:** `.standfirst`. Standfirst type in ink, under the title.
- **Feature photo:** `.feature-photo` with a `.photo-frame`. A square photo for the intro, and a 4:5 portrait photo for each host. The halftone screen covers it. The caption is Label type.
- **Body:** `.feature-body`. Body type in a grid with a 1rem gap. The first paragraph of a host profile has a drop cap (`.opener`).
- **Award panel:** the intro body ends with the award line (`.award`).

### Host profiles (About)
- **Judith:** `.profile-judith`. Paper White band. Photo at the left from 64rem.
- **Jenny:** `.profile-jenny`. Cover Pink band. Photo at the right from 64rem (`.feature-flip`).
- **Second photo:** `.second-photo`. A white print, 20rem maximum, with the Print shadow. It turns -1.5deg. In the Judith profile it turns 1.5deg and has a 1px ink border at 15% opacity, so it shows on the white band.

### Contact sheet (About)
- **Style:** `.contact-sheet`. A strip of film on Ink, with white sprocket holes at the top and the bottom.
- **Title:** `.sheet-title`. Barlow Condensed 600, 1.25rem, capitals, letter spacing 0.08em, white.
- **Frames:** `.sheet-frames`. Square photos with a Label caption under each one. Two frames in a row on phones, four from 48rem.

### Hear them for yourself band (About)
- **Style:** `.about-listen`. A Masthead Red band with white text. The focus ring is Flash Yellow.
- **Title:** `.hear-title`. Headline type, white.
- **Links:** a white coverline slab with a play disc ("Play the latest episode"), and a text link to every episode on Acast (`.hear-all`, 2.75rem high).

### Follow slabs (Message Board)
- **Instagram slab:** `.slab.slab-lead.board-slab`. A red slab with a yellow Instagram icon disc (`.board-slab-icon`, 3.5rem), a Title line at 2.5rem and the handle (`.board-handle`, 1.375rem, not in capitals).
- **Facebook slab:** `.slab.slab-white.board-slab-small`. A white slab with a red Subhead line and the Facebook icon.
- **Hover / Focus:** The Page Lift Rule applies.

### Halftone print with Hello roundel (Message Board)
- **Print:** `.board-print`. A white print of the hosts, 34rem maximum, turned 1.5deg, with the Print shadow. The halftone screen covers the photo.
- **Roundel:** `.flash.board-flash`. A Flash Yellow circle at the top left corner of the print. The top line is "Hello". The size is 6.5rem, and 8rem from 64rem.
- **State:** The roundel is a paragraph, not a link. It does not lift on hover. It keeps the -8deg turn and the Rest shadow.

### Click-to-load consent block (Message Board)
- **Purpose:** Nothing loads from Instagram until the visitor presses the button. No cookie is set before that.
- **Button:** `.board-load`. A square Masthead Red button with white Barlow Condensed 600 capitals at 1.5rem, an Instagram icon and the Rest shadow. Minimum height 3.25rem.
- **Hover / Focus:** The Page Lift Rule applies, with an underline.
- **Cookie note:** `.board-note`. Body type under the button. It tells the visitor that Instagram can set cookies.
- **Script:** `assets/js/message-board.js` adds Instagram's `embed.js` when the visitor presses the button. The button is disabled while the script loads.
- **After load:** The script hides the block (`hidden`) and moves focus to the "On the board" title.
- **On error:** The script removes the failed script and enables the button again. The post links still work.

### Click-to-load player (Home)
- **Purpose:** Nothing loads from Acast until the visitor presses the button. The site does not remember the choice.
- **Panel:** `.player-consent`. A Ticket Pink panel with a 0.5rem radius. The minimum height is 14rem, and 28rem from 64rem.
- **Button:** `.board-load.player-load`. The load button style, with a play icon and the label "Play here".
- **Note:** `.player-note`. Body type. It tells the visitor that the player stores a language setting and a session item.
- **Without JavaScript:** the button and the note are hidden. A "Listen on Acast" link in the same style shows.
- **Script:** `assets/js/player.js` puts the Acast iframe in place of the panel and moves focus to it.

### Cookie banner (all pages)
- **Purpose:** It asks about analytics cookies only. Google Analytics loads only after "Accept".
- **Position:** `.consent`. It sits after the footer and sticks to the bottom of the window. It does not trap focus.
- **Style:** Paper White with ink text, a 3px ink rule at the top and a soft upward shadow.
- **Title:** `.consent-title`. Barlow Condensed 600, 1.5rem, capitals, Masthead Red.
- **Buttons:** `.consent-button`. "Accept" and "Reject" have the same size, colour and weight: Masthead Red with white Label type, 3.25rem high. They are in two equal columns on phones, and 10rem each from 48rem.
- **Hover / Focus:** the button lifts by 0.25rem with the Lift shadow and an underline.
- **Motion:** the banner rises from the bottom over 0.45s on the out-expo curve. Under `prefers-reduced-motion: reduce` it has no animation.
- **Reopen:** the "Cookie settings" button in the footer (`.footer-settings`) opens the banner and shows the earlier choice.

### Privacy page
- **Intro band:** Cover Pink. A Headline title in Masthead Red (`.privacy-title`), the issue line with the date, and Body Large text (`.privacy-lead`).
- **Table band:** Paper White. On phones, each row of `.privacy-table` is a block with a Label above each value. From 48rem it is a table with a 3px ink rule under the headings.
- **Lower band:** Cover Pink, two columns from 64rem. It holds "Changing your mind" and "Who looks after this site".
- **Section titles:** `.privacy-heading`. Anton, 2.75rem, then 3.5rem from 48rem, Masthead Red, with a 3px ink rule.

### Pinned post wall (Message Board)
- **Structure:** `.board-list`. Each post is a `blockquote.instagram-media` with one link inside. Without JavaScript, each post is a link to Instagram.
- **Paper stocks:** Each post uses one of three stocks:
  - Pink letter (`.post-letter`): Ticket Pink, with ink post text.
  - Red slab (`.post-red`): Masthead Red, with white text.
  - White print (`.post-white`): Paper White, with a 1px ink border at 18% opacity and ink post text.
- **Pin:** A Flash Yellow circle, 1.125rem, at the top centre of each post, with the Pin shadow.
- **Content:** a meta line (`.post-meta`: Label type, icon, kind of post and date), the post text (`.post-text`) and an underlined link (`.post-link`).
- **Tilt and width:** Each post has its own turn (`--tilt`) and width. See Shapes and Layout.
- **Hover / Focus:** The post lifts by 0.375rem, turns -0.6deg and takes the Lift shadow. The link underline gets thicker.

### Loaded post wall (Message Board)
- **Trigger:** `.board-list:has(iframe)`. Instagram replaces each post with an iframe.
- **Grid:** `repeat(auto-fill, minmax(min(100%, 21rem), 1fr))` with a 1.5rem gap.
- **Tilt:** removed. Each post stretches to the full width of its cell. Column spans and top offsets are removed.
- **Width override:** Instagram sets an inline `min-width` of 326px on the iframe. The CSS overrides it with `width: 100%`, `min-width: 0` and `margin: 0`, all with `!important`. This lets a post fit a small phone.

### Error in print (404)
- **Title:** `.err-title`. Headline type in Masthead Red: "This page went to press missing".
- **Issue line:** the issue line component, with "Error in print" and an apology from the hosts.
- **Lead:** `.err-lead`. Body Large, 34rem maximum.
- **Actions:** a lead coverline slab (`.err-slab`, 30rem maximum) to play the latest episode, and a text link to the home page (`.err-home`, 2.75rem high).
- **Print:** `.err-photo`. A photo of Judith with the halftone screen, a 0.625rem white border and the Lift shadow. It turns 2deg. The width is 22rem, and 26rem from 64rem.
- **Roundel:** `.err-flash`. A Flash Yellow circle at the top left of the print, turned -8deg, with the Rest shadow. The top line is "404" in Anton. The bottom line is "Gone to press". The size is 7.75rem, and 10rem from 64rem. It is not a link, and it has `aria-hidden="true"`.
- **Page head:** `<meta name="robots" content="noindex">`. No meta refresh.

## Do's and Don'ts

### Do:
- **Do** write the show name as "Older and Wider", with AND in Logotype Magenta in display lettering.
- **Do** set display, subhead, label, nav and button text in capitals.
- **Do** use the contrast pairs in the Colors section, and keep the large-text-only pairs at large sizes.
- **Do** put the halftone screen on every photo, and remove it under `prefers-contrast: more`.
- **Do** remove the lift and the turn under `prefers-reduced-motion: reduce`.
- **Do** keep every touch target 2.75rem high or more.
- **Do** keep all style rules in the stylesheet and all tokens as custom properties on `:root`.
- **Do** load a third-party embed only after the visitor presses a button. Tell the visitor about cookies next to the button.
- **Do** remove the tilt from a post when Instagram loads it.

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
- **Don't** load Instagram, Acast, Google Analytics, or any other third-party script, before the visitor asks.
- **Don't** add a meta refresh to a page.
- **Don't** link to the deleted contact and completion pages.
