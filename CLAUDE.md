# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A static marketing site for the Older and Wider podcast (first a Code Institute project). The site has hand-written HTML, one CSS file and one small script. It has no framework, no package manager and no test suite. Font Awesome loads from a CDN. The four font files are in `assets/fonts/`. The pages do not use Bootstrap.

Source pages live at the repo root: `index.html`, `about.html`, `live-shows.html`, `archive.html`, `message-board.html`, `404.html`, `privacy.html`. The redesign removed `contact.html`, `contact-completion.html` and `mailing-list-completion.html`.

**Design.** `DESIGN.md` holds the design system: colours, fonts, components and rules. `PRODUCT.md` holds the product record. Read both before you change the look or the copy. The show name is "Older and Wider". Do not use an ampersand in new text. `design-options/` holds five earlier design concepts for reference. `build.sh` does not deploy it.

## Commands

```bash
./build.sh                 # assemble deploy/ from source (safe, no AWS calls)
./build.sh --deploy        # build, then sync to S3 (prompts before touching the bucket)
python3 -m http.server 8000  # local preview at http://localhost:8000
python3 scripts/update_episodes.py --check   # diff index.html against the live feed, write nothing
python3 scripts/update_episodes.py           # update the episode sections of index.html
python3 scripts/update_instagram.py --check  # diff the message board posts, write nothing
python3 scripts/update_archive_venues.py --check  # diff the archive venue list, write nothing
python3 scripts/update_archive_venues.py          # rebuild the venue list in archive.html
python3 -m unittest discover -s scripts -v   # tests for the three update scripts
```

`.claude/launch.json` defines the same preview server for the Claude Code preview tool.

There is no linter. The only automated tests cover `scripts/update_episodes.py`, `scripts/update_instagram.py` and `scripts/update_archive_venues.py`. Each scheduled workflow runs only the tests of its own script. Other verification is manual and is recorded in `TESTING.md`: W3C Markup Validator for each page, W3C CSS Validator for the stylesheet, Lighthouse for mobile and desktop, plus a manual pass across Chrome, Edge, Firefox, Opera and Safari. Screenshots of each result go in `documentation/validation/` and are linked from `TESTING.md`.

## Deployment pipeline

Three files work together and should be understood as one unit:

- **`build.sh`** copies an explicit allowlist of pages (`PAGES`) and directories (`DIRS`) into `deploy/`, wiping it first. `deploy/` is gitignored and always regenerated.
- **`.github/workflows/deploy.yml`** runs `./build.sh --deploy --yes` on every push to `main` that touches `*.html`, `assets/**`, `build.sh`, `sitemap.xml`, `robots.txt`, `favicon.ico`, or the workflow itself. CI runs the identical script a human runs locally, so the two cannot drift.
- **`infra/deploy-role.yaml`** is the CloudFormation stack (`older-and-wider-deploy-role`, eu-west-2) for the OIDC role CI assumes. Trust is locked to this repo's `main` branch. Permissions are scoped to this site's folder in the bucket, and to the one distribution. The role cannot read or delete the folder of another site. No stored AWS keys.

**The bucket is shared.** The site is in the folder `older-and-wider` of the bucket `portfolio-dominicfrancis`. The bucket holds the other dominicfrancis.co.uk sites, one folder for each site. The CloudFront distribution (`E1G3DY1FAYHJJJ`) reads the folder through the origin path `/older-and-wider`. Thus the public addresses do not contain the folder name. The live site is https://older-and-wider.dominicfrancis.co.uk.

Four deliberate details in `build.sh` that are easy to break:

- **Every S3 path goes through `DEST`.** `DEST` is `s3://$BUCKET/$PREFIX`. The deploy syncs with `--delete`. A sync that points at the bucket root erases the other sites. Do not write `s3://$BUCKET/` in the script. Do not change `PREFIX` unless you also change the origin path and the `Prefix` parameter of the role stack.
- **Cache-Control does the invalidation work.** Assets sync with `max-age=31536000, immutable`; HTML syncs with `no-cache`. That is why a deploy lands without a CloudFront invalidation. Changing these headers reintroduces the 24h default TTL.
- **CSS and JS file names get a hash.** `build.sh` renames each file in `assets/css/` and `assets/js/` in `deploy/`, for example `main.bea7c67fec.css`. It then changes the links in each page. A changed file gets a new name, so the one-year cache cannot serve an old copy. The source files keep their plain names. Images do not get a hash. Give a replaced image a new file name.
- **HTML syncs last**, after assets, so a live page never references an asset that has not uploaded yet.

