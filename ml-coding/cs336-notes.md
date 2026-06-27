# CS336 — Lecture Notes

> **Watch:** [YouTube playlist](https://www.youtube.com/watch?v=JuoVZkPBiKk&list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV) @ 1.25×  
> **Scripts:** [cs336-materials/](cs336-materials/) · **Reference:** [notes.md](notes.md)  
> **Drills (Jul W2+):** [drills/](drills/) + [practice-log.md](practice-log.md)

---

## Lec 1 — Overview, tokenization ✅

**Date watched:** 6/25/26 · **Trace:** [Lec 1](https://cs336.stanford.edu/lectures/?trace=lecture_01)

### 3 takeaways

1. LM stack: tokenizer → embed → decoder-only transformer → next-token loss
2. BPE balances vocab size vs compression; attention O(T²) → fewer tokens helps
3. Char/byte/word each fail; BPE is the practical default

### Tokenization

- **BPE:** Byte Pair Encoding — merge most frequent adjacent pairs from bytes until vocab K
- **Subword vs word:** fixed vocab, handles OOV, better compression → shorter T

### Pipeline

- **tokenization →** strings ↔ token IDs (vocab + BPE merges)
- **embed →** token ID → D-dim vector
- **decoder-only →** causal blocks, next-token prediction

---

## Lec 2 — PyTorch, einops, FLOPs, memory

**Date watched:**  
**Trace:** [Lec 2](https://cs336.stanford.edu/lectures/?trace=lecture_02) · [lecture_02.py](cs336-materials/lecture_02.py)

### 3 takeaways

1.
2.
3.

### Shapes

- `(B, T, D)` = **B** batch · **T** sequence length · **D** model/hidden dim
- Example: batch 32, seq 512, dim 768 → `(32, 512, 768)`

### einops (one example each)

- **rearrange:** (split/merge dims, e.g. heads)
- **reduce:** (sum/mean over dim)
- **einsum:** (matmul pattern)

My example:

```python
# fill after watching tensor_einops / einops_rearrange sections
```

### FLOPs / memory

- Attention cost vs T: **O(T²)** compute and memory
- Matmul FLOPs: roughly **2×** multiply-adds for `(M,K) @ (K,N)`
- **Arithmetic intensity:** FLOPs / bytes moved — if low, **memory bandwidth** bound (GPU HBM)

### Questions → review

-

---

## Lec 3 — Architectures, hyperparameters

**Date watched:**  
**Link:** playlist #3 · PDF on [course site](https://cs336.stanford.edu/)

### 3 takeaways

1.
2.
3.

### Architecture

- **Decoder-only** used for GPT-style LMs because:
- **One block contains:**
- **Pre-norm vs post-norm:**

### Key hyperparameters

| Param | What it controls |
|---|---|
| L (layers) | depth |
| H (heads) | parallel attention paths; D = H × Dh |
| D (model dim) | width |
| T_max (context) | max sequence length |

### Decoder-only stack (draw from memory)

```
(paste your drawing here — or use THIS_WEEK.md template)
```

---

## Lec 7–9 · Lec 15–16 · Lec 13–14

*Stretch / Aug — see [ML_JOB_SEARCH_PLAN.md](../plan/ML_JOB_SEARCH_PLAN.md)*
