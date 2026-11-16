# Données du portfolio : référentiel, réalisations, preuves, veille.
# Chaque texte est un couple (français, anglais).
# Pour ajouter une réalisation : copier un bloc de REALISATIONS, changer l'id,
# remplir les champs, et lister les sous-compétences mobilisées dans "comps".

REFERENTIEL = [
 ("e5", "E5", ("Bloc 1", "Block 1"), ("Support et mise à disposition de services informatiques", "IT service support and delivery"), [
  ("B1.1", ("Gérer le patrimoine informatique", "Manage IT assets"), [
   ("Recenser et identifier les ressources numériques", "Inventory and identify digital resources"),
   ("Exploiter des référentiels, normes et standards adoptés par le prestataire informatique", "Use the frameworks, norms and standards adopted by the IT provider"),
   ("Mettre en place et vérifier les niveaux d’habilitation associés à un service", "Set up and check the authorisation levels for a service"),
   ("Vérifier les conditions de la continuité d’un service informatique", "Check the conditions for IT service continuity"),
   ("Gérer des sauvegardes", "Manage backups"),
   ("Vérifier le respect des règles d’utilisation des ressources numériques", "Check that the rules for using digital resources are followed")]),
  ("B1.2", ("Répondre aux incidents et aux demandes d’assistance et d’évolution", "Handle incidents and support or change requests"), [
   ("Collecter, suivre et orienter des demandes", "Collect, track and route requests"),
   ("Traiter des demandes concernant les services réseau et système, applicatifs", "Handle requests about network, system and application services"),
   ("Traiter des demandes concernant les applications", "Handle requests about applications")]),
  ("B1.3", ("Développer la présence en ligne de l’organisation", "Develop the organisation’s online presence"), [
   ("Participer à la valorisation de l’image de l’organisation sur les médias numériques en tenant compte du cadre juridique et des enjeux économiques", "Help promote the organisation’s image on digital media, taking legal and economic issues into account"),
   ("Référencer les services en ligne de l’organisation et mesurer leur visibilité", "Get the organisation’s online services listed and measure their visibility"),
   ("Participer à l’évolution d’un site Web exploitant les données de l’organisation", "Contribute to a website that uses the organisation’s data")]),
  ("B1.4", ("Travailler en mode projet", "Work in project mode"), [
   ("Analyser les objectifs et les modalités d’organisation d’un projet", "Analyse a project’s objectives and organisation"),
   ("Planifier les activités", "Plan activities"),
   ("Évaluer les indicateurs de suivi d’un projet et analyser les écarts", "Evaluate project tracking indicators and analyse gaps")]),
  ("B1.5", ("Mettre à disposition des utilisateurs un service informatique", "Make an IT service available to users"), [
   ("Réaliser les tests d’intégration et d’acceptation d’un service", "Run integration and acceptance tests for a service"),
   ("Déployer un service", "Deploy a service"),
   ("Accompagner les utilisateurs dans la mise en place d’un service", "Support users when a service is introduced")]),
  ("B1.6", ("Organiser son développement professionnel", "Manage one’s professional development"), [
   ("Mettre en place son environnement d’apprentissage personnel", "Set up one’s personal learning environment"),
   ("Mettre en œuvre des outils et stratégies de veille informationnelle", "Use information-watch tools and strategies"),
   ("Gérer son identité professionnelle", "Manage one’s professional identity"),
   ("Développer son projet professionnel", "Develop one’s career plan")]),
 ]),
 ("e6", "E6", ("Bloc 2", "Block 2"), ("Administration des systèmes et des réseaux", "Systems and network administration"), [
  ("B2.1", ("Concevoir une solution d’infrastructure réseau", "Design a network infrastructure solution"), [
   ("Analyser un besoin exprimé et son contexte juridique", "Analyse a stated need and its legal context"),
   ("Étudier l’impact d’une évolution d’un élément d’infrastructure sur le système informatique", "Study the impact of changing an infrastructure component on the IT system"),
   ("Élaborer un dossier de choix d’une solution d’infrastructure et rédiger les spécifications techniques", "Build a solution-selection file and write the technical specifications"),
   ("Choisir les éléments nécessaires pour assurer la qualité et la disponibilité d’un service", "Choose the components needed for service quality and availability"),
   ("Maquetter et prototyper une solution d’infrastructure permettant d’atteindre la qualité de service attendue", "Model and prototype an infrastructure solution that meets the expected quality of service"),
   ("Déterminer et préparer les tests nécessaires à la validation de la solution d’infrastructure retenue", "Define and prepare the tests needed to validate the chosen solution")]),
  ("B2.2", ("Installer, tester et déployer une solution d’infrastructure réseau", "Install, test and deploy a network infrastructure solution"), [
   ("Installer et configurer des éléments d’infrastructure", "Install and configure infrastructure components"),
   ("Installer et configurer des éléments nécessaires pour assurer la continuité des services", "Install and configure components for service continuity"),
   ("Installer et configurer des éléments nécessaires pour assurer la qualité de service", "Install and configure components for quality of service"),
   ("Rédiger ou mettre à jour la documentation technique et utilisateur d’une solution d’infrastructure", "Write or update the technical and user documentation of a solution"),
   ("Tester l’intégration et l’acceptation d’une solution d’infrastructure", "Test the integration and acceptance of an infrastructure solution"),
   ("Déployer une solution d’infrastructure", "Deploy an infrastructure solution")]),
  ("B2.3", ("Exploiter, dépanner et superviser une solution d’infrastructure réseau", "Operate, troubleshoot and monitor a network infrastructure solution"), [
   ("Administrer sur site et à distance des éléments d’une infrastructure", "Administer infrastructure components on site and remotely"),
   ("Automatiser des tâches d’administration", "Automate administration tasks"),
   ("Gérer des indicateurs et des fichiers d’activité des éléments d’une infrastructure", "Manage indicators and activity logs of infrastructure components"),
   ("Identifier, qualifier, évaluer et réagir face à un incident ou à un problème", "Identify, qualify, assess and respond to an incident or problem"),
   ("Évaluer, maintenir et améliorer la qualité d’un service", "Assess, maintain and improve service quality")]),
 ]),
 ("e7", "E7", ("Bloc 3", "Block 3"), ("Cybersécurité des services informatiques", "IT services cybersecurity"), [
  ("B3.1", ("Protéger les données à caractère personnel", "Protect personal data"), [
   ("Recenser les traitements sur les données à caractère personnel au sein de l’organisation", "List the processing of personal data within the organisation"),
   ("Identifier les risques liés à la collecte, au traitement, au stockage et à la diffusion des données à caractère personnel", "Identify the risks of collecting, processing, storing and sharing personal data"),
   ("Appliquer la réglementation en matière de collecte, de traitement et de conservation des données à caractère personnel", "Apply the rules on collecting, processing and keeping personal data"),
   ("Sensibiliser les utilisateurs à la protection des données à caractère personnel", "Raise users’ awareness of personal data protection")]),
  ("B3.2", ("Préserver l’identité numérique de l’organisation", "Preserve the organisation’s digital identity"), [
   ("Protéger l’identité numérique d’une organisation", "Protect an organisation’s digital identity"),
   ("Déployer les moyens appropriés de preuve électronique", "Deploy appropriate means of electronic proof")]),
  ("B3.3", ("Sécuriser les équipements et les usages des utilisateurs", "Secure user equipment and practices"), [
   ("Informer les utilisateurs sur les risques associés à l’utilisation d’une ressource numérique et promouvoir les bons usages à adopter", "Inform users about the risks of a digital resource and promote good practice"),
   ("Identifier les menaces et mettre en œuvre les défenses appropriées", "Identify threats and put appropriate defences in place"),
   ("Gérer les accès et les privilèges appropriés", "Manage appropriate access and privileges"),
   ("Vérifier l’efficacité de la protection", "Check that protection is effective")]),
  ("B3.4", ("Garantir la disponibilité, l’intégrité et la confidentialité des services informatiques et des données de l’organisation face à des cyberattaques", "Ensure the availability, integrity and confidentiality of IT services and data against cyberattacks"), [
   ("Caractériser les risques liés à l’utilisation malveillante d’un service informatique", "Characterise the risks of malicious use of an IT service"),
   ("Recenser les conséquences d’une perte de disponibilité, d’intégrité ou de confidentialité", "List the consequences of a loss of availability, integrity or confidentiality"),
   ("Identifier les obligations légales qui s’imposent en matière d’archivage et de protection des données de l’organisation", "Identify the legal obligations for archiving and protecting the organisation’s data"),
   ("Organiser la collecte et la conservation des preuves numériques", "Organise the collection and preservation of digital evidence"),
   ("Appliquer les procédures garantissant le respect des obligations légales", "Apply procedures that ensure legal obligations are met")]),
  ("B3.5", ("Cybersécuriser une infrastructure réseau, un système, un service", "Secure a network infrastructure, a system or a service"), [
   ("Participer à la vérification des éléments contribuant à la sûreté d’une infrastructure informatique", "Help check the components that make an IT infrastructure safe"),
   ("Prendre en compte la sécurité dans un projet de mise en œuvre d’une solution d’infrastructure", "Take security into account when implementing an infrastructure solution"),
   ("Mettre en œuvre et vérifier la conformité d’une infrastructure à un référentiel, une norme ou un standard de sécurité", "Implement and check an infrastructure’s compliance with a security framework, norm or standard"),
   ("Prévenir les attaques", "Prevent attacks"),
   ("Détecter les actions malveillantes", "Detect malicious actions"),
   ("Analyser les incidents de sécurité, proposer et mettre en œuvre des contre-mesures", "Analyse security incidents, propose and apply countermeasures")]),
 ]),
]

