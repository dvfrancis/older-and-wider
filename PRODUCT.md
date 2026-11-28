# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

The site has two audiences.

- **Existing listeners (the OWLs).** Most are women in middle age and older. They know Jenny Eclair and Judith Holder well. They come to find episodes, live shows, the shop, and ways to stay in touch.
- **New listeners.** These people know the names but have not heard the podcast yet. They decide fast whether the show is for them.

Many visitors use a phone. Some visitors have weaker eyesight or less confidence with technology.

## Product Purpose

The site is the home of the Older and Wider podcast on the web. It is a real podcast site. It is no longer a Code Institute assessment.

The visitor actions, in order of priority:

1. Listen to an episode.
2. Book a ticket for a live show.
3. Visit the shop and the social pages.

Success means that a visitor plays an episode or books a ticket with little effort.

## Positioning

Two well-known women talk honestly, and with humour, about life after 50. The site must sound and look like the two hosts. It must not look like a general podcast directory.

## Operating Context

- The podcast is on Acast, Apple Podcasts and Spotify. The home page embeds the Acast player.
- Live shows sell through jennyeclair.com/olderandwider and See Tickets. The "Even Older and Wider" tour runs from April to July 2027. Tickets go on sale on 27 November 2026.
- The shop is at olderandwider.shop.
- The hosts do not like technology. They call boring technical detail "Snore Law". The site must need no work from them.
- The site may move to olderandwider.com if the hosts agree. They have not agreed yet.

## Capabilities and Constraints

- Static site: hand-written HTML and one CSS file. No build tools and no framework.
- Small JavaScript files are approved: one for the message board (Instagram click-to-load), one for the home page player (Acast click-to-load), one for cookie consent, one for analytics, and one for the live shows page (issue #29). The site must work without them. No inline scripts and no inline styles (issue #24).
- The site has no forms. The contact page and the mailing-list form were removed. Do not add server-side handling without a discussion first.
- Deploy: `build.sh` copies an allowlist of pages to a shared S3 bucket. A push to `main` deploys to production.
- Keep `README.md`. Update it to show the new design. Do not delete it.
- Undecided: the future of `TESTING.md` and of the assessment screenshots in `documentation/`.
- Deferred: a mailing list. The hosts use Gmail, and no person is available to send emails. Ask the hosts again after the site has run for some time. Issue #30 holds the plan.
- To do: a sitemap (issue #19) and a robots.txt (issue #20).
- Analytics and cookie consent (issues #21 and #22): done, except the real Google Analytics ID. Google Analytics loads only after the visitor accepts.

## Brand Commitments

- Name: "Older and Wider", with the word "and" spelled out. Do not use an ampersand. The cover art and the tour poster use this form. The 2027 tour name is "Even Older and Wider".
- In display lettering, set the word "AND" in a different pink from the page ground, as on the tour flyer.
- Voice: warm, frank, self-mocking and funny. Plain words. No jargon.
- The user made the colours and fonts of the 2027 tour poster binding. Issue #16 records them, with contrast figures.

## Evidence on Hand

- Photos of the hosts and the carousel images, with width variants, in `assets/images/`.
- The tour poster and the merchandise photo, in a comment on issue #16.
- 912 dated shows from 2006 to 2027, in issue #29 and its comments.
- The podcast RSS feed (383 episodes) on Acast.
- Links to Instagram, Facebook, Spotify, Apple Podcasts and the shop.

Absences. Do not invent these:

- Testimonials or listener quotes.
- Listener numbers, download figures, or awards other than the one below.
- Permission from the hosts to use their photos and artwork. The site uses them without permission at present.

Confirmed by the owner: the podcast was nominated for the British Podcast Awards, Listeners' Choice 2022. Use this wording only.

Confirmed by the owner: the podcast has had over 7.5 million downloads, across 374 episodes. The source is the press release for the 2027 tour (PodcastingToday, November 2026). Do not use a higher figure without a new source.

The message board quotes the opening words of six Instagram posts, with their dates. The source is each post on @olderandwiderpodcast, read on 27 November 2026. The first post is a video, so the page gives a summary of it, not a quote. Replace these six posts when they are out of date.

## Product Principles

1. Listening comes first. A visitor can play an episode from the home page.
2. Live shows are easy to find and book, and past shows stay on record.
3. The hosts' voice leads. The site sounds like them, not like a company.
4. Easy to read for older eyes and for people who are unsure with technology.
5. No work for the hosts. Content that changes, such as show dates, updates itself where possible.

## Accessibility & Inclusion

- WCAG 2.1 AA as a minimum.
- Body text at a large, comfortable size, with strong contrast.
- Large touch targets for the phone.
- The site works without JavaScript.
- Respect `prefers-reduced-motion`.
