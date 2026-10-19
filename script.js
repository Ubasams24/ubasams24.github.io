(function () {
  var racine = document.documentElement;
  var calme = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Bouton mode sombre (le choix est mémorisé dans le navigateur)
  var btn = document.getElementById("theme");
  if (btn) {
    btn.setAttribute("aria-pressed", racine.dataset.theme === "dark");
    btn.addEventListener("click", function () {
      var t = racine.dataset.theme === "dark" ? "light" : "dark";
      racine.dataset.theme = t;
      btn.setAttribute("aria-pressed", t === "dark");
      try { localStorage.setItem("theme", t); } catch (e) {}
    });
  }

  // Schéma réseau interactif : survol ou clavier = description de l'équipement
  var legende = document.getElementById("legende");
  if (legende) {
    var defaut = legende.textContent;
    document.querySelectorAll(".noeud").forEach(function (n) {
      var montrer = function () { legende.textContent = n.dataset.desc; n.classList.add("actif"); };
      var cacher = function () { legende.textContent = defaut; n.classList.remove("actif"); };
      n.addEventListener("mouseenter", montrer); n.addEventListener("focus", montrer);
      n.addEventListener("mouseleave", cacher); n.addEventListener("blur", cacher);
      n.addEventListener("click", montrer);
    });
  }

  // Apparition douce des blocs au défilement
  if (calme || !("IntersectionObserver" in window)) return;
  var cibles = document.querySelectorAll(".section, .fiche, .carte, .etapes li, .bloc, .table-wrap, .entete-page, .pied");
  cibles.forEach(function (el) {
    el.classList.add("reveal");
    var rang = Array.prototype.indexOf.call(el.parentNode.children, el);
    el.style.transitionDelay = Math.min(rang, 4) * 80 + "ms";
  });
  var obs = new IntersectionObserver(function (entrees) {
    entrees.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add("visible"); obs.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  cibles.forEach(function (el) { obs.observe(el); });
})();
