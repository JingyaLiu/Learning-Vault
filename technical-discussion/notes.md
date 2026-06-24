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
- [ ] 
- [ ] 
- [ ] 

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

## §D — Company-Specific Cram Sheet (template)

Copy this block per upcoming interview:

```markdown
## Company: ___  Team: ___  Date: ___

Recruiter said format:
Team cares about (papers, blog, product):
My 10 cram topics:
1.
...
Research pitch angle for this team:
Questions I will ask them:
```

---

## Weekly Drill

**Monday:** 10 rapid-fire (§A) — timed  
**Thursday:** 1 experiment design (§B) — written + spoken  
**Before onsite:** fill §D for each company
