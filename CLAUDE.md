# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A static marketing site for the Older & Wider podcast (a Code Institute project). Hand-written HTML and one CSS file — no framework, no package manager, no JavaScript of its own, no test suite. Bootstrap 5.3.3, Font Awesome, and Google Fonts all load from CDNs.

Source pages live at the repo root: `index.html`, `about.html`, `contact.html`, `contact-completion.html`, `mailing-list-completion.html`, `message-board.html`, `404.html`.

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
- **`infra/deploy-role.yaml`** is the CloudFormation stack (`older-and-wider-deploy-role`, eu-west-2) for the OIDC role CI assumes. Trust is locked to this repo's `main` branch; permissions are scoped to the one bucket and one distribution. No stored AWS keys.

Two deliberate details in `build.sh` that are easy to break:

- **Cache-Control does the invalidation work.** Assets sync with `max-age=31536000, immutable`; HTML syncs with `no-cache`. That is why a deploy lands without a CloudFront invalidation. Changing these headers reintroduces the 24h default TTL.
- **HTML syncs last**, after assets, so a live page never references an asset that has not uploaded yet.

Routine deploys should go through CI — push to `main` and let the workflow run. If you do deploy by hand, note that this machine's default AWS profile is a read-only user. `build.sh`'s safety check only reads (`aws s3 ls`), so it passes, and the run then fails partway through the first `aws s3 sync`. A local `--deploy` needs a write-capable profile (`admin` or `poweruser` are configured), e.g. `AWS_PROFILE=admin ./build.sh --deploy`.

**Gotcha: adding a new page is two steps.** Creating `foo.html` at the root is not enough — it must also be added to the `PAGES` array in `build.sh` or it will never reach the bucket. The allowlist is intentional: it stops stray root files silently going live.

## Structure and conventions

**No templating.** The header, nav and footer are duplicated in every page — the footer is byte-identical across all seven, and the nav differs only in which link carries `class="nav-link selected"` and `aria-current="page"`. A nav or footer change means editing all seven files by hand.

**The three dead-end pages self-redirect.** `contact-completion.html`, `mailing-list-completion.html` and `404.html` each carry `<meta http-equiv="refresh" content="30; url=index.html">`. This is intentional site design; `TESTING.md` notes it as the known cause of their lower Lighthouse accessibility scores.

**Responsive images.** Every photo has pre-generated fixed-width variants alongside the original (`home-page-carousel-1_256.webp`, `_800.webp`, `_1190.webp`, …) wired up via `srcset` with a `sizes` expression. Two `sizes` recipes are in use — one for the index carousel, one for the about-page cards. Adding an image means generating its width variants too, not just dropping in a single file.

**Forms have no backend.** The contact and mailing-list forms are `method="GET"` pointing at a static `*-completion.html` page. Do not assume a server or add server-side handling without discussing it first.

**CSS** is a single 373-line `assets/css/styles.css`: a small reset, element defaults, then colour utility classes (`.teal` `#007696`, `.raspberry` `#a30041`), then six `@media` blocks matching Bootstrap's breakpoints. Colours are literal hex values, not custom properties.

## Documentation is part of the deliverable

`README.md` (~27k) and `TESTING.md` (~47k) are assessment documents with maintained indexes of anchor links, not incidental notes. Most recent commits are `docs:` changes to them. If you change a feature, the corresponding section — and often a screenshot in `documentation/` — needs updating too. `documentation/` is assessment material and is deliberately excluded from `deploy/`.

Note that README's "Site Link" and Deployment sections still describe the GitHub Pages setup, which predates the S3/CloudFront pipeline now in `.github/workflows/`.

## Not project code

`.vscode/` (`arctictern.py`, `init_tasks.sh`, `heroku_config.sh`, `upgrades.json`) and `.gitpod.yml` / `.gitpod.dockerfile` are Code Institute template scaffolding for their Gitpod workspaces. They are unrelated to the site and generally should not be edited.

## Git

Conventional commit prefixes are used throughout: `docs:`, `refactor:`, `style:`, `chore:`, `feat:`. Work happens on a branch and merges to `main` via pull request — a push to `main` deploys to production.
