# This Week · Jul W2

> **Profile:** Jingya Liu · Staff DS @ Walmart · ~12–14 hr/week  
> **Full plan:** [ML_JOB_SEARCH_PLAN.md](ML_JOB_SEARCH_PLAN.md#jul-w2--jul-1420--ml-drills--outreach)  
> **Branch:** `lc` for LC · this branch for ML/process  
> **Prev week:** [JUL_W1.md](JUL_W1.md)

**Last updated:** Tue Jul 15 · **Day 2 (Tuesday)** ← start here

---

## W1 carry-over (schedule early)

| Item | From W1 | Slot |
|---|---|---|
| CS336 **Lec 3** + decoder diagram | Sat skipped | **Mon** |
| Pipeline tier tags | Sun optional | **Thu** 30 min |
| LinkedIn bullets (**R** + **X**) | deferred | **Thu** optional |
| Pitch **X** — one offline eval metric (vs GPT-4 or resolution rate) | pitch gap | **Thu** 30 min |

---

## Active track this week

| Tier | Focus | Why now |
|---|---|---|
| 🎯 **Primary** | **R** + **X** fundamentals | Drills + behavioral before referrals convert |
| 🏋️ Practice | Map only | Not applying yet |
| 🎯 Stretch | **Defer P** | Aug W3 |
| ⭐ Dream | **Skip** | Oct+ |

**Study mix (ML + rapid-fire, excl. LC):** R 15% · X 25% · fundamentals 50% · T 10% · **P 0%**

---

## Week milestones (Sun Jul 20)

- [ ] **01_attention** + **02_mha** pass without peeking ([practice-log](../ml-coding/practice-log.md))
- [ ] CS336 **Lec 3** notes + decoder diagram · **Lec 4** watched
- [ ] LC **34** (first/last) + **15** (3Sum) cold · **704** re-solve still clean
- [ ] §G-X rapid-fire **Q1–5** aloud ([technical-discussion](../technical-discussion/notes.md))
- [ ] Pitch **X** — add **≥1 eval metric** ([pitch-template](../research/pitch-template.md))
- [ ] Behavioral stories **1–4** drafted ([story-bank](../behavioral/story-bank.md))
- [ ] **2 outreach** sent — **Amazon Ads (R)** first ([process-tracker](../job-search/process-tracker.md))
- [ ] Timed: attention from blank **≤ 45 min** (Sat)

---

## Day by day

### Monday · Day 1 ✅

| Block | Time | Task | Done |
|---|---|---|---|
| **1** | 90 min | CS336 **Lec 3** @ 1.25× · [YouTube](https://www.youtube.com/watch?v=lVynu4bo1rY) · notes → [cs336-notes.md](../ml-coding/cs336-notes.md) | [x] |
| **2** | 30 min | **Decoder-only stack** from memory — template in notes | [ ] |

---

### Tuesday · Day 2 ← **start here**

| Block | Time | Task | Done |
|---|---|---|---|
| **1** | 30 min | LC **34** Find First and Last Position · [02_search_first_last.py](../binary-search/problems/02_search_first_last.py) · cold | [ ] |
| **2** | 60 min | Drill **01_attention** · [01_attention.py](../ml-coding/drills/01_attention.py) · no AI | [ ] |

**Pattern preview (LC 34):** left/right boundary binary search · `result` + shrink left or right on equal · differs from 704's `left <= right` exact match

**Drill pass criteria:** `_test()` green · explain QKᵀ/√d · mask multiply · softmax axis

Log time in [practice-log.md](../ml-coding/practice-log.md).

---

### Wednesday · Day 3

| Block | Time | Task | Done |
|---|---|---|---|
| **1** | 45 min | LC **15** 3Sum · sort + two pointers · [02_triplet_sum.py](../two-pointer/problems/02_triplet_sum.py) | [ ] |
| **2** | 60 min | Drill **02_mha** · [02_mha.py](../ml-coding/drills/02_mha.py) | [ ] |

**3Sum sketch:** sort `nums` · for each `i`: `l=i+1`, `r=n-1` · skip dupes at `i`, `l`, `r`

**MHA:** split D into H heads · per-head attention · concat · W_o projection

---

### Thursday · Day 4

| Block | Time | Task | Done |
|---|---|---|---|
| **1** | 30 min | §G-X rapid-fire **Q1–5** aloud · [technical-discussion/notes.md](../technical-discussion/notes.md) | [ ] |
| **2** | 30 min | Pitch **X** — fill **one eval metric** + ownership line in [pitch-template](../research/pitch-template.md) | [ ] |
| **3** | 30 min | Tag **Primary** rows in [process-tracker](../job-search/process-tracker.md) if not done | [ ] |
| *opt* | 30 min | LinkedIn bullets paste (**R** + **X**) | [ ] |

#### §G-X Q1–5 (answer aloud, ≤60 sec each)

1. Domain FM vs prompt-only GPT-4 — when is FM worth the cost?
2. Offline eval suite for CX FM — what metrics beyond perplexity?
3. SFT data mix — how do you balance seller vs consumer utterances?
4. Online guardrails for production FM — what do you monitor?
5. **Your CX FM:** one metric you'd defend + one failure mode

---

### Friday · Day 5

| Block | Time | Task | Done |
|---|---|---|---|
| **1** | 45 min | LC **3** Longest Substring · [longest_substring_unique_3.py](../sliding-windows/problems/longest_substring_unique_3.py) | [ ] |
| **2** | 15 min | Re-solve LC **704** cold — confirm `left <= right` stuck | [ ] |

**Sliding window:** expand `r`, shrink `l` when constraint breaks · track best window

---

### Saturday · Day 6

| Block | Time | Task | Done |
|---|---|---|---|
| **1** | 90 min | CS336 **Lec 4** @ 1.25× · systems / parallelism skim for interview talk | [ ] |
| **2** | 45 min | **Timed:** [01_attention.py](../ml-coding/drills/01_attention.py) from **blank file** · no peek | [ ] |

**Sat exit:** attention re-implement ≤ 45 min OR note blockers for Sun review

---

### Sunday · Day 7 — do not skip outreach

| Block | Time | Task | Done |
|---|---|---|---|
| **1** | 90 min | Behavioral stories **1–4** STAR · [story-bank.md](../behavioral/story-bank.md) | [ ] |
| **2** | 60 min | Send **2 outreach** — Amazon Ads (**R**) priority | [ ] |

#### Stories 1–4 (pick Walmart examples)

| # | Theme | Walmart angle (prompt) |
|---|---|---|
| 1 | Conflict / disagreement | Cross-functional ads vs infra on latency budget? |
| 2 | Failed experiment | Multimodal variant that didn't ship — what you learned |
| 3 | Tight deadline | A/B launch under holiday traffic / stat-sig window |
| 4 | Lost technical disagreement | Text-only vs multimodal path before your win |

#### Outreach checklist

1. **Amazon Ads Applied Scientist** — [4173762699](https://www.linkedin.com/jobs/view/4173762699) · pillar **R** · cite multimodal retrieval A/B
2. Second message: warm contact **or** Microsoft Copilot / Apple Search (**X** or **R**)

**Template:** 3 sentences — who you are · one metric · specific ask (15-min chat / referral)

Use **personal email** · keep confidential per [process-tracker](../job-search/process-tracker.md).

---

## If energy is low

| Day | Minimum | Tier |
|---|---|---|
| Mon | Half Lec 3 + diagram skeleton | fundamentals |
| Tue | LC 34 only | LC |
| Wed | MHA drill only | fundamentals |
| Thu | Pitch X metric only | Primary **X** |
| Sun | **1** outreach + story **1** only | Primary |

---

## Sync with `lc` INTERVIEW_PLAN

| `lc` day | Jul W2 |
|---|---|
| Day 3 Two Pointers | W1 done (125, 167) |
| Day 4 Sliding Window | Fri · LC 3 |
| Day 1 Binary Search extras | Tue · LC 34 · Fri · 704 refresh |

---

## Next week preview (Jul W3)

- Drills **03_transformer_block** → **04_mini_lm**
- LC: Longest Substring deep, Min Window (76), Container Water (11)
- Record **pitch R** (2 min)
- Behavioral stories **5–8**

---

## Jul W1 retrospective

| Done | Deferred to W2 |
|---|---|
| Lec 1–2 · §G-R Q1–10 | Lec 3 + diagram → **Mon** |
| Pitch **R** + **X** drafts | Pitch **X** metric → **Thu** |
| LC 125, 167, 704 | LC 34, 15, 3 |
| | LinkedIn bullets · pipeline tags |
| | Behavioral · outreach → **Sun** |

Full W1 log: [JUL_W1.md](JUL_W1.md)