# Groupes : "formation", "pro", "perso"
REALISATIONS = [
 dict(id="tp-vlan", groupe="formation", tags=(("Réseau","Network"),("Cisco","Cisco"),("Packet Tracer","Packet Tracer")),
  titre=("Maquette d’un réseau segmenté en VLAN avec routage inter-VLAN", "Model of a VLAN-segmented network with inter-VLAN routing"),
  resume=("TP Packet Tracer : création de VLAN, liens trunk et routage entre VLAN.", "Packet Tracer lab: creating VLANs, trunk links and routing between VLANs."),
  champs=[
   ("TP de première année de BTS SIO SISR à l’IMIE, réalisé sur simulateur.", "First-year BTS SIO SISR lab at IMIE, done in a simulator."),
   ("Séparer les flux de plusieurs services d’une organisation sur un même réseau local, tout en leur permettant de communiquer de façon contrôlée.", "Separate the traffic of several departments on one local network, while still letting them communicate in a controlled way."),
   ("Création des VLAN sur les switchs, affectation des ports en mode accès, configuration d’un lien trunk (802.1Q), mise en place du routage inter-VLAN, adressage IP des postes, tests de connectivité (ping) entre VLAN.", "Created VLANs on the switches, assigned access ports, configured an 802.1Q trunk link, set up inter-VLAN routing, addressed the hosts, tested connectivity (ping) between VLANs."),
   ("Cisco Packet Tracer, Cisco IOS (ligne de commande), VLAN 802.1Q, adressage IPv4.", "Cisco Packet Tracer, Cisco IOS (command line), 802.1Q VLANs, IPv4 addressing."),
   ("Maquette fonctionnelle : chaque VLAN est isolé et les échanges entre VLAN passent par le routage.", "Working model: each VLAN is isolated and traffic between VLANs goes through routing.")],
  comps=["B2.1.5", "B2.2.1", "B2.2.5"]),
 dict(id="tp-linux", groupe="formation", tags=(("Système","Systems"),("Linux","Linux")),
  titre=("Installation et administration d’un serveur Linux (Debian)", "Installing and administering a Linux server (Debian)"),
  resume=("TP Linux : installation, configuration réseau, utilisateurs et droits en ligne de commande.", "Linux lab: installation, network setup, users and permissions from the command line."),
  champs=[
   ("TP de première année de BTS SIO SISR à l’IMIE, en machine virtuelle.", "First-year BTS SIO SISR lab at IMIE, in a virtual machine."),
   ("Disposer d’un serveur Linux opérationnel, joignable sur le réseau et administrable en ligne de commande.", "Have a working Linux server, reachable on the network and managed from the command line."),
   ("Installation de Debian, configuration de l’interface réseau, mise à jour et installation de paquets, création d’utilisateurs et de groupes, gestion des droits sur les fichiers.", "Installed Debian, configured the network interface, updated and installed packages, created users and groups, managed file permissions."),
   ("Debian / Ubuntu, virtualisation, shell Bash, apt.", "Debian / Ubuntu, virtualisation, Bash shell, apt."),
   ("Serveur fonctionnel et accès des utilisateurs limités à ce dont ils ont besoin.", "Working server, with each user’s access limited to what they need.")],
  comps=["B2.2.1", "B2.3.1", "B3.3.3"]),
 dict(id="tp-glpi", groupe="formation", tags=(("Support","Support"),("GLPI","GLPI")),
  titre=("Gestion de parc et suivi des incidents avec GLPI", "IT asset management and incident tracking with GLPI"),
  resume=("TP GLPI : inventaire des équipements et suivi des demandes par tickets.", "GLPI lab: equipment inventory and ticket-based request tracking."),
  champs=[
   ("TP de première année de BTS SIO SISR à l’IMIE.", "First-year BTS SIO SISR lab at IMIE."),
   ("Connaître précisément le matériel d’une organisation et suivre les demandes des utilisateurs jusqu’à leur résolution.", "Know exactly what equipment an organisation has and follow user requests through to resolution."),
   ("Inventaire des équipements (postes, périphériques, matériel réseau) dans GLPI, création, catégorisation et priorisation de tickets, suivi jusqu’à la clôture.", "Inventoried equipment (computers, peripherals, network devices) in GLPI, created, categorised and prioritised tickets, followed them until closed."),
   ("GLPI (gestion de parc et service d’assistance).", "GLPI (asset management and help desk)."),
   ("Parc inventorié et demandes tracées de bout en bout.", "Assets inventoried and requests tracked end to end.")],
  comps=["B1.1.1", "B1.2.1", "B1.2.2"]),
 dict(id="ubnest", groupe="pro", tags=(("Alternance","Work-study"),("Cisco / Meraki","Cisco / Meraki")),
  titre=("Missions de technicien réseau chez UBNEST — à venir", "Network technician assignments at UBNEST — coming soon"),
  resume=("Missions en entreprise : à compléter dès le début de l’alternance.", "Work assignments: to be filled in once the work-study placement starts."),
  champs=[
   ("Alternance chez UBNEST (Les Lilas), PME d’une dizaine de salariés qui conçoit et maintient des réseaux Cisco et Meraki pour des PME et entreprises.", "Work-study at UBNEST (Les Lilas), a company of about ten people that designs and maintains Cisco and Meraki networks for businesses."),
   ("À compléter au fil des missions.", "To be completed as assignments come in."),
   ("Prévu : installation, configuration et dépannage d’équipements réseau chez les clients.", "Planned: installing, configuring and troubleshooting network equipment at client sites."),
   ("Cisco, Cisco Meraki (gestion depuis le cloud).", "Cisco, Cisco Meraki (cloud-managed)."),
   ("À compléter.", "To be completed.")],
  comps=[]),
 dict(id="portfolio", groupe="perso", tags=(("Web","Web"),("Git","Git"),("Déploiement","Deployment")),
  titre=("Conception et mise en ligne de mon portfolio", "Designing and publishing my portfolio"),
  resume=("Ce site : HTML, CSS, JavaScript, version bilingue générée en Python, publié sur GitHub Pages.", "This website: HTML, CSS, JavaScript, bilingual pages generated with Python, published on GitHub Pages."),
  champs=[
   ("Portfolio demandé pour l’épreuve E5 du BTS SIO, sur le modèle fourni par mon professeur.", "Portfolio required for the BTS SIO E5 exam, based on a model provided by my teacher."),
   ("Présenter mes compétences, mes réalisations et mes preuves dans un site accessible en ligne, en français et en anglais.", "Present my skills, projects and evidence on a website available online, in French and English."),
   ("Création du dépôt GitHub, découpage en sept pages, mise en page en HTML et CSS, mode sombre et schéma réseau interactif en JavaScript, génération des pages FR et EN avec un script Python, publication sur GitHub Pages, ajout du contenu page par page.", "Created the GitHub repository, split the site into seven pages, built the layout in HTML and CSS, added dark mode and an interactive network diagram in JavaScript, generated the FR and EN pages with a Python script, published on GitHub Pages, added content page by page."),
   ("HTML5, CSS3, JavaScript, Python, Git, GitHub, GitHub Pages.", "HTML5, CSS3, JavaScript, Python, Git, GitHub, GitHub Pages."),
   ("Site en ligne sur ubasams24.github.io, code source public sur GitHub.", "Site live at ubasams24.github.io, public source code on GitHub.")],
  comps=["B1.4.2", "B1.5.2", "B1.6.1", "B1.6.3"]),
 dict(id="circuit-court", groupe="perso", tags=(("Web","Web"),("PHP","PHP"),("MySQL","MySQL")),
  titre=("Plateforme de vente en circuit court (click & collect)", "Short-supply-chain sales platform (click & collect)"),
  resume=("Projet de groupe : ma partie, l’envoi d’e-mails et la génération de codes en PHP/MySQL.", "Group project: my part was sending emails and generating codes in PHP/MySQL."),
  champs=[
   ("Projet de groupe : une plateforme qui met en relation des agriculteurs et des acheteurs, avec commande en ligne et retrait sur place.", "Group project: a platform connecting farmers and buyers, with online ordering and in-person collection."),
   ("Informer automatiquement les utilisateurs et sécuriser le retrait des commandes.", "Inform users automatically and secure order collection."),
   ("Ma partie : développement du système d’envoi d’e-mails et de génération de codes, relié à la base de données.", "My part: developing the email-sending and code-generation system, connected to the database."),
   ("PHP, MySQL, HTML, CSS.", "PHP, MySQL, HTML, CSS."),
   ("E-mails envoyés automatiquement et codes générés à partir des données de la plateforme.", "Emails sent automatically and codes generated from the platform’s data.")],
  comps=["B1.3.3", "B1.4.1"]),
]

