# CB-002 — UGC Application Demo (Video) — BG Market

## Technique change (why the nozzle is now accurate)
Avatar/text-to-video models **regenerate** the product and morph the nozzle (confirmed by
the `video` skill: "Specific products/brands → AI generation: No"). Fix = **image-to-video
from the real product photo** so the nozzle/label/color are the actual pixels, not reinvented.

## Approved-approach asset
- **Model:** Seedance 2.0 (image-to-video)
- **Start frame:** real Shopify photo `spf50-product-color-1.jpg` (locks nozzle fidelity)
- **Aspect:** 9:16 | 720p | 10s
- **Job ID:** 0f05d95a-b075-4ad5-9417-54ecf5e7a4c1
- **URL:** https://d8j0ntlcm91z4.cloudfront.net/user_3AAke1QD9MZlxW9IxIN7IXlQ8tB/hf_20260602_104112_0f05d95a-b075-4ad5-9417-54ecf5e7a4c1.mp4
- **Output:** clean, no text (Bulgarian overlaid in post per runbook)

## Bulgarian conversion copy package (overlay in Canva/editor)

### On-screen captions (per beat)
| Time | Caption (BG) |
|---|---|
| 0–2s (HOOK) | SPF 50+, който **НЕ усещаш** 👀 |
| 2–5s | Прозрачен гел — **0% бял слой** |
| 5–8s | Защита + хидратация + основа за грим |
| 8–10s (CTA) | COBACCO · **Поръчай сега** |

### Voiceover script (BG, ~10s)
> „Това е слънцезащитата, която не усещаш. Прозрачен гел със SPF 50+, който попива
> веднага — без бял слой и без лепкавост. Защитава, хидратира и създава перфектна
> основа за грим. COBACCO — поръчай сега."

### Meta ad copy
- **Primary text:** Слънцезащита, която НЕ усещаш. ☀️ Прозрачен SPF 50+ гел — без бял слой, без лепкавост. Защитава, хидратира и е перфектната основа за грим. За всеки тип кожа.
- **Headline (≤40):** Невидим SPF 50+ — без бял слой
- **Description (≤30):** Безплатна доставка над €30

### Hook variants to A/B test (first 2s)
1. SPF 50+, който НЕ усещаш
2. Защо още носиш лепкав SPF? 🙅‍♀️
3. Прозрачен SPF — изчезва на кожата
4. Тествах SPF без бял оттенък

## Generation history
- v1 (9bcefd05) / NSFW + Seedance person morph — rejected
- v2 (14389bae) Marketing Studio avatar — rejected: nozzle morphed, English, creepy avatar
- v3 (0f05d95a) **image-to-video from real photo** — nozzle-accurate; BG copy packaged for overlay
- v4 (79d4cfe1) **Marketing Studio UGC, Bulgarian-speaking presenter** — 15s, 9:16, 720p; presenter delivers full BG VO script in natural bathroom setting; **URL:** https://d8j0ntlcm91z4.cloudfront.net/user_3AAke1QD9MZlxW9IxIN7IXlQ8tB/hf_20260603_052902_79d4cfe1-693e-4b57-a334-967ef835d12e.mp4
- v5 (cf1a7e3b) Marketing Studio, avatar "Nia" (auto-picked) — **rejected**: avatar not culturally appropriate for Bulgarian/Eastern European market
- v6 (e31c5141) Marketing Studio, avatar "Margot", entity `400b1f5d` (13-img) — European presenter; product entity still 13-image; **URL:** https://d8j0ntlcm91z4.cloudfront.net/user_3AAke1QD9MZlxW9IxIN7IXlQ8tB/hf_20260603_071827_e31c5141-3d2e-4c98-9243-d917b72bf457.mp4
- v7 (fbcc4a2a) **Marketing Studio, avatar "Margot" + canonical 2-img entity `a0b3173d`** — 15s, 9:16, 720p, UGC; angle-locked to images #2 and #5 only; VO-over-B-roll (no mouth sync needed); pending review

## Presenter
- **Approved avatar: Margot** (`1da384ed-3856-45e4-bf4c-a496c7aa95ff`) — European female, appropriate for Bulgarian market
- Do NOT use auto-picked avatars (Nia etc.) — not suitable for Eastern European audience

**Free-shipping line (BG):** "над €30" (per runbook Localization/Shipping Reference).
