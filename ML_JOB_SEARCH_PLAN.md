# ML / Research Scientist Job Search Plan

> **Companion to:** [`lc` branch](https://github.com/JingyaLiu/Learning-Vault/tree/lc) → LeetCode / general coding (`INTERVIEW_PLAN.md`)  
> **Inspired by:** [Alisa's industry job search notes](https://alisawuffles.github.io/blog/job-search/)  
> **Your pace:** ~90 min/day on ML topics + keep `lc` at 2 problems/day  
> **Start here:** [Daily split](#daily-split-lc--ml) → [Phase 1](#phase-1--foundations-weeks-1–4)

**Last updated:** June 23, 2026  
**Current:** Phase 1 · Week 1 · not started  
**Legend:** 🔴 = highest ROI · 🟡 = common · ⚪ = company-specific

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
| ML & research | `main` | **This file** |
| ML implement-from-scratch | `main/ml-coding/` | [notes.md](ml-coding/notes.md) |
| Rapid-fire & system design | `main/technical-discussion/` | [notes.md](technical-discussion/notes.md) |
| Research pitch & CV deep-dives | `main/research/` | [pitch-template.md](research/pitch-template.md) |
| Behavioral (STAR) | `main/behavioral/` | [story-bank.md](behavioral/story-bank.md) |
| Math | `main/math/` | [notes.md](math/notes.md) |
| Job talk | `main/job-talk/` | [outline.md](job-talk/outline.md) |
| Negotiation | `main/negotiation/` | [playbook.md](negotiation/playbook.md) |

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
| W1D4 | Skim [ml-coding/notes.md](ml-coding/notes.md); BPE encode/decode on paper | A1 tokenizer | [ ] |
| W1D5 | Pre-norm block: attention + FFN + residuals + LayerNorm | A1 model | [ ] |
| W1D6 | Full decoder-only stack diagram from memory | A1 preview | [ ] |
| W1D7 | Rest: re-draw architecture; journal gaps | — | [ ] |

### Week 2 — Assignment 1 core (implement, no AI) 🔴

Maps to CS336 A1: *tokenizer + transformer + optimizer + minimal LM training*.

| Day | Block B | Vault drill | Done |
|---|---|---|---|
| W2D1 | Scaled dot-product attention | [01_attention.py](ml-coding/drills/01_attention.py) | [ ] |
| W2D2 | Multi-head attention | [02_mha.py](ml-coding/drills/02_mha.py) | [ ] |
| W2D3 | Transformer block (attn + FFN + norms) | [03_transformer_block.py](ml-coding/drills/03_transformer_block.py) | [ ] |
| W2D4 | Mini LM forward pass | [04_mini_lm.py](ml-coding/drills/04_mini_lm.py) | [ ] |
| W2D5 | Causal LM loss (label shift) + AdamW step | A1 training loop | [ ] |
| W2D6 | **Optional:** start [A1 code](https://cs336.stanford.edu/spring2025/) on CPU | A1 | [ ] |
| W2D7 | Timed re-implement: attention from blank file (45 min) | 01_attention | [ ] |

### Week 3 — Lec 5–6, 10, 12: systems + inference

| Day | Block B | CS336 | Done |
|---|---|---|---|
| W3D1 | Lec 5–6: GPUs, arithmetic intensity, kernels/Triton (concepts) | Lec 5–6 | [ ] |
| W3D2 | Lec 10: inference — KV cache implement + explain | Lec 10 | [ ] |
| W3D3 | Greedy / top-k / top-p decoding | [05_greedy_decode.py](ml-coding/drills/05_greedy_decode.py) | [ ] |
| W3D4 | Beam search (optional) | — | [ ] |
| W3D5 | Lec 12: evaluation — perplexity, benchmarks, pitfalls | Lec 12 | [ ] |
| W3D6 | Backprop through attention by hand (one layer) | — | [ ] |
| W3D7 | Rapid-fire: 20 Qs from [technical-discussion/](technical-discussion/notes.md) §A | — | [ ] |

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

Track times in [ml-coding/practice-log.md](ml-coding/practice-log.md).

### Weekly technical deep-dives (Block B, days you aren't doing a long drill)

| Week | Theme | Prep |
|---|---|---|
| 5 | Experiment design | [technical-discussion/](technical-discussion/notes.md) §B — 3 prompts |
| 6 | Scaling & systems | §C + "How to Scale Your Model" |
| 7 | RLHF / alignment | PPO vs GRPO, reward modeling |
| 8 | Your specialty area | 5 papers + 10 rapid-fire Qs you write yourself |

### Math (2× per week, 30 min each — fold into Block B or C)

Use [math/notes.md](math/notes.md). Focus: probability, linear algebra, calculus.

---

## Phase 3 — Research, Behavioral, Job Talk (Weeks 9–12)

**Goal:** Sound like a researcher *and* an engineer in the same hour.

### Research pitch (start Week 9)

1. Fill [research/pitch-template.md](research/pitch-template.md) for **one flagship project**.
2. Prepare 2-min, 5-min, and 15-min versions.
3. For every CV paper: *motivation → method one-liner → key result → what you'd do next*.
4. Tailor keywords to role (pretraining / post-training / eval / infra).

**Weekly:** 1 mock research conversation (friend or record yourself).

### Behavioral (start Week 9, 30 min × 2/week)

1. Complete [behavioral/story-bank.md](behavioral/story-bank.md) — **minimum 8 STAR stories**.
2. Map stories → Amazon LP-style questions + generic "tell me about a time…"
3. **Do not wing behavioral.** Alisa's first one failed for exactly this reason.

### Job talk (Weeks 10–12)

1. Draft using [job-talk/outline.md](job-talk/outline.md).
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

**After each mock:** notes in [interview-journal.md](interview-journal.md).

---

## Phase 4 — Negotiation & Process (When You Have Offers)

Don't start here early — but read [negotiation/playbook.md](negotiation/playbook.md) once before first recruiter call so you know the game exists.

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

Parallel to studying — track in a spreadsheet or [process-tracker.md](process-tracker.md):

- [ ] List 15–20 target companies / teams
- [ ] Map 1st-degree + 2nd-degree contacts per company
- [ ] Schedule 2–3 **practice** processes early (not favorites first if stamina-limited)
- [ ] Track: applied → recruiter → phone → onsite → offer → outcome
- [ ] Log ghosted vs withdrawn vs reject — normalizes the noise

**Getting the first interview:** referrals + conference connections + cold outreach to researchers on teams you want. Expected and okay to reconnect with people you haven't talked to in years.

---

## Progress at a Glance

| Phase | Weeks | Focus | Status |
|---|---|---|---|
| 1 Foundations | 1–4 | CS336 + transformer | not started |
| 2 Drills | 5–8 | ML coding rotation | not started |
| 3 Mocks | 9–12 | Research + behavioral + talk | not started |
| 4 Negotiation | offers | Comp + decisions | — |
| lc (parallel) | 1–11 | LeetCode Pass 1–3 | Day 1 done (`lc`) |

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

*90 min ML + 2 LC problems. Tailor each week to your next interview. Circle back to weak drills like you circle back to weak LC patterns.*
