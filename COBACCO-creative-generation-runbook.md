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
- **⚠️ CANONICAL entity (as of 2026-06-03):** `400b1f5d-6483-4de3-ad83-9b7adaa08fb0` — rebuilt with all 13 Shopify images + corrected clear-gel/ribbed-nozzle description. Use this for all new Marketing Studio jobs.
- **DEPRECATED:** `66923fab-36ee-4e72-92e2-94236c87ac38` (wrong "golden-amber gel" description — do not use)
- **DEPRECATED:** `0afd4ba7-b57b-42b9-bef0-4cc46be16929` (wrong "flip cap" description — do not use)
- **DEPRECATED:** `91238a80-5b4a-472c-9c79-cca9a79e2f7b` (lean 3-image entity — deprecated in favour of full 13-image rebuild)
- For raw image/video generation (non-Marketing-Studio), attach references manually (see below).

### Step 2 — Confirm reference images cover all three accuracy axes
Before generating, verify the reference set visually includes:
- [ ] **Nozzle** — narrow pointed white **ribbed/threaded** dispensing tip at the bottom of the tube (squeeze tube). NOT a pump, NOT a flip cap, NOT a wide opening. ✅ confirmed correct.
- [ ] **Tube body color** — soft mint-green fading to white at base, with a lilac/lavender accent stripe
- [ ] **Serum color & texture** — **clear, transparent, colorless glossy gel** (like a thick water-gel). NOT golden, NOT amber, NOT white, NOT pigmented. It reads glassy/see-through on skin.

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
**Serum texture/color:** clear, transparent, colorless glossy gel — a thick water-gel that
streams from the nozzle and reads glassy/see-through on skin. NOT golden, NOT amber, NOT white,
NOT pigmented. Blends to an invisible, luminous finish.

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

---

## Localized Video Pipeline (generate → QC → localize → mux)

> This section replaces the ad-hoc approach used in CB-001/CB-002. Follow this
> pipeline for every new video creative. It enforces product fidelity, automated QC,
> and real Bulgarian localization (not Higgsfield TTS, which cannot speak Bulgarian).

### Core rule — Seedance-first for product accuracy
Avatar/text-to-video models **regenerate** the product and morph the nozzle.
**Always use `seedance_2_0` with `start_image` = a real Shopify photo for any shot
where the product or nozzle is visible.** Use Marketing Studio (avatar) only for
wide/medium talking segments where the tube is not the focal subject, and back-cut
to Seedance B-roll for any close-up.

**Format: VO-over-B-roll.** Most shots are Seedance product B-roll + Bulgarian
voiceover on top. No visible speaking mouth → BG audio syncs perfectly.

### Stage 0 — Real product pixels
Pull real product URLs from Shopify (`get-product`, handle `spf-face`). The 13-image
table in "Full Shopify reference image set" above is the source of truth.

### Stage 1 — (Re)build the canonical Marketing Studio entity
Run once (or when Shopify images change):
- `show_marketing_studio` action=create, type=product
- Upload all ~13 images (use `media_upload` for each, then pass media IDs)
- Description (verbatim): "Mint-green squeeze tube fading to white at base, lilac/lavender
  accent stripe. POINTED WHITE RIBBED nozzle tip at the BOTTOM (squeeze tube — user
  squeezes from the bottom, serum exits through a narrow pointed white nozzle tip).
  NOT a pump, NOT a flip cap. Serum is CLEAR TRANSPARENT COLORLESS glossy gel — a thick
  water-gel that reads glassy/see-through on skin. NOT golden, NOT amber, NOT white,
  NOT pigmented. Label: COBACCO · Invisible protection & Lightweight feel · SPF 50+ ·
  FACE SERUM & PRIMER · 30ML · Moisturising · All skin types."
- Canonical entity ID: `400b1f5d-6483-4de3-ad83-9b7adaa08fb0` (created 2026-06-03, 13 images).
  Rebuild only if Shopify product images change significantly.

### Stage 2 — Generate B-roll (Seedance image-to-video)
```
generate_video(
  model="seedance_2_0",
  start_image="<real Shopify photo URL or uploaded media ID>",
  aspect_ratio="9:16",
  duration=10,
  prompt="<shot description — product animation, no speaking presenter>"
)
```
Poll `job_display` until `completed`. Generate 2–4 B-roll clips per brief.

