#!/usr/bin/env python3
"""Builds the static Lupo site. Run: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "hi@joel-wolf.de"

LEGAL = {
    "name": "Joel Wolf",
    "street": "Dobbenstraße 17",
    "city": "49152 Bad Essen",
    "country": "Deutschland",
    "vat": "Kleinunternehmer im Sinne von § 19 UStG. Es wird keine Umsatzsteuer berechnet.",
    "authority": "Die Landesbeauftragte für den Datenschutz Niedersachsen, Prinzenstraße 5, 30159 Hannover, www.lfd.niedersachsen.de",
}

T = {
    "de": {
        "lang": "de", "prefix": "", "other": "en/", "other_label": "English",
        "title": "Lupo: Noten-App fürs Orchester auf dem iPad",
        "desc": "Noten auf dem iPad lesen, per Tipp oder Pedal umblättern und mit dem Apple Pencil eintragen. Für Orchestermusiker. Einmal kaufen, kein Abo, ohne Konto.",
        "nav": [("Funktionen", "#funktionen"), ("Preis", "#preis"), ("Fragen", "#fragen"), ("Support", "support.html")],
        "cta": "Bald im App Store",
        "h1": "Deine Stimme.<br><span>Alles am Pult.</span>",
        "sub": "Die Noten-App fürs Orchester auf dem iPad: Ein Tipp blättert um, der Apple Pencil schreibt sofort, und das ganze Konzert läuft am Stück.",
        "proof": "Gebaut von einem Holzbläser für sein eigenes Pult.",
        "shots_alt": ["Notenseite mit Studierbuchstaben, Apple-Pencil-Stempeln und Da capo", "Programm Frühjahrskonzert mit vier Stücken", "Alle Funktionen als Symbole: Designed for iPad", "Zwei iPads blättern gemeinsam", "Konzertmodus mit dem Hinweis auf das nächste Stück"],
        "problem_h": "„Das richtige Stück finde ich erst, wenn der Dirigent schon einzählt.“",
        "problems": [
            "„Die PDFs aus der WhatsApp-Gruppe drucke ich aus, weil ich auf dem iPad <b>nicht weiß, wohin damit</b>.“",
            "„Ich hab manche Stücke dreimal kopiert, und <b>auf keiner Kopie stehen alle meine Eintragungen</b>.“",
            "„Bei schnellen Wendestellen <b>fehlt mir die Hand zum Umblättern</b>, oder mein Pultnachbar muss ran.“",
        ],
        "solution_h": "Spielen statt blättern: Lupo kümmert sich um die Seiten.",
        "benefits": [
            ("Umblättern ohne freie Hand", "Tippe rechts für vor, links für zurück, oder tritt aufs Bluetooth-Pedal. Mit halben Seiten siehst du oben schon die nächste Seite, während du unten noch spielst. Auch MIDI, Gamecontroller und die Apple Watch blättern."),
            ("Eintragungen, die bleiben", "Der Apple Pencil schreibt sofort, dein Finger blättert weiter. Deine PDF bleibt unverändert, die Eintragungen liegen in Ebenen darüber. Stempel in echter Notenschrift gibt es für 7 Gruppen, von Holz bis Dirigat."),
            ("Das ganze Konzert am Stück", "Leg ein Programm an, und Lupo blättert vom letzten Takt direkt ins nächste Stück. Dein Pultnachbar blättert auf seinem iPad mit, in Gruppen bis zu 8 iPads, ohne Internet."),
        ],
        "steps_h": "In drei Schritten am Pult",
        "steps": [("Laden", "Hol dir Lupo aus dem App Store, ohne Konto und ohne Anmeldung."), ("Noten holen", "Zieh PDFs aus der Dateien-App oder scanne Seiten mit der Kamera."), ("Spielen", "Öffne die Stimme und tippe zum Blättern. Ein Pedal weist du mit einem Druck zu.")],
        "price_h": "Einmal kaufen. Für immer behalten.",
        "free_t": "Lupo Free", "free": "Kostenlos. Bis zu 3 Stücke hinzufügen, ansehen und darin blättern.",
        "prem_t": "Lupo Premium", "prem": "Alles andere, auch Notizen mit Apple Pencil, mit einem einzigen Kauf. Kein Abo, keine Zusatzkäufe, mit Familienfreigabe.",
        "faq_h": "Häufige Fragen",
        "faq": [
            ("Ich nutze schon eine andere Noten-App. Lohnt sich der Wechsel?", "Probier es mit drei Stücken aus, das kostet nichts. Lupo übernimmt PDFs, Angaben, Lesezeichen und Programme aus der Sicherung einer anderen Noten-App."),
            ("Wer sieht meine Noten und Eintragungen?", "Niemand außer dir. Lupo hat kein Konto, keinen Server, keine Cloud und keine Analyse. Deine Noten liegen als normale PDFs in echten Ordnern, sichtbar in der Dateien-App."),
            ("Funktioniert mein Pedal?", "Bluetooth-Pedale, die sich wie eine Tastatur verhalten, und MIDI-Pedale funktionieren. Du drückst in den Einstellungen einmal auf das Pedal, und Lupo merkt sich die Taste."),
            ("Welches iPad brauche ich?", "Ein iPad mit iPadOS 18 oder neuer. Zum Lesen und Blättern brauchst du keinen Apple Pencil, nur für Eintragungen."),
            ("Was, wenn im Konzert etwas schiefgeht?", "Im Konzertmodus blättert eine aufliegende Hand nicht, und Wischen und Zoomen sind aus. Deine Original-PDFs verändert Lupo nie, und gelöschte Noten liegen 30 Tage im Papierkorb."),
        ],
        "final_h": "Bring deine nächste Probe aufs iPad, ohne Ordner und ohne Abo.",
        "final_note": "Kostenlos mit 3 Stücken, ohne Konto.",
        "footer": [("Support", "support.html"), ("Datenschutz", "datenschutz.html"), ("Impressum", "impressum.html")],
        "trademark": "Apple, Apple Pencil, Apple Watch und iPad sind Marken der Apple Inc.",
    },
    "en": {
        "lang": "en", "prefix": "../", "other": "../", "other_label": "Deutsch",
        "title": "Lupo: sheet music for orchestra on iPad",
        "desc": "Read sheet music on iPad, turn pages with a tap or a pedal and write with Apple Pencil. For orchestra musicians. Pay once, no subscription, no account.",
        "nav": [("Features", "#features"), ("Price", "#price"), ("FAQ", "#faq"), ("Support", "support.html")],
        "cta": "Coming soon to the App Store",
        "h1": "Your part.<br><span>All at your stand.</span>",
        "sub": "The sheet music app for orchestra on iPad: one tap turns the page, Apple Pencil writes instantly, and the whole concert plays straight through.",
        "proof": "Built by a woodwind player for his own stand.",
        "shots_alt": ["Score page with rehearsal letters, Apple Pencil stamps and da capo", "The Frühjahrskonzert programme with four pieces", "All features as icons: Designed for iPad", "Two iPads turning pages together", "Concert mode with the hint for the next piece"],
        "problem_h": "“I only find the right piece when the conductor is already counting in.”",
        "problems": [
            "“I print the PDFs from the group chat because <b>I don't know where to put them</b> on my iPad.”",
            "“Some pieces I've copied three times, and <b>no copy has all my markings</b>.”",
            "“At quick page turns <b>I don't have a hand free</b>, or my stand partner has to do it.”",
        ],
        "solution_h": "Play instead of turning: Lupo takes care of the pages.",
        "benefits": [
            ("Turn pages hands-free", "Tap right to go forward, left to go back, or press a Bluetooth pedal. With half-page turns you see the next page at the top while you still play the bottom. MIDI, game controllers and Apple Watch turn pages too."),
            ("Markings that stay", "Apple Pencil writes instantly, your finger keeps turning. Your PDF stays untouched, your markings sit in layers on top. Stamps in real music notation come in 7 groups, from woodwinds to conducting."),
            ("The whole concert in one go", "Build a programme, and Lupo turns from the last bar straight into the next piece. Your stand partner turns along on their iPad, in groups of up to 8 iPads, without internet."),
        ],
        "steps_h": "At your stand in three steps",
        "steps": [("Download", "Get Lupo from the App Store, no account and no sign-in."), ("Add music", "Drag PDFs in from the Files app or scan pages with the camera."), ("Play", "Open your part and tap to turn. Assign a pedal with a single press.")],
        "price_h": "Pay once. Keep it forever.",
        "free_t": "Lupo Free", "free": "Free. Add up to 3 pieces, view them and turn their pages.",
        "prem_t": "Lupo Premium", "prem": "Everything else, including notes with Apple Pencil, in a single purchase. No subscription, no add-ons, with Family Sharing.",
        "faq_h": "Questions",
        "faq": [
            ("I already use another sheet music app. Is it worth switching?", "Try it with three pieces for free. Lupo brings over PDFs, details, bookmarks and programmes from another sheet music app's backup."),
            ("Who can see my music and markings?", "Nobody but you. Lupo has no account, no server, no cloud and no analytics. Your music stays as regular PDFs in real folders, visible in the Files app."),
            ("Does my pedal work?", "Bluetooth pedals that act like a keyboard work, and so do MIDI pedals. Press the pedal once in Settings, and Lupo remembers the key."),
            ("Which iPad do I need?", "An iPad with iPadOS 18 or later. You don't need Apple Pencil to read and turn pages, only for markings."),
            ("What if something goes wrong in a concert?", "In concert mode a resting hand doesn't turn the page, and swiping and zooming are off. Lupo never changes your original PDFs, and deleted music stays in the trash for 30 days."),
        ],
        "final_h": "Bring your next rehearsal to iPad, without binders and without a subscription.",
        "final_note": "Free with 3 pieces, no account.",
        "footer": [("Support", "support.html"), ("Privacy", "privacy.html"), ("Imprint", "../impressum.html")],
        "trademark": "Apple, Apple Pencil, Apple Watch and iPad are trademarks of Apple Inc.",
    },
}


def page(t, title, desc, body, path_other):
    p = t["prefix"]
    og = f'{p}img/og-{t["lang"]}.jpg'
    footer = " · ".join(f'<a href="{h}">{l}</a>' for l, h in t["footer"])
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og}">
<meta name="theme-color" content="#8F5B0E">
<link rel="icon" href="{p}favicon.png">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="stylesheet" href="{p}style.css">
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="./"><img src="{p}img/icon.png" alt="" width="36" height="36">Lupo</a>
<nav>{''.join(f'<a href="{h}">{l}</a>' for l, h in t['nav'])}<a class="lang" href="{path_other}">{t['other_label']}</a></nav>
</div></header>
{body}
<footer><div class="wrap"><p>{footer}</p><p class="small">© 2026 Joel Wolf. {t['trademark']}</p></div></footer>
</body>
</html>
"""


