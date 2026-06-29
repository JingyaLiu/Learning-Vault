# Research Pitch Template

Prepare **2 min**, **5 min**, and **15 min** versions of the same thread. Interviewers are tired — lead with the punchline.

---

## Career arc (fill once — reuse across pitches)

**Name:** Jingya (Tina) Liu · [LinkedIn](https://www.linkedin.com/in/jingya-tina-liu/)  
**PhD:** Electrical Engineering, CUNY City College (2016–2021) · Yingli Tian lab · CV / medical imaging · ~431 citations · patent  

**Walmart Global Tech:**
| Period | Title | Location |
|---|---|---|
| Aug 2022 – Mar 2024 | Research Engineer | Redmond |
| Apr 2024 – present | **Staff Data Scientist** | Bellevue |

| Phase | Project | One-line hook | Key metric (fill) |
|---|---|---|---|
| 1 | AR shelf object detection | Shipped CV for in-store / AR use | mAP / coverage: ___ |
| 2 | Ads retrieval | Multimodal sponsored products retrieval vs text baseline | **CTR +4.46%** · **Ad revenue +5.46%** · Clicks +5.78% (stat sig A/B) |
| 3 | Advertiser/seller-facing agent | Tool-using agent in production | serves **thousands** of sellers & advertisers |
| 4 | CX foundation model | Domain FM — SFT, eval, post-train · roadmap: **search, ads, personalization** | production · **thousands** of sellers/advertisers |

**2-min thread:** PhD (1 sentence) → Walmart arc emphasizing **R → X** with **T** methods → deep-dive on pillar matching the role → want RS in **R / X / P / T** (pick 2 for this interview).

**Title bridge (if asked):** Staff DS today; targeting RS to own **retrieval, domain FM, or LM training** at research depth — not pure SWE.

**Pretrain gap (if asked for P roles):** Industrial work is post-train + domain FM; PhD + citations + FM data/scale decisions show pretrain research taste — eager to go deeper on data mix and scaling.

**Why leave Walmart (honest, forward-looking):** ___

---

## Project: Walmart Sponsored Products — multimodal ads retrieval

### One-liner (≤ 20 words)

Multimodal retrieval for sponsored products ads — stat-sig CTR +4.5% and revenue +5.5% over text-only production.

### Why this problem? (motivation)

- Production retrieval was **text-only** — missed visual product relevance in sponsored products
- Multimodal signals (image + text) better match how users judge ad relevance

### Method (≤ 3 bullets)

- Multimodal retrieval model replacing / augmenting text-based production retrieval
- Online A/B: control **13657** (text baseline) vs treatment **13658** (multimodal)
- Evaluated on standard ads metrics with statistical significance gating

### Key result (numbers)

- **CTR: +4.46%** lift (stat sig)
- **Ad revenue: +5.46%** lift (stat sig)
- **Clicks: +5.78%** · **Impressions: +1.26%** (stat sig)
- Also improved: **ad eCTR, eCPM, eCPMV** (stat sig)

### Your specific contribution

- Fill: modeling / experiment design / deployment / cross-functional — *your ownership*

### Limitations (honest)

- Fill: latency cost of multimodal encoding, cold-start items, text-only fallback paths

### Future work (shows research taste)

- Two-stage retrieve-rerank with multimodal cross-encoder; hard negatives for visually similar SKUs

---

## CV Paper Checklist

For **every** paper on your CV, fill a mini version:

| Paper | 10-sec hook | Main figure to draw | Likely hard question | My answer |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

---

## Pitch variants by pillar

Use the same Walmart arc; **lead with the pillar the team cares about**.

### R — Retrieval / ranking / search (Amazon Ads, Google Search/Ads, Glean, SeekOut, Perplexity)

**Lead:** multimodal ads retrieval — **CTR +4.46%**, **ad revenue +5.46%** vs text-only production (stat sig A/B)  
**Deep-dive (30 sec):** multimodal vs text baseline, bucket 13657 vs 13658, eCTR/eCPM/eCPMV, stat sig gating  
**Bridge:** PhD CV → visual relevance in ads → seller agent → CX FM  
**Close:** RS on retrieval + ranking + search at scale  

#### Pitch R draft (2 min) — read aloud (~260 words)

```
I'm Tina Liu — PhD in EE from CUNY, about 431 citations, Staff Data Scientist
at Walmart Global Tech.

My strongest retrieval result is sponsored products ads. Production used
text-only retrieval; we shipped a multimodal retrieval model that combines
product visuals with text. In a live A/B test against the production control,
all primary metrics were statistically significant: CTR up 4.46 percent,
clicks up 5.78 percent, ad revenue up 5.46 percent, and impressions up
1.26 percent. We also saw significant lifts on eCTR, eCPM, and eCPMV.

The design choice I'd defend is multimodal retrieval over text-only matching,
because sponsored products are inherently visual — text alone misses relevance
signals users actually react to. My PhD in computer vision maps directly to
this problem.

My arc at Walmart: AR object detection, then ads retrieval, then seller-facing
agents, and now customer experience foundation model — same through-line from
representations and ranking to domain-scale ML.

I'm targeting Research Scientist or Applied Scientist roles in ads retrieval
and search. Amazon Sponsored Products is a strong fit — same retrieval-at-scale
problem, rigorous online experimentation, and a clear path from my multimodal
ranking work.
```

#### Pitch R — 60 sec version (phone screen)

```
Staff DS at Walmart. I shipped multimodal sponsored-products retrieval vs a
text-only production baseline. Live A/B: CTR +4.5%, ad revenue +5.5%,
clicks +5.8% — all stat sig. I'd defend multimodal signals because ad
relevance is visual. PhD CV background. Now building CX FM; targeting RS
in ads retrieval — Amazon Ads is a direct fit.
```

#### §G-R Q10 (your ads retrieval — one metric + one design choice)

- **Metric:** CTR **+4.46%** · ad revenue **+5.46%** (stat sig online A/B vs text baseline)
- **Defend:** **Multimodal retrieval** (image + text) — text-only production missed visual relevance; all key ad metrics improved with stat sig

### X — CX foundation model (Sierra, Decagon, Microsoft, ServiceNow, Snowflake)

**Lead:** domain CX FM in production (**thousands** of sellers/advertisers) → roadmap: **search, ads, personalization**  
**Deep-dive (30 sec):** domain SFT + eval; FM as shared representation layer for retrieval, ranking, and personalized CX  
**Bridge:** multimodal ads retrieval + seller agents → FM unifies **R** (search/ads) and **X** (domain CX)  
**Close:** RS owning domain FM that powers search, ads, and personalization — not chat-only  

#### Pitch X draft (2 min) — read aloud

```
I'm Tina Liu — PhD EE from CUNY, ~431 citations, Staff Data Scientist at
Walmart Global Tech.

I lead customer experience foundation model work for Walmart marketplace.
The FM is in production today serving thousands of sellers and advertisers
— domain SFT, offline eval, post-training, real production iteration.

The strategic bet is bigger: this CX foundation model is the shared
domain layer we plan to extend into search, ads, and personalization.
Same Walmart catalog, policies, and user context — one FM that improves
retrieval relevance, ad matching, and personalized experiences instead
of three disconnected text pipelines.

That's why my arc fits together. Multimodal ads retrieval gave me
ranking and online A/B at scale — CTR plus 4.5 percent on sponsored
products. Seller and advertiser agents taught me tool use, handoffs,
and what domain workflows the FM must support. CX FM is the unified
representation and reasoning layer on top.

The design choice I'd defend is building a domain foundation model —
not prompt-only GPT — because search, ads, and personalization all
need the same policy-safe, catalog-grounded understanding. A general
LLM can't be fine-tuned once and deployed consistently across those
surfaces.

I'm targeting Research Scientist roles at the intersection of domain FM,
search, and ads — Microsoft Copilot, Amazon Ads, or marketplace AI
where retrieval and foundation models converge.
```

#### Pitch X — 60 sec version

```
Staff DS at Walmart. I lead a CX foundation model in production for
thousands of sellers and advertisers. Roadmap: extend that same domain
FM into search, ads, and personalization — one shared layer vs siloed
pipelines. Before this: multimodal ads retrieval, CTR plus 4.5 percent
stat sig, and seller/advertiser agents. Targeting RS roles where domain
FM meets search and ads.
```

#### Unified R + X pitch (when interview spans both pillars)

```
Same thread: multimodal ads retrieval proved visual relevance matters
(CTR plus 4.5 percent). CX FM now serves thousands of sellers and
advertisers in production. Next: that domain FM powers search, ads,
and personalization — retrieval plus foundation model, not separate stacks.
```

#### LinkedIn bullets — CX FM (Block 3)

**Staff DS · Bellevue · Apr 2024–present:**
- Lead **customer experience foundation model** in production — **thousands of sellers & advertisers**
- Domain SFT, eval harness, post-train pipeline
- **Roadmap:** extend domain FM to **search, ads, and personalization** — unified representation vs siloed pipelines
- Builds on **multimodal ads retrieval** (+4.5% CTR A/B) and **seller/advertiser agents**

**Add when ready:** one offline eval metric vs GPT-4 baseline

### P — Pretraining (AI2, Meta, OpenAI, DeepMind, Hugging Face)

**Lead:** PhD (~431 cit) + shipped domain FM — research taste with production grounding  
**Deep-dive (30 sec):** data mix / scale decisions you made; what you'd pretrain differently  
**Honest gap:** less industrial pretrain compute; strong on data quality, eval, architecture intuition  
**Close:** RS on pretraining — data, scaling, open models  

### T — Post-training (Databricks, Scale, Cohere, NVIDIA NeMo, Meta GenAI, Reddit)

**Lead:** CX FM built via SFT + alignment pipeline — choices and eval `___`  
**Deep-dive (30 sec):** SFT vs DPO/RLHF, preference data, reward hacking, eval contamination  
**Bridge:** post-train is how domain FM actually ships  
**Close:** RS on post-training, alignment, and domain adaptation  

---

## Tailoring by Role Type

| Role emphasis | Lead with | Keywords to hit |
|---|---|---|
| Pretraining | data, scale, architecture | compute, chinchilla, stability |
| Post-training / RLHF | alignment, eval, iteration speed | PPO, reward, human eval |
| Applied / product | user impact, deployment | latency, A/B, failure cases |
| Research (open-ended) | novelty, insight, what's next | limitations, new questions |

---

## Mock Flow (45 min)

1. "Walk me through a project you're proud of." → **5 min pitch**
2. Interviewer digs into method → **10 min**
3. "What would you do differently?" → **5 min**
4. Second paper or related work → **15 min**
5. "What do you want to work on next?" → **5 min**

Record audio. Listen for: filler, defensiveness, missing numbers.

---

## Red Flags to Avoid

- Starting with related work history before the problem
- Can't state your contribution clearly on co-authored work
- No quantitative result in the first 2 minutes
- Pretending a limitation doesn't exist