# Sous-compétences travaillées ailleurs que dans une fiche (page Veille)
AUTRES = {"B1.6.2": [("veille", ("Veille technologique", "Technology watch"), "veille.html")]}

DEPOT = "https://github.com/Ubasams24/ubasams24.github.io"
# Preuves : (texte FR, texte EN, lien ou None si à ajouter)
PREUVES = {
 "tp-vlan": [("Schéma de la topologie (capture Packet Tracer)", "Topology diagram (Packet Tracer screenshot)", None),
             ("Fichier de la maquette (.pkt)", "Model file (.pkt)", None),
             ("Résultat de « show vlan brief » et tests de ping entre VLAN", "Output of “show vlan brief” and ping tests between VLANs", None)],
 "tp-linux": [("Captures de l’installation et de la configuration réseau", "Screenshots of the installation and network setup", None),
              ("Commandes de gestion des utilisateurs et des droits", "User and permission management commands", None)],
 "tp-glpi": [("Capture de l’inventaire du parc", "Screenshot of the asset inventory", None),
             ("Exemple de ticket traité, de l’ouverture à la clôture", "Example ticket, from opening to closing", None)],
 "ubnest": [("Comptes-rendus de missions et attestation de l’entreprise", "Assignment reports and company certificate", None)],
 "portfolio": [("Site en ligne", "Live website", "https://ubasams24.github.io"),
               ("Code source du site (dépôt GitHub)", "Website source code (GitHub repository)", DEPOT),
               ("Script de génération des pages FR / EN", "FR / EN page generation script", DEPOT + "/blob/main/build.py")],
 "circuit-court": [("Extrait du code PHP d’envoi d’e-mails", "Excerpt of the PHP email-sending code", None),
                   ("Capture d’un e-mail reçu avec son code", "Screenshot of a received email with its code", None)],
}

