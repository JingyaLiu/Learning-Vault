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

## Lec 2 — PyTorch, einops, FLOPs, memory ✅

**Date watched:** 6/27/26  
**Trace:** [Lec 2](https://cs336.stanford.edu/lectures/?trace=lecture_02) · [lecture_02.py](cs336-materials/lecture_02.py)

### 3 takeaways

1. **Mechanics:** PyTorch tensor semantics, einops, FLOP counting
2. **Mindset:** always do **resource accounting** (memory + compute)
3. **Intuition:** elementwise ops → **memory-bound**; large matmuls → can be **compute-bound**

### Shapes & dtypes

- `(B, T, D)` = **B** batch · **T** sequence length · **D** model/hidden dim
- Example: batch 32, seq 512, dim 768 → `(32, 512, 768)`
- **Dtypes:** fp32, fp16, bf16, mixed precision (AMP), fp8, fp4 — trade precision vs memory/speed

### einops (one example each)

- **rearrange:** split/merge dims (e.g. flatten `heads × hidden` ↔ separate dims)
- **reduce:** sum/mean/max over a named dim
- **einsum:** generalized matmul with named dims

```python
# rearrange + einsum (from lecture einops_rearrange)
x = torch.ones(3, 8)   # seq, total_hidden (= heads * hidden1)
w = torch.ones(4, 4)   # hidden1, hidden2

x = rearrange(x, "... (heads hidden1) -> ... heads hidden1", heads=2)
x = einsum(x, w, "... hidden1, hidden1 hidden2 -> ... hidden2")
x = rearrange(x, "... heads hidden2 -> ... (heads hidden2)")

# reduce (from lecture einops_reduce)
y = reduce(x, "... hidden -> ...", "sum")
```

### FLOPs / memory

- **FLOPs** = floating-point **operations** (amount of work)
- **FLOP/s** (FLOPS) = ops **per second** (hardware speed) — same pronunciation, different meaning
- Matmul FLOPs: **2 × M × K × N** for `(M,K) @ (K,N)` — one mul + one add per (i,j,k)
- **Training (rough):** total ≈ **6 × (# tokens) × (# parameters)**; per step ≈ **6 × B × num_params**
- **Arithmetic intensity:** FLOPs / bytes moved
- **Roofline:** memory-bound if intensity **<** accelerator intensity (H100 FLOP/s ÷ bytes/s)
- **MFU** (model FLOPs utilization) = actual_FLOP/s ÷ promised_FLOP/s — **≥ 0.5** is good
- **Bottleneck timing:** `total_time = max(bytes/bandwidth, flops/FLOP/s)` (with perfect overlap)
  - Memory-bound: communication time > computation time (e.g. ReLU, GELU)
  - Compute-bound: computation time > communication time (e.g. large matmul)

### Questions → review

- Transformer FLOP accounting in detail (Assignment 1 / later lectures)
- Attention O(T²) — covered more in Lec 3 / Lec 10

---

## Lec 3 — Architectures, hyperparameters

**Date watched:**  
**Watch:** [YouTube Lec 3](https://www.youtube.com/watch?v=lVynu4bo1rY) @ **1.25×** (~70 min) · PDF on [course schedule](https://cs336.stanford.edu/) (no trace viewer for Lec 3)

### Monday session — how to watch (90 min)

**Goal:** fill **3 takeaways** + decoder diagram. Skip stability/MQA/long-context on first pass.


| Phase | Time   | What                                              |
| ----- | ------ | ------------------------------------------------- |
| **A** | 60 min | YouTube @ 1.25× — pause only at checkpoints below |
| **B** | 15 min | Fill 3 takeaways + architecture bullets           |
| **C** | 15 min | Draw decoder stack from memory (Block 2)          |


#### Listen-for checkpoints (pause → one sentence in notes)


| ~time | Topic                                                    | Your one-liner                                                                                                                                                                                                         |
| ----- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0:00  | Why survey many LMs instead of ablate everything?        | LM has different approach on dim, attention, prenorm postnorm and differnt combination, it is hard to say a standard format. Based on exp, data, model size etc. But there are some standard parameters for suggestion |
| 8:54  | **Pre-norm vs post-norm** — which do modern LMs use?     | pre-norm on non residual block                                                                                                                                                                                         |
| 20:16 | **FFN:** ReLU → GELU → **SwiGLU** — what's in one block? | swiglu                                                                                                                                                                                                                 |
| 27:10 | Serial vs parallel block (attn then FFN)                 | seriel longer processing time but high acc,parallel sacrific acc at small model but catch up for larger one. it is about processing attention                                                                        |
| 31:12 | **RoPE** — why relative position?                        | relative position save comp of embeddings and you don't have to know the absolute one                                                                                                                                  |
| 43:36 | FFN dim ≈ **4× D** (or **8/3× D** with GLU)              |                                                                                                                                                                                                                        |
| 50:41 | **H heads**, Dh = D/H                                    | h heads * head_dim = model dim                                                                                                                                                                                         |


**Skip guilt-free (Tue drill covers this):** Z-loss, QK norm, MQA/GQA, sliding window (~1:05–1:28)

#### Interview answers to verify while watching

- **Decoder-only for GPT LMs:** causal self-attn only · one stack predicts next token · no encoder cross-attn
- **One block (modern):** pre-norm → MHA (causal) → residual → pre-norm → SwiGLU FFN → residual
- **Causal mask:** position i cannot attend to j > i
- **Shapes:** embed `(B,T,D)` · same through each block · logits `(B,T,V)`

### 3 takeaways





### Architecture

- **Decoder-only** used for GPT-style LMs because:
- **One block contains:**
- **Pre-norm vs post-norm:**

### Key hyperparameters


| Param           | What it controls         | Interview default                          |
| --------------- | ------------------------ | ------------------------------------------ |
| L (layers)      | depth                    | more L = deeper reasoning, harder to train |
| H (heads)       | parallel attention paths | D = H × Dh                                 |
| D (model dim)   | width                    | aspect ratio D/L ≈ 100 (rule of thumb)     |
| T_max (context) | max sequence length      | longer T → O(T²) attention cost            |
| D_ff            | FFN inner dim            | ≈ 4D (SwiGLU: ≈ 8/3 × D)                   |
| V (vocab)       | tokenizer size           | ~32k mono · 100k+ multilingual             |


### Decoder-only stack (draw from memory)

```
Input token IDs (B, T)
    ↓
Token embed + positional (RoPE/learned)
    ↓
┌─ Transformer block × L ─────────────────┐
│  Pre-norm → Multi-head self-attn (causal)│
│  + residual                              │
│  Pre-norm → FFN (SwiGLU)                 │
│  + residual                              │
└──────────────────────────────────────────┘
    ↓
Layer norm → LM head (D → V)
    ↓
Logits (B, T, V) → next-token CE loss
```

**Check aloud after drawing:** `(B,T,D)` at embed and block out · why causal mask · where O(T²) happens

---

## Lec 7–9 · Lec 15–16 · Lec 13–14

*Stretch / Aug — see [ML_JOB_SEARCH_PLAN.md](../plan/ML_JOB_SEARCH_PLAN.md)*