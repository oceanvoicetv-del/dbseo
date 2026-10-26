# File Name: DbSeo30LanguageFunnelEngine.py
import os
import json

play_base = "https://play.google.com/store/apps/details?id=com.divebreathe.app"
dbseo_url = "https://oceanvoicetv-del.github.io/dbseo"
vectors_url = "https://oceanvoicetv-del.github.io/dive-breathe-ai-vectors"
host_domain = "oceanvoicetv-del.github.io"
pkg_id = "com.divebreathe.app"
meta_id = "931159316411497"
indexnow_key = "db382245a1b2c3d4e5f60718293a4b5c"
gsc_meta = '<meta name="google-site-verification" content="Ab9H26U0g20gR8Ydv_-BSVxoWRluup7utzj4G0vn7Ic" />'
lastmod_date = "2026-10-26"

# Exact 30-Language Matrix matching the Dive Breathe Core App
languages = {
    "en": ("English", "Nitrox Calculator, Scuba Logbook & Breath Trainer", "Instant-access scuba diving toolkit: calculate MOD & EAD, train breath control to lower SAC rate, and log dives.", "Open in Google Play App"),
    "ar": ("العربية", "حاسبة النيتروكس، سجل الغوص ومدرب التنفس", "أدوات غوص متكاملة: حساب أقصى عمق للنيتروكس (MOD)، تدريب التحكم في التنفس لتقليل استهلاك الهواء، وسجل غوص رقمي.", "افتح في تطبيق Google Play"),
    "cs": ("Čeština", "Kalkulačka Nitrox, Potápěčský Deník a Dechový Trenér", "Kompletní nástroje pro potápěče: výpočet MOD a EAD, trénink dechu pro snížení spotřeby vzduchu (SAC) a digitální deník.", "Otevřít v Google Play"),
    "da": ("Dansk", "Nitrox-beregner, Dykkerlogbog & Åndedrætstræner", "Komplet dykkerværktøj: beregn MOD og EAD, træn åndedrætskontrol for lavere luftforbrug og log dine dyk.", "Åbn i Google Play"),
    "de": ("Deutsch", "Nitrox-Rechner, Tauchlogbuch & Atemtrainer", "Das komplette Tauch-Toolkit: MOD & EAD berechnen, Atemkontrolle zur Senkung des Luftverbrauchs (SAC) trainieren und Tauchgänge loggen.", "In Google Play öffnen"),
    "el": ("Ελληνικά", "Υπολογιστής Nitrox, Ημερολόγιο Καταδύσεων & Προπόνηση Αναπνοής", "Πλήρες εργαλείο κατάδυσης: υπολογίστε MOD & EAD, εκπαιδεύστε την αναπνοή σας για μείωση SAC και καταγράψτε καταδύσεις.", "Άνοιγμα στο Google Play"),
    "es": ("Español", "Calculadora Nitrox, Bitácora de Buceo y Entrenador de Respiración", "Kit completo de buceo: calcula MOD y EAD, entrena el control respiratorio para reducir tu consumo de aire (SAC) y registra inmersiones.", "Abrir en Google Play"),
    "et": ("Eesti", "Nitroxi Kalkulaator, Sukeldumislogi ja Hingamistreener", "Täielik sukeldumistööriist: arvuta MOD ja EAD, treeni hingamist õhukulu vähendamiseks ja logi sukeldumisi.", "Ava Google Plays"),
    "fi": ("Suomi", "Nitrox-laskuri, Sukelluslokikirja & Hengityskouluttaja", "Kattavat sukellustyökalut: laske MOD ja EAD, harjoittele hengitystä ilmankulutuksen pienentämiseksi ja kirjaa sukellukset.", "Avaa Google Playssa"),
    "fr": ("Français", "Calculateur Nitrox, Carnet de Plongée & Entraîneur Respiratoire", "Boîte à outils complète de plongée : calculez MOD et EAD, maîtrisez votre respiration (SAC) et enregistrez vos plongées.", "Ouvrir dans Google Play"),
    "he": ("עברית", "מחשבון נייטרוקס, יומן צלילה ומאמן נשימה", "ערכת כלי צלילה מלאה: חישוב MOD ו-EAD, אימון שליטה בנשימה להורדת צריכת אוויר (SAC) ויומן צלילות דיגיטלי.", "פתח ב-Google Play"),
    "hi": ("हिन्दी", "नाइट्रोक्स कैलकुलेटर, स्कूबा लॉगबुक और ब्रीद ट्रेनर", "संपूर्ण स्कूबा डाइविंग टूलकिट: MOD और EAD की गणना करें, हवा की खपत कम करने के लिए सांस नियंत्रण का अभ्यास करें और डाइव लॉग करें।", "Google Play में खोलें"),
    "hu": ("Magyar", "Nitrox Kalkulátor, Búvárnapló és Légzéstréner", "Teljes búvár eszköztár: MOD és EAD számítás, légzéskontroll a levegőfogyasztás (SAC) csökkentésére és digitális merülésnapló.", "Megnyitás a Google Playen"),
    "id": ("Bahasa Indonesia", "Kalkulator Nitrox, Logbook Selam & Pelatih Napas", "Alat selam lengkap: hitung MOD & EAD, latih kontrol pernapasan untuk menghemat konsumsi udara (SAC), dan catat penyelaman.", "Buka di Google Play"),
    "it": ("Italiano", "Calcolatore Nitrox, Logbook Subacqueo e Trainer Respiratorio", "Toolkit subacqueo completo: calcola MOD ed EAD, allena il respiro per ridurre il consumo d'aria (SAC) e registra le immersioni.", "Apri su Google Play"),
    "ja": ("日本語", "ナイトロックス計算機・ダイブログ・呼吸トレーナー", "スキューバダイビング総合ツール：MOD・EADの即時計算、空気消費量（SAC）を抑える呼吸トレーニング、デジタルログブック。", "Google Playで開く"),
    "ko": ("한국어", "나이트록스 계산기, 다이빙 로그북 및 호흡 트레이너", "올인원 스쿠버 다이빙 툴킷: MOD 및 EAD 계산, 공기 소모율(SAC) 감소를 위한 호흡 조절 훈련 및 다이빙 로그 기록.", "Google Play에서 열기"),
    "ms": ("Bahasa Melayu", "Kalkulator Nitrox, Log Selam & Jurulatih Pernafasan", "Alat menyelam lengkap: kira MOD & EAD, latih kawalan pernafasan untuk kurangkan penggunaan udara (SAC) dan rekod selaman.", "Buka di Google Play"),
    "nl": ("Nederlands", "Nitrox Calculator, Duiklogboek & Ademhalingstrainer", "Complete duiktoolkit: bereken MOD & EAD, train ademhalingscontrole voor een lager luchtverbruik (SAC) en log je duiken.", "Openen in Google Play"),
    "no": ("Norsk", "Nitrox-kalkulator, Dykkelogg & Pustetrener", "Komplett dykkeverktøy: beregn MOD og EAD, tren pustekontroll for lavere luftforbruk (SAC) og loggfør dykk.", "Åpne i Google Play"),
    "pl": ("Polski", "Kalkulator Nitrox, Dziennik Nurkowy i Trener Oddechu", "Kompletny zestaw narzędzi nurkowych: obliczaj MOD i EAD, trenuj kontrolę oddechu (SAC) i zapisuj nurkowania w logbooku.", "Otwórz w Google Play"),
    "pt": ("Português", "Calculadora Nitrox, Diário de Mergulho e Treinador de Respiração", "Kit completo de mergulho: calcule MOD e EAD, treine o controle respiratório para reduzir o consumo de ar (SAC) e registre mergulhos.", "Abrir no Google Play"),
    "ru": ("Русский", "Калькулятор Nitrox, Журнал Дайвинга и Тренажер Дыхания", "Полный набор инструментов дайвера: расчет MOD и EAD, тренировка дыхания для снижения расхода воздуха (SAC) и цифровой логбук.", "Открыть в Google Play"),
    "sk": ("Slovenčina", "Kalkulačka Nitrox, Potápačský Denník a Dychový Tréner", "Kompletný nástroj pre potápačov: výpočet MOD a EAD, tréning dýchania na zníženie spotreby vzduchu (SAC) a digitálny denník.", "Otvoriť v Google Play"),
    "sv": ("Svenska", "Nitrox-kalkylator, Dykloggbok & Andningstränare", "Komplett dykverktyg: beräkna MOD och EAD, träna andningskontroll för lägre luftförbrukning (SAC) och logga dina dyk.", "Öppna i Google Play"),
    "th": ("ไทย", "เครื่องคำนวณ Nitrox สมุดบันทึกการดำน้ำ และฝึกการหายใจ", "เครื่องมือดำน้ำครบวงจร: คำนวณความลึก MOD & EAD ฝึกควบคุมการหายใจเพื่อประหยัดอากาศ (SAC) และบันทึกไดฟ์ล็อกดิจิทัล", "เปิดในแอป Google Play"),
    "tl": ("Tagalog", "Nitrox Calculator, Dive Logbook at Breath Trainer", "Kumpletong scuba diving toolkit: kalkulahin ang MOD at EAD, sanayin ang paghinga para tipirin ang hangin (SAC), at mag-log ng dives.", "Buksan sa Google Play"),
    "tr": ("Türkçe", "Nitrox Hesaplayıcı, Dalış Günlüğü ve Nefes Eğitmeni", "Eksiksiz dalış araç seti: MOD ve EAD hesaplayın, hava tüketimini (SAC) azaltmak için nefes kontrolü çalışın ve dalışları kaydedin.", "Google Play'de Aç"),
    "vi": ("Tiếng Việt", "Máy Tính Nitrox, Nhật Ký Lặn & Huấn Luyện Hơi Thở", "Bộ công cụ lặn biển toàn diện: tính MOD & EAD, luyện kiểm soát hơi thở giảm tiêu thụ khí (SAC) và ghi nhật ký lặn.", "Mở trong Google Play"),
    "zh": ("中文", "高氧计算器、潜水日志与呼吸训练器", "全能水肺潜水工具包：即时计算高氧最大工作深度 (MOD) 与等效空气深度 (EAD)、降低耗气率 (SAC) 的呼吸控制训练及数字潜水日志。", "在 Google Play 中打开")
}

