// Message board: load Instagram posts only when the visitor asks.
// Nothing loads from Instagram, and nothing is stored, until the button is pressed.
(function () {
    "use strict";

    var button = document.getElementById("board-load");
    var consent = document.getElementById("board-consent");
    var heading = document.getElementById("posts-title");

    if (!button) {
        return;
    }

    button.addEventListener("click", function () {
        button.disabled = true;

        // Add Instagram's embed script to the page.
        var script = document.createElement("script");
        script.src = "https://www.instagram.com/embed.js";
        script.async = true;

        // When it has loaded, turn each blockquote into a post.
        script.addEventListener("load", function () {
            if (window.instgrm && window.instgrm.Embeds) {
                window.instgrm.Embeds.process();
            }
            consent.hidden = true;
            heading.focus();
        });

        // If it fails, let the visitor try again. The links still work.
        script.addEventListener("error", function () {
            script.remove();
            button.disabled = false;
        });

        document.body.appendChild(script);
    });
})();
