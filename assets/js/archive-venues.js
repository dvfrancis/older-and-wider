/* Archive venue search.
   This script shows the search box above the venue list.
   It hides each town that does not match the search text.
   It opens each letter that has a match, and dims the other dots on the map.
   Without JavaScript, the search box stays hidden and the full list shows. */
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

    var letters = Array.prototype.slice.call(document.querySelectorAll(".arc-venue-letter"));
    var towns = Array.prototype.slice.call(document.querySelectorAll(".arc-venue-town")).map(function (town) {
        return { item: town, text: fold(town.textContent) };
    });
    var dots = Array.prototype.slice.call(document.querySelectorAll(".arc-venue-map-dots circle"));

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

    input.addEventListener("input", update);
    box.hidden = false;
}());