Routine deploys should go through CI — push to `main` and let the workflow run. If you do deploy by hand, note that this machine's default AWS profile is a read-only user. `build.sh`'s safety check only reads (`aws s3 ls`), so it passes, and the run then fails partway through the first `aws s3 sync`. A local `--deploy` needs a write-capable profile (`admin` or `poweruser` are configured), e.g. `AWS_PROFILE=admin ./build.sh --deploy`.

**Gotcha: adding a new page is two steps.** Creating `foo.html` at the root is not enough — it must also be added to the `PAGES` array in `build.sh` or it will never reach the bucket. The allowlist is intentional: it stops stray root files silently going live. `PAGES` is now `(index.html about.html live-shows.html archive.html message-board.html 404.html privacy.html sitemap.xml robots.txt favicon.ico)`. A file that is not HTML can go in `PAGES`, because the loop uses `cp`. Add each new page to `sitemap.xml` too. `DIRS` is `(assets)`, so `design-options/` and `documentation/` do not deploy.

## Structure and conventions

**No templating.** Each of the seven pages has its own copy of the header, nav and footer. The footer is byte-identical in `index.html`, `about.html`, `live-shows.html`, `archive.html`, `message-board.html` and `privacy.html`. The footer in `404.html` differs only in its root-relative paths. The footer has a "Privacy" link and a "Cookie settings" button (`data-consent-open`, `hidden` until `consent.js` runs). The nav has five links, in this order: Home, About, Message Board, Shows and Archive. The "Shows" link opens `live-shows.html`. On phones the links are smaller (rules in the live shows block of `main.css`), so that the strip fits on one row at 375px. The privacy page has no nav item. The link to the current page carries `aria-current="page"`. `404.html` uses root-relative paths (`/index.html`, `/assets/...`), so it works at any missing address. A nav or footer change means you must edit all seven files by hand.

**External links open in a new tab.** Each `<a>` with an `http://` or `https://` address has `rel="external noopener" target="_blank" aria-describedby="new-tab"`. Keep any other `rel` values. The target of `aria-describedby` is `<span id="new-tab" hidden>Opens in a new tab</span>`, the last child of each footer. Internal links and `mailto:` links do not get these attributes. The link templates in `scripts/update_episodes.py` and `scripts/update_instagram.py` write the same attributes. If you change a template, keep the attributes, then update the fixtures.

**Episode sections are generated.** `index.html` has marker comments such as `<!-- episodes:masthead:start -->` and `<!-- episodes:masthead:end -->`. `scripts/update_episodes.py` rewrites the text between each pair from the Acast RSS feed. Do not edit the text between the markers by hand. The next run replaces it. To change the markup of a section, change the template in the script, then update `scripts/fixtures/index.html` and run the tests. `.github/workflows/update-episodes.yml` runs the script each Friday, commits a change to `main` and calls `deploy.yml` through `workflow_call`. The tests use `scripts/fixtures/index.html`, a copy of the page at episode 374. `scripts/` does not deploy.

**The archive venue list is generated.** The "Venues" section of `archive.html` has the markers `<!-- venues:list:start -->` and `<!-- venues:list:end -->`. `scripts/update_archive_venues.py` reads every show row of the archive and writes a closed `details` list of venues with show counts between them. Do not edit that text by hand. After a change to any show table, run the script. Merge names of one venue through `VENUE_ALIASES` and `TOWN_ALIASES` in the script. The archive tables keep the names as the sources give them. No workflow runs this script. The test `test_live_list_is_up_to_date` fails when the list is out of date.

**Message board posts are generated.** `message-board.html` has the markers `<!-- instagram:posts:start -->` and `<!-- instagram:posts:end -->` around the posts list. `scripts/update_instagram.py` rewrites the text between them. Do not edit that text by hand. The script has two modes. List mode is active now: without the secrets `IG_ACCESS_TOKEN` and `IG_USER_ID`, it builds the posts from `scripts/instagram-posts.txt` (one line per post: `date | URL | text`, optional `| photo set`) in the embed markup that `message-board.js` loads. API mode starts when both secrets exist: it gets the 10 latest posts from the Instagram API with Instagram Login, saves WebP variants in `assets/images/instagram/` (names carry the post ID and a photo hash) and writes static cards (`.board-post`, CSS block `/* Instagram feed */` at the end of `main.css`). `.github/workflows/update-instagram.yml` runs every 6 hours and on a push to `main` that changes the post list, commits a change and calls `deploy.yml` through `workflow_call`. Its `refresh` job refreshes the token weekly with `GH_SECRETS_PAT`. After the first API run, a person must remove `message-board.js`, the click-to-load button and the Instagram row in `privacy.html`; the README section "Tasks After the First API Run" lists the steps. The tests use `scripts/fixtures/instagram/`.

