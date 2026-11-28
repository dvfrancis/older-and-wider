# The Older and Wider Podcast

## Overview

Older and Wider is a humorous (and [real](https://shows.acast.com/older-and-wider-podcast)) podcast, where two friends chat and share their day-to-day experiences as older women. It is hosted by retired television producer/writer, Judith Holder, and award-winning comedian, Jenny Eclair.

The website gives information about the podcast. It has an embedded podcast player, the dates of the 2027 live tour, a link to the shop, and access to the Instagram page that the hosts call the "message board". The podcast has had over 7.5 million downloads.

### Background Information

There are several references scattered across the site which refer back to items that are regularly mentioned, or discussed, on the podcast:

- Older and Wider Listeners are called OWLs.
- Anyone listening to the podcast is regarded as "part of the gang", or a "gang member".
- Snore Law is invoked by either Jenny or Judith when they feel the conversation has got too boring; this is usually accompanied by a loud snoring noise.
- Jenny and Judith both love coleslaw, and it is mentioned frequently.
- When people contact the podcast, Jenny and Judith insist that people include their age with fractions; for example, "This email is from Sarah who is 59 and three quarters" (the removed contact form used a text input for age for this reason).
- Jenny and Judith have stated that a Breton top is the de facto uniform of an OWL.
- Jenny and Judith regularly refer to the podcast Instagram page as the "message board".
- There are a couple of regular podcast features:
    - Culture corner - Jenny and Judith discuss any books they are reading, television they've enjoyed, visits to art galleries, etc.
    - Taste sensations - Jenny and Judith discuss any amazing meals they may have had in the previous week.

### Site Preview

![Preview of the Older and Wider website at different screen sizes](assets/images/site-preview.webp)

This preview shows the earlier design. The [Screenshots](#screenshots) section shows the new design.

### Site Link

[here]: https://older-and-wider.dominicfrancis.co.uk
The live site can be accessed [here].

## Index

1. [Overview](#the-older-and-wider-podcast)
    1. [Background Information](#background-information)
    2. [Site Preview](#site-preview)
    3. [Site Link](#site-link)
2. [Design](#design)
    1. [Design System](#design-system)
    2. [Screenshots](#screenshots)
    3. [Earlier Design Concepts](#earlier-design-concepts)
3. [User Experience Design](#user-experience-design)
    1. [Strategy](#strategy)
        1. [User Experience](#user-experience)
        2. [User Expectations](#user-expectations)
        3. [User Stories](#user-stories)
    2. [Scope](#scope)
        1. [Existing Features](#existing-features)
        2. [Removed Features](#removed-features)
        3. [Future Features](#future-features)
    3. [Structure](#structure)
        1. [User Flow Diagram](#user-flow-diagram)
    4. [Skeleton](#skeleton)
        1. [Wireframes](#wireframes)
            1. [Mobile](#mobile)
            2. [Mobile with Expanded Menu](#mobile-with-expanded-menu)
            3. [Tablet](#tablet)
            4. [Desktop](#desktop)
    5. [Surface](#surface)
        1. [Colours](#colours)
        2. [Typography](#typography)
        3. [Media](#media)
        4. [Content](#content)
4. [Testing](#testing)
5. [Deployment](#deployment)
    1. [Amazon S3 and CloudFront](#amazon-s3-and-cloudfront)
    2. [Automatic Episode Update](#automatic-episode-update)
    3. [Live Shows Maintenance](#live-shows-maintenance)
        1. [Add a Show](#add-a-show)
        2. [Correct a Show](#correct-a-show)
        3. [Remove a Cancelled Show](#remove-a-cancelled-show)
        4. [Move a Finished Tour to the Archive](#move-a-finished-tour-to-the-archive)
    4. [Sitemap and robots.txt](#sitemap-and-robotstxt)
    5. [Forks](#forks)
    6. [Local Clones](#local-clones)
    7. [Gitpod Workspaces](#gitpod-workspaces)
6. [Credits and References](#credits-and-references)
7. [Technologies Used](#technologies-used)
8. [Acknowledgements](#acknowledgements)

## Design

### Design System

The redesign gives the site the look of a weekly magazine. The 2027 tour poster for "Even Older and Wider" sets the colours and the fonts. [DESIGN.md](DESIGN.md) holds the full design system. Read it before you change the look of the site. [PRODUCT.md](PRODUCT.md) holds the product record: the users, the purpose and the brand rules.

The main parts of the design are:

- A pink ground (#F492BF).
- Red (#A60201) for the masthead and the display text.
- The logotype "Older and Wider". The word "and" is magenta (#E8046C), as on the tour poster.
- Three fonts, hosted on the site: Anton for display text, Barlow Condensed for labels, and Barlow for body text.
- A halftone dot screen on the photos, as in a printed magazine.
- A magazine cover on the home page, with an issue line and cover lines.
- A bingo ticket on the home page that leads to back issues of the podcast.
- A table of the dates of the 2027 tour.
- A letter to the listeners, "Dear OWLs", from Jenny and Judith.

The show name is "Older and Wider". The site does not use an ampersand in the name.

### Screenshots

The screenshots show the live site on 27 November 2026, in Safari's engine (WebKit). The phone width is 390 px. The desktop width is 1440 px.

| Page | Phone | Desktop |
|---|---|---|
| Home | [Phone](documentation/screenshots/phone-index.webp) | [Desktop](documentation/screenshots/desktop-index.webp) |
| About | [Phone](documentation/screenshots/phone-about.webp) | [Desktop](documentation/screenshots/desktop-about.webp) |
| Message Board | [Phone](documentation/screenshots/phone-message-board.webp) | [Desktop](documentation/screenshots/desktop-message-board.webp) |
| Privacy | [Phone](documentation/screenshots/phone-privacy.webp) | [Desktop](documentation/screenshots/desktop-privacy.webp) |
| 404 | [Phone](documentation/screenshots/phone-404.webp) | [Desktop](documentation/screenshots/desktop-404.webp) |
| Cookie banner | [Phone](documentation/screenshots/phone-consent-banner.webp) | [Desktop](documentation/screenshots/desktop-consent-banner.webp) |

The home page on a phone:

![The home page on a phone, with the masthead, the cover photo, the latest episode and the cookie banner](documentation/screenshots/phone-consent-banner.webp)

The home page on a desktop:

![The top of the home page on a desktop, with the masthead, the cover photo and the cookie banner](documentation/screenshots/desktop-consent-banner.webp)

### Earlier Design Concepts

The folder `design-options/` holds five earlier design concepts:

- `bingo`
- `magazine`
- `pier-show`
- `step-row`
- `variety-bill`

The project keeps them for reference. The build script does not deploy them. The live design develops the magazine concept.

## User Experience Design

### Strategy

#### User Experience

- Target audience

    - Women over 60 (but anyone welcome).
    - Are mature individuals, with lots of life experience.
    - May have children and grandchildren.
    - Might still be working or retired.
    - Could be anyone looking for information about the podcast.
 
#### User Expectations

- An accessible and responsive website.
- Relevant information that is easily found.
- Simple website navigation.
- A way to get in touch with the podcast, to share experiences.
- An experience that matches existing expectations of what to expect from a website; for example, links are easy to identify and function as expected.
- An appealing visual design.

#### User Stories

- First time visitor goals:

    - "What is the Older and Wider podcast about?"
    - "Who is Jenny Eclair?"
    - "Who is Judith Holder?"
    - "Where can I listen to the Older and Wider Podcast"
    - "When are episodes of the Older and Wider podcast released?"

- Returning visitor goals:

    - "I want to find out more background information about the Older and Wider podcast"
    - "What was mentioned during the 'Culture Corner' segment of this week's show?"
    - "Has the podcast won any awards?"
    - "What is the 'Message Board' - it was mentioned by Jenny and Judith in this week's episode, but where can I access it?"

- Frequent visitor goals:

    - "How can I contact Jenny and Judith to share my experiences, or comment on an item that was mentioned in the show?"
    - "Is there any podcast merchandise available?"
    - "Can I watch the podcast being performed live?"

### Scope

#### Existing Features

- General

    - Each page is responsive. The layout changes at 48rem (768px) and at 64rem (1024px).
    - Each page works without JavaScript.
    - The site has six pages: Home, About, Live Shows, Message Board, Privacy and a custom 404 page.
    - No third-party embed loads until the visitor asks for it. Google Analytics loads only after the visitor accepts analytics cookies.
    - The screenshots in this section show the earlier design. New screenshots of the redesign are to be added.

- Browser Tab Icon:

    - A custom favicon helps users to identify the site. It also shows when a user adds the site as a bookmark or favourite.
    - The favicon shows OLDER, AND and WIDER on three lines, as on the merchandise. AND is smaller and in magenta.
    - The site has a multi-size `.ico` file (16, 32 and 48 pixels), a 192 pixel PNG and a 180 pixel Apple touch icon.
    - A copy of the `.ico` file is at the root of the site as `favicon.ico`. Some browsers and crawlers ask for that address directly.

        ![Website custom favicon](assets/images/oaw-icon-192.png)

- Header:

    - The header is a strip at the top of each page. It holds the main navigation.
    - The navigation has five links: Home, About, Live Shows, Archive and Message Board.
    - On phones the links are a little smaller, so that the five links fit on one row at 375 pixels wide.
    - The link to the current page has the attribute `aria-current="page"`. This attribute tells screen readers which page is open.
    - The header as it appeared on desktops in the earlier design:

        ![Website header](assets/images/website-header.webp)

    - The header as it appeared on mobile in the earlier design:

        ![Website mobile menu](assets/images/website-mobile-menu.webp)

    - and with the expanded hamburger menu of the earlier design:

        ![Website mobile menu expanded](assets/images/website-mobile-menu-expanded.webp)

- Footer:

    - The footer is at the bottom of each page. It shows the logotype "Older and Wider".
    - It has links to Instagram, Facebook and the shop at [olderandwider.shop](https://olderandwider.shop).
    - It has a credit link to the author of the website.
    - It has a "Privacy" link to `privacy.html`, and a "Cookie settings" button. The button opens the cookie banner again.
    - The "Cookie settings" button is hidden without JavaScript, because it needs `assets/js/consent.js`.
    - The footer as it appeared in the earlier design:

        ![Website footer](assets/images/website-footer.webp)

- Home (index):

    - The home page looks like the cover of a weekly magazine. It has these sections:
        - Cover: the masthead, an issue line with the episode number and the date, a halftone photo of the hosts, and cover lines. Each cover line links to a section of the page or to the shop.
        - This week: a "Play here" button for the latest episode, and links to Apple Podcasts, Spotify and Acast. The Acast player loads only when the visitor presses the button. A note next to the button tells the visitor that the player stores a language setting and a session item in the browser. The site does not remember this choice, so the button shows on each visit. The script `assets/js/player.js` does this work. Without JavaScript, the button is replaced by a "Listen on Acast" link.
        - Back issues: a bingo ticket. Each number on the ticket links to its own episode on Acast. A "Last called" list shows the four previous episodes.
        - The episode content updates automatically each Friday from the podcast RSS feed. Refer to [Automatic Episode Update](#automatic-episode-update).
        - Tour: "Even Older and Wider", the 2027 live tour. A table shows the eight dates, towns and venues. The "Book tickets" link opens the ticket page. The "See all shows" link opens `live-shows.html`.
        - Letter: "Dear OWLs", a letter from Jenny and Judith, with the award nomination.
    - The home page as it appeared in the earlier design:

        ![Website home page](assets/images/website-index-feature.webp)

- About:

    - The about page gives information about the podcast and the two hosts. It has these sections:
        - What is Older and Wider? This section tells the history of the podcast. It gives the number of downloads (over 7.5 million) and the award nomination.
        - Who is Judith Holder? A biography, with a contact sheet of more photos.
        - Who is Jenny Eclair? A biography, with a contact sheet of more photos.
        - Hear them for yourself: links to the latest episode and to every episode on Acast.
    - The about page as it appeared in the earlier design:

        ![Website about page](assets/images/website-about-feature.webp)

- Live Shows:

    - The page `live-shows.html` lists the live shows of the current tour. It has these sections:
        - Intro: the page title, a short text and the 2027 tour poster. The poster has alt text, and each date on it is also on the page as text.
        - Forthcoming shows: white text on the red of the poster dates panel. Each show gives the date with the day of the week and the year, the town or city, the venue, the tour name and a ticket link. The earliest show is first.
        - Recent shows: the shows of the current tour that are in the past. The latest show is first. Past shows have no ticket link.
    - Each date is in a `time` element with a `datetime` attribute, for example `datetime="2027-04-25"`.
    - Each ticket link names the show, for example "Tickets for Leeds, 25 April". The link opens the ticket page of the venue. The Bristol show is not on sale yet, so its link opens [jennyeclair.com/olderandwider](https://jennyeclair.com/olderandwider).
    - The poster gives the last London show as "SAT 04 JUL". The Leicester Square Theatre website gives Sunday 4 July 2027. The page uses the date from the theatre and tells the visitor about the error on the poster.
    - The script `assets/js/live-shows.js` moves each past show to Recent shows when the page loads. It does these steps:
        1. It gets the date of today in the time zone `Europe/London`. The time zone of the visitor has no effect.
        2. It reads the `datetime` of each forthcoming show.
        3. It moves each show with a date before today to Recent shows, in order with the latest date first.
        4. It removes the ticket link from each show that it moves.
        5. It shows the message of each list that is empty, and hides the empty list.
    - A show stays in Forthcoming shows for all of the day of the show. It moves on the next day.
    - Without JavaScript, each show stays in the section where the HTML has it. A past show can then stay in Forthcoming shows, with its ticket link. No show is lost. To limit this, move the past shows in the HTML each time you edit the page.
    - Refer to [Live Shows Maintenance](#live-shows-maintenance) for the procedures that stay manual.

- Message Board:

    - The hosts call the podcast's Instagram page the "message board". This page links to it, and to the Facebook page.
    - The page shows six recent Instagram posts as short text quotes or summaries, with their dates and links. No content loads from Instagram when the page opens.
    - The button "Show the posts here" loads the full Instagram posts. The note next to the button tells the visitor that Instagram then sets cookies.
    - The script `assets/js/message-board.js` does this work. Without JavaScript, the text and the links still work.
    - The message board page as it appeared in the earlier design:

        ![Website message board page](assets/images/website-message-board-feature.webp)

- Privacy:

    - The privacy page `privacy.html` tells the visitor that the site has no forms and collects no personal data directly.
    - A table shows each third party, what it stores, and when. The third parties are the Acast player, Instagram, Google Analytics and Font Awesome from cdnjs.
    - The page tells the visitor how to change or withdraw consent, with the "Cookie settings" button.
    - It names the controller, Dominic Francis, with a link to his website. It shows no email address.
    - The page has no link in the navigation. The footer of each page links to it.

- Cookie consent and analytics:

    - On the first visit, a banner at the bottom of the window asks about analytics cookies only. The "Accept" and "Reject" buttons have the same size, colour and weight.
    - The script `assets/js/consent.js` makes the banner. It stores the choice in `localStorage`, under the key `oaw-consent`, with the date.
    - The banner does not trap focus. It sits after the footer in the page, and sticks to the bottom of the window.
    - "Reject" deletes the `_ga` and `_ga_*` cookies for the current host and its parent domains.
    - The script `assets/js/analytics.js` loads Google Analytics only when the stored choice is "accepted". It listens for the event `oaw:consentchange` from `consent.js`. Thus "Accept" loads Google Analytics without a reload.
    - Without JavaScript, the banner does not show, and no analytics load.
    - The constant `GA_MEASUREMENT_ID` at the top of `assets/js/analytics.js` holds the GA4 ID `G-KQEX5744PM`. dominicfrancis.co.uk uses the same ID. Filter GA4 reports by the hostname `older-and-wider.dominicfrancis.co.uk` to see this site alone.

- Custom 404:

    - A custom 404 error page shows when a user goes to a page that does not exist.
    - The page uses the humour of the podcast ("Snore Law has been invoked"). It links to the latest episode and to the home page.
    - The page does not redirect. The earlier design redirected to the home page after 30 seconds.
    - The page uses root-relative links, so it works at any address.
    - The 404 page as it appeared in the earlier design:

        ![Website custom 404 error page](assets/images/website-404-feature.webp)

#### Removed Features

The redesign removed these pages and features:

- The mailing list form on the home page, and its completion page `mailing-list-completion.html`.
- The contact page `contact.html`, with its contact form, and its completion page `contact-completion.html`.
- The "Contact" link in the navigation.
- The image carousels on the home page and the about page.
- The Bootstrap framework.

The forms had no backend. They did not send data to the hosts. A mailing list is deferred until the site has run for some time. Issue #30 holds the plan.

#### Future Features

- The addition of a website forum would allow fans of the podcast to interact, discuss the show, and share their life experiences.
- A mailing list, if the hosts want one after the site has run for some time (issue #30).

### Structure

#### User Flow diagram

This diagram shows how the user may interact and navigate through the website; dashed lines indicate optional routes.

![User flow diagram](assets/images/user-flow-diagram.webp)

### Skeleton

#### Wireframes

After I created the wireframes, and was bulding the site, I altered the layout of the header and footer so that the logo was replaced by a centred site title in the header but removed from the footer.

The hamburger menu (shown in the header on smaller mobile devices) was also centred on the screen.

The wireframes presented here show my initial ideas. They show the first design, before the redesign. The redesign removed three of these pages. Their headings below are marked "(page removed)".

##### Mobile

###### Home
![Home (index)](documentation/wireframes/mobile/home.webp)
###### Mailing List Completion (page removed)
![Mailing List Completion](documentation/wireframes/mobile/mailing-list-completion.webp)
###### About
![About](documentation/wireframes/mobile/about.webp)
###### Message Board
![Message Board](documentation/wireframes/mobile/message-board.webp)
###### Contact (page removed)
![Contact](documentation/wireframes/mobile/contact.webp)
###### Contact Completion (page removed)
![Contact Completion](documentation/wireframes/mobile/contact-completion.webp)
###### Custom 404
![Custom 404](documentation/wireframes/mobile/404.webp)

##### Mobile (with expanded menu)

###### Home
![Home (index)](documentation/wireframes/mobile/home-menu.webp)
###### Mailing List Completion (page removed)
![Mailing List Completion](documentation/wireframes/mobile/mailing-list-completion-menu.webp)
###### About
![About](documentation/wireframes/mobile/about-menu.webp)
###### Message Board
![Message Board](documentation/wireframes/mobile/message-board-menu.webp)
###### Contact (page removed)
![Contact](documentation/wireframes/mobile/contact-menu.webp)
###### Contact Completion (page removed)
![Contact Completion](documentation/wireframes/mobile/contact-completion-menu.webp)
###### Custom 404
![Custom 404](documentation/wireframes/mobile/404-menu.webp)

##### Tablet

###### Home
![Home (index)](documentation/wireframes/tablet/home.webp)
###### Mailing List Completion (page removed)
![Mailing List Completion](documentation/wireframes/tablet/mailing-list-completion.webp)
###### About
![About](documentation/wireframes/tablet/about.webp)
###### Message Board
![Message Board](documentation/wireframes/tablet/message-board.webp)
###### Contact (page removed)
![Contact](documentation/wireframes/tablet/contact.webp)
###### Contact Completion (page removed)
![Contact Completion](documentation/wireframes/tablet/contact-completion.webp)
###### Custom 404
![Custom 404](documentation/wireframes/tablet/custom-404.webp)

##### Desktop

###### Home
![Home (index)](documentation/wireframes/desktop/home.webp)
###### Mailing List Completion (page removed)
![Mailing List Completion](documentation/wireframes/desktop/mailing-list-completion.webp)
###### About
![About](documentation/wireframes/desktop/about.webp)
###### Message Board
![Message Board](documentation/wireframes/desktop/message-board.webp)
###### Contact (page removed)
![Contact](documentation/wireframes/desktop/contact.webp)
###### Contact Completion (page removed)
![Contact Completion](documentation/wireframes/desktop/contact-completion.webp)
###### Custom 404
![Custom 404](documentation/wireframes/desktop/custom-404.webp)

### Surface

#### Colours

The colours come from the 2027 tour poster. [DESIGN.md](DESIGN.md) gives the full palette, the rules for each colour, and the contrast figures. The main colours are:

- Pink (#F492BF): the page ground.
- Red (#A60201): the masthead and the display text.
- Magenta (#E8046C): the word "and" in the logotype.

The stylesheet defines each colour as a CSS custom property in `:root`, for example `--pink`.

The earlier design used palette 389 of the [Sarah Renae Clarke Colour Catalogue, Volume 2](https://sarahrenaeclark.com/shop/the-color-catalog-volume-2/), with teal and raspberry. The redesign replaced it.

#### Typography

The fonts come from the 2027 tour poster. The site hosts the font files in `assets/fonts/`. Each page preloads Anton, Barlow 400 and Barlow Condensed 600. This stops the layout shift that occurred when the fonts loaded from Google Fonts:

- [Anton](https://fonts.google.com/specimen/Anton) for the masthead and the display text.
- [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) for labels.
- [Barlow](https://fonts.google.com/specimen/Barlow) for body text.

The earlier design used Marcellus and Pontano Sans. The redesign replaced them.

#### Media

All images used on the site have been taken from the Older and Wider podcast [Instagram](https://www.instagram.com/olderandwiderpodcast) page, the [shop](https://olderandwider.shop), and the 2027 tour poster.

The stylesheet puts a halftone dot screen on the photos, so that they look like print in a magazine.

Each photo has fixed-width variants (for example `_256.webp`, `_480.webp` and `_800.webp`). The HTML `img` `srcset` and `sizes` attributes select the correct variant for the screen. I used [RespImageLint](https://ausi.github.io/respimagelint/) to advise about these variants.

#### Content

All page content was initially written by myself, inspired by the sources listed in the credits, and then polished using Copilot in Microsoft Edge.

## Testing

- Please refer to [TESTING.md](TESTING.md) for details.

## Deployment

### Amazon S3 and CloudFront

The site is stored in an Amazon S3 bucket, and served through Amazon CloudFront, in the `eu-west-2` region. The bucket is `portfolio-dominicfrancis`. It holds more than one site. Each site has its own folder, and this site uses the folder `older-and-wider`. CloudFront reads that folder through an origin path. Thus the address of each page stays the same. Deployment is automatic. Each push to the `main` branch that changes a page, an asset, or the build script publishes the site again. The weekly episode update also publishes the site. Refer to [Automatic Episode Update](#automatic-episode-update).

Three files do this work, and are easier to understand together:

- `build.sh` assembles the site into a `deploy/` directory, and then copies it to the site folder in the bucket. It copies only the pages and directories in its list. Thus an unwanted file in the repository root cannot go live by accident. Git does not track `deploy/`, and the script makes it again on each run.
- `.github/workflows/deploy.yml` runs the command `./build.sh --deploy --yes` on each push to the `main` branch that changes `*.html`, `assets/**`, `build.sh`, or the workflow file. GitHub Actions runs the same script that you run on your own computer. Thus the two cannot become different. Another workflow can also call this workflow (`workflow_call`). The episode update workflow uses this trigger.
- `infra/deploy-role.yaml` is the CloudFormation template for the role that the workflow uses. The role trusts only the `main` branch of this repository. Its permissions apply only to this site's folder, and to the one distribution. The role cannot read or delete the folder of another site. No Amazon Web Services keys are kept in the repository, or in GitHub.

To assemble the site on your own computer, but not deploy it, run the command `./build.sh` in the repository root.

Two details are important before you change any of this:

- The cache headers remove the necessity for a cache invalidation step. The script uploads the assets with a one year `max-age`, and the mark `immutable`. It uploads the pages with `no-cache`. CloudFront obeys these headers. Thus a new deployment becomes visible immediately.
- The script adds a hash to the name of each CSS and JS file in `deploy/`, for example `main.bea7c67fec.css`. It changes the links in each page to match. A changed file gets a new name. Thus returning visitors do not keep an old copy from the one-year cache. The build stops if a page links to a file without a hash.
- The deploy workflow also runs when `sitemap.xml`, `robots.txt` or `favicon.ico` changes.
- The script uploads the pages last, after the assets. Thus a live page cannot refer to an asset that is not yet in the bucket.

To add a new page, you must do two steps. It is not sufficient to make the file in the repository root. You must also add the name of the file to the `PAGES` list in `build.sh`. If you do not, the site will never include that page.

The `PAGES` list contains these files:

- `index.html`
- `about.html`
- `message-board.html`
- `404.html`
- `privacy.html`
- `sitemap.xml`
- `robots.txt`
- `favicon.ico`

The `DIRS` list contains only `assets`. Thus the script does not deploy `design-options/` or `documentation/`. The redesign removed `contact.html`, `contact-completion.html` and `mailing-list-completion.html` from the list.

### Automatic Episode Update

The home page shows the latest episode and the 15 episodes before it. A GitHub Action keeps this content up to date. The hosts do not need to do any work.

The parts that update are these:

- The issue line in the masthead, for example "Issue 374 · 27 November 2026".
- The cover headline and the duration of the latest episode.
- The "This week" number, title, date and duration.
- The bingo ticket. It shows the 15 episodes before the latest episode. The 4 newest of these have a pink dab.
- The ticket serial ("Ticket 374").
- The "Last called" list. It shows the 4 episodes before the latest episode, newest first.

These files do the work:

- `scripts/update_episodes.py` reads the Acast RSS feed. It changes only the text between the episode marker comments in `index.html`, for example `<!-- episodes:masthead:start -->`. The script uses the Python standard library only.
- `.github/workflows/update-episodes.yml` runs the script each Friday at 06:17 and 18:17 UTC. You can also start it manually from the Actions tab in GitHub.
- `scripts/test_update_episodes.py` contains the tests. The workflow runs the tests before the script.

The workflow does these steps:

1. It runs the tests.
2. It runs the script against the live feed.
3. If `index.html` changes, it commits `index.html` and `sitemap.xml` to `main` as "chore: update the home page for episode N". It rebases the commit on `main` before the push, because `main` can move while the job runs.
4. It calls `deploy.yml` to publish the commit.

If `index.html` does not change, the workflow stops after step 2.

A push from the `GITHUB_TOKEN` of a workflow does not start other workflows. Thus step 4 calls `deploy.yml` directly. The called workflow runs on `refs/heads/main`, so the deploy role trusts it.

The script obeys these rules:

- It takes the episode number from the `itunes:episode` field. If that field is missing, it uses the prefix of the title, for example "Ep 374.".
- A title prefix must start with "Ep" or "Episode". A title such as "2027: the tour" does not give a number.
- It puts the episodes in number order. The latest episode is the highest number.
- It skips a second item with the same number, for example a repost of an old episode.
- It removes the number prefix from the title on the page.
- If the newest episode has no number, the script stops. It does not change the page.
- It skips an older item that has no number, for example a "sick note" week.
- If the feed does not load or does not parse, the script stops. It does not change the page.
- If the feed has fewer than 16 numbered episodes, the script stops. It does not change the page.
- It links each bingo number to the page of its episode on Acast.
- It keeps the bingo layout. The 15 numbers go up column by column. Each row has five numbers and four blanks.
- When `index.html` changes, it sets the `lastmod` date of the home page in `sitemap.xml` to the date of the latest episode.

The start time of 06:17 UTC is after the usual release time of an episode. The feed shows a release at about 02:00 to 04:00 UTC each Friday. The run at 18:17 UTC catches an episode that comes out late.

Do not edit the text between the episode markers by hand. The next run replaces it.

To see the change that the script would make, run this command in the repository root:

```bash
python3 scripts/update_episodes.py --check
```

The command shows a diff. It does not change the page. It exits with code 1 if the page would change.

To update the page on your own computer, run this command:

```bash
python3 scripts/update_episodes.py
```

To use a local feed file, add `--feed` and the path of the file.

### Live Shows Maintenance

The script `assets/js/live-shows.js` moves past shows. Other changes to `live-shows.html` are manual. Each show is one `li` element in the list `shows-forthcoming` or the list `shows-recent`. A forthcoming show has this form:

```html
<li class="show">
    <p class="show-date"><time datetime="2027-04-25">Sunday 25 April 2027</time></p>
    <h3 class="show-place">Leeds</h3>
    <p class="show-venue">City Varieties</p>
    <p class="show-tour">Even Older and Wider</p>
    <p class="show-tickets"><a href="https://leedsheritagetheatres.com/whats-on/even-older-and-wider-2027/" rel="external">Tickets for Leeds, 25 April</a></p>
</li>
```

After each change, do these steps:

1. Validate `live-shows.html` with the W3C Markup Validator.
2. Open the page in a browser. Make sure that each show is in the correct section.
3. Change the `lastmod` date of `live-shows.html` in `sitemap.xml`.
4. Push the change to a branch, and merge it to `main` with a pull request.

#### Add a Show

1. Get the date, the town or city, the venue and the ticket address from the venue or from [jennyeclair.com](https://jennyeclair.com/olderandwider).
2. Make sure that the day of the week agrees with the date.
3. Copy one `li` element in the list `shows-forthcoming`.
4. Put the copy in date order. The earliest show is first.
5. Set the `datetime` attribute to the date in the form `YYYY-MM-DD`.
6. Write the date in the `time` element with the day of the week and the year.
7. Change the town or city, the venue and the tour name.
8. Set the `href` of the ticket link to the ticket page of the show.
9. If the show has no ticket page, use `https://jennyeclair.com/olderandwider`.
10. Change the link text to "Tickets for" and the town and date, for example "Tickets for Leeds, 25 April".
11. If the home page shows the tour, add the show to the table in the `tour` section of `index.html`.

A solo tour of Jenny Eclair has more dates than an Older and Wider tour. Do these steps for each date of a solo tour.

#### Correct a Show

1. Find the `li` element of the show.
2. If the date changes, change the `datetime` attribute and the text of the `time` element.
3. Move the `li` element to keep the date order.
4. If the venue changes, change the venue text and the ticket address.
5. Change the link text if the town or the date changes.
6. Make the same change in the `tour` section of `index.html`.

#### Remove a Cancelled Show

1. Find the `li` element of the show.
2. Delete the `li` element.
3. Delete the row of the show from the table in the `tour` section of `index.html`.
4. If the list `shows-forthcoming` is then empty, leave the empty `ol` element in the page. Add the attribute `hidden` to it.
5. Remove the attribute `hidden` from the message `forthcoming-empty`.

Do not move a cancelled show to Recent shows. Recent shows holds only the shows that occurred.

#### Move a Finished Tour to the Archive

Do these steps after the last show of a tour.

1. Copy each show of the tour to the Older and Wider live shows section of `archive.html`.
2. Put the latest show first.
3. Remove the ticket link from each copied show.
4. Check each show against a reliable source, for example a podcast episode after the date. Do not copy a show that did not occur.
5. Delete the shows of the tour from `live-shows.html`.
6. Add the attribute `hidden` to each empty list in `live-shows.html`.
7. Remove the attribute `hidden` from the message of each empty list.
8. Add the shows of the next tour, if one is announced. Refer to [Add a Show](#add-a-show).
9. Change the poster and its alt text in `live-shows.html` for the next tour. Make the `_480` and `_800` width variants of the new poster.
10. Change the `lastmod` dates of `live-shows.html` and `archive.html` in `sitemap.xml`.

### Sitemap and robots.txt

The repository root contains a `sitemap.xml` file and a `robots.txt` file. Both files are in the `PAGES` list. Thus they deploy to the root of the site, with `no-cache`.

- `sitemap.xml` lists the pages for search engines. It lists the home page, `about.html`, `live-shows.html`, `message-board.html` and `privacy.html`. It does not list `404.html`, because that page has a `noindex` tag.
- `robots.txt` lets all crawlers read all pages. It gives the address of the sitemap.

When you add or remove a page, update `sitemap.xml`. Change the `lastmod` date of each page that you change.

After the deploy, submit the sitemap in Google Search Console:

1. Open Google Search Console for `https://older-and-wider.dominicfrancis.co.uk`.
2. Open the Sitemaps page.
3. Enter `sitemap.xml` and select Submit.
4. Make sure that the status shows no errors.

### Forks

To copy the repository to your own GitHub account, so you can make changes without affecting the original version, you can fork it:

- Navigate to the GitHub repository.
- Just above the 'About' section, on the right of the page, click the 'Fork' button.

![Fork deployment](assets/images/fork-deployment.webp)

### Local Clones

To deploy the project on your own computer you can clone it:

- Navigate to the GitHub repository.
- Click the green '<> Code' button above the list of project files.
- From the 'Local' tab, select either HTTPS, SSH, or GitHub CLI as the method of cloning, and copy the associated link.
- Open the terminal or Bash prompt.
- Navigate to the directory where you want to store the cloned copy.
- At the prompt, type `git clone` and add the string copied earlier.
- Press 'Enter' to create the copy.

![Clone deployment](assets/images/local-clone-deployment.webp)

### Gitpod Workspaces

When using Gitpod, you can click the button below to create a workspace from this repository, which also requires that you [install the Gitpod browser extension](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/dvfrancis/older-and-wider)

## Credits and References

All images on this site are taken from the podcast's [Instagram](https://www.instagram.com/olderandwiderpodcast/) page, the Older and Wider shop at [olderandwider.shop](https://olderandwider.shop), or the 2027 tour poster. The colours and fonts of the site also come from the tour poster. Links to live sites are also used for the social media icons, and in the footer. This is done to help promote the podcast, and as a mark of respect for all the work that has gone into it. Once this project has been assessed, my intention is to get in touch with the podcast to let Jenny and Judith know about it.

The following references were used for general advice and help in implementing specific functionality on the website:
- [Duckett, J. (2011) HTML & CSS - Design and Build Websites. Indianapolis: John Wiley & Sons, Inc.](https://htmlandcssbook.com/) - general coding advice.
- [Microsoft Edge Copilot](https://www.microsoft.com/en-us/edge/features/copilot) - coding advice, particularly around CSS rules of ingeritance.
- [How to create a copyright symbol](https://blog.hubspot.com/website/html-code-copyright) - creating the copyright symbol in the footer.
- [How to set a favicon in GitHub Pages]( https://stackoverflow.com/questions/35037482/favicon-with-github-pages) - setting a favicon on GitGub Pages.
- [W3 Schools CSS :visited Selector](https://www.w3schools.com/cssref/sel_visited.php) and 
 [CSS-Tricks :visited](https://css-tricks.com/almanac/selectors/v/visited/) - styling the navigation links after they had been visited.
- [Background on semantic HTML5 elements](https://www.freecodecamp.org/news/semantic-html5-elements/) - ordering semantic HTMl elements.
- [Redirect to custom form completion page](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections?ref=library.linkbot.com) - creating a redirect from the website's custom completion pages (earlier design; the redesign removed these pages and the redirect).
- [How to Implement ARIA Tags for Better Accessibility](https://dev.to/sarveshh/how-to-implement-aria-tags-for-better-accessibility-a-comprehensive-guide-for-web-developers-h3k) - how and where to use ARIA tags.
- [Using Media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries) - creating media queries to control ``body`` padding at different screen sizes.
- [Creating a custom 404 page for your GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site) - implementing a GutHub Pages custom 404 page.
- [How To Change the Color of the Bootstrap 5 Mobile Menu Icon](https://www.youtube.com/watch?v=45QSuJaHEss) - altering the colour of the hamburger menu on mobile devices (earlier design).
- [How to use srcset and sizes for responsive images](https://stackoverflow.com/questions/35099471/how-to-use-srcset-and-sizes-for-responsive-images) - making the website's images responsive.
- [The Only Markdown Cheatsheet You Need](https://github.com/im-luka/markdown-cheatsheet) - creating the README.md and TESTING.md documentation.

References used to gain a general understanding about the podcast, and for creating website content:

- PodcastingToday press release for the 2027 tour (November 2026) - the source of the figure of over 7.5 million downloads.

- [Jenny Eclair's website](https://jennyeclair.com)
- [Jenny Eclair's Wikipedia page](https://en.wikipedia.org/wiki/Jenny_Eclair)
- [Interview in The Guardian with Jenny Eclair](https://www.theguardian.com/stage/2020/jun/28/jenny-eclair-menopause-gave-me-incandescent-rage-it-was-like-a-superpower)
- [Jenny Eclair's Amazon author profile](https://www.amazon.co.uk/stores/author/B001KDFYU2/allbooks)
- [Judith Holder's website](http://www.judithholder.com/)
- [Interview in The Guardian with Judith Holder](https://www.theguardian.com/lifeandstyle/2023/aug/14/a-new-start-after-60-i-came-out-of-my-shell-when-i-retired-now-im-a-podcast-star-at-67)
- [Interview in Readers Digest with Judith Holder](https://www.readersdigest.co.uk/inspire/life/under-the-grandfluence-judith-holder)
- [Judith Holder's Amazon author profile](https://www.amazon.co.uk/stores/author/B001KJ46JG?ingress=0&visitId=2980f5c1-ed6a-45d2-ab5b-16abd95eaa16&ref_=sr_ntt_srch_lnk_1)
- [Wikipedia entry about 'Grumpy Old Women'](https://en.wikipedia.org/wiki/Grumpy_Old_Women)
- [The Older & Wider Facebook](https://www.facebook.com/profile.php?id=61555198800248)
- [Older & Wider Live! Avalon Press Release #1](https://avalonuk.com/2023/03/23/jenny-eclair-and-judith-holder-co-writers-of-internationally-successful-grumpy-old-women-live-stage-shows-bring-their-podcast-series-older-and-wider-to-the-london-stage-this-summer/)
- [Older & Wider Live! Avalon Press Release #2](https://avalonuk.com/2023/03/29/extra-london-date-at-leicester-square-theatre-announced-for-jenny-eclair-and-judith-holders-older-and-wider-live-podcast-show/)
- [Older & Wider Live! Theatre at The Tabard](https://tabard.org.uk/whats-on/olderandwider/)
- [What's On Stage - Older & Wider Live!](https://www.whatsonstage.com/shows/outer-london-theatre/older-and-wider-live_300423/)
- [UKTW - Older & Wider Live!](https://www.uktw.co.uk/archive/Tour/Talk/Older-and-Wider-live/T833145318/)
- [The Lowry - Older & Wider Live!](https://thelowry.com/whats-on/older-and-wider-live-jenny-eclair-and-judith-holder/)
- [See Tickets - Older & Wider Live!](https://www.seetickets.com/tour/older-and-wider-live)

Links to the podcast, on various platforms:

- [Acast](https://shows.acast.com/older-and-wider-podcast)
- [Apple Podcasts](https://podcasts.apple.com/gb/podcast/older-and-wider-podcast/id1446310659)
- [Spotify](https://open.spotify.com/show/3ScVA6cJZpMifpJJDmmodP)
- [Soundcloud](https://soundcloud.com/user-575974822)
    
## Technologies Used

- The website is built with [HTML](https://en.wikipedia.org/wiki/HTML) and [CSS](https://en.wikipedia.org/wiki/CSS). The earlier design also used [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)). The redesign removed it.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) is used in five small scripts. The site works without them.
    - `assets/js/consent.js` shows the cookie banner and stores the choice.
    - `assets/js/analytics.js` loads Google Analytics only after the visitor accepts.
    - `assets/js/player.js` loads the Acast player only when the visitor presses "Play here".
    - `assets/js/message-board.js` loads the Instagram posts only when the visitor asks for them.
- [Google Analytics](https://marketingplatform.google.com/about/analytics/) counts visits, only after the visitor accepts analytics cookies.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) was used for website troubleshooting, and testing (including [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) reports).
- [Google Chrome](https://www.google.co.uk/chrome/) was used for website testing.
- The [Responsive Viewer](https://responsiveviewer.org/) extension was used in all browsers (except Firefox, which does not seem to support it) to create images of the website's pages on a variety of devices.
- The [GoFullPage](https://gofullpage.com/) extension was used in all browsers (except Firefox, which does not seem to support it) to capture full-sized images of the website's pages.
- [Microsoft Edge](https://www.microsoft.com/en-gb/edge/) was used for website testing.
- [Firefox](https://www.mozilla.org/en-GB/firefox/new/) was used for website testing.
- [Opera](https://www.opera.com/) was used for website testing.
- [Safari](https://www.apple.com/uk/safari/) was used for website testing, and mobile screenshots ofan iPhone 12 Pro Max and iPad Pro (12.9-inch) (2nd generation).
- [Figma](https://www.figma.com/) was used to create the wireframes and the user flow diagram.
- [Elfsight](https://elfsight.com/) was used to create the Instagram embed code for message-board.html in the earlier design. The redesign uses Instagram's own `embed.js`, which loads only when the visitor asks.
- [Sarah Renae Clarke's Colour Catalogue V2](https://sarahrenaeclark.com/color-palettes/) was used to determine the colour scheme of the earlier design.
- [Font Joy](https://fontjoy.com/) was used to determine font pairings for the earlier design.
- [Google Fonts](https://fonts.google.com/) is the source of the Anton, Barlow Condensed and Barlow font files. The site hosts the files. All three fonts use the SIL Open Font License. The earlier design used Marcellus and Pontano Sans.
- [Brand Palettes](https://brandpalettes.com) was used to source the correct Instagram and Facebook colours.
- [Microsoft Photos](https://apps.microsoft.com/detail/9wzdncrfjbh4?hl=en-gb&gl=US) was used to edit all images.
- [RespImageLint](https://ausi.github.io/respimagelint/) was used to ensure all website images were fully responsive.
- [To WebP](https://towebp.io/) was used to compress images into webp format.
- [FontAwesome](https://fontawesome.com/) was used for social media icons.
- [GitHub](https://github.com/) was used for version control.
- [Amazon S3](https://aws.amazon.com/s3/) was used to store the website files.
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) was used to serve the website.
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/) was used to create the deployment role.
- [GitHub Actions](https://github.com/features/actions) was used to deploy the website automatically.
- [Gitpod](https://gitpod.io/) was used as an online IDE.
- [Markdown](https://en.wikipedia.org/wiki/Markdown) was used to create the README.md and TESTING.md documentation.

## Acknowledgements

Thanks to my mentor, Juliia Konovalova, my cohort facilitator, Lewis Dillon, and fellow student cohorts, in particular Luke McCall, for their support and advice.

Extra special thanks to Andrew Parton, for always being there.
