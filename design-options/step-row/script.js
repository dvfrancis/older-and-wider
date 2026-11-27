// Chase light: on load, sweep once along the sixteen keys and settle on the newest.
// Without this script, the newest key is lit by the HTML and CSS alone.
(function () {
  "use strict";

  var row = document.getElementById("step-row");
  if (!row) {
    return;
  }

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) {
    return;
  }

  var keys = row.querySelectorAll(".key");
  var step = 0;
  var interval = 70;

  row.classList.add("is-sweeping");

  function advance() {
    if (step > 0) {
      keys[step - 1].classList.remove("is-lit");
    }
    if (step === keys.length) {
      row.classList.remove("is-sweeping");
      return;
    }
    keys[step].classList.add("is-lit");
    step += 1;
    window.setTimeout(advance, interval);
  }

  window.setTimeout(advance, 300);
})();