def index(t):
    L = t["lang"]
    p = t["prefix"]
    fid, pid, qid = (["funktionen", "preis", "fragen"] if L == "de" else ["features", "price", "faq"])
    shots = "".join(f'<img src="{p}img/{L}-{i}.jpg" alt="{a}" width="900" height="1200" loading="{"eager" if i < 3 else "lazy"}">' for i, a in enumerate(t["shots_alt"], 1))
    problems = "".join(f"<li>{x}</li>" for x in t["problems"])
    benefits = "".join(f"<div class='card'><h3>{h}</h3><p>{b}</p></div>" for h, b in t["benefits"])
    steps = "".join(f"<li><span>{i}</span><h3>{h}</h3><p>{b}</p></li>" for i, (h, b) in enumerate(t["steps"], 1))
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    body = f"""
<section class="hero"><div class="wrap">
<h1>{t['h1']}</h1>
<p class="sub">{t['sub']}</p>
<p><span class="button">{t['cta']}</span></p>
<p class="proof">{t['proof']}</p>
</div>
<div class="shots" tabindex="0">{shots}</div>
</section>
<section class="problem"><div class="wrap narrow">
<h2>{t['problem_h']}</h2>
<ul class="quotes">{problems}</ul>
</div></section>
<section id="{fid}"><div class="wrap">
<h2>{t['solution_h']}</h2>
<div class="cards">{benefits}</div>
</div></section>
<section class="steps"><div class="wrap">
<h2>{t['steps_h']}</h2>
<ol>{steps}</ol>
</div></section>
<section id="{pid}"><div class="wrap">
<h2>{t['price_h']}</h2>
<div class="cards two"><div class="card"><h3>{t['free_t']}</h3><p>{t['free']}</p></div><div class="card accent"><h3>{t['prem_t']}</h3><p>{t['prem']}</p></div></div>
</div></section>
<section id="{qid}"><div class="wrap narrow">
<h2>{t['faq_h']}</h2>
{faq}
</div></section>
<section class="final"><div class="wrap narrow">
<h2>{t['final_h']}</h2>
<p><span class="button">{t['cta']}</span></p>
<p class="proof">{t['final_note']}</p>
</div></section>
"""
    return page(t, t["title"], t["desc"], body, t["other"])