### Stage 3 — Automated QC gate
1. **Engagement:** Run `virality_predictor` on completed clip. Use `scripts/qc_gate.py`
   to check scores against thresholds: hook ≥70 / attention ≥65 / retention ≥60 /
   creative ≥65 / distraction low.
2. **Fidelity (binary):** Extract frames with imageio-ffmpeg (or `python3 -c "import imageio_ffmpeg; ..."`),
   Read them, verify against the three accuracy axes: ribbed nozzle at bottom / mint-green
   body / clear transparent colorless gel. Morphed nozzle or wrong gel color = automatic fail.
3. On fail: re-submit Seedance i2v from a different real photo angle. Max 3 attempts.
   Log each attempt's job ID + scores in the CB brief's Generation history table.

### Stage 4 — Assemble
- `upscale_video` approved clips; `reframe` to 9:16 if needed.
- Concatenate multi-shot B-roll with ffmpeg (imageio-ffmpeg):
  ```
  ffmpeg -f concat -safe 0 -i shots.txt -c copy build/assembled.mp4
  ```
  where `shots.txt` is a list of `file 'build/clip_01.mp4'` lines.

### Stage 5 — Bulgarian voiceover (ElevenLabs, PATH A)
**Prerequisites** (user must do these; agent cannot):
1. Add `api.elevenlabs.io` to the environment network allowlist.
2. Set `ELEVENLABS_API_KEY` env var.

Verify before running:
```bash
curl -sS -m 10 -o /dev/null -w "%{http_code}" https://api.elevenlabs.io/v1/models
echo $ELEVENLABS_API_KEY | cut -c1-4  # should print first 4 chars, not blank
```

Generate BG VO:
```bash
python3 scripts/elevenlabs_bg_vo.py \
  --text-file scripts/vo_bg_cb002.txt \
  --out build/vo_bg_cb002.mp3
```
Model: `eleven_multilingual_v2`, `language_code: bg`, voice: Aria (female multilingual).
Override `--voice <id>` for a different ElevenLabs voice.

**PATH B fallback (if network blocked):** The VO script text is committed in
`scripts/vo_bg_cb002.txt`. Generate MP3 on your machine via ElevenLabs web UI or
any TTS tool supporting Bulgarian, then proceed to Stage 6.

### Stage 6 — Mux + verify
```bash
python3 scripts/mux_bg_vo.py \
  --video build/assembled.mp4 \
  --audio build/vo_bg_cb002.mp3 \
  --out build/out_bg_cb002.mp4
```
Verification:
- `ffprobe -v error -show_entries format=duration -of csv=p=0 build/out_bg_cb002.mp4`
  → compare to video duration, assert |Δ| < 0.5s.
- Extract frame: `python3 -c "import imageio_ffmpeg, subprocess; subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-i', 'build/out_bg_cb002.mp4', '-vf', 'fps=1', 'build/frame_%03d.png'])"`.
  Read `build/frame_001.png`, `build/frame_005.png` → confirm product fidelity visually.
- Confirm audio is non-silent and Bulgarian.
- Run final `virality_predictor` on `build/out_bg_cb002.mp4`; log scores in the CB brief.

### Scripts reference
| Script | Purpose |
|---|---|
| `scripts/elevenlabs_bg_vo.py` | ElevenLabs TTS → `build/vo_bg_<cb>.mp3` |
| `scripts/mux_bg_vo.py` | ffmpeg mux VO onto silent video |
| `scripts/qc_gate.py` | Virality predictor QC gate thresholds |
| `scripts/vo_bg_cb002.txt` | CB-002 Bulgarian VO script |
| `build/` | Working artifacts (gitignored) |

---

## Drive locations
- Folder: COBACCO Meta Ads Campaign → Creative Briefs (sub-folder)
- Briefs: CB-001…CB-004, CB-005 v2, CB-006, CB-007 v2
- Localization Reference v2, Shipping Reference v2 (current truth)
- Campaign Tracker sheets: Tabs 1–4 (log output URLs in Tab 4 Creative Tracker)
