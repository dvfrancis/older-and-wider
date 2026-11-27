// Google Analytics: load only after the visitor accepts analytics cookies.
// consent.js stores the choice. This file reads it and listens for changes.
(function () {
    "use strict";

    // REPLACE THIS PLACEHOLDER with the real GA4 measurement ID before go-live.
    // While the value is the placeholder, this file does nothing.
    var GA_MEASUREMENT_ID = "G-XXXXXXXXXX";

    // A real ID is "G-" and letters or digits. The placeholder is all X.
    var isRealId = /^G-[A-Z0-9]{4,}$/.test(GA_MEASUREMENT_ID) && !/^G-X+$/.test(GA_MEASUREMENT_ID);
    var consent = window.oawConsent;

    if (!isRealId || !consent) {
        return;
    }

    var loaded = false;

    function gtag() {
        window.dataLayer.push(arguments);
    }

    function load() {
        window["ga-disable-" + GA_MEASUREMENT_ID] = false;

        if (loaded) {
            gtag("consent", "update", { analytics_storage: "granted" });
            return;
        }
        loaded = true;

        window.dataLayer = window.dataLayer || [];
        window.gtag = gtag;
        gtag("js", new Date());
        gtag("config", GA_MEASUREMENT_ID);

        var script = document.createElement("script");
        script.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA_MEASUREMENT_ID);
        script.async = true;
        document.head.appendChild(script);
    }

    // Stop Google Analytics on this page when the visitor withdraws consent.
    // consent.js deletes the cookies after this event.
    function stop() {
        window["ga-disable-" + GA_MEASUREMENT_ID] = true;
        if (loaded) {
            gtag("consent", "update", { analytics_storage: "denied" });
        }
    }

    if (consent.get() === "accepted") {
        load();
    }

    document.addEventListener(consent.eventName, function (event) {
        if (event.detail && event.detail.choice === "accepted") {
            load();
        } else {
            stop();
        }
    });
})();
