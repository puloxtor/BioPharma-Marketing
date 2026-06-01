# COBACCO — Higgsfield Creative Generation Runbook

> Purpose: execute the full COBACCO creative batch in one pass via the **Higgsfield MCP**
> (connector: `https://mcp.higgsfield.ai/mcp`). The MCP must be connected **before** the
> session starts, or its tools won't register. If using the CLI/skill locally instead, the
> network must allowlist `higgsfield.ai` / `fnf.higgsfield.ai`.

## How to use
1. Start a fresh Claude Code session with the Higgsfield connector already attached.
2. Say: "generate the COBACCO creatives from the runbook."
3. Validate **CB-004 (the single static)** first. Only proceed to the rest once the product
   match (tube shape, pointed nozzle tip, mint-green + lilac body, label legibility) is approved.
4. Save every output URL into the Drive **Creative Tracker** (Tab 4) + Creative Briefs folder.

## ⛔ MANDATORY PRE-FLIGHT: Product Reference Audit

**Do not submit any generation job until this checklist is complete.**

Product accuracy — especially cap shape, tube color, and serum consistency — is non-negotiable.
A generation that misrepresents the product cannot be used and wastes the credit.

### Step 1 — Verify the Marketing Studio product entity
Use the full-reference product entity (created 2026-06-01) which contains all 11 Shopify images:
- **Marketing Studio product ID:** `66923fab-36ee-4e72-92e2-94236c87ac38` (FULL REF v2 — corrected nozzle + serum color, 2026-06-01)
- Always pass this via `--product_ids` for Marketing Studio jobs.
- For raw image/video generation (non-Marketing-Studio), attach references manually (see below).

### Step 2 — Confirm reference images cover all three accuracy axes
Before generating, verify the reference set visually includes:
- [ ] **Nozzle** — narrow pointed white dispensing tip at the bottom of the tube (squeeze tube). NOT a pump, NOT a flip cap, NOT a wide opening.
- [ ] **Tube body color** — soft mint-green fading to white at base, with a lilac/lavender accent stripe
- [ ] **Serum color & texture** — warm golden-amber gel, visibly pigmented and glossy when dispensed. NOT transparent, NOT white.

### Step 3 — Attach the right references per job type
**For image generation (GPT Image 2 / Nano Banana):** attach at minimum:
- `cobacco-product-imgs-1000x1000-SPF-1.png` (clean studio, full tube)
- `spf50-product-color-1.jpg` or `spf50-product-color-2.jpg` (cap + color close-up)
- A `spf50-product-color-*` shot that shows the actual serum/use context

**For video generation (Seedance / Marketing Studio):** always use the Marketing Studio product
entity `0afd4ba7-b57b-42b9-bef0-4cc46be16929` which carries all 11 images. Do not generate
video with only 1–2 reference images — this was the root cause of CB-001's inaccuracy.

### Full Shopify reference image set (source of truth)
| File | Shows |
|---|---|
| `cobacco-product-imgs-1000x1000-SPF-1.png` | Clean white-bg, full tube front |
| `cobacco-product-imgs-1000x1000-SPF-2.png` | Full tube angle 2 |
| `cobacco-product-imgs-1000x1000-SPF-3.png` | Full tube angle 3 |
| `cobacco-product-imgs-1000x1000-SPF-4.png` | Full tube angle 4 |
| `spf-product-1-v2-compressed.jpg` | Styled hero |
| `spf50-product-color-1.jpg` | Cap + body color close-up |
| `spf50-product-color-2.jpg` | Cap + body color close-up |
| `spf50-product-color-3.jpg` | Color/texture |
| `spf50-product-color-4.jpg` | Color/texture |
| `spf50-product-color-5.jpg` | Color/texture |
| `spf50-product-color-6.jpg` | Color/texture |
| `spf-buy2-get1.png` | Bundle (3 tubes) |
| `spf-buy2-getmini.png` | Bundle variant |

All URLs: `https://cdn.shopify.com/s/files/1/0944/6339/4141/files/<filename>?v=<version>`
(versions listed in Shopify product media, handle: `spf-face`).

---

## Reference images (product fidelity — ALWAYS attach)
Use these in every job so the tube/label stays consistent:
- Primary (clean white-bg tube): `https://cdn.shopify.com/s/files/1/0944/6339/4141/files/cobacco-product-imgs-1000x1000-SPF-1.png?v=1758013041`
- Cap close-up 1: `https://cdn.shopify.com/s/files/1/0944/6339/4141/files/spf50-product-color-1.jpg?v=1758013041`
- Cap close-up 2: `https://cdn.shopify.com/s/files/1/0944/6339/4141/files/spf50-product-color-2.jpg?v=1772013863`
- Styled hero: `https://cdn.shopify.com/s/files/1/0944/6339/4141/files/spf-product-1-v2-compressed.jpg?v=1772013863`
- Bundle 2+gift / 2+3rd-free reference: `https://cdn.shopify.com/s/files/1/0944/6339/4141/files/spf-buy2-get1.png?v=1758013041`

