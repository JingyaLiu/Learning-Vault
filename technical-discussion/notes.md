# Technical Discussion — Study Guide

Two interview shapes:
1. **Deep dive** — one topic (experiment design, system tradeoffs); interviewer pushes on choices.
2. **Rapid fire** — breadth check; short crisp answers.

Practice both. Record yourself — rambling hurts more than wrong answers.

---

## §A — Rapid-Fire Bank (answer in ≤ 60 sec each)

Study until you can hit 80%+ cold. Add your own specialty questions at the bottom.

### Transformers & architectures
- [ ] Why scale dot-product attention by √d_k?
- [ ] Difference between encoder-only, decoder-only, encoder-decoder?
- [ ] How does RoPE work at a high level?
- [ ] ALiBi vs learned positional embeddings?
- [ ] Pre-norm vs post-norm — tradeoffs?
- [ ] What is SwiGLU / gated FFN?
- [ ] MoE at inference — what changes vs dense?

### Training
- [ ] Why AdamW over Adam?
- [ ] What is warmup + cosine decay for?
- [ ] Gradient clipping — when and why?
- [ ] Mixed precision (fp16/bf16) — benefits and risks?
- [ ] What causes loss spikes in LM training?
- [ ] Data contamination in eval — how do you detect/mitigate?

### Inference
- [ ] What is KV cache and memory cost?
- [ ] Latency vs throughput batching tradeoff?
- [ ] Top-k vs top-p vs temperature?
- [ ] Speculative decoding — idea?

### RL / alignment
- [ ] PPO clipped objective — intuition?
- [ ] Difference between PPO and GRPO?
- [ ] Reward hacking examples?
- [ ] Why KL penalty to reference model?

### Distributed / systems
- [ ] Data parallel vs model parallel?
- [ ] What is FSDP?
- [ ] Tensor parallel vs pipeline parallel?
- [ ] What is "5D parallelism" (DP × TP × PP × EP × CP)?

### Classic ML / NLP
- [ ] Bias-variance tradeoff?
- [ ] Precision/recall/F1 — when optimize which?
- [ ] BLEU limitations?
- [ ] Subword tokenization — BPE vs WordPiece?

### Your specialty (fill in)
- [ ] See **§G** — pillar rapid-fire (R / X / P / T)

---

## §B — Experiment Design Prompts

For each prompt: **hypothesis → baselines → metrics → ablations → failure modes → follow-ups**.

Spend 30 min per prompt; write bullet answers, then say them out loud.

1. **Context length:** You suspect 32k context hurts short-context tasks. How do you test this?
2. **Tokenizer change:** New BPE vocab for code. How do you validate before a full pretrain?
3. **RLHF:** Model becomes verbose after RL. Diagnose and propose fixes.
4. **Eval gaming:** Benchmark score up but human rating flat. What happened?
5. **Data mix:** Add 10% synthetic data. Design experiment to measure harm/benefit.
6. **Inference cost:** Need 2× throughput with ≤1% quality drop. Options?
7. **Your project:** Pick one paper from your CV — "What would you do differently?"

**Answer skeleton:**
```
Goal:
Baselines:
Metrics (primary + guardrails):
Data / splits:
Ablations (ordered):
How you'd know you're wrong:
Next experiment if results are ambiguous:
```

---

## §C — Systems & Scaling

Read once, then explain aloud without slides:

- [ ] [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) (or equivalent scaling laws summary)
- [ ] Chinchilla-optimal compute — rough idea
- [ ] Checkpointing vs recomputation in large training
- [ ] Evaluation at scale — stratified sampling, CI on metrics

---

## §D — Company cram sheets (your pipeline)

Copy and fill before each loop. Pre-filled angles for your top targets — edit with recruiter format + dates.

### Sierra · Pillar **X** (CX FM)

```markdown
## Company: Sierra  Team: CX FM  Pillar: X  Date: ___

Recruiter format: research chat + ML fundamentals + behavioral (verify)
Team cares about: customer experience foundation model, domain eval, enterprise CX
My 10 cram topics:
1. CX FM — SFT, domain data, eval vs general LLM
2. Domain data curation — synthetic vs real CX conversations
3. Offline eval suite — what's in it, what failed to predict online
4. Post-train choices for domain FM (SFT / DPO / RLHF)
5. Retrieval grounding for CX (link to **R** pillar)
6. Seller/advertiser context vs consumer CX
7. Why domain FM beats prompt-only GPT
8. Scaling domain data — quality vs quantity
9. Biggest FM limitation — honest
10. Metric `___` vs baseline
Research pitch angle: **X** — lead CX FM; bridge from ads **R** + post-train **T**
Questions I will ask: FM roadmap · eval ownership · research vs product split
```