SUPPORT = {
    "de": ("Support", "Hilfe und Kontakt zu Lupo.", f"""
<h1>Support</h1>
<p>Fragen, Fehler oder Wünsche? Schreib mir an <a href="mailto:{EMAIL}?subject=Lupo">{EMAIL}</a>. Ich spiele selbst im Orchester und lese jede Nachricht.</p>
<p>Hilfreich ist, wenn du dazuschreibst, welches iPad und welche iPadOS-Version du nutzt und was du gerade gemacht hast.</p>
<h2>Häufige Fragen</h2>
<h3>Wie kommen meine Noten in Lupo?</h3>
<p>Zieh PDFs aus der Dateien-App, öffne sie aus Mail oder Safari mit Lupo, oder scanne Papiernoten mit der Kamera.</p>
<h3>Wie richte ich mein Pedal ein?</h3>
<p>Öffne in Lupo die Einstellungen und drück im Bereich für Pedale einmal auf dein Pedal. Lupo merkt sich die Taste.</p>
<h3>Wo liegen meine Noten?</h3>
<p>Als normale PDF-Dateien im Ordner von Lupo, sichtbar in der Dateien-App unter „Auf meinem iPad“. Lupo legt außerdem jeden Tag eine automatische Sicherung auf deinem iPad an.</p>
<h3>Ich habe Lupo Premium gekauft, sehe es aber nicht.</h3>
<p>Öffne die Kaufseite und tippe auf „Käufe wiederherstellen“. Der Kauf ist an deine Apple-ID gebunden und gilt dank Familienfreigabe auch für deine Familie.</p>
<h3>Wie bekomme ich mein Geld zurück?</h3>
<p>Rückerstattungen laufen über Apple unter <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
"""),
    "en": ("Support", "Help and contact for Lupo.", f"""
<h1>Support</h1>
<p>Questions, bugs or ideas? Write to me at <a href="mailto:{EMAIL}?subject=Lupo">{EMAIL}</a>. I play in an orchestra myself and read every message.</p>
<p>It helps if you mention your iPad model, your iPadOS version and what you were doing.</p>
<h2>Questions</h2>
<h3>How do I get my music into Lupo?</h3>
<p>Drag PDFs in from the Files app, open them from Mail or Safari with Lupo, or scan paper music with the camera.</p>
<h3>How do I set up my pedal?</h3>
<p>Open Settings in Lupo and press your pedal once in the pedal section. Lupo remembers the key.</p>
<h3>Where is my music stored?</h3>
<p>As regular PDF files in Lupo's folder, visible in the Files app under On My iPad. Lupo also makes an automatic backup on your iPad every day.</p>
<h3>I bought Lupo Premium but don't see it.</h3>
<p>Open the purchase sheet and tap Restore Purchases. The purchase belongs to your Apple Account and is shared with your family through Family Sharing.</p>
<h3>How do I get a refund?</h3>
<p>Refunds go through Apple at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
"""),
}

