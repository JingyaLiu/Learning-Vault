# Jul W1 · Jul 7–13 ✅ archive

> **Current week:** [THIS_WEEK.md](THIS_WEEK.md)  
> **Profile:** Jingya Liu · Staff DS @ Walmart · [LinkedIn](https://www.linkedin.com/in/jingya-tina-liu/) · ~12–14 hr/week  
> **Full plan:** [ML_JOB_SEARCH_PLAN.md](ML_JOB_SEARCH_PLAN.md#prep-by-target-tier)  
> **Branch:** `lc` for LC · this branch for ML/process

**Closed:** Sun Jun 28 · Pitch R+X · LC 125/167/704 · Lec 1–2 · §G-R

---

## Today · Day 6 · Sunday (~2.5 hr) ← **start here**

**Do not skip** — this is the highest-ROI block of the week.

| Block | Time | Task | Done |
|---|---|---|---|
| **1** | 45 min | Draft **pitch R** (2 min) + fill **Q10** metrics | [x] |
| **2** | 45 min | Draft **pitch X** (2 min) — production FM, thousands of sellers/advertisers | [x] |
| **3** | 30 min | LinkedIn **Walmart bullets** (ads + CX FM) | [ ] deferred |
| **4** | 30 min | LC **704** re-solve from memory | [x] |
| *opt* | 15 min | Confirm pipeline tiers in [process-tracker](../job-search/process-tracker.md) | [ ] |

**Templates:** [pitch-template.md](../research/pitch-template.md) → search "Pitch R draft"

### Block 1 · Pitch R (Amazon Ads path)

Open [pitch-template → Pitch R draft](#) and fill:

1. **One metric** — recall@100, CTR lift, or p99 latency (even a range)
2. **One design choice** — dual-tower, hard negatives, two-stage, etc.
3. Read aloud in **≤ 2 min** · record optional

### Block 2 · Pitch X (Microsoft Copilot / Sierra path)

1. **One metric** — offline eval score, vs GPT-4, resolution rate, etc.
2. **Domain FM angle** — data mix, eval suite, production iteration
3. Read aloud **≤ 2 min**

### Block 3 · LinkedIn bullets — **skipped for now**

Bullets drafted in [pitch-template.md](../research/pitch-template.md) → search **"LinkedIn bullets"**. Paste when ready.

### Block 4 · LC 704 ← **do this**

`lc` branch · Binary Search · **no hints** · target **10 min** cold.

### LC 704 · Binary Search ✅

**Pattern:** `left, right = 0, len(nums)-1` · `while left <= right` · three-way compare

```python
while left <= right:          # NOT left < right — skips last element
    mid = left + (right - left) // 2
    if nums[mid] == target: return mid
    elif nums[mid] < target: left = mid + 1
    else: right = mid - 1
return -1
```

**Gotcha:** `left < right` fails when target is last index or single-element array (`[5], 5` → -1).

---

## Carry-over from Sat (optional, not today)

- [ ] Lec 3 + decoder diagram → [cs336-notes.md](../ml-coding/cs336-notes.md) · Jul W2 Sat AM if skipped

---

| Block | Time | Task | Done |
|---|---|---|---|
| **1** | 90 min | CS336 **Lec 2** @ 1.25× · [trace](https://cs336.stanford.edu/lectures/?trace=lecture_02) · notes → [cs336-notes.md](../ml-coding/cs336-notes.md) | [ ] |
| **2** | 60 min | CS336 **Lec 3** @ 1.25× · playlist #3 · architecture notes | [ ] |
| **3** | 30 min | **Draw decoder-only stack** from memory (template below) | [ ] |

**LC:** off · **No Stretch/P**

### Lec 2 focus (while watching)

- `(B, T, D)` through a batch
- **einops:** `rearrange`, `reduce`, `einsum` — one example each
- **FLOPs:** attention **O(T²)** · matmul dominates
- **Arithmetic intensity:** memory bandwidth bottleneck (HBM ↔ compute)

### Lec 3 focus (while watching)

- Decoder-only vs encoder-decoder
- Block = attention + FFN + norms + residuals
- Hyperparameters: layers, heads, D, context length

### Block 3 · Decoder-only stack (draw after Lec 3)

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

**Check:** label shapes `(B,T,D)` at embed and block output.

---

## Yesterday · Day 4 · Friday ✅

- [x] LC 125 Valid Palindrome
- [x] LC 167 Two Sum II

### LC 125 · Valid Palindrome

**Pattern:** two pointers · `l`, `r` from ends · skip non-alphanumeric · `lower()`

```python
while l < r:
    while l < r and not s[l].isalnum(): l += 1
    while l < r and not s[r].isalnum(): r -= 1
    if s[l].lower() != s[r].lower(): return False
    l += 1; r -= 1
return True
```

**Gotchas:** empty string → True · single char → True · don't forget `isalnum()`

---

### LC 167 · Two Sum II (sorted array)

**Pattern:** two pointers · `l=0`, `r=len-1` · move pointer by sum vs `target`

```python
l, r = 0, len(numbers) - 1
while l < r:
    s = numbers[l] + numbers[r]
    if s == target: return [l + 1, r + 1]   # 1-indexed
    elif s < target: l += 1
    else: r -= 1
```

**Why it works:** sorted → if sum too small, must increase left; too big, decrease right.

**Gotchas:** return **1-indexed** indices · exactly one solution guaranteed

---

**After both:** note pattern in `lc` branch log · target **20 min each** cold.

---

## Yesterday · Day 3 · Thursday ✅

- [x] CS336 Lec 1 + notes
- [x] §G-R Q1–9

---

## Active track this week

| Tier | Focus | Why now |
|---|---|---|
| 🎯 **Primary** | **R** + **X** | Amazon Ads + Microsoft Copilot = Oct–Nov offer path |
| 🏋️ Practice | Map only — apply in Aug | Not applying yet |
| 🎯 Stretch | **Defer P** | Apple FM / Google wait until Aug W3 |
| ⭐ Dream | **Skip** | Meta/OpenAI until Oct+ |

**Study mix (ML + rapid-fire, excl. LC):** R 35% · X 35% · T 10% · fundamentals 20% · **P 0%**

---

## Week milestone (Sun)

- [ ] Pipeline tiers tagged in [process-tracker.md](../job-search/process-tracker.md) (🏋️ / 🎯 Primary / 🎯 Stretch / ⭐)
- [ ] Pitch **R** + **X** — 2 min each, **each with ≥1 metric** · [pitch-template](../research/pitch-template.md#pitch-variants-by-pillar)
- [ ] Walmart LinkedIn bullets: ads retrieval (**R**) + CX FM (**X**) — **deferred**

---

## Pillar focus

| Pillar | This week | Next week |
|---|---|---|
| **R** | §G-R Thu (10 Qs) · pitch **R** outline Sun | Jul W3: record pitch **R** |
| **X** | pitch **X** outline Sun | Jul W4: §G-X + record |
| **T** | — | Aug W1: Lec 15–16 |
| **P** | **Do not study** | Aug W3: Lec 7–9 |

---

## Day by day

### Tuesday · Day 1 ✓

- [x] **`lc`:** Binary Search — LC 704 + LC 34
- [ ] Optional: LC 35 Search Insert

---

### Wednesday · Day 2 ✓

| Block | Task | Tier |
|---|---|---|
| **LC** 60 min | Two Sum (1) + Valid Anagram (242) | Primary (LC baseline) |
| **Process** 30 min | Tag 8 **Primary** rows in [process-tracker](../job-search/process-tracker.md) | Primary |

**Primary rows to confirm:** Amazon Ads · Amazon Search · Microsoft Copilot · Microsoft Ads · Apple Search · Apple Siri · Snowflake ×2

---

### Thursday · Day 3 ✓

| Block | Task | Done |
|---|---|---|
| **ML** 60 min | CS336 **Lec 1** + notes | [x] |
| **Rapid-fire** 15 min | §G-R Q1–9 ✅ · Q10 draft below | [x] |

#### §G-R rapid-fire (Day 3 — answer aloud, ≤60 sec each)

- [x] 1. Dual-tower vs cross-encoder — when use which at ads/search scale?

**Your answer:** dual-tower for retrieval (query–item, cosine); cross-encoder for pair relevance score.

**Model:** **Dual-tower** — separate query/item encoders → cosine/dot → **ANN over full catalog** (recall stage, fast). **Cross-encoder** — query+doc **jointly** encoded → accurate relevance but O(n) → **rerank top-K only** (e.g. 100–500). At ads scale: retrieve with dual-tower + FAISS/HNSW, rerank with cross-encoder.

---

- [x] 2. What is ANN (FAISS/HNSW) and what does recall@k trade off against?

**Your answer:** ~~ANN = attention neural network~~; FAISS batch similarity; recall vs search pool.

**Model:** **ANN = Approximate Nearest Neighbor** (not attention). **FAISS/HNSW** = index structures for fast similarity search at scale. **recall@k** = how often the true match appears in top-k. Trades against **latency / compute / memory** — higher recall → scan more candidates or slower index.

---

- [x] 3. NDCG vs recall@k — offline vs online, which when?

**Your answer:** ~~NDCG online, recall offline~~

**Model:** **Both NDCG and recall@k are offline.** recall@k → retrieval quality; NDCG@k → ranking with **graded** relevance + position discount. **Online** = A/B: CTR, CVR, RPM, revenue. Train/eval offline on NDCG/recall; ship only if online CTR + guardrails pass.

---

- [x] 4. Hard negative mining — why and one failure mode

**Your answer:** similar items, same category; pushes boundary; false negative / popular-negative bias.

**Model:** **Why:** easy negatives don't sharpen the boundary; hard negatives (similar but irrelevant) improve ranking. **Failure mode:** **false negative** — mined item was actually relevant → wrong gradient; or **popularity bias** — always mining head items.

---

- [x] 5. Cold start for new queries or advertisers — your approach?

**Your answer:** embedding + similar-item warm-start.

**Model:** **Side features** (category, metadata) in tower; **cluster/default embedding** warm-start; **exploration** budget until enough clicks; **content-based** retrieval until events accumulate; periodic **embedding refresh** as data arrives.

---

- [x] 6. Latency budget: 50ms p99 — what do you cut first?

**Your answer:** smaller K, cache embeddings, skip rerank, distill model, ANN params.

**Model:** (1) Reduce **K** candidates (2) **Precompute/cache** item embeddings; cache hot queries (3) **Skip/lighten cross-encoder** rerank (4) **Distill** first-stage model (5) Tune ANN (**efSearch** ↓ = faster, lower recall).

---

- [x] 7. Embedding refresh cadence — stale embeddings symptom?

**Your answer:** (was blank)

**Model:** **Cadence:** hot items hourly/daily; full index weekly (depends on catalog churn). **Stale symptoms:** new ads/items **never retrieve well**; offline recall OK but **online CTR drops**; similarity scores miscalibrated after catalog shift.

---

- [x] 8. Online A/B for ranking — one metric + one guardrail

**Your answer:** CTR; guardrail revenue?

**Model:** **Primary:** CTR or CVR (ads relevance). **Guardrails:** latency p99 < 50ms; **revenue/session** not down > X%; spam/low-quality rate; user complaint rate. (Revenue is usually the **goal**, not the guardrail.)

---

- [x] 9. RAG as retrieval — how is it same/different from ads retrieval?

**Your answer:** both embed + search; ads multi-aspect.

**Model:** **Same:** encode query → retrieve top-K by embedding similarity. **Different:** **RAG** retrieves **chunks** to **augment LLM context** (generative downstream). **Ads** retrieves **ads** → **rank + auction**; multi-objective (relevance × bid × quality score); real-time feedback loops; policy/fraud constraints.

---

- [x] 10. **Your ads retrieval:** one metric + one design choice you'd defend

**Your answer (filled from A/B results):**

> **Metric:** CTR **+4.46%** · ad revenue **+5.46%** · clicks **+5.78%** · impressions **+1.26%** — all **stat sig** vs text-only production control (bucket 13657 vs multimodal 13658). Also eCTR, eCPM, eCPMV improved.

> **Defend:** **Multimodal retrieval** (visual + text signals) over text-only baseline — sponsored products relevance is inherently visual; multimodal model improved engagement and revenue with rigorous online A/B.

→ Full pitch: [pitch-template.md](../research/pitch-template.md) **Pitch R draft**

**After Lec 1:** tokenization → encode strings to token IDs · embed → ID → D-dim vector · decoder-only → causal next-token prediction ✅ ([cs336-notes.md](../ml-coding/cs336-notes.md))

---

### Friday · Day 4 ← **today**

| Block | Task | Done |
|---|---|---|
| **LC** 60 min | Valid Palindrome (125) + Two Sum II (167) | [ ] |
| **Bonus** | Group Anagrams (49) or §G-R Q2/Q3/Q7 re-drill | [ ] |

---

### Saturday · Day 5

| Block | Task | Done |
|---|---|---|
| **ML** 90 min | Lec 2 — PyTorch, einops, FLOPs | [x] |
| **ML** 60 min | Lec 3 — architectures | [ ] |
| **ML** 30 min | Decoder stack diagram | [ ] |

---

### Sunday · Day 6 ← **today**

| Block | Task | Done |
|---|---|---|
| **Process** 90 min | Pitch **R** + **X** (2 min each) + Q10 metrics | [x] |
| **Process** 30 min | LinkedIn Walmart bullets | [ ] |
| **LC** 30 min | Re-solve LC 704 from memory | [ ] |

---

## If energy is low

| Day | Minimum | Tier |
|---|---|---|
| Wed | Two Sum only | Primary |
| Thu | Half of Lec 1 + 5 §G-R Qs | Primary **R** |
| Sun | **Do not skip** — pitch **R** outline + tier tags | Primary |

---

## Sync with `lc` INTERVIEW_PLAN

| `lc` day | This week |
|---|---|
| Day 1 Binary Search | Tue |
| Day 2 Hash Maps | Wed |
| Day 3 Two Pointers | Fri |

---

## Next week preview (Jul W2)

Primary: attention/MHA drills · behavioral stories 1–4 · **2 outreach (Amazon Ads first)** · still **no P**.
