# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A static marketing site for the Older and Wider podcast (first a Code Institute project). The site has hand-written HTML, one CSS file and one small script. It has no framework, no package manager and no test suite. Font Awesome and Google Fonts load from CDNs. The pages do not use Bootstrap.

Source pages live at the repo root: `index.html`, `about.html`, `message-board.html`, `404.html`. The redesign removed `contact.html`, `contact-completion.html` and `mailing-list-completion.html`.

**Design.** `DESIGN.md` holds the design system: colours, fonts, components and rules. `PRODUCT.md` holds the product record. Read both before you change the look or the copy. The show name is "Older and Wider". Do not use an ampersand in new text. `design-options/` holds five earlier design concepts for reference. `build.sh` does not deploy it.

## Commands

```bash
./build.sh                 # assemble deploy/ from source (safe, no AWS calls)
./build.sh --deploy        # build, then sync to S3 (prompts before touching the bucket)
python3 -m http.server 8000  # local preview at http://localhost:8000
```

`.claude/launch.json` defines the same preview server for the Claude Code preview tool.

There is no linter and no automated tests. Verification is manual and is recorded in `TESTING.md`: W3C Markup Validator for each page, W3C CSS Validator for the stylesheet, Lighthouse for mobile and desktop, plus a manual pass across Chrome, Edge, Firefox, Opera and Safari. Screenshots of each result go in `documentation/validation/` and are linked from `TESTING.md`.

## Deployment pipeline

Three files work together and should be understood as one unit:

- **`build.sh`** copies an explicit allowlist of pages (`PAGES`) and directories (`DIRS`) into `deploy/`, wiping it first. `deploy/` is gitignored and always regenerated.
- **`.github/workflows/deploy.yml`** runs `./build.sh --deploy --yes` on every push to `main` that touches `*.html`, `assets/**`, `build.sh`, or the workflow itself. CI runs the identical script a human runs locally, so the two cannot drift.
- **`infra/deploy-role.yaml`** is the CloudFormation stack (`older-and-wider-deploy-role`, eu-west-2) for the OIDC role CI assumes. Trust is locked to this repo's `main` branch. Permissions are scoped to this site's folder in the bucket, and to the one distribution. The role cannot read or delete the folder of another site. No stored AWS keys.

**The bucket is shared.** The site is in the folder `older-and-wider` of the bucket `portfolio-dominicfrancis`. The bucket holds the other dominicfrancis.co.uk sites, one folder for each site. The CloudFront distribution (`E1G3DY1FAYHJJJ`) reads the folder through the origin path `/older-and-wider`. Thus the public addresses do not contain the folder name. The live site is https://older-and-wider.dominicfrancis.co.uk.

Three deliberate details in `build.sh` that are easy to break:

- **Every S3 path goes through `DEST`.** `DEST` is `s3://$BUCKET/$PREFIX`. The deploy syncs with `--delete`. A sync that points at the bucket root erases the other sites. Do not write `s3://$BUCKET/` in the script. Do not change `PREFIX` unless you also change the origin path and the `Prefix` parameter of the role stack.
- **Cache-Control does the invalidation work.** Assets sync with `max-age=31536000, immutable`; HTML syncs with `no-cache`. That is why a deploy lands without a CloudFront invalidation. Changing these headers reintroduces the 24h default TTL.
- **HTML syncs last**, after assets, so a live page never references an asset that has not uploaded yet.

Routine deploys should go through CI — push to `main` and let the workflow run. If you do deploy by hand, note that this machine's default AWS profile is a read-only user. `build.sh`'s safety check only reads (`aws s3 ls`), so it passes, and the run then fails partway through the first `aws s3 sync`. A local `--deploy` needs a write-capable profile (`admin` or `poweruser` are configured), e.g. `AWS_PROFILE=admin ./build.sh --deploy`.

**Gotcha: adding a new page is two steps.** Creating `foo.html` at the root is not enough — it must also be added to the `PAGES` array in `build.sh` or it will never reach the bucket. The allowlist is intentional: it stops stray root files silently going live. `PAGES` is now `(index.html about.html message-board.html 404.html)`. `DIRS` is `(assets)`, so `design-options/` and `documentation/` do not deploy.

## Structure and conventions

**No templating.** Each of the four pages has its own copy of the header, nav and footer. The footer is byte-identical in all four pages. The nav has three links: Home, About and Message Board. The link to the current page carries `aria-current="page"`. `404.html` uses root-relative paths (`/index.html`, `/assets/...`), so it works at any missing address. A nav or footer change means you must edit all four files by hand.

**No page redirects.** No page has a `<meta http-equiv="refresh">`. The earlier `404.html` and the two completion pages redirected after 30 seconds. The redesign removed this behaviour.

**Responsive images.** Every photo has pre-generated fixed-width variants next to the original (for example `home-cover-merch_256.webp`, `_480.webp`, `_800.webp`, `_960.webp`). Each `img` uses `srcset` with a `sizes` expression that matches its layout slot. If you add an image, also make its width variants.

**No forms.** The redesign removed the contact form and the mailing-list form. Issue #30 covers a future mailing-list backend. Do not add a server or server-side handling without a discussion first.

**CSS** is one stylesheet, `assets/css/main.css` (about 2,000 lines). `styles.css` was deleted. `:root` defines custom properties for the colours, fonts, gutter and shadows. Use these properties for colour. The rules use literal `#000` and `#fff` only in mask and halftone gradients. The main colours are pink `--pink` `#F492BF`, red `--red` `#A60201` and magenta `--magenta` `#E8046C`. The fonts are Anton, Barlow Condensed and Barlow. The breakpoints are `48rem` and `64rem`. The file also has `prefers-reduced-motion` and `prefers-contrast` blocks. The masthead uses a container query unit (`cqi`).

**JavaScript.** `assets/js/message-board.js` is the only script. Only `message-board.html` loads it. It adds Instagram's `embed.js` after the visitor presses "Show the posts here", because `embed.js` sets cookies. Every page works without JavaScript. Do not add inline scripts or inline styles (issue #24).

## Documentation is part of the deliverable

`README.md` (~27k) and `TESTING.md` (~47k) are assessment documents with maintained indexes of anchor links, not incidental notes. Most recent commits are `docs:` changes to them. If you change a feature, the corresponding section — and often a screenshot in `documentation/` — needs updating too. `documentation/` is assessment material and is deliberately excluded from `deploy/`.

The Deployment section of the README describes this pipeline. If you change `build.sh`, the workflow, or `infra/deploy-role.yaml`, update that section too.

## Not project code

`.vscode/` (`arctictern.py`, `init_tasks.sh`, `heroku_config.sh`, `upgrades.json`) and `.gitpod.yml` / `.gitpod.dockerfile` are Code Institute template scaffolding for their Gitpod workspaces. They are unrelated to the site and generally should not be edited.

## Git

Conventional commit prefixes are used throughout: `docs:`, `refactor:`, `style:`, `chore:`, `feat:`. Work happens on a branch and merges to `main` via pull request — a push to `main` deploys to production.
