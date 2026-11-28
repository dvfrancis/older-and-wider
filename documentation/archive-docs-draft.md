# Draft text for the archive page

This file follows ASD-STE100 Simplified Technical English.

This file holds draft text for `README.md` and `TESTING.md`. Merge the text by hand. Then delete this file.

## Text for README.md

### Features: the archive page

The archive page, `archive.html`, has three sections:

1. Older and Wider live. This table shows each show with both hosts, with the latest show first.
2. Jenny's solo shows. This section has these parts:
   - "Coming up". This part shows a message and a link to `jennyeclair.com` when no solo show is on sale.
   - "Earlier tours". This table has one row for each tour or Edinburgh show.
   - "Every date we found". Each tour has its dates in a `details` element. The Grumpy Old Women shows are in a separate group.
3. Wider work. This section lists the books, television and radio of each host. Each item has a link to its source.

Each date is in a `time` element with a `datetime` attribute. If only the month is known, the attribute has the form `YYYY-MM`.

The page has no script of its own. All the content shows without JavaScript.

### Procedures: the archive page

#### Add an Older and Wider show to the archive

1. Make sure that a podcast episode or a venue listing confirms the show.
2. Open `archive.html`.
3. Find the table with the class `arc-shows` in the section "Older and Wider live".
4. Add a new `tr` element in the correct position. The latest show is first.
5. Put the date in a `time` element. Use the form `YYYY-MM-DD`.
6. If only the month is confirmed, use the form `YYYY-MM`. Write the month and the year only.
7. Add the source to the paragraph of sources below the table, if the source is new.

#### Move a tour from the live shows page to the archive

1. Wait until the last show of the tour is in the past.
2. Copy each show of the tour from `live-shows.html`.
3. Add each show to the Older and Wider table in `archive.html`, as in the procedure above.
4. Remove the ticket links. The archive has no ticket links.
5. Remove the shows from the recent section of `live-shows.html`.

#### Add a solo tour

A solo tour has many more dates than an Older and Wider tour. You must add the dates by hand.

1. Add a row to the "Earlier tours" table. Give the name of the tour, the years and a short note.
2. Write the note in your own words. Do not copy text from another website.
3. Add a new `li` element to the list with the class `arc-tour-list`, below "Solo tours".
4. In the `li` element, add a `details` element with the class `arc-tour` and a unique `id`, for example `dates-new-tour`.
5. In the `summary` element, give the name of the tour, the years and the number of dates.
6. Add a table with the class `arc-dates`. Use one `tbody` element for each year, with the latest year first.
7. Start each `tbody` element with a row of the class `arc-year`.
8. Give each date in the form "Sat 5 Oct 2024". Put it in a `time` element.
9. Write the town or city in the second cell. Write the venue in the third cell.
10. Link the name of the tour in the "Earlier tours" table to the `id` of the `details` element.

#### Correct or remove a show

1. Find the show in `archive.html`. Search for its date in the form `YYYY-MM-DD`.
2. To correct the show, change the date, the town or the venue.
3. To remove the show, delete its `tr` element.
4. If you change a tour, change the number of dates in its `summary` element.
5. Change the total number of dates in the paragraph below "Every date we found".

### Data sources and limits

- The Older and Wider shows come from the episode notes of the podcast feed, and from the listings of the venues.
- The solo dates come from archived copies of `jennyeclair.com` and `grumpyoldwomenlive.com`. Issue #29 gives the method.
- A solo date was announced. The data does not show that the show occurred.
- The page shows the Grumpy Old Women UK tour of autumn 2007. Jenny Eclair wrote the show, but a different cast performed it. A note on the tour tells the visitor this.
- Two rows in the source data had no place. The page does not show them. The dates are 20 April 2016 and 20 April 2017.

### Navigation

The nav strip on `archive.html` has five links, in this order: Home, About, Live Shows, Archive, Message Board. The Archive link has `aria-current="page"`.

## Text for TESTING.md

### Archive page tests

| Test | Action | Expected result | Result |
|---|---|---|---|
| W3C Markup Validator | Send `archive.html` to the Nu validator. | No errors and no warnings. | Pass. No messages, 28 November 2026. |
| W3C CSS Validator | Send `assets/css/main.css` to the CSS validator. | No new errors from the archive block. | Pass. The three errors are older. They are on lines 185, 191 and 1030, outside the archive block. |
| Phone width | Open the page at 375 pixels wide. Open each `details` element. | No horizontal scroll. Each row of a table shows as a block. | Pass. The scroll width is 375 pixels. |
| Desktop width | Open the page at 1440 pixels wide. | The tables show as tables. The tours show in two columns. | Pass. |
| Details elements | Click the summary of each tour. Then press Enter on a summary with the keyboard. | The tour opens and closes. The plus sign changes to a minus sign. | To do. |
| No JavaScript | Disable JavaScript. Reload the page. | All content shows. The `details` elements still open and close. | To do. |
| Contrast | Examine each pair of colours. | Each pair meets WCAG 2.1 level AA. Red text on pink is 1.75rem or larger. | Pass, by the contrast pairs in `DESIGN.md`. |
| Jump links | Click each link below the introduction. | The page moves to the correct section. | To do. |
| Lighthouse | Run Lighthouse for mobile and desktop. | Record the four scores. | To do. |