### Amazon Ads · Pillar **R** (retrieval / ranking)

```markdown
## Company: Amazon  Team: Ads ML / retrieval  Pillar: R  Date: ___

Recruiter format: ML coding + applied science deep-dive + LP behavioral (verify)
Team cares about: large-scale retrieval, ranking, advertiser workflows
My 10 cram topics:
1. Dual-tower vs cross-encoder — when each
2. ANN recall@k — FAISS/ScaNN intuition
3. Negative sampling at ads scale
4. Offline metrics vs online lift
5. Cold start / new advertiser handling
6. Latency budget for retrieval path
7. Embedding drift / retraining cadence
8. Your Walmart ads retrieval metric (fill)
9. A/B design for ranking change
10. Amazon LP story mapped (customer obsession → advertiser outcome)
Research pitch angle: **R** — lead ads retrieval; FM/post-train as bridge only
Questions I will ask: team scope · ranking stack · search + ads roadmap
```

### Microsoft · Pillar **X** + **T** (CX FM / post-train)

```markdown
## Company: Microsoft  Team: M365 Copilot / domain FM  Pillars: X, T  Date: ___

Recruiter format: ML coding + research + system design (verify)
Team cares about: enterprise domain FM, Copilot quality, post-train at scale
My 10 cram topics:
1. Domain FM for enterprise — parallels to your CX FM
2. SFT / DPO pipeline for product quality (**T**)
3. Eval for enterprise (privacy, tenant isolation)
4. Retrieval over enterprise corpus (**R** bridge)
5. Offline→online eval for domain FM
6. Data mix for domain adaptation
7. CX FM metric `___` — transferable lesson
8. Why leave Walmart — growth in **R/X/P/T** RS work
9. Local Redmond — team fit
10. Copilot / FM recent paper skim (fill)
Research pitch angle: **X** CX FM deep-dive + **T** post-train pipeline
Questions I will ask: FM vs Copilot stack · research vs applied split
```

### Databricks Mosaic · Pillar **T** (+ **P**)

```markdown
## Company: Databricks  Team: Mosaic AI  Pillars: T, P  Date: ___

Recruiter format: ML coding + FM/post-train discussion (verify)
Team cares about: data + FM stack, Mosaic, enterprise LLM
My 10 cram topics:
1. SFT pipeline — data, filtering, mixing
2. RLHF/DPO/GRPO — when to use which
3. Eval harness design
4. Domain FM lessons from Walmart
5. Transformer implementation (timed drill)
6. Data contamination in benchmarks
7. Preference data collection
8. Reward hacking examples
9. Mosaic product skim
10. Practice-loop goal: calibrate format, not must-accept offer
Research pitch angle: **T** post-train + domain FM; touch **P** if Mosaic pretrain discussed
Questions I will ask: Mosaic roadmap · research freedom
```

### AI2 · Pillar **P** (+ **T**)

```markdown
## Company: AI2  Team: OLMo  Pillars: P, T  Date: ___

Recruiter format: research deep-dive + coding (verify)
Team cares about: open pretraining, OLMo, Seattle local
My 10 cram topics:
1. PhD contribution — pretrain-relevant hook
2. Chinchilla / compute-optimal — rough intuition
3. Data mix & dedup — what you'd change for OLMo-scale
4. Architecture choices (dense, MoE) — high level
5. OLMo / recent AI2 paper (fill)
6. CX FM lessons → what matters at pretrain scale
7. Limitation of your work — honest
8. What you'd publish next
9. Open research motivation
10. Bridge: industrial **T** + research **P** taste
Research pitch angle: **P** — PhD + scaling insight; **T** from CX FM as applied proof
Questions I will ask: OLMo pretrain roadmap · data strategy
```

### Glean · Pillar **R** (+ **T**)

```markdown
## Company: Glean  Team: Enterprise search  Pillars: R, T  Date: ___

Recruiter format: ML coding + retrieval deep-dive (verify)
Team cares about: enterprise search, RAG, ranking at scale
My 10 cram topics:
1. Dual-tower vs cross-encoder for search
2. ANN recall@k vs precision tradeoffs
3. Query-document matching at enterprise scale
4. Negative sampling / hard negatives
5. Search + LLM (RAG as retrieval problem)
6. Offline NDCG vs online click metrics
7. Your Walmart ads retrieval parallel
8. Embedding refresh cadence
9. Latency budget
10. Practice-loop: calibrate **R** interview format
Research pitch angle: **R** — ads retrieval → enterprise search
Questions I will ask: ranking stack · eval methodology
```

### Apple · Pillar **P** + **X** + **R** (pick role)

