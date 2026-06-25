# ML / Research Scientist Job Search Plan

> **Companion to:** [`lc` branch](https://github.com/JingyaLiu/Learning-Vault/tree/lc) → LeetCode / general coding (`INTERVIEW_PLAN.md`)  
> **Inspired by:** [Alisa's industry job search notes](https://alisawuffles.github.io/blog/job-search/)  
> **Start here (employed):** [Employed Track](#employed-track--jul-2026--nov-2026-start-here) → **[Prep by target tier](#prep-by-target-tier)**  
> **Weekly tasks:** [THIS_WEEK.md](THIS_WEEK.md) · **Start here (full-time prep):** [Phase 1](#phase-1--foundations-weeks-1–4)

**Last updated:** July 2026  
**Profile:** **Jingya Liu** · Staff DS @ Walmart · [LinkedIn](https://www.linkedin.com/in/jingya-tina-liu/) · ~12–14 hrs/week · offer **Oct–Nov 2026**  
**Target areas:** **R** retrieval/ranking/search · **X** CX FM · **P** pretraining · **T** post-training  
**Legend:** 🔴 = highest ROI · 🟡 = common · ⚪ = company-specific · ✅ = milestone

---

## Employed Track — Jul 2026 → Nov 2026 (START HERE)

**Why this calendar:** Tech hiring peaks **Sep–Oct**. Jul–Aug is slow (vacations) but ideal for **prep + referrals**. Employed ML/RS searches realistically take **4–6 months** ([data](https://asmekal.github.io/blog/posts/interviews-2025-ml-research-engineer-uk)).

```
Jul–Aug        Sep–Oct           Oct–Nov
prep+referrals → interview peak  → offers / sign
practice loops   target onsites
```

### Targets

| Milestone | Date | Done |
|---|---|---|
| 15-company list + pitch draft | Jul 13 | [ ] |
| 8 behavioral STAR stories | Jul 20 | [ ] |
| attention + MHA in < 45 min | Jul 27 | [ ] |
| First batch of referrals sent (≥5) | Jul 31 | [ ] |
| First phone screen | Aug 31 | [ ] |
| ≥2 companies in pipeline | Sep 15 | [ ] |
| First onsite | Sep 30 | [ ] |
| First written offer | Oct 31 | [ ] |
| Signed offer | Nov 15 | [ ] |

### Weekly time budget (~12–14 hrs)

| Slot | Time | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|---|
| **LC** | 60 min | ⭐⭐ | — | ⭐⭐ | — | ⭐⭐ | — | re-solve |
| **ML** | 60 min | — | drill | — | drill | — | **3 hr** | — |
| **Process** | 30–60 min | — | — | outreach | — | — | — | **2 hr** |
| **Rapid-fire** | 15 min | — | 10 Qs | — | 10 Qs | — | — | — |

**Rules**
- ML coding drills: **no AI**
- **Never skip Sunday process block** in Jul–Aug (referrals > one more problem)
- **Study follows active tier** — see [Prep by target tier](#prep-by-target-tier); don't spread four pillars equally
- Interview season (Sep+): cram for **the tier + pillar of the active interview** only
- Tell recruiters you're employed; you need **≥1 week** between rounds

---

## Prep by target tier

Your pipeline has **33 rows** in three tiers — prep intensity should **not** be equal across them. Oct–Nov offer depends on **Primary** targets; **Dream** is a second wave.

### Tier map (from [process-tracker](../job-search/process-tracker.md))

| Tier | When | Roles | Oct–Nov offer? | Jul–Aug prep share | Lead pillars |
|---|---|---|---|---|---|
| 🏋️ **Practice** | Aug | Glean, Sierra, Databricks, AI2, … (14) | No — format calibration | **Match that company's pillar** for 1 week before apply | R, X, or T each |
| 🎯 **Primary** | Sep | Amazon ×3, Microsoft ×2, Apple Search/Siri, Snowflake ×2 (9) | **Yes — 85% of study time** | R + X + T | **R** **X** **T** |
| 🎯 **Stretch local** | Sep | Apple FM, Google ×2, NVIDIA, ByteDance (5) | Possible Nov | **15% from Aug W3** | **P** + T |
| ⭐ **Dream** | Oct+ | Meta Llama, MSR, OpenAI, Anthropic, DeepMind (5) | Dec+ or parallel | **30 min/wk skim** until Oct; ramp if Primary offers | **P** **T** |

**Primary cluster (optimize for these):**

| Pillar | Companies | Your proof | Must-have by Aug 31 |
|---|---|---|---|
| **R** | Amazon Ads, Amazon Search, Microsoft Ads, Apple Search, Snowflake Retrieval, Glean | Ads retrieval | Pitch **R** + §G-R 80% · §D Amazon cram |
| **X** | Microsoft Copilot, Apple Siri, Sierra, Snowflake Agents, Amazon Sandstone | CX FM | Pitch **X** + §G-X 80% · §D Microsoft cram |
| **T** | Amazon Ads, Microsoft Copilot, Databricks, NVIDIA NeMo | CX FM post-train | Pitch **T** + §G-T 70% · CS336 Lec 15–16 |

**Stretch cluster (don't front-load — Aug W3+):**

| Pillar | Companies | Extra prep |
|---|---|---|
| **P** | Apple FM, Google Cloud AI, AI2, Meta Llama | CS336 Lec 7–9, 13–14 · §G-P · pitch **P** · 2 OLMo/Llama papers |
| **P+T** | ByteDance, NVIDIA NeMo | Above + alignment stack skim |

**Dream cluster (Oct+ unless spare bandwidth):**

- Apply after ≥1 Primary phone screen OR Sep 30
- 1 hr/wk: one paper + pitch **P** maintenance
- Accept timeline may slip to **Dec–Jan** for Meta/OpenAI

### Weekly time mix by phase (~12–14 hr total)

LC block (~3 hr/wk) is fixed. **ML + rapid-fire + process** blocks follow tier:

```
              Primary (R+X+T)   Stretch (P)   Dream    LC
Jul           55%               5%            —        40%
Aug W1–2      50%               10%           —        40%
Aug W3–4      45%               20%           5% skim  30%
Sep*          active interview pillar only    30 min   maintenance
Oct+          maintenance                     ramp P   maintenance

* Sep: drop new CS336; §D cram + mock for scheduled company only
```

Within **Primary** ML time (Jul–Aug):

```
        R (retrieval)   X (CX FM)   T (post-train)   fundamentals
Jul     35%             35%         25%              5%
Aug     30%             30%         35%              5%
```

**P** is **not** in the Primary mix — only in Stretch blocks (Sat Aug W3+, or 30 min Thu when no Primary interview).

### Tier → weekly focus (Jul–Aug)

| Week | Primary track (always) | Practice / apply | Stretch (optional) |
|---|---|---|---|
| Jul W1 | CS336 Lec 1–3 · pitch **R** + **X** | Map pipeline tiers | — |
| Jul W2 | attention/MHA drills · behavioral | 2 referrals | — |
| Jul W3 | mini LM · pitch **R** recorded | Amazon warm outreach | — |
| Jul W4 | §G-R + §G-X · KV cache | 3 referrals | — |
| Aug W1 | transformer timed · **T** Lec 15–16 | §D Glean (**R**) + Databricks (**T**) · 1 mock | — |
| Aug W2 | drill rotation · §G-X | Apply Sierra (**X**) or Glean | §G-P skim (30 min) |
| Aug W3 | §D **Amazon Ads (R)** · warm intro | Apply + journal | Apple FM / Lec 7–9 (1 hr Sat) |
| Aug W4 | §D **Microsoft (X)** + Snowflake | Apply Amazon + Microsoft | pitch **P** draft (30 min) |

### Interview-season rule (Sep+)

When a company is scheduled, **only** prep that row's tier + pillars:

| If interviewing… | Tier | Cram | Pitch | LC night before |
|---|---|---|---|---|
| Amazon Ads | Primary | §D Amazon · §G-R | **R** + **T** | 1 medium LC |
| Microsoft Copilot | Primary | §D Microsoft · §G-X | **X** + **T** | 1 medium LC |
| Apple Search | Primary | §D Apple · §G-R | **R** | 1 medium LC |
| Apple FM | Stretch | §D Apple · §G-P | **P** + **X** | ML drill only |
| Meta Llama | Dream | §G-P + paper | **P** + **T** | ML drill only |
| Glean / Sierra | Practice | §D that company | matching pillar | 1 easy LC |

**Pitch variants:** [research/pitch-template.md](../research/pitch-template.md#pitch-variants-by-pillar)  
**Cram sheets:** [technical-discussion/notes.md](../technical-discussion/notes.md) §D–§G  
**Verified roles:** [LINKEDIN_ROLE_SCAN.md](../job-search/LINKEDIN_ROLE_SCAN.md)

---

## Four-pillar reference (what each pillar means)

### The four pillars

| Pillar | What you want | Walmart proof | Top companies in pipeline | Study focus |
|---|---|---|---|---|
| **R — Retrieval / ranking / search** | Large-scale IR, ads, enterprise search | Ads retrieval phase | Amazon Ads, Google Kirkland, Glean, SeekOut, Perplexity | §G-R · pitch **R** · LC medium-high |
| **X — CX foundation model** | Domain FM for customer experience | CX FM + seller agent | Sierra, Decagon, Microsoft, ServiceNow, Snowflake | §G-X · pitch **X** · eval + data mix |
| **P — Pretraining** | Data, scale, architecture, open models | PhD + FM scale story; gap = industrial pretrain | AI2, Meta, OpenAI, Google DeepMind, Hugging Face | CS336 Lec 7–9, 13–14 · §G-P · pitch **P** |
| **T — Post-training** | SFT, RLHF/DPO/GRPO, alignment, eval | CX FM post-train pipeline | Databricks, Scale, Cohere, NVIDIA NeMo, Reddit | CS336 Lec 15–16 · §G-T · pitch **T** |

**Your unified story:** Same Walmart arc — retrieval (**R**) → domain CX FM (**X**) built with post-train (**T**); PhD + citations support pretrain labs (**P**) when targeting Stretch/Dream.

### What to deprioritize

| Topic | Why |
|---|---|
| Pure CV / OD trivia | One 60-sec bridge only — lead **R/X/T/P** |
| Generic "agentic" framing | Reframe as **X** (domain FM) or **R** (search grounding) |
| CS336 A2–A5 systems | Optional unless **P** infra interview |
| Medical imaging depth | PhD hook only |

### Application order (by tier)

```
Aug practice   Glean (R) · Sierra (X) · Databricks (T) — 1 mock each format
Aug referral   Amazon Ads LI 4173762699 (Primary R) — warm path first
Sep Primary    Microsoft Copilot · Amazon Ads · Apple Search · Snowflake Retrieval
Sep Stretch    Apple FM · Google Cloud AI · NVIDIA NeMo · ByteDance
Oct Dream      Meta Llama Bellevue · DeepMind · OpenAI/Anthropic (if Primary moving)
```

**Re-scan monthly:** [LINKEDIN_ROLE_SCAN.md](../job-search/LINKEDIN_ROLE_SCAN.md)

### 3-day cram by pillar

**R — Retrieval/search:** dual-tower vs cross-encoder · ANN recall@k · NDCG vs recall tradeoff · negative sampling · cold start · latency budget · embedding refresh · online A/B · your ads metric · search + LLM (RAG as retrieval)  
**X — CX FM:** domain data curation · SFT mix for CX · offline eval suite · online guardrails · FM vs prompt-only · seller/advertiser vs consumer CX · failure cases · metric `___` · scaling domain data  
**P — Pretrain:** Chinchilla / compute-optimal · data dedup & mixing · tokenizer choice · scaling laws intuition · architecture choices (dense vs MoE) · stability (loss spikes) · what you'd pretrain differently · OLMo/Llama skim · your PhD → pretrain bridge  
**T — Post-train:** SFT pipeline · DPO vs PPO vs GRPO · reward hacking · KL penalty · preference data · eval contamination · RLHF at scale · your CX FM post-train choices · NeMo/Mosaic skim

---

## July 2026 — Primary track prep + pipeline

**Theme:** ML fundamentals + **R/X pitches** + referrals. No Stretch/Dream prep yet (no **P** block).

### Jul W1 · Jul 7–13 — Map Primary targets

**Track:** 🎯 Primary (**R** + **X**) · Stretch/Dream deferred

| Block | Task | File | Done |
|---|---|---|---|
| LC ×3 | Two Sum (1), Valid Anagram (242), Group Anagrams (49) | `lc` hash-maps | [ ] |
| ML ×2 | CS336 Lec 1–2 (1.25×); skim shape conventions | [ml-coding/notes.md](../ml-coding/notes.md) | [ ] |
| ML Sat | Lec 3 + draw decoder-only architecture from memory | CS336 | [ ] |
| Rapid-fire | §G-R (10 Qs) Thu | [technical-discussion/notes.md](../technical-discussion/notes.md) | [ ] |
| Process Sun | Tag pipeline rows: 🏋️ / 🎯 Primary / 🎯 Stretch / ⭐ | [process-tracker.md](../job-search/process-tracker.md) | [ ] |
| Process Sun | Pitch **R** + **X** — 2 min each **with 1 metric each** | [pitch-template.md](../research/pitch-template.md) | [ ] |

### Jul W2 · Jul 14–20 — ML drills + outreach

**Track:** Primary fundamentals · first referrals

| Block | Task | Done |
|---|---|---|
| LC ×3 | Valid Palindrome (125), Two Sum II (167), 3Sum (15) | [ ] |
| ML ×2 | [01_attention.py](../ml-coding/drills/01_attention.py) → [02_mha.py](../ml-coding/drills/02_mha.py) | [ ] |
| ML Sat | Lec 4 + Illustrated GPT-2; timed attention 45 min | [ ] |
| Process Sun | Behavioral stories 1–4 | [behavioral/story-bank.md](../behavioral/story-bank.md) | [ ] |
| Process Sun | Send **2** outreach — **Amazon Ads (Primary R)** priority | [ ] |

### Jul W3 · Jul 21–27 — Mini LM + pitch R

**Track:** Primary **R** deep · warm path

| Block | Task | Done |
|---|---|---|
| LC ×3 | Longest Substring (3), Min Window (76), Container Water (11) | [ ] |
| ML ×2 | [03_transformer_block.py](../ml-coding/drills/03_transformer_block.py) → [04_mini_lm.py](../ml-coding/drills/04_mini_lm.py) | [ ] |
| ML Sat | Causal loss + AdamW; record **pitch R** (2 min) | [practice-log.md](../ml-coding/practice-log.md) | [ ] |
| Process Sun | Behavioral stories 5–8 + question map | [ ] |
| Process Sun | Amazon warm intro OR 2nd referral | [ ] |

### Jul W4 · Jul 28 – Aug 3 — R+X rapid-fire + referrals

**Track:** Primary **R** + **X** · still no **P**

| Block | Task | Done |
|---|---|---|
| LC ×3 | Merge Intervals (56), Meeting Rooms II (253), Product Except Self (238) | [ ] |
| ML ×2 | Lec 10 concepts; [05_greedy_decode.py](../ml-coding/drills/05_greedy_decode.py); KV cache aloud | [ ] |
| ML Sat | §G-R + §G-X (10 Qs each); record **pitch X** (2 min) | [technical-discussion/notes.md](../technical-discussion/notes.md) | [ ] |
| Process Sun | Read [negotiation/playbook.md](../negotiation/playbook.md) once | [ ] |
| Process Sun | Send **3** referrals (≥1 Amazon); LinkedIn Walmart bullets for **R** + **X** | [ ] |

**July exit criteria (Primary track)**
- [ ] attention + MHA < 45 min
- [ ] pitch **R** + **X** recorded with metrics
- [ ] 8 STAR stories complete
- [ ] ≥5 referrals sent (Amazon warm path started)
- [ ] Pipeline tiers tagged in process-tracker

---

## August 2026 — Practice loops + Primary apply prep

**Theme:** 🏋️ Practice calibrates format · 🎯 Primary crams · 🎯 Stretch **P** starts W3 only.

### Aug W1 · Aug 4–10

**Track:** Primary **T** + 🏋️ Practice (**R** + **T**)

| Block | Task | Done |
|---|---|---|
| LC ×3 | Reverse LL (206), LRU Cache (146), Max Depth (104) | [ ] |
| ML ×2 | **Timed:** full transformer forward 90 min | [ ] |
| ML Sat | Lec 15–16 (SFT/RLHF) + GRPO — pillar **T** | [ ] |
| Process Sun | §D cram: **Glean (R)** + **Databricks (T)** | [technical-discussion/notes.md](../technical-discussion/notes.md) | [ ] |
| Process Sun | **1 mock** research chat (self-recorded, Primary **R** pitch) | [ ] |

### Aug W2 · Aug 11–17

**Track:** Primary **X** + 🏋️ apply Sierra

| Block | Task | Done |
|---|---|---|
| LC ×3 | Level Order (102), Validate BST (98), LCA (236) | [ ] |
| ML ×2 | Drill rotation; §G-X CX FM (10 Qs) | [ ] |
| ML Sat | §G-T post-train (10 Qs); optional §G-P skim **30 min only** | [ ] |
| Process Sun | Apply **Sierra (X)** or **Glean (R)** — practice tier | [ ] |
| Process Sun | **1 external mock** (friend/colleague, 45 min) if available | [ ] |

### Aug W3 · Aug 18–24

**Track:** Primary **R** (Amazon) + Stretch **P** intro

| Block | Task | Done |
|---|---|---|
| LC ×3 | Number of Islands (200), Course Schedule (207), Clone Graph (133) | [ ] |
| ML ×2 | Drill rotation; §D **Amazon Ads (R)** cram | [ ] |
| ML Sat | **Stretch:** CS336 Lec 7–9 (1 hr) + skim Apple FM role | [ ] |
| Process | Amazon warm intro + apply if referral ready | [ ] |
| Process Sun | [interview-journal.md](../job-search/interview-journal.md) after any screen | [ ] |

### Aug W4 · Aug 25–31

**Track:** Primary **X** apply + Stretch pitch **P** draft

| Block | Task | Done |
|---|---|---|
| LC ×3 | Kth Largest (215), Top K (347), Merge K Lists (23) | [ ] |
| ML ×2 | §D **Microsoft Copilot (X)** + **Snowflake (R/X)** | [technical-discussion/notes.md](../technical-discussion/notes.md) | [ ] |
| ML Sat | Mock ML coding + pitch **X** aloud; draft pitch **P** (30 min) | [ ] |
| Process Sun | Apply: **Microsoft Copilot** + **Amazon Ads** (Primary) | [ ] |

**August exit criteria**

| Tier | Must hit by Aug 31 |
|---|---|
| 🎯 **Primary** | Transformer 90 min · pitch **R** + **X** + **T** fluent · §G-R/X/T ≥ 70% · ≥1 practice loop done |
| 🏋️ **Practice** | ≥2 applications · 1 mock · journal entry |
| 🎯 **Stretch** | pitch **P** outline · Lec 7–9 watched · §G-P ≥ 50% |
| ⭐ **Dream** | Not required — do not apply yet unless Primary screens active |

---

## September 2026 — Interview peak (tier-driven)

**Theme:** Prep **only** for scheduled interviews. Primary first; Stretch if scheduled; Dream only if bandwidth.

### Weekly rhythm (interview season)

| Day | Active Primary interview | Active Stretch interview | No interview |
|---|---|---|---|
| Weekday 30 min | §D + §G for **that** pillar | + §G-P if Apple FM / Google | 1 ⭐⭐ LC re-solve |
| Weekday 30 min | Pitch rehearsal (matching pillar) | pitch **P** add-on | 10 rapid-fire (weakest §G) |
| Saturday 2 hr | Mock + ML drill for active tier | Lec 13–14 if **P** interview | 1 ML maintenance drill |
| Sunday 1 hr | [interview-journal](../job-search/interview-journal.md) | — | Outreach follow-up |

### September milestone weeks

| Week | Interview goal | Study (by tier) | Done |
|---|---|---|---|
| Sep W1 | Finish 🏋️ practice loop | Primary weak spots from journal | [ ] |
| Sep W2 | ≥1 **Primary** phone screen | §D for that company only | [ ] |
| Sep W3 | ≥2 **Primary** parallel processes | Behavioral mock 30 min | [ ] |
| Sep W4 | First Primary onsite | Job-talk if needed; Stretch apply if ready | [job-talk/outline.md](../job-talk/outline.md) |
| Sep W4+ | Optional **Stretch** screen (Apple FM / Google) | §G-P cram | [ ] |

**September exit criteria**
- [ ] ≥2 **Primary** companies in pipeline
- [ ] ≥1 Primary onsite completed
- [ ] Journal entry for every round
- [ ] **Dream** applications: 0–2 max unless Primary stalled

---

## October 2026 — Onsites + offers

| Week | Focus | Done |
|---|---|---|
| Oct W1–2 | Concentrated onsites; cram day before each | [ ] |
| Oct W3 | First verbal/written offer → [negotiation/playbook.md](../negotiation/playbook.md) | [ ] |
| Oct W4 | Align offer deadlines; teammate 1:1s | [ ] |

**October exit criteria**
- [ ] ≥1 written offer in hand
- [ ] Negotiation script used at least once

---

## November 2026 — Decide + sign

| Task | Done |
|---|---|
| Compare offers (base / equity / vest / level) | [ ] |
| Finalize level + comp; get written final | [ ] |
| **Sign** (target Nov 15) | [ ] |
| Plan resignation notice period | [ ] |

---

## LC accelerated path (employed)

Skip full Pass 1–3. Finish the ⭐⭐ list below by **Aug 31**.

| # | Problem | LC | By |
|---|---|---|---|
| 1 | Two Sum | 1 | Jul W1 |
| 2 | Valid Parentheses | 20 | Jul W4 |
| 3 | Longest Substring | 3 | Jul W3 |
| 4 | Min Window | 76 | Jul W3 |
| 5 | 3Sum | 15 | Jul W2 |
| 6 | Container Water | 11 | Jul W3 |
| 7 | Product Except Self | 238 | Jul W4 |
| 8 | Merge Intervals | 56 | Jul W4 |
| 9 | Meeting Rooms II | 253 | Jul W4 |
| 10 | Binary Search | 704 | done (`lc`) |
| 11 | Search Range | 34 | done (`lc`) |
| 12 | Search Rotated | 33 | Aug W2 |
| 13 | Reverse Linked List | 206 | Aug W1 |
| 14 | LRU Cache | 146 | Aug W1 |
| 15 | Number of Islands | 200 | Aug W3 |
| 16 | Course Schedule | 207 | Aug W3 |
| 17 | Max Depth / Level Order | 104/102 | Aug W2 |
| 18 | Validate BST | 98 | Aug W2 |
| 19 | LCA | 236 | Aug W2 |
| 20 | Kth Largest | 215 | Aug W4 |
| 21 | Top K Frequent | 347 | Aug W4 |
| 22 | Merge K Lists | 23 | Aug W4 |
| 23 | Subsets | 78 | Sep W1 |
| 24 | Combination Sum | 39 | Sep W1 |
| 25 | Climbing Stairs | 70 | Sep W1 |
| 26 | House Robber | 198 | Sep W2 |
| 27 | Coin Change | 322 | Sep W2 |
| 28 | Word Break | 139 | Sep W2 |
| 29 | LIS | 300 | Sep W3 |
| 30 | Trapping Rain Water | 42 | Sep W3 |
| 31 | Word Ladder | 127 | Sep W4 |

**Sep+:** Re-solve only, no new problems. Night before interview: 1 ⭐⭐ cold solve.

---

## ML skill milestones (by tier)

| Date | Tier | Must hit | How to verify |
|---|---|---|---|
| Jul 27 | Primary | attention + MHA | timed drills |
| Jul 31 | Primary | pitch **R** + **X** with metrics | recorded 2 min each |
| Aug 10 | Primary | mini LM + loss | [04_mini_lm.py](../ml-coding/drills/04_mini_lm.py) |
| Aug 10 | Primary | pitch **T** outline | 2 min recorded |
| Aug 24 | Primary | full transformer 90 min | blank file timed |
| Aug 31 | Primary | §G-R + §G-X + §G-T ≥ 70% | pillar rapid-fire |
| Aug 31 | Stretch | §G-P ≥ 50% · pitch **P** outline | 10 Qs + 2 min draft |
| Aug 31 | Practice | ≥1 real/practice loop | journal |
| Sep 15 | Active interview | §D cram matches scheduled tier | company row |
| Oct 1 | Dream | pitch **P** fluent · 2 papers | if Meta/OpenAI scheduled |
| Ongoing | Primary | KV cache + decoding explainable | whiteboard |

**CS336 (employed — by tier):**
- **Primary (all):** Lec 1–4, 10, 15–16
- **Stretch only:** Lec 7–9, 13–14
- **Dream only:** A2–A5 skim optional

---

## Interview-season weekly checklist

Copy to your calendar; check off every Sunday:

```
[ ] Update process-tracker
[ ] Catch up interview-journal
[ ] Follow up ≥2 stale threads
[ ] 1 ML drill or 1 ⭐⭐ re-solve
[ ] Next-round cram sheet drafted
[ ] ≥7h sleep night before any interview
```

---

## Low-energy days (employed)

| State | Do | Not a failure |
|---|---|---|
| Normal day | 60 min LC **or** ML + rehearse pitch on commute | — |
| Overtime day | 10 rapid-fire Qs only | Skip LC |
| Interview day | Cram + sleep only | Skip all new material |
| Half weekend | Process Sun block first | Defer ML Sat |

---

## Relationship to the 12-week plan

| Original phase | Employed track |
|---|---|
| Phase 1 (4 wk) | **Jul** — compressed to 4 weeks |
| Phase 2 (4 wk) | **Aug** — drill rotation + mocks |
| Phase 3 (4 wk) | **Sep** — interviews replace mock week |
| Phase 4 | **Oct–Nov** — negotiation |

Phase 1–4 details remain as reference; **this weekly schedule** is the source of truth when employed.

---

## How This Plan Fits With `lc`

Alisa's search had **11 companies, 57 interviews** — and ML coding + technical discussion dominated. LeetCode alone won't cover that.

```
┌─────────────────────────────────────────────────────────────┐
│  Daily (aim for ~2.5–3 hrs total)                           │
├─────────────────────────────────────────────────────────────┤
│  Block A — lc branch     │  45–60 min │  2 LeetCode problems│
│  Block B — this plan     │  90 min    │  1 ML focus area    │
│  Block C — optional      │  30 min    │  behavioral / pitch │
└─────────────────────────────────────────────────────────────┘
```

**Rule:** ML coding practice = **no AI assistance** (same as interviews).

| Track | Branch / folder | Plan file |
|---|---|---|
| General coding | `lc` | `INTERVIEW_PLAN.md` |
| ML & research | this branch | **This file** |
| ML implement-from-scratch | `ml-coding/` | [notes.md](../ml-coding/notes.md) |
| Rapid-fire & system design | `technical-discussion/` | [notes.md](../technical-discussion/notes.md) |
| Research pitch & CV deep-dives | `research/` | [pitch-template.md](../research/pitch-template.md) |
| Behavioral (STAR) | `behavioral/` | [story-bank.md](../behavioral/story-bank.md) |
| Math | `math/` | [notes.md](../math/notes.md) |
| Job talk | `job-talk/` | [outline.md](../job-talk/outline.md) |
| Negotiation | `negotiation/` | [playbook.md](../negotiation/playbook.md) |

---

## Interview Types → What to Prepare

| Type | Frequency (RS/MTS) | Vault folder | Phase |
|---|---|---|---|
| ML coding (PyTorch) | 🔴 Very high | `ml-coding/` | 1–2 |
| Technical discussion | 🔴 Very high | `technical-discussion/` | 1–3 |
| Research discussion | 🟡 High | `research/` | 2–3 |
| General coding (LC) | 🟡 Medium | `lc` branch | ongoing |
| Behavioral | 🟡 Medium | `behavioral/` | 2 |
| Job talk | 🟡 Medium | `job-talk/` | 3 |
| Math | ⚪ Some companies | `math/` | 2 |
| Negotiation | After offers | `negotiation/` | 4 |

---

## Four Phases

```
Phase 1 (weeks 1–4)   →  CS336 breadth + transformer muscle memory
Phase 2 (weeks 5–8)   →  ML coding drills + rapid-fire topics
Phase 3 (weeks 9–12)  →  Research pitch, job talk, behavioral, mocks
Phase 4 (when offers) →  Negotiation playbook + post-offer chats
```

Phases overlap with `lc` Pass 1–3. By Phase 3 you should be cold-solving ⭐⭐ LC problems *and* implementing a transformer from memory.

---

## Phase 1 — Foundations (Weeks 1–4)

**Goal:** Follow [CS336](https://cs336.stanford.edu/) lecture order + build Assignment 1-level implementation skill (tokenizer → transformer → train loop).

**Course links:**
- **Latest (Spring 2026):** [cs336.stanford.edu](https://cs336.stanford.edu/) — schedule + [YouTube playlist](https://www.youtube.com/watch?v=JuoVZkPBiKk&list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)
- **Self-study code (2025, fully released):** [spring2025 archive](https://cs336.stanford.edu/spring2025/) — use **Assignment 1** as the interview-prep anchor

**CS336 rule for interviews too:** debug on CPU first; disable AI autocomplete when implementing; LLMs for conceptual questions only.

### Week 1 — Lec 1–4: tokenization → architecture 🔴

| Day | Block B (90 min) | CS336 | Done |
|---|---|---|---|
| W1D1 | Lec 1–2: overview, tokenization, PyTorch/einops, FLOPs/memory | [Lec 1](https://cs336.stanford.edu/) · [Lec 2](https://cs336.stanford.edu/) | [ ] |
| W1D2 | Lec 3: architectures, hyperparameters; trace shapes (B,T,D) | Lec 3 | [ ] |
| W1D3 | Lec 4: attention alternatives, MoE; + [Illustrated GPT-2](https://jalammar.github.io/gpt2/) | Lec 4 | [ ] |
| W1D4 | Skim [ml-coding/notes.md](../ml-coding/notes.md); BPE encode/decode on paper | A1 tokenizer | [ ] |
| W1D5 | Pre-norm block: attention + FFN + residuals + LayerNorm | A1 model | [ ] |
| W1D6 | Full decoder-only stack diagram from memory | A1 preview | [ ] |
| W1D7 | Rest: re-draw architecture; journal gaps | — | [ ] |

### Week 2 — Assignment 1 core (implement, no AI) 🔴

Maps to CS336 A1: *tokenizer + transformer + optimizer + minimal LM training*.

| Day | Block B | Vault drill | Done |
|---|---|---|---|
| W2D1 | Scaled dot-product attention | [01_attention.py](../ml-coding/drills/01_attention.py) | [ ] |
| W2D2 | Multi-head attention | [02_mha.py](../ml-coding/drills/02_mha.py) | [ ] |
| W2D3 | Transformer block (attn + FFN + norms) | [03_transformer_block.py](../ml-coding/drills/03_transformer_block.py) | [ ] |
| W2D4 | Mini LM forward pass | [04_mini_lm.py](../ml-coding/drills/04_mini_lm.py) | [ ] |
| W2D5 | Causal LM loss (label shift) + AdamW step | A1 training loop | [ ] |
| W2D6 | **Optional:** start [A1 code](https://cs336.stanford.edu/spring2025/) on CPU | A1 | [ ] |
| W2D7 | Timed re-implement: attention from blank file (45 min) | 01_attention | [ ] |

### Week 3 — Lec 5–6, 10, 12: systems + inference

| Day | Block B | CS336 | Done |
|---|---|---|---|
| W3D1 | Lec 5–6: GPUs, arithmetic intensity, kernels/Triton (concepts) | Lec 5–6 | [ ] |
| W3D2 | Lec 10: inference — KV cache implement + explain | Lec 10 | [ ] |
| W3D3 | Greedy / top-k / top-p decoding | [05_greedy_decode.py](../ml-coding/drills/05_greedy_decode.py) | [ ] |
| W3D4 | Beam search (optional) | — | [ ] |
| W3D5 | Lec 12: evaluation — perplexity, benchmarks, pitfalls | Lec 12 | [ ] |
| W3D6 | Backprop through attention by hand (one layer) | — | [ ] |
| W3D7 | Rapid-fire: 20 Qs from [technical-discussion/](../technical-discussion/notes.md) §A | — | [ ] |

### Week 4 — Lec 7–9, 13–16: parallelism, scaling, data, alignment

| Day | Block B | CS336 | Done |
|---|---|---|---|
| W4D1 | Lec 7–8: data/tensor/pipeline parallel — vocab only | Lec 7–8 | [ ] |
| W4D2 | Lec 9/11: scaling laws (Chinchilla intuition) | Lec 9, 11 | [ ] |
| W4D3 | Lec 13–14: data filtering, dedup, mixing (conceptual) | Lec 13–14 | [ ] |
| W4D4 | Lec 15–16: SFT, RLHF, RLVR + [GRPO primer](https://huggingface.co/blog/grpo) | Lec 15–16 | [ ] |
| W4D5 | A3 idea: which transformer parts matter most for scaling? | A3 | [ ] |
| W4D6 | **Timed: full transformer forward + loss from scratch (90 min, no AI)** | A1 level | [ ] |
| W4D7 | Phase 1 review; list 5 weakest topics | — | [ ] |

**Phase 1 exit criteria:**
- [ ] A1-equivalent: tokenizer + transformer + training loop on CPU (or finished A1)
- [ ] Can implement attention + LM head without references in < 45 min
- [ ] Can answer 15/20 rapid-fire §A questions cold
- [ ] Can explain inference (KV cache) and one parallelism term from Lec 7–8

**Alisa's notes:** [LLM notes PDF](https://alisawuffles.github.io/assets/files/llm_notes.pdf) — use as breadth checklist alongside lectures

---

## Phase 2 — ML Coding Drills + Technical Depth (Weeks 5–8)

**Goal:** Interview-shaped coding + deeper topic blocks per company.

### ML coding rotation (pick 1/day, 60–90 min, no AI)

Cycle through these until fluent:

| # | Drill | Why |
|---|---|---|
| 1 | Transformer forward pass (from scratch) | 🔴 Most common |
| 2 | Scaled dot-product attention + mask | 🔴 |
| 3 | Multi-head attention | 🔴 |
| 4 | LayerNorm + RMSNorm | Common |
| 5 | Cross-entropy with ignore_index | Common |
| 6 | Greedy + top-k decoding loop | Common |
| 7 | KV-cache inference step | Common at inference teams |
| 8 | Beam search | Occasional |
| 9 | Log-softmax + NLL loss by hand | Math-adjacent |
| 10 | Simple DataLoader + training loop | Systems sanity |
| 11 | Implement BPE encode (simplified) | NLP-specific |
| 12 | Backward pass for linear layer (numpy) | Rare but brutal |
| 13 | Cosine LR schedule | Quick win |
| 14 | Softmax stability trick | Always |
| 15 | Sampling from logits (temp, top-p) | Inference |

Track times in [ml-coding/practice-log.md](../ml-coding/practice-log.md).

### Weekly technical deep-dives (Block B, days you aren't doing a long drill)

| Week | Theme | Prep |
|---|---|---|
| 5 | Experiment design | [technical-discussion/](../technical-discussion/notes.md) §B — 3 prompts |
| 6 | Scaling & systems | §C + "How to Scale Your Model" |
| 7 | RLHF / alignment | PPO vs GRPO, reward modeling |
| 8 | Your specialty area | 5 papers + 10 rapid-fire Qs you write yourself |

### Math (2× per week, 30 min each — fold into Block B or C)

Use [math/notes.md](../math/notes.md). Focus: probability, linear algebra, calculus.

---

## Phase 3 — Research, Behavioral, Job Talk (Weeks 9–12)

**Goal:** Sound like a researcher *and* an engineer in the same hour.

### Research pitch (start Week 9)

1. Fill [research/pitch-template.md](../research/pitch-template.md) for **one flagship project**.
2. Prepare 2-min, 5-min, and 15-min versions.
3. For every CV paper: *motivation → method one-liner → key result → what you'd do next*.
4. Tailor keywords to role (pretraining / post-training / eval / infra).

**Weekly:** 1 mock research conversation (friend or record yourself).

### Behavioral (start Week 9, 30 min × 2/week)

1. Complete [behavioral/story-bank.md](../behavioral/story-bank.md) — **minimum 8 STAR stories**.
2. Map stories → Amazon LP-style questions + generic "tell me about a time…"
3. **Do not wing behavioral.** Alisa's first one failed for exactly this reason.

### Job talk (Weeks 10–12)

1. Draft using [job-talk/outline.md](../job-talk/outline.md).
2. Shorter than academic job talk; one coherent thread.
3. Practice: 25 min talk + 20 min Q&A, twice per week in Week 12.

### Mock interview week (Week 12)

| Day | Mock type | Duration |
|---|---|---|
| M1 | ML coding (transformer variant) | 60 min |
| M2 | Technical discussion (experiment design) | 45 min |
| M3 | Research deep-dive | 45 min |
| M4 | Behavioral | 30 min |
| M5 | LC timed (from `lc` Pass 3) | 45 min |
| M6 | Weakest mock repeat | 60 min |
| M7 | Light review only | — |

**After each mock:** notes in [interview-journal.md](../job-search/interview-journal.md).

---

## Phase 4 — Negotiation & Process (When You Have Offers)

Don't start here early — but read [negotiation/playbook.md](../negotiation/playbook.md) once before first recruiter call so you know the game exists.

**Key moves:**
- Never accept first verbal number without written offer + time to decide
- Ask peers for comp bands *before* the call, not after
- Script what you'll share (other processes yes/no, competing offers vague vs specific)
- Post-offer chats with future teammates ≠ social — they're mutual eval

---

## Per-Interview Cram Checklist (~3 days before)

Alisa's framing: *each interview is a different class midterm.*

| Step | Action |
|---|---|
| 1 | Read interview description + team blog posts / recent papers |
| 2 | Ask recruiter: format, tools (Colab? shared doc?), time, expectations |
| 3 | Pick **one cram sheet** — 10 topics max for *this* company |
| 4 | Re-solve 1 ML coding drill + 1 LC problem in that domain |
| 5 | Re-read your research pitch tailored to their team |
| 6 | Sleep 7+ hours night before |

---

## Process & Timeline (Non-study)

Parallel to studying — track in a spreadsheet or [process-tracker.md](../job-search/process-tracker.md):

- [ ] List 15–20 target companies / teams
- [ ] Map 1st-degree + 2nd-degree contacts per company
- [ ] Schedule 2–3 **practice** processes early (not favorites first if stamina-limited)
- [ ] Track: applied → recruiter → phone → onsite → offer → outcome
- [ ] Log ghosted vs withdrawn vs reject — normalizes the noise

**Getting the first interview:** referrals + conference connections + cold outreach to researchers on teams you want. Expected and okay to reconnect with people you haven't talked to in years.

---

## Progress at a Glance

| Track | Period | Focus | Status |
|---|---|---|---|
| **Employed (primary)** | Jul–Nov 2026 | [Weekly schedule](#employed-track--jul-2026--nov-2026-start-here) | Jul W1 |
| Phase 1 Foundations | weeks 1–4 | CS336 + transformer | reference |
| Phase 2 Drills | weeks 5–8 | ML coding rotation | reference |
| Phase 3 Mocks | weeks 9–12 | Research + behavioral | reference |
| Phase 4 Negotiation | offers | Comp + decisions | Oct–Nov |
| lc (parallel) | ongoing | ⭐⭐ checklist | Day 1 done |

---

## Session Types (by energy)

| Energy | Block B | Block C |
|---|---|---|
| Normal | Full 90 min deep dive or drill | 1 behavioral story |
| Low | 20 rapid-fire Qs + read notes | — |
| Very low | Re-draw transformer diagram | Re-read one STAR story |

---

## Resources (curated from Alisa + standard)

| Resource | Use for |
|---|---|
| [CS336 (2026)](https://cs336.stanford.edu/) | Lectures + schedule |
| [CS336 (2025 archive)](https://cs336.stanford.edu/spring2025/) | A1–A5 code for self-study |
| [CS336 YouTube playlist](https://www.youtube.com/watch?v=JuoVZkPBiKk&list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV) | Watch at 1.25× |
| [Alisa LLM notes PDF](https://alisawuffles.github.io/assets/files/llm_notes.pdf) | Breadth checklist |
| [Illustrated GPT-2](https://jalammar.github.io/gpt2/) | Attention intuition |
| [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Baseline |
| [Backprop calculus](https://cs231n.github.io/optimization-2/) | Math + ML coding |
| [Policy gradient for LMs](https://huggingface.co/blog/deep-rl-ppo) | RL interviews |
| [GRPO guide](https://huggingface.co/blog/grpo) | 2024–2025 interviews |
| `lc` / NeetCode 75 | General coding |

---

*Employed: ~12 hrs/week. Jul–Aug prep, Sep–Oct interviews, Oct–Nov sign. Follow the [Employed Track](#employed-track--jul-2026--nov-2026-start-here) weekly schedule.*