VEILLE_SUJET = (
 "<p><strong>Les réseaux gérés depuis le cloud : Cisco Meraki, SD-WAN et SASE.</strong></p>"
 "<p>Avec ces solutions, les équipements réseau (bornes Wi-Fi, switchs, pare-feu) se configurent et se surveillent depuis un tableau de bord en ligne, sans se connecter à chaque appareil. Le SD-WAN relie plusieurs sites d’une entreprise par Internet en choisissant le meilleur chemin, et le SASE ajoute à cela des services de sécurité fournis depuis le cloud.</p>"
 "<p><strong>Pourquoi ce sujet :</strong> c’est le cœur du métier d’UBNEST, qui installe des solutions Cisco et Meraki chez ses clients. C’est aussi un sujet où réseau et cybersécurité se rejoignent : un réseau géré à distance reste à mettre à jour et à protéger.</p>",
 "<p><strong>Cloud-managed networks: Cisco Meraki, SD-WAN and SASE.</strong></p>"
 "<p>With these solutions, network devices (Wi-Fi access points, switches, firewalls) are configured and monitored from an online dashboard, without logging in to each device. SD-WAN links a company’s sites over the Internet by picking the best path, and SASE adds security services delivered from the cloud on top.</p>"
 "<p><strong>Why this topic:</strong> it is at the heart of UBNEST’s business, which installs Cisco and Meraki solutions for its clients. It is also where networking and cybersecurity meet: a remotely managed network still has to be updated and protected.</p>")

