# ML / Research Scientist Job Search Plan

> **Companion to:** [`lc` branch](https://github.com/JingyaLiu/Learning-Vault/tree/lc) → LeetCode / general coding (`INTERVIEW_PLAN.md`)  
> **Inspired by:** [Alisa's industry job search notes](https://alisawuffles.github.io/blog/job-search/)  
> **Start here (employed):** [Employed Track — Jul → Nov 2026](#employed-track--jul-2026--nov-2026-start-here)  
> **Start here (full-time prep):** [Phase 1](#phase-1--foundations-weeks-1–4)

**Last updated:** July 2026  
**Profile:** Full-time employee · ~12–14 hrs/week · target offer **Oct–Nov 2026**  
**Legend:** 🔴 = highest ROI · 🟡 = common · ⚪ = company-specific · ✅ = milestone

---

## Employed Track — Jul 2026 → Nov 2026 (START HERE)

**Why this calendar:** Tech hiring peaks **Sep–Oct**. Jul–Aug is slow (vacations) but ideal for **prep + referrals**. Employed ML/RS searches realistically take **4–6 months** ([data](https://asmekal.github.io/blog/posts/interviews-2025-ml-research-engineer-uk)).

```
Jul–Aug        Sep–Oct           Oct–Nov
准备+内推  →   面试高峰    →    谈 offer / 签约
练手面试       目标公司 onsite
```

### Targets

| Milestone | Date | Done |
|---|---|---|
| 15 家公司 list + pitch 初稿 | Jul 13 | [ ] |
| 8 条 behavioral STAR 故事 | Jul 20 | [ ] |
| attention + MHA 45 min 内写完 | Jul 27 | [ ] |
| 第一批内推发出 (≥5) | Jul 31 | [ ] |
| 第一个 phone screen | Aug 31 | [ ] |
| ≥2 家公司在流程中 | Sep 15 | [ ] |
| 第一个 onsite | Sep 30 | [ ] |
| 第一个 written offer | Oct 31 | [ ] |
| 签约 | Nov 15 | [ ] |

### Weekly time budget (~12–14 hrs)

| Slot | Time | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|---|
| **LC** | 60 min | ⭐⭐ | — | ⭐⭐ | — | ⭐⭐ | — | re-solve |
| **ML** | 60 min | — | drill | — | drill | — | **3 hr** | — |
| **Process** | 30–60 min | — | — | outreach | — | — | — | **2 hr** |
| **Rapid-fire** | 15 min | — | 10 Qs | — | 10 Qs | — | — | — |

**Rules**
- ML coding drills: **no AI**
- **Never skip Sunday process block** in Jul–Aug (内推 > 多刷一道题)
- 面试季 (Sep+)：按 [Per-Interview Cram](#per-interview-cram-checklist-3-days-before) 准备，维持性复习即可
- 告诉 recruiter 你在职，每轮之间需要 **≥1 周**

---

## July 2026 — 准备冲刺 + 开管道

**主题：** 最小可行 ML 能力 + pitch/behavioral + 内推。还不追求大厂 onsite。

### Jul W1 · Jul 7–13 — 开图

| 块 | 任务 | 文件 | Done |
|---|---|---|---|
| LC ×3 | Two Sum (1), Valid Anagram (242), Group Anagrams (49) | `lc` hash-maps | [ ] |
| ML ×2 | CS336 Lec 1–2 (1.25×); skim shape conventions | [ml-coding/notes.md](ml-coding/notes.md) | [ ] |
| ML Sat | Lec 3 + 画 decoder-only 架构图 | CS336 | [ ] |
| Process Sun | 列 15 目标公司/团队; 每一家 1 个联系人 | [process-tracker.md](process-tracker.md) | [ ] |
| Process Sun | 填 flagship project 初稿 (2-min pitch) | [research/pitch-template.md](research/pitch-template.md) | [ ] |

### Jul W2 · Jul 14–20 — 第一个 drill

| 块 | 任务 | Done |
|---|---|---|
| LC ×3 | Valid Palindrome (125), Two Sum II (167), 3Sum (15) | [ ] |
| ML ×2 | [01_attention.py](ml-coding/drills/01_attention.py) → [02_mha.py](ml-coding/drills/02_mha.py) | [ ] |
| ML Sat | Lec 4 + Illustrated GPT-2; timed attention 45 min | [ ] |
| Process Sun | behavioral 故事 1–4 | [behavioral/story-bank.md](behavioral/story-bank.md) | [ ] |
| Process Sun | 发 **2 条** 内推/暖消息 | [ ] |

### Jul W3 · Jul 21–27 — mini LM

| 块 | 任务 | Done |
|---|---|---|
| LC ×3 | Longest Substring (3), Min Window (76), Container Water (11) | [ ] |
| ML ×2 | [03_transformer_block.py](ml-coding/drills/03_transformer_block.py) → [04_mini_lm.py](ml-coding/drills/04_mini_lm.py) | [ ] |
| ML Sat | causal loss + AdamW; log times in [practice-log.md](ml-coding/practice-log.md) | [ ] |
| Process Sun | behavioral 故事 5–8 + question map | [ ] |
| Process Sun | 发 **2 条** 内推; 投 **1 家练手公司** | [ ] |

### Jul W4 · Jul 28 – Aug 3 — 推理 + 快问快答

| 块 | 任务 | Done |
|---|---|---|
| LC ×3 | Merge Intervals (56), Meeting Rooms II (253), Product Except Self (238) | [ ] |
| ML ×2 | Lec 10 概念; [05_greedy_decode.py](ml-coding/drills/05_greedy_decode.py); KV cache 口述 | [ ] |
| ML Sat | rapid-fire §A 刷 30 题; 标记不会的 | [technical-discussion/notes.md](technical-discussion/notes.md) | [ ] |
| Process Sun | 读 [negotiation/playbook.md](negotiation/playbook.md) 一遍 | [ ] |
| Process Sun | 发 **3 条** 内推; pitch 录 5-min 版自听 | [ ] |

**Jul 出口标准**
- [ ] attention + MHA < 45 min
- [ ] 5-min research pitch 流利
- [ ] 8 STAR 故事写完
- [ ] ≥5 内推已发出; 1 家已投递

---

## August 2026 — 练手面试 + 巩固

**主题：** 暑假流程慢，正好用练手公司校准题型。LC 切到 trees/graphs。

### Aug W1 · Aug 4–10

| 块 | 任务 | Done |
|---|---|---|
| LC ×3 | Reverse LL (206), LRU Cache (146), Max Depth (104) | [ ] |
| ML ×2 | **Timed:** full transformer forward 90 min | [ ] |
| ML Sat | Lec 15–16 (SFT/RLHF) + GRPO skim | [ ] |
| Process Sun | 投 1–2 练手; 更新 tracker | [ ] |
| Process Sun | 1 次 mock research 对话 (自录) | [ ] |

### Aug W2 · Aug 11–17

| 块 | 任务 | Done |
|---|---|---|
| LC ×3 | Level Order (102), Validate BST (98), LCA (236) | [ ] |
| ML ×2 | ML drill rotation (#1–3); 复习 weak rapid-fire Qs | [ ] |
| ML Sat | experiment design §B 写 2 题答案 + 口述 | [ ] |
| Process Sun | 跟进 stale 内推 (>1 周无回复) | [ ] |

### Aug W3 · Aug 18–24

| 块 | 任务 | Done |
|---|---|---|
| LC ×3 | Number of Islands (200), Course Schedule (207), Clone Graph (133) | [ ] |
| ML ×2 | drill rotation; 1 道 LC ⭐⭐ 限时 45 min | [ ] |
| Process | **第一个 phone screen** (或 mock ML coding 60 min) | [ ] |
| Process Sun | 面完写 [interview-journal.md](interview-journal.md) | [ ] |

### Aug W4 · Aug 25–31

| 块 | 任务 | Done |
|---|---|---|
| LC ×3 | Kth Largest (215), Top K (347), Merge K Lists (23) | [ ] |
| ML ×2 | 针对已投公司填 §D cram sheet ×2 | [technical-discussion/notes.md](technical-discussion/notes.md) | [ ] |
| ML Sat | mock: ML coding 60 min | [ ] |
| Process Sun | 投 **2 家目标公司** (非练手) | [ ] |

**Aug 出口标准**
- [ ] ≥15 ⭐⭐ LC 做过; 5 道可默写
- [ ] 1 次真实或高保真 mock 面试
- [ ] transformer forward 90 min timed pass
- [ ] rapid-fire §A ≥ 70%

---

## September 2026 — 面试高峰

**主题：** 维持性复习 (30 min/day) + 面试优先。周末补弱项。

### 每周固定节奏 (面试季)

| 每天 | 有面试 | 无面试 |
|---|---|---|
| 平日 30 min | cram sheet 复习 | 1 ⭐⭐ LC re-solve |
| 平日 30 min | — | 10 rapid-fire Qs |
| 周六 2 hr | 弱项补课 | 1 ML drill 维持 |
| 周日 1 hr | [interview-journal](interview-journal.md) + 下周排期 | outreach 跟进 |

### Sep 里程碑周

| 周 | 面试目标 | 学习 | Done |
|---|---|---|---|
| Sep W1 | 完成练手流程或拿 feedback | 弱项 from journal | [ ] |
| Sep W2 | ≥1 目标公司 phone screen | cram for that company | [ ] |
| Sep W3 | **≥2 家并行流程** | behavioral mock 30 min | [ ] |
| Sep W4 | 第一个 onsite 或 virtual onsite | job-talk outline 若需要 | [job-talk/outline.md](job-talk/outline.md) |

**Sep 出口标准**
- [ ] ≥2 家公司在流程中
- [ ] 完成 ≥1 onsite
- [ ] 每轮面试有 journal 条目

---

## October 2026 — onsite + offer

| 周 | 重点 | Done |
|---|---|---|
| Oct W1–2 | 集中 onsite; 面前一天 cram | [ ] |
| Oct W3 | 第一个 verbal/written offer → [negotiation/playbook.md](negotiation/playbook.md) | [ ] |
| Oct W4 | 对齐多个 offer 截止日期; teammate 1:1 | [ ] |

**Oct 出口标准**
- [ ] ≥1 written offer in hand
- [ ] 谈判脚本用过至少一次

---

## November 2026 — 决策 + 签约

| 任务 | Done |
|---|---|
| 比较 offer (base / equity / vest / level) | [ ] |
| 谈妥 level + comp; 拿 written final | [ ] |
| **签约** (target Nov 15) | [ ] |
| 规划离职 notice period | [ ] |

---

## LC 加速路径 (在职版)

不走完整 Pass 1–3。目标 **Aug 31** 前完成下方 ⭐⭐ 清单。

| # | Problem | LC | By |
|---|---|---|---|
| 1 | Two Sum | 1 | Jul W1 |
| 2 | Valid Parentheses | 20 | Jul W4 |
| 3 | Longest Substring | 3 | Jul W3 |
| 4 | Min Window | 76 | Jul W3 |
| 5 | 3Sum | 15 | Jul W2 |
| 6 | Container Water | 11 | Jul W3 |
| 7 | Product Except Self | 238 | Jul W4 |
| 8 | Merge Intervals | 56 | Jul W4 |
| 9 | Meeting Rooms II | 253 | Jul W4 |
| 10 | Binary Search | 704 | done (`lc`) |
| 11 | Search Range | 34 | done (`lc`) |
| 12 | Search Rotated | 33 | Aug W2 |
| 13 | Reverse Linked List | 206 | Aug W1 |
| 14 | LRU Cache | 146 | Aug W1 |
| 15 | Number of Islands | 200 | Aug W3 |
| 16 | Course Schedule | 207 | Aug W3 |
| 17 | Max Depth / Level Order | 104/102 | Aug W2 |
| 18 | Validate BST | 98 | Aug W2 |
| 19 | LCA | 236 | Aug W2 |
| 20 | Kth Largest | 215 | Aug W4 |
| 21 | Top K Frequent | 347 | Aug W4 |
| 22 | Merge K Lists | 23 | Aug W4 |
| 23 | Subsets | 78 | Sep W1 |
| 24 | Combination Sum | 39 | Sep W1 |
| 25 | Climbing Stairs | 70 | Sep W1 |
| 26 | House Robber | 198 | Sep W2 |
| 27 | Coin Change | 322 | Sep W2 |
| 28 | Word Break | 139 | Sep W2 |
| 29 | LIS | 300 | Sep W3 |
| 30 | Trapping Rain Water | 42 | Sep W3 |
| 31 | Word Ladder | 127 | Sep W4 |

**Sep+:** 只 re-solve，不做新题。面试前夜：1 道 ⭐⭐ 默写。

---

## ML 能力里程碑 (在职版)

| 日期 | 必须达到 | 验证方式 |
|---|---|---|
| Jul 27 | attention + MHA | timed drills |
| Aug 10 | mini LM + loss | [04_mini_lm.py](ml-coding/drills/04_mini_lm.py) |
| Aug 24 | full transformer 90 min | blank file timed |
| Aug 31 | rapid-fire §A 70% | 20 Qs cold |
| Sep 15 | per-company cram 熟练 | §D sheets |
| Ongoing | KV cache + decoding 能口述 | whiteboard |

**CS336 (在职只看这些):** Lec 1–4, 10, 15–16。A1 drills 必做; A2–A5 选看。

---

## 面试季每周 checklist

复制到日历，每周日打勾：

```
[ ] process-tracker 更新
[ ] interview-journal 补完
[ ] 跟进 ≥2 stale threads
[ ] 1 ML drill 或 1 ⭐⭐ re-solve
[ ] 下轮面试 cram sheet 写好
[ ] 睡眠 ≥7h 面试前夜
```

---

## 能量不足时 (在职必看)

| 状态 | 做 | 不算失败 |
|---|---|---|
| 正常日 | 60 min LC **或** ML + 通勤听 pitch 复述 | — |
| 加班日 | 10 rapid-fire Qs only | 跳过 LC |
| 面试日 | 仅 cram + 睡眠 | 跳过一切新课 |
| 周末只半天 | Process Sun 块优先 | ML Sat 可推迟 |

---

## 与原 12 周计划的关系

| 原 Phase | 在职轨道 |
|---|---|
| Phase 1 (4 wk) | **Jul** — 压缩到 4 周 |
| Phase 2 (4 wk) | **Aug** — drill rotation + mocks |
| Phase 3 (4 wk) | **Sep** — 面试代替 mock week |
| Phase 4 | **Oct–Nov** — negotiation |

原 Phase 1–4 细节仍作参考; 在职以 **本节周表** 为准。

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

| Track | Period | Focus | Status |
|---|---|---|---|
| **Employed (primary)** | Jul–Nov 2026 | [周表](#employed-track--jul-2026--nov-2026-start-here) | Jul W1 |
| Phase 1 Foundations | weeks 1–4 | CS336 + transformer | reference |
| Phase 2 Drills | weeks 5–8 | ML coding rotation | reference |
| Phase 3 Mocks | weeks 9–12 | Research + behavioral | reference |
| Phase 4 Negotiation | offers | Comp + decisions | Oct–Nov |
| lc (parallel) | ongoing | ⭐⭐ checklist | Day 1 done |

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

*Employed: ~12 hrs/week. Jul–Aug 准备, Sep–Oct 面试, Oct–Nov 签约. 以 [Employed Track](#employed-track--jul-2026--nov-2026-start-here) 周表为准.*