Product description (for prompt grounding): COBACCO SPF 50+ face serum & primer, 30ml.
**Tube:** soft mint-green body fading to white at the base, with a lilac/lavender accent stripe.
**Nozzle:** narrow pointed dispensing tip at the bottom (squeeze tube — user squeezes from
the bottom, product comes out through a pointed white nozzle tip). NOT a pump. NOT a flip cap.
**Label reads:** "COBACCO · Invisible protection & Lightweight feel · SPF 50+ · FACE SERUM &
PRIMER · 30ML · Moisturising · All skin types"
**Serum texture/color:** warm golden-amber gel, visibly pigmented and glossy — NOT transparent,
NOT white. When applied to skin it appears as a rich golden drop that blends to invisible finish.

---

## Generation order

### ▶ CB-004 — Hero product static (DO THIS FIRST, validate before continuing)
- Higgsfield: **Generate Image** (MCP) / `product_shot` (skill)
- Aspect: 1:1 (1080×1080), resolution 2k
- Reference: primary + secondary
- Prompt intent: Single tube standing upright on pale stone/beige surface, soft natural
  daylight, gentle shadow, one subtle water droplet, premium minimal skincare aesthetic.
  Clean — NO text overlay (text added later). Match reference tube shape, colors, label exactly.
- Gate: approve product realism before any other job runs.

### CB-001 — SPF texture demo (video)
- Higgsfield: **Generate Video** (image-to-video from CB-004 still, or Marketing Studio)
- Aspect: 9:16, 15–30s, hook in first 3s
- Reference: primary product image
- Intent: fingertip/serum texture absorbing into skin, no white cast; BG text overlay
  "Слънцезащита, която не се усеща" added in post.

### CB-002 — UGC application demo (video)
- Higgsfield: **Marketing Studio** (avatar/presenter) or Generate Video
- Aspect: 9:16, 20–45s, handheld UGC feel
- Reference: primary product image
- Intent: woman applying SPF in natural home light, authentic non-polished; BG captions in post.

### CB-003 — 2-in-1 primer carousel (statics ×4–5)
- Higgsfield: **Generate Image** / `social_carousel`, count 4–5
- Aspect: 1:1
- Reference: primary product image
- Intent: cover hook → problem → solution → social proof → CTA. Copy per market (BG/SK/CZ)
  added in post — see Localization Reference v2.

### CB-005 v2 — Bundle 2+3rd-free static
- Higgsfield: **Generate Image** / `product_shot`
- Aspect: 9:16 (primary) + 1:1
- Reference: bundle reference (`spf-buy2-get1.png`) + primary
- Intent: three tubes, 3rd tagged FREE/ПОДАРЪК. Per-market price + savings added in post
  (BG €40.80 / SK €48.99 −33% / CZ 1 200 Kč). NEVER reuse one market's price for another.

### CB-006 — Beauty Skin Routine Box upsell static
- Higgsfield: **Generate Image** / `lifestyle_scene`
- Aspect: 1:1
- Reference: pull Beauty Box image from Shopify (product handle: resurfacer-spf-face-bundle
  or the Beauty Skin Routine Box product) before generating.
- Intent: routine flat-lay, warm aspirational; "Вече познаваш COBACCO" overlay in post.

### CB-007 v2 — ATC abandoner urgency static
- Higgsfield: **Generate Image** / `product_shot`
- Aspect: 9:16 + 1:1
- Reference: primary product image
- Intent: single tube + cart/urgency motif; bundle upsell nudge. Copy + price in post.

---

## Post-production (not Higgsfield)
Text overlays, prices, savings %, CTAs, and per-market localization are added AFTER generation
(Canva/editor). Higgsfield produces clean visuals; copy is layered per the briefs + Localization
Reference v2. Free-shipping lines: BG "над €30" · SK "nad €35" · CZ "nad 500 Kč" · DE "ab €35".

## Specs recap
- All video: 9:16, thumb-stop in first 2s (88% mobile traffic).
- All statics: deliver 1:1 + 9:16 where noted.
- Resolution: 2k for all product-photoshoot jobs.
- Frequency cap target < 2.5; refresh creative every 3–4 weeks.

## Drive locations
- Folder: COBACCO Meta Ads Campaign → Creative Briefs (sub-folder)
- Briefs: CB-001…CB-004, CB-005 v2, CB-006, CB-007 v2
- Localization Reference v2, Shipping Reference v2 (current truth)
- Campaign Tracker sheets: Tabs 1–4 (log output URLs in Tab 4 Creative Tracker)
