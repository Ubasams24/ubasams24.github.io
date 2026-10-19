# Génère les pages FR (racine) et EN (dossier en/). Tu peux aussi modifier directement les .html.
import os
NOM = "Aboubacar Samassa"
EMAIL = "aboubacar.samassa24@gmail.com"
GITHUB = "https://github.com/Ubasams24"
CV = "cv-aboubacar-samassa.pdf"
SLUGS = ["referentiel","realisations","preuves","synthese","parcours","veille"]

L = {
"fr": dict(
 lang="fr", autre="English", skip="Aller au contenu", theme="Mode sombre", navlabel="Navigation principale",
 nav=["Référentiel","Réalisations","Preuves","Synthèse","Parcours","Veille"],
 ph="Section en cours de rédaction", tbd="À compléter",
 surtitre="Portfolio de preuves — BTS SIO SISR", accroche="BTS SIO SISR — Systèmes, Réseaux & Cybersécurité",
 intro="Étudiant en BTS SIO option SISR à l’IMIE, en alternance chez UBNEST. Ce qui m’attire en réseaux et systèmes : chercher les failles d’un système pour le sécuriser au maximum.",
 statut="Statut : alternance chez UBNEST (contrat en cours de signature).",
 question="Quelles compétences du référentiel puis-je démontrer, par quelles réalisations, et avec quelles preuves ?",
 b1="Explorer le référentiel", b2="Voir les réalisations",
 schema_aria="Schéma réseau interactif", schema_def="Survole ou sélectionne un équipement pour voir son rôle.",
 nodes=[("Internet","Internet : le réseau public, d’où arrivent les flux entrants."),
        ("Pare-feu","Pare-feu : filtre le trafic et protège le réseau interne."),
        ("Switch","Switch : relie entre elles les machines du réseau local."),
        ("Serveur","Serveur : héberge les services (annuaire, fichiers, web…)."),
        ("PC 1","Poste client : l’utilisateur accède aux services du réseau."),
        ("PC 2","Poste client : un autre utilisateur du même réseau local.")],
 cov_s="État du référentiel", cov_h="Couverture des compétences", cov_l="0 / 57 sous-compétences travaillées",
 ep=[("E5","Support et mise à disposition de services informatiques",22),
     ("E6","Administration des systèmes et des réseaux",17),
     ("E7","Cybersécurité des services informatiques",18)],
 ep_petit="0 réalisation · {n} sous-compétences", cov_lien="Tableau de synthèse détaillé",
 etp_s="Comment lire ce portfolio", etp_h="Du référentiel à la preuve",
 etp_l="Chaque compétence affichée renvoie aux réalisations qui la mobilisent et aux preuves qui la justifient.",
 etapes=[("Référentiel","Les épreuves E5, E6 et E7 et leurs compétences officielles."),
         ("Compétence","Chaque sous-compétence, avec son statut de maîtrise."),
         ("Réalisation","Les projets et expériences qui mobilisent la compétence."),
         ("Preuve","Captures, schémas, configurations et documents à l’appui.")],
 pr_s="Réalisations principales", pr_h="Projets au cœur du portfolio", pr_lien="Toutes les réalisations",
 pr_titre="Projet principal — à venir", pr_tags=("Réseau","Système","Sécurité"),
 bref_s="En bref", bref_h="Formation, alternance et projets personnels", b3="Mon parcours", b4="Mes preuves",
 fiche_champs=["Contexte","Besoin","Actions menées","Technologies utilisées","Résultats / Livrables"],
 pied_sub="BTS SIO — option SISR · Portfolio de preuves", pied_nav="Navigation", pied_contact="Contact",
 copy="© 2026 " + NOM + " · hébergé sur GitHub Pages",
 titres=["Référentiel de compétences","Réalisations","Preuves","Tableau de synthèse","Parcours et formation","Veille technologique"],
 ref_l="Chaque compétence renverra vers les réalisations qui la mobilisent et vers les preuves à l’appui.",
 ref_e=["E5 — Support et mise à disposition de services informatiques","E6 — Administration des systèmes et des réseaux","E7 — Cybersécurité des services informatiques"],
 real_l="Chaque projet suit la même fiche : contexte, besoin, actions, technologies, résultats.",
 real_g=["Projets réalisés en formation","Réalisations en milieu professionnel","Projets personnels ou associatifs"],
 real_t=["Projet 1 — à venir","Mission 1 — à venir","Projet perso 1 — à venir"],
 prv_l="Captures d’écran, schémas, configurations, documents et attestations rattachés aux réalisations.",
 prv_b=["Captures et schémas","Configurations et documentation","Attestations et comptes-rendus"],
 syn_l="Récapitulatif des compétences du référentiel.", syn_th=["Compétence","Réalisation(s)","Preuve(s)","Statut"],
 syn_btn="Télécharger le tableau (PDF à ajouter)",
 par_b=["Cursus scolaire","Expériences","Compétences et langues"],
 par_c=["<ul><li><strong>BTS SIO option SISR</strong> — IMIE, depuis 2026</li><li><strong>Baccalauréat STI2D</strong> — Lycée Condorcet, Montreuil, 2026</li><li><strong>BAFA, phase 1</strong> — CEMEA, Aubervilliers, octobre 2023</li></ul>",
        "<ul><li><strong>Alternance chez UBNEST</strong> — contrat en cours de signature. Missions : à compléter.</li><li><strong>Entraîneur adjoint</strong> — Association Ensemble (basketball), Bagnolet, depuis septembre 2025. Planification et animation des séances d’entraînement avec le coach principal, remplacement lors des matchs en cas d’indisponibilité.</li><li><strong>Stage de seconde</strong> — ORIZONS, Paris, 2024. Visite de site avec un cofondateur : collecte et saisie des données techniques d’un bâtiment (inventaire des équipements) dans l’application d’audit assistée par IA, prise de notes en réunion.</li></ul>",
        "<ul><li><strong>Informatique :</strong> HTML, CSS, Python, Processing, Pack Office</li><li><strong>Langues :</strong> français et soninké (langues maternelles), espagnol B2, anglais B2</li><li><strong>Atouts :</strong> écoute active, persévérance, adaptation, autonomie, sens des responsabilités</li></ul>"],
 cv_btn="Télécharger mon CV",
 vei_b=["Sujet de veille choisi","Outils de veille utilisés","Synthèses et fiches de lecture"],
 vei_outils="<ul><li>Google Alerts : alertes sur mes mots-clés</li><li>TLDR : newsletter de veille technologique</li></ul>",
),
"en": dict(
 lang="en", autre="Français", skip="Skip to content", theme="Dark mode", navlabel="Main navigation",
 nav=["Framework","Projects","Evidence","Summary","Background","Tech watch"],
 ph="Section being written", tbd="To be completed",
 surtitre="Evidence portfolio — BTS SIO SISR", accroche="BTS SIO SISR — Systems, Networks & Cybersecurity",
 intro="BTS SIO SISR student at IMIE, on a work-study placement at UBNEST. What draws me to networks and systems: hunting for weaknesses in a system so I can secure it as much as possible.",
 statut="Status: work-study placement at UBNEST (contract being signed).",
 question="Which skills from the framework can I demonstrate, through which projects, and with what evidence?",
 b1="Explore the framework", b2="See the projects",
 schema_aria="Interactive network diagram", schema_def="Hover over or select a device to see its role.",
 nodes=[("Internet","Internet: the public network, where incoming traffic comes from."),
        ("Firewall","Firewall: filters traffic and protects the internal network."),
        ("Switch","Switch: connects the machines of the local network together."),
        ("Server","Server: hosts services (directory, files, web…)."),
        ("PC 1","Client workstation: a user reaching the network’s services."),
        ("PC 2","Client workstation: another user on the same local network.")],
 cov_s="Framework status", cov_h="Skills coverage", cov_l="0 / 57 sub-skills covered",
 ep=[("E5","IT service support and delivery",22),("E6","Systems and network administration",17),
     ("E7","IT services cybersecurity",18)],
 ep_petit="0 project · {n} sub-skills", cov_lien="Detailed summary table",
 etp_s="How to read this portfolio", etp_h="From framework to evidence",
 etp_l="Every skill shown links to the projects that use it and the evidence that backs it up.",
 etapes=[("Framework","The E5, E6 and E7 exams and their official skills."),
         ("Skill","Each sub-skill, with its mastery status."),
         ("Project","The projects and experiences that use the skill."),
         ("Evidence","Screenshots, diagrams, configurations and documents.")],
 pr_s="Main projects", pr_h="Projects at the heart of the portfolio", pr_lien="All projects",
 pr_titre="Main project — coming soon", pr_tags=("Network","Systems","Security"),
 bref_s="At a glance", bref_h="Training, work-study and personal projects", b3="My background", b4="My evidence",
 fiche_champs=["Context","Need","Actions taken","Technologies used","Results / Deliverables"],
 pied_sub="BTS SIO — SISR option · Evidence portfolio", pied_nav="Navigation", pied_contact="Contact",
 copy="© 2026 " + NOM + " · hosted on GitHub Pages",
 titres=["Skills framework","Projects","Evidence","Summary table","Background and training","Technology watch"],
 ref_l="Each skill will link to the projects that use it and to the supporting evidence.",
 ref_e=["E5 — IT service support and delivery","E6 — Systems and network administration","E7 — IT services cybersecurity"],
 real_l="Every project follows the same sheet: context, need, actions, technologies, results.",
 real_g=["Projects carried out during training","Work-based projects","Personal or community projects"],
 real_t=["Project 1 — coming soon","Assignment 1 — coming soon","Personal project 1 — coming soon"],
 prv_l="Screenshots, diagrams, configurations, documents and certificates attached to the projects.",
 prv_b=["Screenshots and diagrams","Configurations and documentation","Certificates and reports"],
 syn_l="Overview of the framework’s skills.", syn_th=["Skill","Project(s)","Evidence","Status"],
 syn_btn="Download the table (PDF to be added)",
 par_b=["Education","Experience","Skills and languages"],
 par_c=["<ul><li><strong>BTS SIO, SISR option</strong> — IMIE, since 2026</li><li><strong>STI2D baccalaureate</strong> — Lycée Condorcet, Montreuil, 2026</li><li><strong>BAFA, phase 1</strong> (youth activity leader certificate) — CEMEA, Aubervilliers, October 2023</li></ul>",
        "<ul><li><strong>Work-study placement at UBNEST</strong> — contract being signed. Assignments: to be completed.</li><li><strong>Assistant coach</strong> — Association Ensemble (basketball), Bagnolet, since September 2025. Planning and running training sessions with the head coach, standing in for them during matches when needed.</li><li><strong>Year 10 internship</strong> — ORIZONS, Paris, 2024. Site visit with a co-founder: collecting and entering a building’s technical data (equipment inventory) in the AI-assisted audit application, taking notes in meetings.</li></ul>",
        "<ul><li><strong>IT:</strong> HTML, CSS, Python, Processing, Microsoft Office</li><li><strong>Languages:</strong> French and Soninke (native), Spanish B2, English B2</li><li><strong>Strengths:</strong> active listening, perseverance, adaptability, autonomy, sense of responsibility</li></ul>"],
 cv_btn="Download my CV",
 vei_b=["Chosen watch topic","Watch tools used","Summaries and reading notes"],
 vei_outils="<ul><li>Google Alerts: alerts on my keywords</li><li>TLDR: tech watch newsletter</li></ul>",
),
}

