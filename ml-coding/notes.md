# ML Coding — Notes & Drill Index

> **Interview rule:** PyTorch allowed unless they say numpy-only. **No AI, no Copilot.**

---

## Shape Conventions

Always annotate tensor shapes in comments:

```
B = batch size
T = sequence length (time)
D = model dim (d_model)
H = num heads
Dh = D // H  (head dim)
V = vocab size
```

---

## 🔴 Must Implement From Memory

These come up repeatedly in RS/MTS loops. Target: complete without docs.

| Drill | File | Target time |
|---|---|---|
| Scaled dot-product attention | `drills/01_attention.py` | 20 min |
| Multi-head attention | `drills/02_mha.py` | 30 min |
| Transformer block | `drills/03_transformer_block.py` | 35 min |
| Mini LM forward + loss | `drills/04_mini_lm.py` | 45 min |
| Greedy decode loop | `drills/05_greedy_decode.py` | 20 min |

Start with stubs in `drills/` — implement yourself before peeking at solutions (add solutions only after you've timed yourself).

---

## Attention — Core Equations

**Single head:**

```
Q, K, V = X @ Wq, X @ Wk, X @ Wv     # X: (B, T, D)
scores = (Q @ K^T) / sqrt(Dh)        # (B, T, T)
if mask: scores = scores.masked_fill(mask == 0, -inf)
weights = softmax(scores, dim=-1)
out = weights @ V                      # (B, T, Dh)
```

**Multi-head:** project to Q/K/V, split heads, run attention, concat, output projection.

**Causal mask:** lower-triangular ones; position i may not attend to j > i.

---

## Common Interview Variants

| Prompt | What they're testing |
|---|---|
| "Implement attention" | Shapes, scaling, mask |
| "Add KV cache" | Inference memory + incremental decode |
| "Write training loop for LM" | loss shift, grad clip, basic sanity |
| "Implement beam search" | Priority queue / scoring |
| "Backprop through softmax + linear" | Numerical stability |
| "BPE encode this string" | NLP fundamentals |
| "LayerNorm vs RMSNorm" | Know both; implement one |

---

## Pitfalls (from real loops)

1. **Softmax dimension** — always specify `dim=-1` for attention weights.
2. **Mask dtype** — use `-inf` or a large negative before softmax, not 0.
3. **LM loss shift** — predict token t+1 from position t; logits[:, :-1] vs labels[:, 1:].
4. **Dropout** — off during inference; mention it even if not asked to code.
5. **Off-by-one in loops** — Alisa lost 10 min on 2 hours sleep; test tiny shapes.

---

## Practice Log

Track every timed attempt in [practice-log.md](practice-log.md):

```
Date | Drill | Time | Pass? | Stuck on
```

---

## CS336 Assignment Mapping

Course: [cs336.stanford.edu](https://cs336.stanford.edu/) · Self-study code: [2025 archive](https://cs336.stanford.edu/spring2025/)

| Assignment | What you build | Interview relevance |
|---|---|---|
| **A1 Basics** | Tokenizer + transformer + optimizer + minimal LM | 🔴🔴🔴 — same as `drills/`; do until automatic |
| **A2 Systems** | Profiling, FlashAttention2 (Triton), distributed training | MTS / inference teams; KV cache + memory |
| **A3 Scaling** | Transformer ablations + scaling law fit | "What matters at scale?" rapid-fire |
| **A4 Data** | Common Crawl → filtered pretraining data | Pretraining team discussions |
| **A5 Alignment** | SFT + RL for math reasoning; optional DPO | Post-training / RLHF loops |

**Honor code note:** use lectures + handouts for learning; don't paste solutions into interviews. For vault drills, implement yourself with AI off (stricter than course policy, matches interview conditions).

---

## Before the Interview

- [ ] Fresh blank file → attention in < 25 min
- [ ] Explain KV cache on whiteboard
- [ ] Run one drill without `torch.nn` helpers (only `F` and matmul)
