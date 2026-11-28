/* Archive venue search.
   This script shows the search box and the letter buttons above the venue list.
   The search hides each town that does not match the search text.
   It opens each letter that has a match, and dims the other dots on the map.
   It opens the show list of a venue when a show or a date matches.
   The buttons open or close all the letters.
   Without JavaScript, the search box and the buttons stay hidden. The full list shows. */
(function () {
    "use strict";

    var box = document.getElementById("arc-venue-search");
    var input = document.getElementById("arc-venue-search-input");
    var status = document.getElementById("arc-venue-search-status");
    if (!box || !input || !status) {
        return;
    }

    // Make the text lower case, and remove accents and curly apostrophes.
    function fold(text) {
        return text
            .normalize("NFD")
            .replace(/[̀-ͯ]/g, "")
            .replace(/[‘’]/g, "'")
            .replace(/\s+/g, " ")
            .toLowerCase()
            .trim();
    }

    function all(selector, root) {
        return Array.prototype.slice.call((root || document).querySelectorAll(selector));
    }

    var letters = all(".arc-venue-letter");
    var towns = all(".arc-venue-town").map(function (town) {
        return { item: town, text: fold(town.textContent) };
    });
    var lists = all(".arc-venue-shows").map(function (list) {
        var shows = list.querySelector(".arc-venue-show-list");
        return { item: list, text: fold(shows ? shows.textContent : "") };
    });
    var dots = all(".arc-venue-map-dots circle");

    function update() {
        var query = fold(input.value);
        var matches = {};
        var count = 0;

        towns.forEach(function (town) {
            var match = query === "" || town.text.indexOf(query) !== -1;
            town.item.hidden = !match;
            if (match) {
                matches[town.item.id] = true;
                count += 1;
            }
        });

        letters.forEach(function (letter) {
            var match = letter.querySelector(".arc-venue-town:not([hidden])") !== null;
            letter.hidden = !match;
            if (query !== "") {
                letter.open = match;
            }
        });

        // Open a show list when the search text is in it. Close the lists
        // that the search opened when the text changes.
        lists.forEach(function (list) {
            var match = query !== "" && list.text.indexOf(query) !== -1;
            if (match) {
                list.item.open = true;
                list.item.setAttribute("data-search-open", "");
            } else if (list.item.hasAttribute("data-search-open")) {
                list.item.open = false;
                list.item.removeAttribute("data-search-open");
            }
        });

        dots.forEach(function (dot) {
            var match = matches[dot.getAttribute("data-town")] === true;
            dot.classList.toggle("is-match", query !== "" && match);
            dot.classList.toggle("is-dim", query !== "" && !match);
        });

        if (query === "") {
            status.textContent = "";
        } else if (count === 0) {
            status.textContent = "No town or venue matches the search.";
        } else if (count === 1) {
            status.textContent = "1 town matches the search.";
        } else {
            status.textContent = count + " towns match the search.";
        }
    }

    // The buttons open or close each letter that shows now.
    all("[data-letters]", box).forEach(function (button) {
        button.addEventListener("click", function () {
            var open = button.getAttribute("data-letters") === "open";
            letters.forEach(function (letter) {
                if (!letter.hidden) {
                    letter.open = open;
                }
            });
        });
    });

    input.addEventListener("input", update);
    box.hidden = false;
}());
