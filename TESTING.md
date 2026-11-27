[Return to Older and Wider README.md](https://github.com/dvfrancis/older-and-wider/blob/main/README.md)

# Testing

## Index

1. [Test Status After the Redesign](#test-status-after-the-redesign)
2. [Code Validation](#code-validation)
    1. [HTML](#html)
        1. [HTML Results for the New Design](#html-results-for-the-new-design)
        2. [Earlier HTML Results](#earlier-html-results)
    2. [CSS](#css)
        1. [main.css](#maincss)
        2. [Validator Limits](#validator-limits)
        3. [Earlier CSS Results](#earlier-css-results)
    3. [Sitemap and robots.txt](#sitemap-and-robotstxt)
3. [Manual Validation](#manual-validation)
    1. [index.html](#indexhtml)
    2. [mailing-list-completion.html (page removed)](#mailing-list-completionhtml-page-removed-1)
    3. [about.html](#abouthtml)
    4. [message-board.html](#message-boardhtml)
    5. [contact.html (page removed)](#contacthtml-page-removed-1)
    6. [contact-completion.html (page removed)](#contact-completionhtml-page-removed-1)
    7. [404.html](#404html)
    8. [privacy.html](#privacyhtml)
    9. [Cookie Consent and Click-to-Load](#cookie-consent-and-click-to-load)
4. [User Story Validation](#user-story-validation)
    1. [First Time Visitor Goals](#first-time-visitor-goals)
    2. [Returning Visitor Goals](#returning-visitor-goals)
    3. [Frequent Visitor Goals](#frequent-visitor-goals)
5. [Browser Compatibility](#browser-compatibility)
    1. [Google Chrome](#google-chrome)
    2. [Microsoft Edge](#microsoft-edge)
    3. [Firefox](#firefox)
    4. [Opera](#opera)
    5. [Safari (on an iPad)](#safari-on-an-ipad)
    6. [Safari (on an iPhone)](#safari-on-an-iphone)
6. [Accessibility](#accessibility)
    1. [index.html](#indexhtml-1)
    2. [mailing-list-completion.html (page removed)](#mailing-list-completionhtml-page-removed-2)
    3. [about.html](#abouthtml-1)
    4. [message-board.html](#message-boardhtml-1)
    5. [contact.html (page removed)](#contacthtml-page-removed-2)
    6. [contact-completion.html (page removed)](#contact-completionhtml-page-removed-2)
    7. [404.html](#404html-1)
7. [Responsiveness](#responsiveness)
    1. [index.html](#indexhtml-2)
    2. [mailing-list-completion.html (page removed)](#mailing-list-completionhtml-page-removed-3)
    3. [about.html](#abouthtml-2)
    4. [message-board.html](#message-boardhtml-2)
    5. [contact.html (page removed)](#contacthtml-page-removed-3)
    6. [contact-completion.html (page removed)](#contact-completionhtml-page-removed-3)
    7. [404.html](#404html-2)
8. [Performance](#performance)
    1. [index.html](#indexhtml-3)
    2. [mailing-list-completion.html (page removed)](#mailing-list-completionhtml-page-removed-4)
    3. [about.html](#abouthtml-3)
    4. [message-board.html](#message-boardhtml-3)
    5. [contact.html (page removed)](#contacthtml-page-removed-4)
    6. [contact-completion.html (page removed)](#contact-completionhtml-page-removed-4)
    7. [404.html](#404html-3)
9. [Bugs](#bugs)
10. [Unfixed Bugs](#unfixed-bugs)

## Test Status After the Redesign

The site had a full redesign in November 2026. The redesign made these changes:

- The site now has five pages: `index.html`, `about.html`, `message-board.html`, `404.html` and `privacy.html`.
- The redesign removed `contact.html`, `contact-completion.html` and `mailing-list-completion.html`.
- One stylesheet, `assets/css/main.css`, replaced `styles.css` and Bootstrap.
- Four small scripts:
    - `assets/js/consent.js` shows the cookie banner.
    - `assets/js/analytics.js` loads Google Analytics after consent.
    - `assets/js/player.js` loads the Acast player when the visitor asks.
    - `assets/js/message-board.js` loads the Instagram posts when the visitor asks.
- No page has an automatic redirect.

The status of each test is:

| TEST | STATUS |
| --- | --- |
| HTML validation | Done on the new design, 27 November 2026 |
| CSS validation | Done on the new design, 27 November 2026 |
| Manual validation | Earlier design only. To be re-run on the new design. |
| User story validation | Earlier design only. To be re-run on the new design. |
| Browser compatibility | Earlier design only. To be re-run on the new design. |
| Accessibility (WAVE) | Earlier design only. To be re-run on the new design. |
| Responsiveness | Earlier design only. To be re-run on the new design. |
| Performance (Lighthouse) | Earlier design only. To be re-run on the new design. |

**Lighthouse and browser tests: to be re-run on the new design.** This document does not give scores for the new design yet. The screenshots in the sections after Code Validation show the earlier design.

This document keeps the results for the removed pages for the record. Each heading for a removed page has the label "(page removed)".

## Code Validation

### HTML

#### HTML Results for the New Design

The [W3C Nu HTML Checker](https://validator.w3.org/nu/) checked the source file of each page on 27 November 2026. The checker version was 26.11.27.

| PAGE | ERRORS | WARNINGS | RESULT |
| --- | --- | --- | --- |
| index.html | 0 | 0 | PASS |
| about.html | 0 | 0 | PASS |
| message-board.html | 0 | 0 | PASS |
| 404.html | 0 | 0 | PASS |
| privacy.html | 0 | 0 | PASS |

To repeat the test, run this command in the repository root for each page:

```bash
curl -s -H 'Content-Type: text/html; charset=utf-8' --data-binary @index.html 'https://validator.w3.org/nu/?out=gnu'
```

An empty output means that the checker found no errors and no warnings. Screenshots of the new results are to be added.

#### Earlier HTML Results

These results are for the earlier design. The [W3C Markup Validation Service](https://validator.w3.org) made them.

##### index.html (earlier design)

![HTML validation of index.html](documentation/validation/html-index.webp)

##### mailing-list-completion.html (page removed)

![HTML validation of mailing-list-completion.html](documentation/validation/html-mailing-list-completion.webp)

##### about.html (earlier design)

![HTML validation of about.html](documentation/validation/html-about.webp)

##### message-board.html (earlier design)

![HTML validation of message-board.html](documentation/validation/html-message-board.webp)

##### contact.html (page removed)

![HTML validation of contact.html](documentation/validation/html-contact.webp)

##### contact-completion.html (page removed)

![HTML validation of contact-completion.html](documentation/validation/html-contact-completion.webp)

##### 404.html (earlier design)

![HTML validation of 404.html](documentation/validation/html-404.webp)

### CSS

#### main.css

The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator) checked `assets/css/main.css` on 27 November 2026. The profile was "CSS level 3 + SVG", with all warnings shown.

| FILE | ERRORS | WARNINGS |
| --- | --- | --- |
| main.css | 3 | 63 |

The 3 errors are limits of the validator. They are not errors in the CSS. The section [Validator Limits](#validator-limits) gives the reason for each error.

The 63 warnings are:

- 60 warnings that the validator does not check CSS custom properties (variables). This is a limit of the validator.
- 3 warnings that `-webkit-mask` (two times) and `-webkit-mask-composite` are vendor extensions. The stylesheet uses them as a fallback for older WebKit browsers. The standard `mask` properties follow them.

To repeat the test, run this command in the repository root:

```bash
curl -s -F "file=@assets/css/main.css;type=text/css" -F output=text -F profile=css3svg -F warning=1 'https://jigsaw.w3.org/css-validator/validator'
```

Screenshots of the new results are to be added.

#### Validator Limits

The validator does not know three CSS features that `main.css` uses. Current versions of Chrome, Edge, Firefox and Safari support all three features.

| LINE | SELECTOR | VALIDATOR MESSAGE | REASON |
| --- | --- | --- | --- |
| 147 | `.cover-inner` | Property "container-type" does not exist | `container-type` comes from the CSS container queries specification. The validator does not know this property. |
| 153 | `.masthead` | Value Error: font-size. Parse Error | The value is `calc(100cqi / 6.45)`. `cqi` is a container query unit. The validator does not know this unit, so it cannot read the `calc()`. |
| 986 | `.cover-photo` | Too many values or values are not recognized | The `mask` property has two `linear-gradient()` layers. The CSS Masking specification permits a comma-separated list of mask layers. The validator does not accept the list. |

#### Earlier CSS Results

These results are for the earlier design. They check `styles.css` and Bootstrap. The redesign deleted `styles.css` and removed Bootstrap. There were no warnings for the local CSS file, but warnings were generated for Bootstrap's CSS file, over which I had no control:

![Bootstrap CSS errors](documentation/validation/css-bootstrap-warnings.webp)

##### index.html (earlier CSS)

![CSS validation of index.html](documentation/validation/css-index.webp)

##### mailing-list-completion.html (page removed, earlier CSS)

![CSS validation of mailing-list-completion.html](documentation/validation/css-mailing-list-completion.webp)

##### about.html (earlier CSS)

![CSS validation of about.html](documentation/validation/css-about.webp)

##### message-board.html (earlier CSS)

![CSS validation of message-board.html](documentation/validation/css-message-board.webp)

##### contact.html (page removed, earlier CSS)

![CSS validation of contact.html](documentation/validation/css-contact.webp)

##### contact-completion.html (page removed, earlier CSS)

![CSS validation of contact-completion.html](documentation/validation/css-contact-completion.webp)

##### 404.html (earlier CSS)

![CSS validation of 404.html](documentation/validation/css-404.webp)

### Sitemap and robots.txt

These checks apply to `sitemap.xml` and `robots.txt` in the repository root.

| CHECK | RESULT |
| --- | --- |
| `sitemap.xml` is well-formed XML | Pass |
| `sitemap.xml` lists the home page, `about.html`, `message-board.html` and `privacy.html` | Pass |
| `sitemap.xml` does not list `404.html` | Pass |
| `robots.txt` contains the `Sitemap` line with the full address | Pass |
| `./build.sh` copies both files into `deploy/` | Pass |
| The live `sitemap.xml` loads as XML | To be tested after the deploy |
| The live `robots.txt` returns 200 as `text/plain` | To be tested after the deploy |
| Google Search Console reads the sitemap with no errors | To be tested after the deploy |

To repeat the local checks, run these commands in the repository root:

```bash
python3 -c "import xml.dom.minidom; xml.dom.minidom.parse('sitemap.xml')"
./build.sh
ls deploy/sitemap.xml deploy/robots.txt
```

The first command shows no output if the XML is well-formed.

## Manual Validation

These results are for the earlier design. They include the "Contact" link, the image carousels and the forms. The redesign removed these items. To be re-run on the new design.

Here are the results of a manual test of all links, and any form fields, for each page:

### index.html

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Site title - "The Older & Wider Podcast" | Click to return to index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "Home" | Click to open index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "About" | Click to open about.html | The user is redirected to about.html (even if already there) | The user is redirected to about.html (even if already there) | PASS |
| Navigation bar link - "Message Board" | Click to open message-board.html | The user is redirected to message-board.html (even if already there) | The user is redirected to message-board.html (even if already there) | PASS |
| Navigation bar link - "Contact"" | Click to open contact.html | The user is redirected to contact.html (even if already there) | The user is redirected to contact.html (even if already there) | PASS |
| Image carousel | Use arrow and indicator controls to move between all image slides | Slides transition succesfully | Slides transition succesfully | PASS |
| Link - "Acast" | Click to open external website in new tab | The link opens in a new tab | The link opens in a new tab | PASS |
| Link - "Apple Podcasts" | Click to open external website in new tab | The link opens in a new tab | The link opens in a new tab | PASS |
| Link - "Spotify" | Click to open external website in new tab | The link opens in a new tab | The link opens in a new tab | PASS |
| Button - "About the Podcast" | Click to move to about.html | The user is redirected to the about page | The user is redirected to the about page | PASS |
| Podcast player | Click play to play the podcast, and then click pause to pause playback | Playback begins or ends | Playback begins or ends | PASS |
| Button - "Buy Tickets" | Click to open external website in new tab | The link opens in a new tab | The link opens in a new tab | PASS |
| Button - "See the Merch" | Click to open external website in new tab | The link opens in a new tab | The link opens in a new tab | PASS |
| "Mailing List" - using a valid email | Enter a valid email address and click 'Send' | The email address is accepted and the user redirected to mailing-list-completion.html  | The email is accepted and the user is redirected to mailing-list-completion.html | PASS |
| "Mailing List" - using an invalid email | Enter an invalid email address and click 'Send' | The email address is rejected  | The email is rejected | PASS |
| Social media icon - Instagram | Click to open the Older & Wider Instagram page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Social media icon - Facebook | Click to open the Older & Wider Facebook page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Dominic Francis" | Click to open dominicfrancis.co.uk in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Older & Wider" | Click to open the Acast Older & Wider website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Acast" | Click to open the Acast website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |

### mailing-list-completion.html (page removed)

The redesign removed this page. These results are kept for the record.

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Site title - "The Older & Wider Podcast" | Click to return to index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "Home" | Click to open index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "About" | Click to open about.html | The user is redirected to about.html (even if already there) | The user is redirected to about.html (even if already there) | PASS |
| Navigation bar link - "Message Board" | Click to open message-board.html | The user is redirected to message-board.html (even if already there) | The user is redirected to message-board.html (even if already there) | PASS |
| Navigation bar link - "Contact"" | Click to open contact.html | The user is redirected to contact.html (even if already there) | The user is redirected to contact.html (even if already there) | PASS |
| Auto redirect (after 30 seconds) | The page is automatically redirected to index.html after 30 seconds have elapsed | The index.html page loads after 30 seconds | The index.html page loads after 30 seconds | PASS |
| Button - "Return to the home page" | Click to move to index.html | The user is redirected to the home page | The user is redirected to the home page | PASS |
| Button - "Learn about the podcast" | Click to move to about.html | The user is redirected to the about page | The user is redirected to the about page | PASS |
| Button - "View the 'Message Board'" | Click to move to message-board.html | The user is redirected to the message board page | The user is redirected to the message board page | PASS |
| Button - "Why not send us a message?" | Click to move to contact.html | The user is redirected to the contact page | The user is redirected to the contact page | PASS |
| Social media icon - Instagram | Click to open the Older & Wider Instagram page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Social media icon - Facebook | Click to open the Older & Wider Facebook page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Dominic Francis" | Click to open dominicfrancis.co.uk in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Older & Wider" | Click to open the Acast Older & Wider website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Acast" | Click to open the Acast website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |

### about.html

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Site title - "The Older & Wider Podcast" | Click to return to index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "Home" | Click to open index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "About" | Click to open about.html | The user is redirected to about.html (even if already there) | The user is redirected to about.html (even if already there) | PASS |
| Navigation bar link - "Message Board" | Click to open message-board.html | The user is redirected to message-board.html (even if already there) | The user is redirected to message-board.html (even if already there) | PASS |
| Navigation bar link - "Contact"" | Click to open contact.html | The user is redirected to contact.html (even if already there) | The user is redirected to contact.html (even if already there) | PASS |
| Image carousel for "What is Older & Wider?" | Use arrow and indicator controls to move between all image slides | Slides transition succesfully | Slides transition succesfully | PASS |
| Image carousel for "Who is Judith Holder" | Use arrow and indicator controls to move between all image slides | Slides transition succesfully | Slides transition succesfully | PASS |
| Image carousel for "Who is Jenny Eclair?" | Use arrow and indicator controls to move between all image slides | Slides transition succesfully | Slides transition succesfully | PASS |
| Social media icon - Instagram | Click to open the Older & Wider Instagram page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Social media icon - Facebook | Click to open the Older & Wider Facebook page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Dominic Francis" | Click to open dominicfrancis.co.uk in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Older & Wider" | Click to open the Acast Older & Wider website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Acast" | Click to open the Acast website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |

### message-board.html

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Site title - "The Older & Wider Podcast" | Click to return to index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "Home" | Click to open index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "About" | Click to open about.html | The user is redirected to about.html (even if already there) | The user is redirected to about.html (even if already there) | PASS |
| Navigation bar link - "Message Board" | Click to open message-board.html | The user is redirected to message-board.html (even if already there) | The user is redirected to message-board.html (even if already there) | PASS |
| Navigation bar link - "Contact"" | Click to open contact.html | The user is redirected to contact.html (even if already there) | The user is redirected to contact.html (even if already there) | PASS |
| Instagram embed - "Older and Wider Podcast" header | Click to open the Older & Wider Instagram page in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Instagram embed button - "Follow" | Click to open the Older & Wider Instagram page in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Instagram embed - load more posts | Click navigation arrows on either side of the instagram embed to load more posts | More posts slide into view  | More posts slide into view | PASS |
| Instagram embed - view post | Click a post to open it in a pop-up window | The post opens in a pop-up window  | The post opens in a pop-up window | PASS |
| Instagram embed - scroll posts | Use a mouse wheel (on desktop) or a finger (on mobile) to scroll down through other posts, from within a post's pop-up window | Further posts are shown  | Further posts are shown | PASS |
| Instagram embed - close post | Use a mouse wheel (on desktop) or a finger (on mobile) to click the cross in the top-right of a post's pop-up window | The post's pop-up window closes  | The post's pop-up window closes | PASS |
| Social media icon - Instagram | Click to open the Older & Wider Instagram page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Social media icon - Facebook | Click to open the Older & Wider Facebook page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Dominic Francis" | Click to open dominicfrancis.co.uk in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Older & Wider" | Click to open the Acast Older & Wider website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Acast" | Click to open the Acast website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |

### contact.html (page removed)

The redesign removed this page. These results are kept for the record.

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Site title - "The Older & Wider Podcast" | Click to return to index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "Home" | Click to open index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "About" | Click to open about.html | The user is redirected to about.html (even if already there) | The user is redirected to about.html (even if already there) | PASS |
| Navigation bar link - "Message Board" | Click to open message-board.html | The user is redirected to message-board.html (even if already there) | The user is redirected to message-board.html (even if already there) | PASS |
| Navigation bar link - "Contact"" | Click to open contact.html | The user is redirected to contact.html (even if already there) | The user is redirected to contact.html (even if already there) | PASS |
| Contact form - "First Name" | Where all other fields are empty, enter first name and click send | The user is prompted to enter their last name  | The user is prompted to enter their last name | PASS |
| Contact form - "Last Name" | Where all other fields are empty, except the first name, enter last name and click send | The user is prompted to enter their age  | The user is prompted to enter their age | PASS |
| Contact form - "Age" | Where all other fields are empty, except the first and last names, enter age and click send | The user is prompted to enter their email address  | The user is prompted to enter their email address | PASS |
| Contact form - "Email" - using an invalid email address | Where all other fields are empty, except the first name, last name, and age, enter an invalid email address and click 'Send' | The email address is rejected  | The email is rejected | PASS |
| Contact form - "Email" - using a valid email address | Where all other fields are empty, except the first name, last name, and age, enter a valid email address and click 'Send' | The user is prompted to enter a message  | The user is prompted to enter a message | PASS |
| Contact form - "Message" | Where all fields are completed correctly, enter a message and click 'Send' | The form is accepted and the user redirected to contact-completion.html  | The form is accepted and the user redirected to contact-completion.html | PASS |
| Contact form button - "Send" | Where all fields are completed correctly, click 'Send' | The form is accepted and the user redirected to contact-completion.html  | The form is accepted and the user redirected to contact-completion.html | PASS |
| Contact form button - "Reset" | Enter any information on the form, and click 'Reset' | The information on the form is cleared, ready for fresh data entry  | The information on the form is cleared, ready for fresh data entry | PASS |
| Social media icon - Instagram | Click to open the Older & Wider Instagram page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Social media icon - Facebook | Click to open the Older & Wider Facebook page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Dominic Francis" | Click to open dominicfrancis.co.uk in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Older & Wider" | Click to open the Acast Older & Wider website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Acast" | Click to open the Acast website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |

### contact-completion.html (page removed)

The redesign removed this page. These results are kept for the record.

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Site title - "The Older & Wider Podcast" | Click to return to index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "Home" | Click to open index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "About" | Click to open about.html | The user is redirected to about.html (even if already there) | The user is redirected to about.html (even if already there) | PASS |
| Navigation bar link - "Message Board" | Click to open message-board.html | The user is redirected to message-board.html (even if already there) | The user is redirected to message-board.html (even if already there) | PASS |
| Navigation bar link - "Contact"" | Click to open contact.html | The user is redirected to contact.html (even if already there) | The user is redirected to contact.html (even if already there) | PASS |
| Auto redirect (after 30 seconds) | The page is automatically redirected to index.html after 30 seconds have elapsed | The index.html page loads after 30 seconds | The index.html page loads after 30 seconds | PASS |
| Button - "Return to the home page" | Click to move to index.html | The user is redirected to the home page | The user is redirected to the home page | PASS |
| Button - "Learn about the podcast" | Click to move to about.html | The user is redirected to the about page | The user is redirected to the about page | PASS |
| Button - "View the 'Message Board'" | Click to move to message-board.html | The user is redirected to the message board page | The user is redirected to the message board page | PASS |
| Social media icon - Instagram | Click to open the Older & Wider Instagram page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Social media icon - Facebook | Click to open the Older & Wider Facebook page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Dominic Francis" | Click to open dominicfrancis.co.uk in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Older & Wider" | Click to open the Acast Older & Wider website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Acast" | Click to open the Acast website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |

### 404.html

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Site title - "The Older & Wider Podcast" | Click to return to index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "Home" | Click to open index.html | The user is redirected to index.html (even if already there) | The user is redirected to index.html (even if already there) | PASS |
| Navigation bar link - "About" | Click to open about.html | The user is redirected to about.html (even if already there) | The user is redirected to about.html (even if already there) | PASS |
| Navigation bar link - "Message Board" | Click to open message-board.html | The user is redirected to message-board.html (even if already there) | The user is redirected to message-board.html (even if already there) | PASS |
| Navigation bar link - "Contact"" | Click to open contact.html | The user is redirected to contact.html (even if already there) | The user is redirected to contact.html (even if already there) | PASS |
| Auto redirect (after 30 seconds) | The page is automatically redirected to index.html after 30 seconds have elapsed | The index.html page loads after 30 seconds | The index.html page loads after 30 seconds | PASS |
| Button - "Return to the home page" | Click to move to index.html | The user is redirected to the home page | The user is redirected to the home page | PASS |
| Button - "Learn about the podcast" | Click to move to about.html | The user is redirected to the about page | The user is redirected to the about page | PASS |
| Button - "View the 'Message Board'" | Click to move to message-board.html | The user is redirected to the message board page | The user is redirected to the message board page | PASS |
| Button - "Why not send us a message?" | Click to move to contact.html | The user is redirected to the contact page | The user is redirected to the contact page | PASS |
| Social media icon - Instagram | Click to open the Older & Wider Instagram page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Social media icon - Facebook | Click to open the Older & Wider Facebook page in a new tab  | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Dominic Francis" | Click to open dominicfrancis.co.uk in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Older & Wider" | Click to open the Acast Older & Wider website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |
| Footer link - "Acast" | Click to open the Acast website in a new tab | The link opens in a new tab  | The link opens in a new tab | PASS |

### privacy.html

The tests used a local server and headless Google Chrome on 27 November 2026. The viewport widths were 390px and 1440px.

| TEST | EXPECTED RESULT | RESULT |
| --- | --- | --- |
| Open the page | The page shows the title, the date "Last updated 27 November 2026" and the table of third parties. | PASS |
| Check the navigation | The navigation shows Home, About and Message Board. No link has `aria-current`. | PASS |
| Check the table at 390px | Each service shows as one block, with a label above each value. | PASS |
| Check the table at 1440px | The table shows four columns. | PASS |
| Press "Cookie settings" in the page | The cookie banner opens. | PASS |
| Press the link to the website of Dominic Francis | The link opens https://www.dominicfrancis.co.uk/. | PASS |
| Check for horizontal scroll at 390px | The page does not scroll sideways. | PASS |

### Cookie Consent and Click-to-Load

The tests used a local server and headless Google Chrome, driven by a Playwright script, on 27 November 2026. Each test started with a new browser profile.

| TEST | EXPECTED RESULT | RESULT |
| --- | --- | --- |
| Open each of the five pages for the first time | The banner shows. No request goes to `embed.acast.com`, `instagram.com` or `googletagmanager.com`. | PASS |
| Measure "Accept" and "Reject" | The two buttons have the same width, height, font size, weight and colours. | PASS |
| Press "Accept" with the placeholder ID | The site stores "accepted". No request goes to `googletagmanager.com`. | PASS |
| Press "Accept" with a test ID | The site loads `gtag/js` from `googletagmanager.com`, with no reload. No request goes before "Accept". | PASS |
| Press "Reject" | The site stores "rejected" and deletes the `_ga` and `_ga_*` cookies. Other cookies stay. | PASS |
| Reload the page after "Reject" | The banner stays closed. | PASS |
| Press "Cookie settings" in the footer | The banner opens, shows the earlier choice and gets focus. | PASS |
| Use the banner with the keyboard | Tab goes to the privacy link, "Accept" and "Reject". After a choice, focus goes back to "Cookie settings". | PASS |
| Press "Play here" on the home page | The Acast player loads in place of the button and gets focus. | PASS |
| Turn off JavaScript | No banner shows. "Cookie settings" and "Play here" are hidden. The "Listen on Acast" link shows. No third-party embed loads. | PASS |
| Set `prefers-reduced-motion: reduce` | The banner shows with no animation. | PASS |

Before go-live, replace the placeholder ID `G-XXXXXXXXXX` in `assets/js/analytics.js`. Then do the GA4 Realtime test in issue #21.

## User Story Validation

These results are for the earlier design. Some section names in the tables are from the earlier design. To be re-run on the new design.

### First Time Visitor Goals

1. "What is the Older and Wider podcast about?"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| About page | Navigate to the about page using the navigation bar at the top of each page, and scroll down to the section called "What is Older & Wider?" | View information about the podcast | View information about the podcast | PASS |

![First time visitor goal 1](documentation/validation/first-time-visitor-goal-1.webp)

2. "Who is Jenny Eclair?"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| About page | Navigate to the about page using the navigation bar at the top of each page, and scroll down to the section called "Who is Jenny Eclair?" | View information about Jenny Eclair | View information about Jenny Eclair | PASS | 

![First time visitor goal 2](documentation/validation/first-time-visitor-goal-2.webp)

3. "Who is Judith Holder?"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| About page | Navigate to the about page using the navigation bar at the top of each page, and scroll down to the section called "Who is Judith Holder?" | View information about Judith Holder | View information about Judith Holder | PASS | 

![First time visitor goal 3](documentation/validation/first-time-visitor-goal-3.webp)

4. "Where can I listen to the Older and Wider Podcast"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Home page | Navigate to the home page, , scroll down to the section called "Join the Older & Wider Podcast Gang", and find the links to podcast platforms | Find the info and choose a provider where you can download and listen to the podcast | Find the info and choose a provider where you can download and listen to the podcast | PASS | 
| Home page | Navigate to the home page, scroll down to the section called "Listen to the Podcast", and play the latest episode from the embedded podcast player | Find the podcast player and listen to the latest episode | Find the podcast player and listen to the latest episode | PASS | 

![First time visitor goal 4](documentation/validation/first-time-visitor-goal-4.webp)

5. "When are episodes of the Older and Wider podcast released?"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Home page | Navigate to the home page, scroll down to the section called "Join the Older & Wider Podcast Gang", and read about the podcast release date | Find the release date of the podcast | Find the release date of the podcast | PASS | 

![First time visitor goal 5](documentation/validation/first-time-visitor-goal-5.webp)

### Returning Visitor Goals:

1. "I want to find out more background information about the Older and Wider podcast"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| About page | Navigate to the about page using the navigation bar at the top of each page, and scroll down to the section called "What is Older & Wider?" | View information about the podcast | View information about the podcast | PASS |
| Home page | Navigate to the home page, scroll down to the section called "Mailing List", enter a valid email address, and click the button titled 'Send' to be included on the podcast's mailing list | User is added to the mailing list, and will receive further information via email | User is added to the mailing list, and will receive further information via email | REMOVED (the redesign removed the mailing list form) | 

![Returning visitor goal 1](documentation/validation/returning-visitor-goal-1a.webp)
![Returning visitor goal 1](documentation/validation/returning-visitor-goal-1b.webp)

2. "What was mentioned during the 'Culture Corner' segment of this week's show?"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Message board page | Navigate to the message board page, using the navigation bar at the top of each page, and scroll through the posts on Instagram to find the latest Culture Corner update | Find the latest Culture Corner post and read it | Find the latest Culture Corner post and read it | PASS | 

![Returning visitor goal 2](documentation/validation/returning-visitor-goal-2.webp)

3. "Has the podcast won any awards?"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Home page | Navigate to the home page, scroll down to the section called "Join the Older & Wider Podcast Gang", and read about awards for which the podcast has been nominated | Find information about awards | Find information about awards | PASS |

![Returning visitor goal 3](documentation/validation/returning-visitor-goal-3.webp)

4. "What is the 'Message Board' - it was mentioned by Jenny and Judith in this week's episode, but where can I access it?"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Message board page | Navigate to the message board page, and read the text under the Instagram embed | Find information about the message board | Find information about the message board | PASS | 

![Returning visitor goal 4](documentation/validation/returning-visitor-goal-4.webp)

### Frequent Visitor Goals:

1. "How can I contact Jenny and Judith to share my experiences, or comment on an item that was mentioned in the show?"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Contact page | Navigate to the contact page, and complete the contact form to send a message to the podcast | A message is sent, and the user is redirected to the contact completion page | A message is sent, and the user is redirected to the contact completion page | REMOVED (the redesign removed the contact page) | 

The message board page now answers this goal. It links to the Instagram and Facebook pages of the podcast. To be re-run on the new design.

![Frequent visitor goal 1](documentation/validation/frequent-visitor-goals-1.webp)

2. "Is there any podcast merchandise available?"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Home page | Navigate to the home page, scroll down to the section called "Merch", and click the button titled 'See the Merch' to be taken to the merchandise website (in a new tab) | User can purchase merchandise from an external website | User can purchase merchandise from an external website | PASS | 

![Frequent visitor goal 2](documentation/validation/frequent-visitor-goals-2.webp)

3. "Can I watch the podcast being performed live?"

| ITEM | PROCESS | EXPECTED RESULT | ACTUAL RESULT | STATUS |
| --- | --- | --- | --- | --- |
| Home page | Navigate to the home page, scroll down to the section called "Older & Wider - Live!", and click the button titled 'Buy Tickets' to be taken to an external ticketing website (in a new tab) | User can purchase available tickets to a live show, from an external website | User can purchase available tickets to a live show, from an external website | PASS | 

![Frequent visitor goal 3](documentation/validation/frequent-visitor-goals-3.webp)

## Browser Compatibility

**Lighthouse and browser tests: to be re-run on the new design.** The screenshots below show the earlier design.

The website has been successfully tested in the following browsers (desktop screenshots used to allow for a larger preview, except for Safari as there is no Windows version of that browser):

### Google Chrome

![Website in Google Chrome](documentation/validation/compatibility-google-chrome.webp)

### Microsoft Edge

![Website in Microsoft Edge](documentation/validation/compatibility-microsoft-edge.webp)

### Firefox

![Website in Firefox](documentation/validation/compatibility-firefox.webp)

### Opera

![Website in Opera](documentation/validation/compatibility-opera.webp)

### Safari (on an iPad)

![Website in Safari (iPad)](documentation/validation/compatibility-safari-ipad.webp)

### Safari (on an iPhone)

![Website in Safari (iPhone)](documentation/validation/compatibility-safari-iphone.webp)

## Accessibility

These results are for the earlier design. To be re-run on the new design. The redesign removed the auto-redirect, so the redirect errors below do not apply to the new `404.html`.

Pages were tested for accessibility using the [Wave Accessibility Evaluation Tool](https://wave.webaim.org):

### index.html

![WAVE report for index.html](documentation/validation/wave-report-index.webp)

### mailing-list-completion.html (page removed)

The redesign removed this page. These results are kept for the record.

The error being shown here is because of the auto-redirect setup on the page, which is part of the design:

![WAVE report for mailing-list-completion.html](documentation/validation/wave-report-mailing-list-completion.webp)

### about.html

![WAVE report for about.html](documentation/validation/wave-report-about.webp)

### message-board.html

![WAVE report for message-board.html](documentation/validation/wave-report-message-board.webp)

### contact.html (page removed)

The redesign removed this page. These results are kept for the record.

![WAVE report for contact.html](documentation/validation/wave-report-contact.webp)

### contact-completion.html (page removed)

The redesign removed this page. These results are kept for the record.

The error being shown here is because of the auto-redirect setup on the page, which is part of the design:

![WAVE report for contact-completion.html](documentation/validation/wave-report-contact-completion.webp)

### 404.html

The error being shown here is because of the auto-redirect setup on the page, which is part of the design:

![WAVE report for 404.html](documentation/validation/wave-report-404.webp)

## Responsiveness

These results are for the earlier design. To be re-run on the new design.

Pages were tested for responsiveness at mobile size (Samsung Galaxy S5/S6/S7 - 360px x 640px), tablet size (Apple iPad Retina - 768px 1024px), and desktop size (1400px x 700px), using the [Responsive Web Design Checker](https://responsivedesignchecker.com/):

### index.html

#### Mobile

![Responsiveness report for index.html](documentation/validation/responsive-index-mobile.webp)

#### Tablet

![Responsiveness report for index.html](documentation/validation/responsive-index-tablet.webp)

#### Desktop

![Responsiveness report for index.html](documentation/validation/responsive-index-desktop.webp)

### mailing-list-completion.html (page removed)

The redesign removed this page. These results are kept for the record.

#### Mobile

![Responsiveness report for mailing-list-completion.html](documentation/validation/responsive-mailing-list-completion-mobile.webp)

#### Tablet

![Responsiveness report for mailing-list-completion.html](documentation/validation/responsive-mailing-list-completion-tablet.webp)

#### Desktop

![Responsiveness report for mailing-list-completion.html](documentation/validation/responsive-mailing-list-completion-desktop.webp)

### about.html

#### Mobile

![Responsiveness report for about.html](documentation/validation/responsive-about-mobile.webp)

#### Tablet

![Responsiveness report for about.html](documentation/validation/responsive-about-tablet.webp)
#### Desktop

![Responsiveness report for about.html](documentation/validation/responsive-about-desktop.webp)

### message-board.html

For some reason, the Instagram widget does not load for this preview, and the social media icons are squashed. This behaviour is not evident when viewing the site on an actual mobile, tablet, or desktop device so I think it is caused by something this website does during testing.

#### Mobile

![Responsiveness report for message-board.html](documentation/validation/responsive-message-board-mobile.webp)

#### Tablet

![Responsiveness report for message-board.html](documentation/validation/responsive-message-board-tablet.webp)

#### Desktop

![Responsiveness report for message-board.html](documentation/validation/responsive-message-board-desktop.webp)

### contact.html (page removed)

The redesign removed this page. These results are kept for the record.

#### Mobile

![Responsiveness report for contact.html](documentation/validation/responsive-contact-completion-mobile.webp)

#### Tablet

![Responsiveness report for contact.html](documentation/validation/responsive-contact-tablet.webp)

#### Desktop

![Responsiveness report for contact.html](documentation/validation/responsive-contact-desktop.webp)

### contact-completion.html (page removed)

The redesign removed this page. These results are kept for the record.

#### Mobile

![Responsiveness report for contact-completion.html](documentation/validation/responsive-contact-completion-mobile.webp)

#### Tablet

![Responsiveness report for contact-completion.html](documentation/validation/responsive-contact-completion-tablet.webp)

#### Desktop

![Responsiveness report for contact-completion.html](documentation/validation/responsive-contact-completion-desktop.webp)

### 404.html

#### Mobile

![Responsiveness report for 404.html](documentation/validation/responsive-404-mobile.webp)

#### Tablet

![Responsiveness report for 404.html](documentation/validation/responsive-404-tablet.webp)

#### Desktop

![Responsiveness report for 404.html](documentation/validation/responsive-404-desktop.webp)

## Performance

**Lighthouse and browser tests: to be re-run on the new design.** The scores below are for the earlier design. The notes about the redirect do not apply to the new `404.html`, because the redesign removed the redirect.

Each page was audited using [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/), for both mobile and desktop:

### index.html

#### Mobile

![Mobile performance report for index.html](documentation/validation/performance-index-mobile.webp)

#### Desktop

![Desktop performance report for index.html](documentation/validation/performance-index-desktop.webp)

### mailing-list-completion.html (page removed)

The redesign removed this page. These results are kept for the record.

The lower score for accessibility here is caused by two things - the presence of the redirect (which is part of the site design), and because FontAwesome automatically adds the ``aria-hidden="true"`` class to all of its icons. This cannot be stopped and is conflicting with my own ARIA label on each social media icon. 

#### Mobile

![Mobile performance report for mailing-list-completion.html](documentation/validation/performance-mailing-list-completion-mobile.webp)

#### Desktop

![Desktop performance report for mailing-list-completion.html](documentation/validation/performance-mailing-list-completion-desktop.webp)

### about.html

#### Mobile

![Mobile performance report for about.html](documentation/validation/performance-about-mobile.webp)

#### Desktop

![Desktop performance report for about.html](documentation/validation/performance-about-desktop.webp)

### message-board.html

The lower score for performance here is because, among other things, the images being loaded by the Instagram embed are quite large. Unfortunately, I have no control over this. 

#### Mobile

![Mobile performance report for message-board.html](documentation/validation/performance-message-board-mobile.webp)

#### Desktop

![Desktop performance report for message-board.html](documentation/validation/performance-message-board-desktop.webp)

### contact.html (page removed)

The redesign removed this page. These results are kept for the record.

#### Mobile

![Mobile performance report for contact.html](documentation/validation/performance-contact-mobile.webp)

#### Desktop

![Desktop performance report for contact.html](documentation/validation/performance-contact-desktop.webp)

### contact-completion.html (page removed)

The redesign removed this page. These results are kept for the record.

The lower score for accessibility here is caused by two things - the presence of the redirect (which is part of the site design), and because FontAwesome automatically adds the ``aria-hidden="true"`` class to all of its icons. This cannot be stopped and is conflicting with my own ARIA label on each social media icon. 

#### Mobile

![Mobile performance report for contact-completion.html](documentation/validation/performance-contact-completion-mobile.webp)

#### Desktop

![Desktop performance report for contact-completion.html](documentation/validation/performance-contact-completion-desktop.webp)

### 404.html

The lower score for accessibility here is caused by two things - the presence of the redirect (which is part of the site design), and because FontAwesome automatically adds the ``aria-hidden="true"`` class to all of its icons. This cannot be stopped and is conflicting with my own ARIA label on each social media icon. 

#### Mobile

![Mobile performance report for 404.html](documentation/validation/performance-404-mobile.webp)

#### Desktop

![Desktop performance report for 404.html](documentation/validation/performance-404-desktop.webp)

## Bugs

These bugs were found in the earlier design. Some of them relate to Bootstrap or to the contact page, which the redesign removed.

Here is a list of bugs encountered while building this website. Images shown illustrate the original problem:

### Bug 1

![Fixed Bug 1](documentation/bugs/bug-01-fontawesome-icons.webp)

| Bug | Fix |
| --- | --- |
| The Fontawesome logos are not centred | Replace original code with Bootstrap classes to organise the icons into rows and columns before applying text-end and text-start to achieve final position |

### Bug 2

![Fixed Bug 2](documentation/bugs/bug-02-highlight-menu-item.webp)


| Bug | Fix |
| --- | --- |
| The link to the currently loaded page is not highlighted in the navigation bar | Style the pseudo elements - :link, :hover, and :active - to change the navigation links upon use. Add a class called "active" (with the same CSS declarations as :hover) and add to the menu item for the currently active page.

### Bug 3

![Fixed Bug 3](documentation/bugs/bug-03-navbar-position.webp)

| Bug | Fix |
| --- | --- |
| Navigation bar is not centred or responsive | Centred the menu items using the mx-auto Bootstrap class on the internal navbar container

### Bug 4

![Fixed Bug 4](documentation/bugs/bug-04-page-content-hidden.webp)

| Bug | Fix |
| --- | --- |
| Page content is hidden behind fixed header | Created media queries to add padding to the top of the ``body`` element, at different screen resolutions

### Bug 5

![Fixed Bug 5](documentation/bugs/bug-05-images-too-wide.webp)

| Bug | Fix |
| --- | --- |
| Images are too wide at larger resolution | Adjusted the size using a percentage value against ``max-width`` property of the img tag |

### Bug 6

![Fixed Bug 6](documentation/bugs/bug-06-text-size.webp)

| Bug | Fix |
| --- | --- |
| Text is too small at larger screen resolutions | Added Bootstrap classes to manage the text elements at different screen resolutions; for example, fs-4. |

### Bug 7

![Fixed Bug 7](documentation/bugs/bug-07-contact-form-width.webp)

| Bug | Fix |
| --- | --- |
| Contact form is to wide on larger screen resolutions | Needed some adjustment with regards to font size and font weight, using Bootstrap font classes |

### Bug 8

![Fixed Bug 8](documentation/bugs/bug-08-header-red-line.webp)

| Bug | Fix |
| --- | --- |
| A red line appears underneath the header on the contact.html page, at higher screen resolutions | Accidentally added the ``.feature`` class to the header, which added the red line |

### Bug 9

![Fixed Bug 9](documentation/bugs/bug-09-short-click-release.webp)

| Bug | Fix |
| --- | --- |
| If you select a navigation link but then drag away from it, it turns black | The pseudo element ``:visited`` had not been formatted for the links. Once it was they remained white as expected. |

### Bug 10

![Fixed Bug 10](documentation/bugs/bug-10-button-padding.webp)

| Bug | Fix |
| --- | --- |
| When the site width increases, the padding on buttons seems to increase too, leading to misaligned button text | Removed the height property that had been added to the buttons |

### Bug 11

![Fixed Bug 11](documentation/bugs/bug-11-widget-overlap.webp)

| Bug | Fix |
| --- | --- |
| The Instagram widget used for message-board.html overlaps the fixed footer | The footer is no longer fixed and this solved the issue. If it had remained fixed I believe adjusting the z-index of the widget would also have solved the issue. |

### Bug 12

![Fixed Bug 12](documentation/bugs/bug-12-navbar-links-move%20(1).webp)
![Fixed Bug 12](documentation/bugs/bug-12-navbar-links-move%20(2).webp)
![Fixed Bug 12](documentation/bugs/bug-12-navbar-links-move%20(3).webp)
![Fixed Bug 12](documentation/bugs/bug-12-navbar-links-move%20(4).webp)

| Bug | Fix |
| --- | --- |
| When I hover over, or click, a navbar link, the other navbar links move ever so slightly (I have exaggerated it for the screenshots so it is easier to see) | Added a default border size to the item when it wasn't being hovered over or clicked. |

## Unfixed Bugs

Here is a list of bugs I was unable to fix due to circumstances beyond my control:

### Bug 1

![Unfixed Bug 1](documentation/bugs/bug-13-chromium-whitespace.webp)

| Bug | Fix |
| --- | --- |
| There is a white line beneath the footer | This only occurs in Chromium-based browsers such as Google Chrome and Microsoft Edge; the line does not appear in other browers tested. After discussing this with Code Institute's tutor support we came to the conclusion it was either a problem with that type of browser, or a strange quirk of the computer I am using |