VEILLE_OUTILS = (
 "<ul><li><strong>Google Alerts</strong> : alertes sur « Meraki », « SD-WAN », « SASE » et « vulnérabilité Cisco »</li>"
 "<li><strong>TLDR</strong> : newsletter quotidienne de veille technologique</li>"
 "<li><strong>Avis de sécurité Cisco</strong> : publications officielles des failles et correctifs</li>"
 "<li><strong>Communauté Cisco Meraki</strong> : annonces des nouvelles fonctionnalités</li></ul>",
 "<ul><li><strong>Google Alerts</strong>: alerts on “Meraki”, “SD-WAN”, “SASE” and “Cisco vulnerability”</li>"
 "<li><strong>TLDR</strong>: daily tech newsletter</li>"
 "<li><strong>Cisco security advisories</strong>: official publications of flaws and fixes</li>"
 "<li><strong>Cisco Meraki community</strong>: new feature announcements</li></ul>")

# (date, titre, résumé, ce que j'en retiens, [(nom source, url)])
VEILLE_FICHES = [
 (("Octobre 2026", "October 2026"),
  ("Cisco corrige sept failles sur toute la gamme Meraki", "Cisco fixes seven flaws across the whole Meraki range"),
  ("Le 7 octobre 2026, Cisco a publié un avis de sécurité regroupant sept vulnérabilités qui touchent six familles de produits Meraki : bornes Wi-Fi, switchs, appliances de sécurité et SD-WAN, caméras, passerelles cellulaires et Campus Gateways. La plus grave obtient un score de 9,6 sur 10. Il n’existe aucun contournement : seule la mise à jour du firmware corrige le problème, et certains correctifs n’étaient attendus qu’en octobre ou novembre. Cisco ne connaissait pas d’exploitation au moment de la publication.",
   "On 7 October 2026, Cisco published a security advisory covering seven vulnerabilities in six Meraki product families: Wi-Fi access points, switches, security and SD-WAN appliances, cameras, cellular gateways and Campus Gateways. The most severe scores 9.6 out of 10. There is no workaround: only a firmware update fixes the issue, and some fixes were only expected in October or November. Cisco knew of no exploitation when it published."),
  ("Même gérés depuis le cloud, les équipements doivent être mis à jour. Pour un technicien, cela veut dire suivre les avis de sécurité, vérifier les versions installées chez chaque client et planifier les mises à jour.",
   "Even when managed from the cloud, devices still have to be updated. For a technician, that means following security advisories, checking the versions installed at each client and planning updates."),
  [("Cisco Security Advisory", "https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-hardening-meraki-os-drbEX9GH.html"),
   ("eSecurity Planet (FR)", "https://www.esecurityplanet.com/fr/vulnerabilities/la-mise-a-jour-de-securite-de-cisco-meraki-corrige-des-failles-critiques-mais-certains-correctifs-restent-en-attente/")]),
 (("Septembre 2026", "September 2026"),
  ("Le SASE poursuit sa croissance et le SD-WAN repart", "SASE keeps growing and SD-WAN picks up again"),
  ("Selon le cabinet Dell’Oro Group, le marché du SASE a atteint 3,5 milliards de dollars au deuxième trimestre 2026, avec une croissance de plus de 20 % sur un an pour le cinquième trimestre consécutif. Le SD-WAN accélère, porté par la modernisation des réseaux des sites distants (agences, magasins, succursales).",
   "According to Dell’Oro Group, the SASE market reached $3.5 billion in the second quarter of 2026, growing more than 20% year on year for the fifth quarter in a row. SD-WAN is accelerating, driven by the modernisation of branch networks (offices, shops, branches)."),
  ("Les entreprises multi-sites cherchent de plus en plus une solution unique qui gère à la fois la connexion entre sites et la sécurité. Comprendre le SD-WAN et le SASE devient utile pour un technicien réseau.",
   "Multi-site businesses increasingly want a single solution that handles both site connectivity and security. Understanding SD-WAN and SASE is becoming useful for a network technician."),
  [("Dell’Oro Group", "https://www.delloro.com/news/sase-revenue-grows-above-20-percent-as-sd-wan-reaccelerates-in-2q-2026/")]),
 (("Août 2026", "August 2026"),
  ("L’IA arrive dans l’administration des réseaux Meraki", "AI comes to Meraki network administration"),
  ("Cisco a ajouté au tableau de bord Meraki un assistant IA capable d’enchaîner des actions (capacités dites « agentiques »). Le 10 août 2026, l’entreprise a aussi présenté des serveurs MCP qui permettent à des outils d’IA d’accéder aux données de Meraki et de Catalyst Center.",
   "Cisco added an AI assistant to the Meraki dashboard that can chain actions together (so-called “agentic” capabilities). On 10 August 2026, the company also presented MCP servers that let AI tools access Meraki and Catalyst Center data."),
  ("L’administration réseau s’automatise. Il faudra savoir vérifier ce que fait l’IA et limiter les droits qu’on lui donne : c’est aussi une question de sécurité.",
   "Network administration is becoming automated. Technicians will need to check what the AI does and limit the rights it is given: that is a security question too."),
  [("Cisco Meraki Feature Announcements", "https://community.meraki.com/t5/Feature-Announcements/bg-p/new-features"),
   ("Network-Switch.com", "https://network-switch.com/blogs/news/cisco-agentic-networking-and-sd-wan")]),
]