PRIVACY = {
    "de": ("datenschutz.html", "Datenschutz", "Datenschutzerklärung für die App Lupo und diese Website.", f"""
<h1>Datenschutz</h1>
<p>Stand: November 2026</p>
<h2>Verantwortlich</h2>
<p>{LEGAL['name']}, {LEGAL['street']}, {LEGAL['city']}, {LEGAL['country']}. E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>Die App Lupo</h2>
<p>Lupo erhebt keine personenbezogenen Daten. Die App hat kein Konto, keinen eigenen Server, keine Cloud-Synchronisierung, keine Werbung und keine Analyse- oder Tracking-Werkzeuge. Deine Noten, Eintragungen, Aufnahmen und Einstellungen bleiben auf deinem iPad und werden nicht an mich übertragen.</p>
<ul>
<li><b>Kamera:</b> zum Scannen von Papiernoten und, wenn du es einschaltest, zum Umblättern per Kopf- oder Mundbewegung. Die Bilder werden nur auf dem Gerät ausgewertet und weder gespeichert noch übertragen.</li>
<li><b>Mikrofon:</b> für das Stimmgerät und deine Übe-Aufnahmen. Aufnahmen werden nur auf deinem iPad gespeichert.</li>
<li><b>Bluetooth und lokales Netzwerk:</b> für Pedale, MIDI-Geräte, die Apple Watch als Fernbedienung und den Pultpartner. Die Verbindung läuft direkt von Gerät zu Gerät, ohne Server.</li>
<li><b>Käufe:</b> Der Kauf von Lupo Premium läuft über Apple. Ich erhalte keine Zahlungsdaten. Es gilt die Datenschutzrichtlinie von Apple.</li>
<li><b>Absturzberichte:</b> Wenn du in den iPadOS-Einstellungen zugestimmt hast, teilt Apple anonymisierte Absturz- und Nutzungsdaten mit Entwicklern. Das steuerst du in Einstellungen › Datenschutz &amp; Sicherheit › Analyse &amp; Verbesserungen.</li>
</ul>
<h2>Diese Website</h2>
<p>Diese Website wird über GitHub Pages bereitgestellt (GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). Beim Aufruf verarbeitet GitHub technisch notwendige Daten wie deine IP-Adresse, um die Seite auszuliefern und vor Missbrauch zu schützen. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. GitHub ist unter dem EU-US Data Privacy Framework zertifiziert. Mehr dazu in der <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement">Datenschutzerklärung von GitHub</a>.</p>
<p>Die Website setzt keine Cookies, lädt keine Schriften oder Skripte von fremden Servern und nutzt keine Analyse.</p>
<h2>E-Mail</h2>
<p>Wenn du mir schreibst, verarbeite ich deine Nachricht und deine Adresse nur, um zu antworten (Art. 6 Abs. 1 lit. b und f DSGVO). Ich lösche sie, wenn die Anfrage erledigt ist und keine Aufbewahrungspflicht besteht.</p>
<h2>Deine Rechte</h2>
<p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch. Schreib mir dazu an die oben genannte Adresse. Außerdem kannst du dich bei einer Aufsichtsbehörde beschweren, zum Beispiel bei: {LEGAL['authority']}.</p>
"""),
    "en": ("privacy.html", "Privacy", "Privacy policy for the Lupo app and this website.", f"""
<h1>Privacy</h1>
<p>Last updated: November 2026. The German version is binding.</p>
<h2>Controller</h2>
<p>{LEGAL['name']}, {LEGAL['street']}, {LEGAL['city']}, Germany. Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>The Lupo app</h2>
<p>Lupo collects no personal data. The app has no account, no server of its own, no cloud sync, no ads and no analytics or tracking tools. Your music, markings, recordings and settings stay on your iPad and are never sent to me.</p>
<ul>
<li><b>Camera:</b> to scan paper music and, if you turn it on, to turn pages with head or mouth movements. Images are processed on the device only and are neither stored nor sent.</li>
<li><b>Microphone:</b> for the tuner and your practice recordings. Recordings are stored on your iPad only.</li>
<li><b>Bluetooth and local network:</b> for pedals, MIDI devices, the Apple Watch remote and the stand partner. Connections go directly from device to device, without a server.</li>
<li><b>Purchases:</b> Lupo Premium is bought through Apple. I receive no payment data. Apple's privacy policy applies.</li>
<li><b>Crash reports:</b> if you agreed in iPadOS Settings, Apple shares anonymised crash and usage data with developers. You control this in Settings › Privacy &amp; Security › Analytics &amp; Improvements.</li>
</ul>
<h2>This website</h2>
<p>This website is hosted on GitHub Pages (GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). When you visit, GitHub processes technically necessary data such as your IP address to deliver the page and prevent abuse. The legal basis is Art. 6(1)(f) GDPR. GitHub is certified under the EU-US Data Privacy Framework. See <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub's privacy statement</a>.</p>
<p>This website sets no cookies, loads no fonts or scripts from other servers and uses no analytics.</p>
<h2>Email</h2>
<p>If you write to me, I process your message and address only to reply (Art. 6(1)(b) and (f) GDPR) and delete them once the request is settled and no retention duty applies.</p>
<h2>Your rights</h2>
<p>You have the right to access, rectification, erasure, restriction of processing, data portability and objection. Write to me at the address above. You can also complain to a supervisory authority, for example: {LEGAL['authority']}.</p>
"""),
}

