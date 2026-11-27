// Home page player: load the Acast player only when the visitor asks.
// Nothing loads from Acast until the button is pressed.
// The page does not remember the choice, so the button shows on every visit.
(function () {
    "use strict";

    var holder = document.getElementById("player");
    var button = document.getElementById("player-load");
    var note = document.getElementById("player-note");
    var fallback = document.getElementById("player-fallback");

    if (!holder || !button) {
        return;
    }

    // JavaScript is on: show the button and the note, and hide the plain link.
    button.hidden = false;
    note.hidden = false;
    fallback.hidden = true;

    button.addEventListener("click", function () {
        var frame = document.createElement("iframe");
        frame.src = "https://embed.acast.com/63b6b30a19c20a0011527ce4";
        frame.title = "Older and Wider podcast player";
        frame.setAttribute("allow", "autoplay *; encrypted-media *; fullscreen *; clipboard-write");
        frame.setAttribute("loading", "lazy");

        // Put the player in place of the button, then move focus to the player.
        holder.replaceChildren(frame);
        holder.classList.add("is-loaded");
        frame.focus();
    });
})();
