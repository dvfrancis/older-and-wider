// Live shows: move each past show from Forthcoming shows to Recent shows.
// The HTML is correct without this script. The script only keeps the lists up to date.
(function () {
    "use strict";

    var forthcoming = document.getElementById("shows-forthcoming");
    var recent = document.getElementById("shows-recent");
    var forthcomingEmpty = document.getElementById("forthcoming-empty");
    var recentEmpty = document.getElementById("recent-empty");

    if (!forthcoming || !recent) {
        return;
    }

    // Get the date of today in the UK as YYYY-MM-DD.
    // The en-CA format gives this order. The time zone of the visitor has no effect.
    var today = new Intl.DateTimeFormat("en-CA", {
        timeZone: "Europe/London",
        year: "numeric",
        month: "2-digit",
        day: "2-digit"
    }).format(new Date());

    function showDate(item) {
        var time = item.querySelector("time[datetime]");
        return time ? time.getAttribute("datetime").slice(0, 10) : "";
    }

    // Put a show in Recent shows, with the latest date first.
    function addToRecent(item) {
        var date = showDate(item);
        var others = recent.children;
        for (var i = 0; i < others.length; i += 1) {
            if (showDate(others[i]) < date) {
                recent.insertBefore(item, others[i]);
                return;
            }
        }
        recent.appendChild(item);
    }

    // Copy the list first, because each move changes the live list.
    var items = Array.prototype.slice.call(forthcoming.children);

    items.forEach(function (item) {
        var date = showDate(item);
        // A show stays all of its day. It moves on the next day.
        // The dates are in YYYY-MM-DD form, so a text comparison is correct.
        if (date && date < today) {
            var tickets = item.querySelector(".show-tickets");
            if (tickets) {
                tickets.remove();
            }
            addToRecent(item);
        }
    });

    // Show the message for an empty list. Hide the empty list.
    function update(list, message) {
        var empty = list.children.length === 0;
        list.hidden = empty;
        if (message) {
            message.hidden = !empty;
        }
    }

    update(forthcoming, forthcomingEmpty);
    update(recent, recentEmpty);
}());