# Vectors hub mapping (tl maps to fil in vectors repo; et and sk link to main vectors hub)
vector_Custom_Map = {"tl": "fil", "et": "en", "sk": "cs"}

# Build Hreflang blocks for all 30 languages
hreflang_lines = [f'    <link rel="alternate" hreflang="x-default" href="{dbseo_url}/" />']
xml_hreflang_lines = [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{dbseo_url}/"/>']
for code in languages.keys():
    hreflang_lines.append(f'    <link rel="alternate" hreflang="{code}" href="{dbseo_url}/index_{code}.html" />')
    xml_hreflang_lines.append(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{dbseo_url}/index_{code}.html"/>')

hreflang_block = "\n".join(hreflang_lines)
xml_hreflang_block = "\n".join(xml_hreflang_lines)

sponsor_entity = {
    "@type": "RealEstateAgent",
    "name": "Samui Smiles Co., Ltd.",
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Maenam, Koh Samui",
        "addressRegion": "Surat Thani",
        "addressCountry": "TH"
    },
    "founder": {"@type": "Person", "name": "Otilio J. Nunez"}
}

def build_page(code, lang_name, title_native, sub_native, cta_native, filename):
    play_web_url = f"{play_base}&hl={code}"
    play_intent_url = f"intent://details?id={pkg_id}&hl={code}#Intent;scheme=market;package=com.android.vending;S.browser_fallback_url={play_base}%26hl%3D{code};end;"
    page_canonical = f"{dbseo_url}/" if filename == "index.html" else f"{dbseo_url}/{filename}"
    vec_code = vector_Custom_Map.get(code, code)
    vector_link = f"{vectors_url}/dive-breathe-{vec_code}.html"
    rtl_attr = ' dir="rtl"' if code in ("ar", "he") else ""

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareApplication",
                "@id": f"{page_canonical}#app",
                "name": f"Dive Breathe: Scuba Tools ({lang_name})",
                "inLanguage": code,
                "operatingSystem": "ANDROID",
                "applicationCategory": "SportsApplication",
                "applicationSubCategory": "Scuba Diving Logbook, Nitrox Calculator & Breath Trainer",
                "identifier": [pkg_id, meta_id],
                "installUrl": play_web_url,
                "downloadUrl": play_web_url,
                "url": play_web_url,
                "sameAs": [play_web_url, f"{vectors_url}/", vector_link],
                "featureList": [
                    "Enriched Air Nitrox (EANx) Maximum Operating Depth (MOD) Calculator",
                    "Equivalent Air Depth (EAD) & NOAA CNS Oxygen Toxicity Reference",
                    "Guided Scuba Breath-Control & SAC Rate Conditioning Trainer",
                    "Pre-Dive Safety Check (BWRAF), Gear Setup & 3-Minute Safety Stop Simulators",
                    "Digital Scuba Dive Logbook with Metric and Imperial Telemetry"
                ],
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD",
                    "availability": "https://schema.org/InStock",
                    "url": play_web_url
                },
                "author": {
                    "@type": "Person",
                    "name": "Otilio J. Nunez",
                    "jobTitle": "PADI Master Scuba Diver Trainer (#382245) & Founder of Ocean Voice"
                },
                "sponsor": sponsor_entity,
                "description": sub_native
            }
        ]
    }

    lang_grid_links = "".join([
        f'<a href="index_{c}.html" hreflang="{c}" class="lang-chip">{n} ({c.upper()})</a>'
        for c, (n, _, _, _) in languages.items()
    ])

    html_content = f"""<!DOCTYPE html>
<html lang="{code}"{rtl_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {gsc_meta}
    <title>Dive Breathe: {title_native} ({lang_name})</title>
    <meta name="description" content="{sub_native}">
    <link rel="canonical" href="{page_canonical}" />
{hreflang_block}
    <script type="application/ld+json">
{json.dumps(schema_data, ensure_ascii=False, indent=2)}
    </script>
    <style>
        :root {{ --bg: #0f172a; --card: #1e293b; --accent: #0ea5e9; --accent-hover: #0284c7; --text: #f8fafc; --muted: #94a3b8; }}
        * {{ box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 24px 16px; line-height: 1.6; }}
        .wrapper {{ max-width: 760px; margin: 0 auto; }}
        .card {{ background: var(--card); border: 1px solid #334155; border-radius: 16px; padding: 28px 24px; margin-bottom: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.4); text-align: center; }}
        .badge-row {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-bottom: 14px; }}
        .badge {{ background: rgba(14, 165, 233, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); padding: 4px 10px; border-radius: 999px; font-size: 0.8rem; font-weight: 600; }}
        h1 {{ color: #38bdf8; font-size: 1.85rem; margin: 0 0 10px 0; }}
        h2 {{ color: var(--muted); font-size: 1.1rem; font-weight: 400; margin: 0 0 24px 0; }}
        .cta-btn {{ display: inline-block; width: 100%; max-width: 380px; background: linear-gradient(135deg, #0ea5e9, #0284c7); color: #ffffff; font-weight: 800; font-size: 1.15rem; padding: 16px 28px; border-radius: 12px; text-decoration: none; box-shadow: 0 4px 14px rgba(14, 165, 233, 0.4); transition: transform 0.15s ease; }}
        .cta-btn:hover {{ transform: translateY(-2px); }}
        .sub-link {{ display: block; margin-top: 10px; font-size: 0.85rem; color: var(--muted); text-decoration: underline; }}
        .tool-box {{ background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 20px; margin-top: 24px; text-align: left; }}
        .tool-title {{ color: #38bdf8; font-weight: 700; font-size: 1rem; margin-bottom: 12px; text-align: center; }}
        .calc-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 14px; }}
        label {{ display: block; font-size: 0.8rem; color: var(--muted); margin-bottom: 4px; }}
        input[type="number"] {{ width: 100%; background: #1e293b; border: 1px solid #475569; color: #fff; padding: 10px; border-radius: 8px; font-size: 1rem; font-weight: 700; text-align: center; }}
        .calc-result {{ background: rgba(14, 165, 233, 0.1); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 8px; padding: 12px; text-align: center; }}
        .calc-val {{ font-size: 1.6rem; font-weight: 800; color: #38bdf8; }}
        .lang-Cloud {{ display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; margin-top: 12px; }}
        .lang-chip {{ background: #0f172a; color: #cbd5e1; border: 1px solid #334155; padding: 5px 10px; border-radius: 6px; font-size: 0.78rem; text-decoration: none; }}
        .lang-chip:hover {{ border-color: #38bdf8; color: #38bdf8; }}
        .footer-links {{ font-size: 0.82rem; color: var(--muted); margin-top: 14px; }}
        .footer-links a {{ color: #38bdf8; text-decoration: none; }}
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="card">
            <div class="badge-row">
                <span class="badge">PADI IDC Recommended</span>
                <span class="badge">30 Languages</span>
                <span class="badge">Android &amp; PWA</span>
            </div>
            <h1>Dive Breathe: {title_native}</h1>
            <h2>{sub_native}</h2>

            <a id="play-cta" href="{play_web_url}" class="cta-btn" rel="noopener">
                &#9654; {cta_native}
            </a>
            <a href="{play_web_url}" class="sub-link" rel="noopener">Google Play Web Listing ({lang_name})</a>

            <!-- Interactive Live Nitrox MOD Preview Tool -->
            <div class="tool-box">
                <div class="tool-title">&#9889; Live Nitrox MOD Calculator Preview (EANx)</div>
                <div class="calc-row">
                    <div>
                        <label for="o2-in">Oxygen O2 % (21 - 100)</label>
                        <input type="number" id="o2-in" min="21" max="100" value="32" oninput="calcMod()">
                    </div>
                    <div>
                        <label for="ppo2-in">Max ppO2 (ATA)</label>
                        <input type="number" id="ppo2-in" min="1.0" max="1.6" step="0.1" value="1.4" oninput="calcMod()">
                    </div>
                </div>
                <div class="calc-result">
                    <div style="font-size:0.75rem; color:#94a3b8;">Maximum Operating Depth (MOD)</div>
                    <div id="mod-out" class="calc-val">33.8 m / 110.7 ft</div>
                    <div style="font-size:0.72rem; color:#64748b; margin-top:4px;">Unlock EAD, NOAA CNS Limits, Breath Trainer &amp; Full Dive Logbook in the app.</div>
                </div>
            </div>
        </div>

        <div class="card">
            <div class="tool-title">30-Language Global Dive Matrix</div>
            <div class="lang-Cloud">
                {lang_grid_links}
            </div>
            <div class="footer-links">
                <p>
                    <a href="{vector_link}">Technical FAQ &amp; AI Authority Hub ({lang_name})</a> |
                    <a href="{vectors_url}/">Global Scuba Vector Directory</a> |
                    <a href="sitemap.xml">Sitemap</a>
                </p>
                <p>Created by Otilio J. Nunez (PADI MSDT #382245) &bull; Supported by Samui Smiles Co., Ltd. (Maenam, Koh Samui)</p>
            </div>
        </div>
    </div>

    <script>
        function calcMod() {{
            var o2 = parseFloat(document.getElementById('o2-in').value) / 100;
            var ppo2 = parseFloat(document.getElementById('ppo2-in').value);
            var out = document.getElementById('mod-out');
            if (isNaN(o2) || o2 < 0.21 || o2 > 1 || isNaN(ppo2) || ppo2 <= 0) {{
                out.innerText = "Invalid Mix";
                return;
            }}
            var ata = ppo2 / o2;
            var meters = Math.max(0, (ata - 1) * 10);
            var feet = meters * 3.28084;
            out.innerText = meters.toFixed(1) + " m / " + feet.toFixed(1) + " ft";
        }}

        // Upgrade CTA link to native Play Store App Intent on Android devices
        (function() {{
            var ua = navigator.userAgent || navigator.vendor || window.opera;
            if (/android/i.test(ua)) {{
                var btn = document.getElementById('play-cta');
                if (btn) {{
                    btn.setAttribute('href', '{play_intent_url}');
                }}
            }}
        }})();
    </script>
</body>
</html>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

# Generate root index.html (English master) + all 30 index_<code>.html files
en_data = languages["en"]
build_page("en", en_data[0], en_data[1], en_data[2], en_data[3], "index.html")

all_urls = [f"{dbseo_url}/", f"{dbseo_url}/sitemap.xml"]
for code, (lang_name, title_n, sub_n, cta_n) in languages.items():
    fname = f"index_{code}.html"
    build_page(code, lang_name, title_n, sub_n, cta_n, fname)
    all_urls.append(f"{dbseo_url}/{fname}")

# Generate XML Sitemap with 31x31 xhtml:link hreflang cross-graph
sitemap_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    '  <url>',
    f'    <loc>{dbseo_url}/</loc>',
    f'    <lastmod>{lastmod_date}</lastmod>',
    '    <changefreq>daily</changefreq>',
    '    <priority>1.0</priority>',
    xml_hreflang_block,
    '  </url>'
]

for code in languages.keys():
    sitemap_lines.extend([
        '  <url>',
        f'    <loc>{dbseo_url}/index_{code}.html</loc>',
        f'    <lastmod>{lastmod_date}</lastmod>',
        '    <changefreq>weekly</changefreq>',
        '    <priority>0.95</priority>',
        xml_hreflang_block,
        '  </url>'
    ])

sitemap_lines.append('</urlset>')
with open("sitemap.xml", "w", encoding="utf-8") as smf:
    smf.write("\n".join(sitemap_lines))

with open("robots.txt", "w", encoding="utf-8") as rf:
    rf.write(f"User-agent: *\nAllow: /\nSitemap: {dbseo_url}/sitemap.xml\n")

with open(".nojekyll", "w", encoding="utf-8") as nj:
    nj.write("")

with open(f"{indexnow_key}.txt", "w", encoding="utf-8") as kf:
    kf.write(indexnow_key)

indexnow_payload = {
    "host": host_domain,
    "key": indexnow_key,
    "keyLocation": f"{dbseo_url}/{indexnow_key}.txt",
    "urlList": all_urls
}
with open("indexnow-payload.json", "w", encoding="utf-8") as inf:
    json.dump(indexnow_payload, inf, indent=2)

print(f"DBSEO 30-LANGUAGE BUILD COMPLETE: {len(all_urls)} endpoints compiled.")