// Message board: show the date of today in the issue line under the title.
// Without this script, the issue line shows "Message board" only.
(function () {
    "use strict";

    var wrap = document.getElementById("board-date");
    var time = wrap ? wrap.querySelector("time") : null;

    if (!time) {
        return;
    }

    var now = new Date();

    // Get the date of today in the UK. The time zone of the visitor has no effect.
    // The en-CA format gives YYYY-MM-DD for the datetime attribute.
    var iso = new Intl.DateTimeFormat("en-CA", {
        timeZone: "Europe/London",
        year: "numeric",
        month: "2-digit",
        day: "2-digit"
    }).format(now);

    // The en-GB format gives the visible date, for example "28 November 2026".
    var shown = new Intl.DateTimeFormat("en-GB", {
        timeZone: "Europe/London",
        day: "numeric",
        month: "long",
        year: "numeric"
    }).format(now);

    time.setAttribute("datetime", iso);
    time.textContent = shown;
    wrap.hidden = false;
}());