def fiche(t, titre, tags):
    lignes = "".join(f"<dt>{c}</dt><dd>{t['tbd']}</dd>" for c in t["fiche_champs"])
    pastilles = "".join(f'<span class="tag">{x}</span>' for x in tags)
    return f'<article class="fiche"><div class="tags">{pastilles}</div><h3>{titre}</h3><dl>{lignes}</dl></article>'

def block(titre, texte, id_=""):
    i = f' id="{id_}"' if id_ else ""
    return f'<section class="bloc"{i}><h2>{titre}</h2>{texte}</section>'

def schema(t):
    # (cx, cy) de chaque équipement : Internet, pare-feu, switch, serveur, PC1, PC2
    pos = [(210,32),(210,100),(210,168),(80,250),(210,250),(340,250)]
    liens = [((210,52),(210,80)),((210,120),(210,148)),((210,188),(80,230)),((210,188),(210,230)),((210,188),(340,230))]
    traits = "".join(f'<line class="lien" x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}"/>' for a,b in liens)
    noeuds = ""
    for (cx,cy),(nom,desc) in zip(pos, t["nodes"]):
        noeuds += (f'<g class="noeud" tabindex="0" role="button" aria-label="{desc}" data-desc="{desc}">'
                   f'<rect x="{cx-44}" y="{cy-20}" width="88" height="40" rx="8"/><text x="{cx}" y="{cy}">{nom}</text></g>')
    return (f'<figure class="schema"><svg viewBox="0 0 420 285" role="group" aria-label="{t["schema_aria"]}">{traits}{noeuds}</svg>'
            f'<figcaption id="legende" aria-live="polite">{t["schema_def"]}</figcaption></figure>')

