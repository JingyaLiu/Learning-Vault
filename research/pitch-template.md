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
| 2 | Ads retrieval | Large-scale dual-tower / ranking | recall@100: **[+X%]** · CTR: **[+Y%]** · p99: **[Z ms]** |
| 3 | Advertiser/seller-facing agent | Tool-using agent in production | resolution / handoff: ___ |
| 4 | CX foundation model | Domain FM — SFT, eval, data mix | vs general LLM: ___ |

**2-min thread:** PhD (1 sentence) → Walmart arc emphasizing **R → X** with **T** methods → deep-dive on pillar matching the role → want RS in **R / X / P / T** (pick 2 for this interview).

**Title bridge (if asked):** Staff DS today; targeting RS to own **retrieval, domain FM, or LM training** at research depth — not pure SWE.

**Pretrain gap (if asked for P roles):** Industrial work is post-train + domain FM; PhD + citations + FM data/scale decisions show pretrain research taste — eager to go deeper on data mix and scaling.

**Why leave Walmart (honest, forward-looking):** ___

---

## Project: _________________________

### One-liner (≤ 20 words)


### Why this problem? (motivation)
- What was broken / missing before?
- Why now?

### Method (≤ 3 bullets)
- 
- 
- 

### Key result (numbers)
- Main metric: 
- Baselines beaten: 
- Surprising finding: 

### Your specific contribution
- What did *you* own vs collaborators?

### Limitations (honest)
- 
- 

### Future work (shows research taste)
- 
- 

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

**Lead:** large-scale ads retrieval — dual-tower / ranking, recall@k, online lift `___`  
**Deep-dive (30 sec):** negative sampling, ANN, latency vs quality, A/B design  
**Bridge:** retrieval stack grounded later CX FM and search-augmented generation  
**Close:** RS on retrieval + ranking + search at scale  

### X — CX foundation model (Sierra, Decagon, Microsoft, ServiceNow, Snowflake)

**Lead:** customer experience foundation model — domain SFT, eval, production iteration  
**Deep-dive (30 sec):** domain data mix, offline/online eval, vs general LLM `___`  
**Bridge:** seller/advertiser agent informed what the FM must handle  
**Close:** RS owning domain FM research for customer experience  

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
