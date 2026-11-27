// Cookie consent: ask once about analytics cookies, and remember the answer.
// The banner asks about Google Analytics only. Other embeds load on a click.
// Without JavaScript the banner does not show, and no analytics load.
(function () {
    "use strict";

    // The key for the stored choice in localStorage.
    var STORAGE_KEY = "oaw-consent";
    // The event that tells analytics.js about a new choice.
    var CHANGE_EVENT = "oaw:consentchange";

    var banner = null;
    var statusLine = null;
    var returnFocus = null;

    // Read the stored choice. Return null if there is no valid choice.
    function readChoice() {
        try {
            var raw = window.localStorage.getItem(STORAGE_KEY);
            if (!raw) {
                return null;
            }
            var data = JSON.parse(raw);
            if (data && (data.choice === "accepted" || data.choice === "rejected")) {
                return data;
            }
        } catch (error) {
            // Storage is blocked or the value is damaged. Ask again.
        }
        return null;
    }

    // Save the choice with today's date.
    function saveChoice(choice) {
        var data = { choice: choice, date: new Date().toISOString() };
        try {
            window.localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
        } catch (error) {
            // Storage is blocked. The choice applies to this page only.
        }
        return data;
    }

    // Delete the Google Analytics cookies for this host and its parent domains.
    function deleteAnalyticsCookies() {
        var names = document.cookie.split(";").map(function (part) {
            return part.split("=")[0].trim();
        }).filter(function (name) {
            return name === "_ga" || name.indexOf("_ga_") === 0;
        });

        var parts = window.location.hostname.split(".");
        var domains = [""];
        for (var i = 0; i < parts.length - 1; i += 1) {
            domains.push("; domain=." + parts.slice(i).join("."));
        }

        names.forEach(function (name) {
            domains.forEach(function (domain) {
                document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + domain;
            });
        });
    }

    // Write a date in the site style, for example "27 November 2026".
    function formatDate(iso) {
        var date = new Date(iso);
        if (isNaN(date.getTime())) {
            return "";
        }
        return date.toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
    }

    // Show the current choice in the banner, if there is one.
    function updateStatus() {
        var stored = readChoice();
        if (!stored) {
            statusLine.hidden = true;
            statusLine.textContent = "";
            return;
        }
        var word = stored.choice === "accepted" ? "yes" : "no";
        var when = formatDate(stored.date);
        statusLine.textContent = "You said " + word + " to analytics" + (when ? " on " + when : "") + ".";
        statusLine.hidden = false;
    }

    function choose(choice) {
        var data = saveChoice(choice);

        document.dispatchEvent(new CustomEvent(CHANGE_EVENT, { detail: data }));

        if (choice === "rejected") {
            deleteAnalyticsCookies();
        }

        closeBanner();
    }

    function makeButton(label, choice) {
        var button = document.createElement("button");
        button.type = "button";
        button.className = "consent-button";
        button.textContent = label;
        button.addEventListener("click", function () {
            choose(choice);
        });
        return button;
    }

    // Make the banner once. It sits at the end of the page and sticks to the bottom.
    function buildBanner() {
        banner = document.createElement("div");
        banner.className = "consent";
        banner.id = "consent";
        banner.setAttribute("role", "region");
        banner.setAttribute("aria-labelledby", "consent-title");
        banner.hidden = true;

        var inner = document.createElement("div");
        inner.className = "consent-inner";

        var text = document.createElement("div");
        text.className = "consent-text";

        var title = document.createElement("p");
        title.className = "consent-title";
        title.id = "consent-title";
        title.tabIndex = -1;
        title.textContent = "Can we count your visit?";

        var body = document.createElement("p");
        body.className = "consent-body";
        body.appendChild(document.createTextNode(
            "With your yes, Google Analytics sets cookies to count visits. The site works the same either way. "
        ));
        var link = document.createElement("a");
        // Copy the footer link, because 404.html uses root-relative paths.
        var footerLink = document.querySelector(".site-footer a[href$='privacy.html']");
        link.href = footerLink ? footerLink.getAttribute("href") : "privacy.html";
        link.textContent = "Read the privacy policy";
        body.appendChild(link);
        body.appendChild(document.createTextNode("."));

        statusLine = document.createElement("p");
        statusLine.className = "consent-status";
        statusLine.hidden = true;

        text.appendChild(title);
        text.appendChild(body);
        text.appendChild(statusLine);

        var actions = document.createElement("div");
        actions.className = "consent-actions";
        actions.appendChild(makeButton("Accept", "accepted"));
        actions.appendChild(makeButton("Reject", "rejected"));

        inner.appendChild(text);
        inner.appendChild(actions);
        banner.appendChild(inner);
        document.body.appendChild(banner);
    }

    function openBanner(focusIt) {
        updateStatus();
        banner.hidden = false;
        if (focusIt) {
            returnFocus = document.activeElement;
            banner.querySelector(".consent-title").focus({ preventScroll: true });
            // At the end of the page the banner is below the footer. Show all of it.
            banner.scrollIntoView({ block: "nearest" });
        }
    }

    function closeBanner() {
        var hadFocus = banner.contains(document.activeElement);
        banner.hidden = true;
        if (hadFocus && returnFocus && document.body.contains(returnFocus)) {
            returnFocus.focus();
        }
        returnFocus = null;
    }

    // Let analytics.js read the stored choice.
    window.oawConsent = {
        get: function () {
            var stored = readChoice();
            return stored ? stored.choice : null;
        },
        eventName: CHANGE_EVENT
    };

    buildBanner();

    // Show the Cookie settings buttons. They are hidden without JavaScript.
    var openers = document.querySelectorAll("[data-consent-open]");
    Array.prototype.forEach.call(openers, function (opener) {
        opener.hidden = false;
        opener.setAttribute("aria-controls", "consent");
        opener.addEventListener("click", function () {
            openBanner(true);
        });
    });

    // First visit, or no valid choice: ask. Do not move focus.
    if (!readChoice()) {
        openBanner(false);
    }
})();