def accueil(t):
    alt_photo = "Portrait d’Aboubacar Samassa" if t["lang"] == "fr" else "Portrait of Aboubacar Samassa"
    cartes = "".join(f"""<a class="carte" href="referentiel.html#{c.lower()}">
      <div class="carte-tete"><strong>{c}</strong><span class="pct">0 %</span></div><p class="carte-titre">{ti}</p>
      <div class="barre" role="img" aria-label="{c} : 0 %"><i style="width:0%"></i></div>
      <p class="petit">{t['ep_petit'].format(n=n)}</p></a>""" for c,ti,n in t["ep"])
    etapes = "".join(f"<li><strong>{a}</strong><span>{b}</span></li>" for a,b in t["etapes"])
    return f"""
<section class="hero">
  <div class="hero-texte">
    <div class="identite">
      <img class="portrait" src="photo.png" width="480" height="480" alt="{alt_photo}">
      <div><p class="surtitre">{t['surtitre']}</p><h1>{NOM}</h1><p class="accroche">{t['accroche']}</p></div>
    </div>
    <p class="intro">{t['intro']}</p>
    <p class="statut">{t['statut']}</p>
    <blockquote>{t['question']}</blockquote>
    <p class="actions"><a class="bouton" href="referentiel.html">{t['b1']}</a> <a class="bouton clair" href="realisations.html">{t['b2']}</a></p>
  </div>
  {schema(t)}
</section>
<section class="section" id="couverture"><p class="surtitre">{t['cov_s']}</p><h2>{t['cov_h']}</h2>
  <p class="lead">{t['cov_l']}</p><div class="cartes">{cartes}</div>
  <p><a class="lien-fort" href="synthese.html">{t['cov_lien']}</a></p></section>
<section class="section"><p class="surtitre">{t['etp_s']}</p><h2>{t['etp_h']}</h2>
  <p class="lead">{t['etp_l']}</p><ol class="etapes">{etapes}</ol></section>
<section class="section"><p class="surtitre">{t['pr_s']}</p>
  <div class="entete-ligne"><h2>{t['pr_h']}</h2><a class="lien-fort" href="realisations.html">{t['pr_lien']}</a></div>
  {fiche(t, t['pr_titre'], t['pr_tags'])}</section>
<section class="section"><p class="surtitre">{t['bref_s']}</p><h2>{t['bref_h']}</h2>
  <p class="placeholder">{t['ph']}</p>
  <p class="actions"><a class="bouton" href="parcours.html">{t['b3']}</a> <a class="bouton clair" href="preuves.html">{t['b4']}</a></p></section>
"""

