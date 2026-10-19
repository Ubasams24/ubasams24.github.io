// Fond animé : réseau de nœuds reliés, avec de petits « paquets » qui circulent.
// Sobre par construction : lignes très transparentes, mouvement lent, pause quand l'onglet est caché.
// Si la personne réduit les animations dans son système, le fond reste fixe (une seule image).
(function () {
  var c = document.getElementById("fond");
  if (!c || !c.getContext) return;
  var ctx = c.getContext("2d");
  var calme = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var W, H, dpr, D, noeuds = [], paquets = [], img = 0, raf = 0;
  var souris = { x: -999, y: -999 };
  var rgb = [31, 95, 209], sombre = false;

  function couleur() {
    var s = getComputedStyle(document.documentElement).getPropertyValue("--accent").trim();
    var m = /^#([0-9a-f]{6})$/i.exec(s);
    if (m) { var n = parseInt(m[1], 16); rgb = [(n >> 16) & 255, (n >> 8) & 255, n & 255]; }
    sombre = document.documentElement.dataset.theme === "dark";
  }
  function rgba(a) { return "rgba(" + rgb[0] + "," + rgb[1] + "," + rgb[2] + "," + a + ")"; }

  function init() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = window.innerWidth; H = window.innerHeight;
    c.width = W * dpr; c.height = H * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    D = W < 700 ? 125 : 175;                               // distance maximale d'une liaison
    var n = Math.min(W < 700 ? 40 : 95, Math.round(W * H / 14000));
    noeuds = []; paquets = [];
    for (var i = 0; i < n; i++) {
      noeuds.push({ x: Math.random() * W, y: Math.random() * H,
                    vx: (Math.random() - 0.5) * 0.45, vy: (Math.random() - 0.5) * 0.45 });
    }
  }

  function voisin(i) {                                       // un nœud proche, pour y faire circuler un paquet
    var a = noeuds[i], cand = [];
    for (var j = 0; j < noeuds.length; j++) {
      if (j === i) continue;
      var dx = a.x - noeuds[j].x, dy = a.y - noeuds[j].y;
      if (dx * dx + dy * dy < D * D) cand.push(j);
    }
    return cand.length ? cand[Math.floor(Math.random() * cand.length)] : -1;
  }

  function dessiner(bouger) {
    ctx.clearRect(0, 0, W, H);
    var base = sombre ? 0.5 : 0.42, i, j, a, b, dx, dy, d;

    if (bouger) {
      for (i = 0; i < noeuds.length; i++) {
        a = noeuds[i]; a.x += a.vx; a.y += a.vy;
        if (a.x < -10) a.x = W + 10; else if (a.x > W + 10) a.x = -10;
        if (a.y < -10) a.y = H + 10; else if (a.y > H + 10) a.y = -10;
      }
    }
    ctx.lineWidth = 1.2;
    for (i = 0; i < noeuds.length; i++) {
      a = noeuds[i];
      for (j = i + 1; j < noeuds.length; j++) {
        b = noeuds[j]; dx = a.x - b.x; dy = a.y - b.y; d = Math.sqrt(dx * dx + dy * dy);
        if (d < D) {
          ctx.strokeStyle = rgba((1 - d / D) * base);
          ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
        }
      }
      dx = a.x - souris.x; dy = a.y - souris.y; d = Math.sqrt(dx * dx + dy * dy);   // léger lien vers le curseur
      if (d < 210) {
        ctx.strokeStyle = rgba((1 - d / 210) * 0.6);
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(souris.x, souris.y); ctx.stroke();
      }
      ctx.fillStyle = rgba(sombre ? 0.85 : 0.7);
      ctx.beginPath(); ctx.arc(a.x, a.y, 2.3, 0, 6.2832); ctx.fill();
    }

    if (bouger) {
      if (paquets.length < 9 && Math.random() < 0.04 && noeuds.length) {
        var s = Math.floor(Math.random() * noeuds.length), t = voisin(s);
        if (t >= 0) paquets.push({ a: s, b: t, p: 0, v: 0.008 + Math.random() * 0.008 });
      }
      for (i = paquets.length - 1; i >= 0; i--) {
        var k = paquets[i]; k.p += k.v;
        if (k.p >= 1) { paquets.splice(i, 1); continue; }
        a = noeuds[k.a]; b = noeuds[k.b];
        var x = a.x + (b.x - a.x) * k.p, y = a.y + (b.y - a.y) * k.p;
        ctx.fillStyle = rgba(0.18); ctx.beginPath(); ctx.arc(x, y, 7, 0, 6.2832); ctx.fill();
        ctx.fillStyle = rgba(0.95); ctx.beginPath(); ctx.arc(x, y, 3.2, 0, 6.2832); ctx.fill();
      }
    }
  }

  function boucle() { dessiner(true); raf = requestAnimationFrame(boucle); }
  function demarrer() { if (!raf && !calme) raf = requestAnimationFrame(boucle); }
  function arreter() { if (raf) { cancelAnimationFrame(raf); raf = 0; } }

  couleur(); init();
  if (calme) dessiner(false); else demarrer();

  document.addEventListener("visibilitychange", function () { document.hidden ? arreter() : demarrer(); });
  window.addEventListener("pointermove", function (e) { souris.x = e.clientX; souris.y = e.clientY; }, { passive: true });
  document.addEventListener("pointerleave", function () { souris.x = souris.y = -999; });
  window.addEventListener("resize", function () {
    clearTimeout(img);
    img = setTimeout(function () { init(); if (calme) dessiner(false); }, 200);
  });
  new MutationObserver(function () { couleur(); if (calme) dessiner(false); })
    .observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
})();