IMPRINT = f"""
<h1>Impressum</h1>
<p>Angaben gemäß § 5 DDG</p>
<p>{LEGAL['name']}<br>{LEGAL['street']}<br>{LEGAL['city']}<br>{LEGAL['country']}</p>
<h2>Kontakt</h2>
<p>E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>Umsatzsteuer</h2>
<p>{LEGAL['vat']}</p>
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
<p>{LEGAL['name']}, Anschrift wie oben</p>
<h2>Verbraucherstreitbeilegung</h2>
<p>Ich bin nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
"""


def doc(t, title, desc, content, other):
    body = f'<main class="doc"><div class="wrap narrow">{content}</div></main>'
    return page(t, f"{title} · Lupo", desc, body, other)


def main():
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "index.html").write_text(index(T["de"]))
    (ROOT / "en/index.html").write_text(index(T["en"]))
    s = SUPPORT["de"]; (ROOT / "support.html").write_text(doc(T["de"], s[0], s[1], s[2], "en/support.html"))
    s = SUPPORT["en"]; (ROOT / "en/support.html").write_text(doc(T["en"], s[0], s[1], s[2], "../support.html"))
    f, ti, de, c = PRIVACY["de"]; (ROOT / f).write_text(doc(T["de"], ti, de, c, "en/privacy.html"))
    f, ti, de, c = PRIVACY["en"]; (ROOT / "en" / f).write_text(doc(T["en"], ti, de, c, "../datenschutz.html"))
    (ROOT / "impressum.html").write_text(doc(T["de"], "Impressum", "Impressum von Lupo.", IMPRINT, "en/"))


if __name__ == "__main__":
    main()