def interne(t, slug):
    i = SLUGS.index(slug); titre = t["titres"][i]; ph = f'<p class="placeholder">{t["ph"]}</p>'
    intro, corps = "", ""
    if slug == "referentiel":
        intro = t["ref_l"]
        corps = "".join(block(x, ph, c) for x, c in zip(t["ref_e"], ["e5","e6","e7"]))
    elif slug == "realisations":
        intro = t["real_l"]
        corps = "".join(f"<h2>{g}</h2>{fiche(t, ti, ('—',))}" for g, ti in zip(t["real_g"], t["real_t"]))
    elif slug == "preuves":
        intro = t["prv_l"]; corps = "".join(block(x, ph) for x in t["prv_b"])
    elif slug == "synthese":
        intro = t["syn_l"]; tbd = t["tbd"]
        th = "".join(f"<th>{x}</th>" for x in t["syn_th"]); td = f"<td>{tbd}</td>" * 4
        corps = f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody><tr>{td}</tr></tbody></table></div><p><a class="bouton" href="#">{t["syn_btn"]}</a></p>'
    elif slug == "parcours":
        corps = block(t["par_b"][0], t["par_c"][0]) + block(t["par_b"][1], t["par_c"][1]) + block(t["par_b"][2], t["par_c"][2]) + f'<p><a class="bouton" href="{CV}" download>{t["cv_btn"]}</a></p>'
    elif slug == "veille":
        corps = block(t["vei_b"][0], ph) + block(t["vei_b"][1], t["vei_outils"]) + block(t["vei_b"][2], ph)
    lead = f'<p class="lead">{intro}</p>' if intro else ""
    return f'<section class="entete-page"><h1>{titre}</h1>{lead}</section><div class="contenu">{corps}</div>'