```markdown
## Company: Apple  Team: ___ (FM / Search / Siri)  Pillars: P/X/R  Date: ___

Recruiter format: research deep-dive + ML coding (verify)
Apply link: see LINKEDIN_ROLE_SCAN.md § Apple

If **Foundation Models (200641998):** pitch **X** + **T** + PhD; pretrain taste **P**
If **Search & Knowledge (200669635):** pitch **R** — ads retrieval → search
If **Siri Innovation Studio (200667331):** pitch **X** + PhD citations

My 10 cram topics:
1. AFM / on-device FM vs cloud CX FM
2. Your Walmart CX FM eval + data mix
3. Ads retrieval → search ranking bridge (**R**)
4. Post-train pipeline choices (**T**)
5. Pretrain data mix intuition (**P**)
6. Apple Intelligence / AFM public materials skim
7. On-device latency vs quality
8. Multimodal (if applicable)
9. Why Apple vs Walmart — forward-looking
10. Metric `___` for flagship project
Research pitch angle: match role — **R**, **X**, or **P/T**
Questions I will ask: team scope · FM vs SIML · research vs product
```

### Blank template

```markdown
## Company: ___  Team: ___  Pillars: R / X / P / T  Date: ___
LinkedIn / careers URL: ___

Recruiter said format:
Team cares about (papers, blog, product):
My 10 cram topics:
1.
...
Research pitch angle for this team:
Questions I will ask them:
```

---

## §G — Pillar rapid-fire (your four target areas)

Answer in ≤ 90 sec. Rotate Thu 15-min blocks by week.

### G-R — Retrieval / ranking / search
- [ ] Dual-tower vs cross-encoder — when each?
- [ ] ANN (FAISS/ScaNN) — recall@k vs latency?
- [ ] NDCG vs recall@k — optimize which when?
- [ ] Negative sampling at scale?
- [ ] Cold start for new advertisers/items?
- [ ] Embedding drift — when retrain?
- [ ] Offline metric that failed to predict online?
- [ ] Search + LLM: RAG as retrieval?
- [ ] Two-stage retrieve-then-rank pipeline?
- [ ] Your ads retrieval metric `___`?

### G-X — CX foundation model
- [ ] Domain FM vs general LLM — what breaks?
- [ ] SFT data mix for CX — how choose ratios?
- [ ] Offline eval suite for CX FM?
- [ ] Online guardrails / escalation triggers?
- [ ] Biggest limitation of your FM?
- [ ] Domain data quality vs quantity?
- [ ] Seller/advertiser vs consumer CX differences?
- [ ] How retrieval (**R**) grounds the FM?
- [ ] Metric vs GPT-4 baseline `___`?
- [ ] What would you do with 10× domain data?

### G-P — Pretraining
- [ ] Chinchilla / compute-optimal — intuition?
- [ ] Data dedup & mixing — why it matters?
- [ ] Tokenizer choice impact?
- [ ] Scaling laws — what breaks at scale?
- [ ] Dense vs MoE — tradeoff?
- [ ] Loss spikes — causes & fixes?
- [ ] What pretrain decision would you make for CX domain?
- [ ] OLMo / Llama — one architectural choice you'd ask about?
- [ ] PhD work → pretrain research bridge?
- [ ] Honest gap: industrial pretrain compute — how you'd ramp?

### G-T — Post-training
- [ ] SFT vs DPO vs PPO vs GRPO — when each?
- [ ] Reward hacking examples?
- [ ] KL penalty to reference — why?
- [ ] Preference data pipeline design?
- [ ] Eval contamination after post-train?
- [ ] RLHF at scale — bottlenecks?
- [ ] Your CX FM post-train choices?
- [ ] Offline vs online after alignment?
- [ ] Data mix for SFT vs RL stage?
- [ ] NeMo/Mosaic post-train stack skim?

### Bridge (all pillars)
- [ ] One sentence: **R → X** via **T**, with **P** ambition
- [ ] What from PhD still applies?

---

## §F — Pillar rotation (employed track)

| Week of | Thu rapid-fire (15 min) | Sat / experiment (§B) |
|---|---|---|
| Jul W4 | §G-R (10) | Retrieval metric / A/B design |
| Aug W1 | §G-T (10) | SFT data mix ablation |
| Aug W2 | §G-X (10) + §G-P (5) | CX FM eval harness design |
| Aug W3 | §G-R (10) | Ranking offline vs online gap |
| Aug W4 | §G-X (10) | Domain FM limitation → next experiment |

---

## Weekly Drill

**Monday:** 10 rapid-fire (§A) — timed  
**Thursday:** 1 experiment design (§B) — written + spoken  
**Before onsite:** fill §D (Sierra/X, Amazon/R, Microsoft/X, Databricks/T, AI2/P, Glean/R)