**No page redirects.** No page has a `<meta http-equiv="refresh">`. The earlier `404.html` and the two completion pages redirected after 30 seconds. The redesign removed this behaviour.

**Responsive images.** Every photo has pre-generated fixed-width variants next to the original (for example `home-cover-merch_256.webp`, `_480.webp`, `_800.webp`, `_960.webp`). Each `img` uses `srcset` with a `sizes` expression that matches its layout slot. If you add an image, also make its width variants.

**No forms.** The redesign removed the contact form and the mailing-list form. A mailing list is deferred (issue #30, closed as not planned). Raise it with the hosts only after the site has run for some time. Do not add a server or server-side handling without a discussion first.

**CSS** is one stylesheet, `assets/css/main.css` (about 2,000 lines). `styles.css` was deleted. `:root` defines custom properties for the colours, fonts, gutter and shadows. Use these properties for colour. The rules use literal `#000` and `#fff` only in mask and halftone gradients. The main colours are pink `--pink` `#F492BF`, red `--red` `#A60201` and magenta `--magenta` `#E8046C`. The fonts are Anton, Barlow Condensed and Barlow. The breakpoints are `48rem` and `64rem`. The file also has `prefers-reduced-motion` and `prefers-contrast` blocks. The masthead uses a container query unit (`cqi`).

**JavaScript.** Every page works without JavaScript. Do not add inline scripts or inline styles (issue #24). All scripts load with `defer`. The site has six scripts:

- `assets/js/consent.js` runs on every page. It shows the cookie banner on the first visit. The banner asks about analytics cookies only. The script stores the choice in `localStorage` under `oaw-consent`, as `{choice, date}`. It sends the event `oaw:consentchange` and exposes `window.oawConsent`. "Reject" deletes the `_ga` and `_ga_*` cookies.
- `assets/js/analytics.js` runs on every page, after `consent.js`. It loads Google Analytics only when the choice is "accepted". `GA_MEASUREMENT_ID` is `G-KQEX5744PM`, the same ID as dominicfrancis.co.uk. Filter GA4 reports by hostname to see this site alone.
- `assets/js/player.js` runs on `index.html` only. It inserts the Acast iframe after the visitor presses "Play here". It does not remember the choice. Without JavaScript, the page shows a "Listen on Acast" link.
- `assets/js/message-board.js` runs on `message-board.html` only. It adds Instagram's `embed.js` after the visitor presses "Show the posts here", because `embed.js` sets cookies.
- `assets/js/board-date.js` runs on `message-board.html` only. It puts the date of today in `Europe/London` in the issue line under the title. Without JavaScript, the issue line shows "Message board" only.
- `archive.html` has no script of its own. Its long lists of dates are in `details` elements, so the page works without JavaScript.
- `assets/js/live-shows.js` runs on `live-shows.html` only. It gets today's date in `Europe/London` and moves each forthcoming show with an earlier `time[datetime]` to Recent shows (latest first). It removes the ticket link of each moved show, and shows the message of each empty list. Without JavaScript, every show stays where the HTML has it.

## Documentation is part of the deliverable

`README.md` (~27k) and `TESTING.md` (~47k) are assessment documents with maintained indexes of anchor links, not incidental notes. Most recent commits are `docs:` changes to them. If you change a feature, the corresponding section — and often a screenshot in `documentation/` — needs updating too. `documentation/` is assessment material and is deliberately excluded from `deploy/`.

The Deployment section of the README describes this pipeline. If you change `build.sh`, the workflow, or `infra/deploy-role.yaml`, update that section too.

## Not project code

`.vscode/` (`arctictern.py`, `init_tasks.sh`, `heroku_config.sh`, `upgrades.json`) and `.gitpod.yml` / `.gitpod.dockerfile` are Code Institute template scaffolding for their Gitpod workspaces. They are unrelated to the site and generally should not be edited.

## Git

Conventional commit prefixes are used throughout: `docs:`, `refactor:`, `style:`, `chore:`, `feat:`. Work happens on a branch and merges to `main` via pull request — a push to `main` deploys to production.