def page(slug, lang):
    t = L[lang]; en = lang == "en"; pre = ""
    nav = "".join(f'<li><a href="{s}.html"{" aria-current=\"page\"" if s==slug else ""}>{l}</a></li>' for s,l in zip(SLUGS, t["nav"]))
    fichier = "index" if slug == "index" else slug
    autre = "@@AUTRE@@"
    corps = accueil(t) if slug == "index" else interne(t, slug)
    titre = f"{NOM} — Portfolio BTS SIO SISR" if slug == "index" else f"{t['titres'][SLUGS.index(slug)]} — {NOM}"
    pied_nav = "".join(f'<li><a href="{s}.html">{l}</a></li>' for s,l in zip(SLUGS, t["nav"]))
    lang_fr = '<a href="@@AUTRE@@" lang="fr" hreflang="fr" title="Français">FR</a>' if en else '<span aria-current="true" title="Français">FR</span>'
    lang_en = '<span aria-current="true" title="English">EN</span>' if en else '<a href="@@AUTRE@@" lang="en" hreflang="en" title="English">EN</a>'
    return f"""<!DOCTYPE html>
<html lang="{lang}" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{t['surtitre']} · {NOM}">
<script>(function(){{var d=document.documentElement;d.classList.add("js");try{{var s=localStorage.getItem("theme");d.dataset.theme=s||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light")}}catch(e){{}}}})()</script>
<link rel="stylesheet" href="style.css?v=3">
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
<header class="topbar">
  <a class="marque" href="index.html">{NOM} <span>BTS SIO SISR</span></a>
  <nav aria-label="{t['navlabel']}"><ul>{nav}</ul></nav>
  <div class="outils"><div class="langues" role="group" aria-label="Langue / Language">{lang_fr}{lang_en}</div>
  <button class="outil" id="theme" type="button" aria-pressed="false">{t['theme']}</button></div>
</header>
<main id="main">{corps}</main>
<footer class="pied">
  <div><strong>{NOM}</strong><p>{t['pied_sub']}</p></div>
  <div><strong>{t['pied_nav']}</strong><ul>{pied_nav}</ul></div>
  <div><strong>{t['pied_contact']}</strong><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{GITHUB}">GitHub</a></li></ul></div>
  <p class="copy">{t['copy']}</p>
</footer>
<script src="script.js?v=3"></script>
</body>
</html>
"""

import re
for lang in ("fr","en"):
    for slug in ["index"] + SLUGS:
        html = page(slug, lang)
        if lang == "en":
            html = re.sub(r'href="(index|referentiel|realisations|preuves|synthese|parcours|veille)\.html', r'href="\1-en.html', html)
            html = html.replace("@@AUTRE@@", f"{slug}.html")
            nom = f"{slug}-en.html"
        else:
            html = html.replace("@@AUTRE@@", f"{slug}-en.html")
            nom = f"{slug}.html"
        open(nom, "w", encoding="utf-8").write(html)
print("OK")
