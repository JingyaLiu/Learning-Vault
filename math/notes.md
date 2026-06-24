# Math Interview Prep

Some companies (especially theory-leaning or quant-adjacent ML teams) run a math round. Range: logic puzzles → pen-and-paper derivations.

**Cadence:** 2× per week, 30 min, alongside Phase 2.

---

## Probability (highest yield)

- [ ] Bayes' rule — plug-and-chug + intuition
- [ ] Expectation linearity, law of total expectation
- [ ] Common distributions: Bernoulli, Binomial, Poisson, Gaussian
- [ ] MLE intuition for Gaussian mean
- [ ] Markov chains — stationary distribution (simple 2-state)
- [ ] Birthday problem / collision probability sketch

**Classic puzzle types:** dice, coins, cards, expected waiting time.

---

## Linear Algebra

- [ ] Rank, null space, projection — geometric picture
- [ ] Eigendecomposition — why PCA works
- [ ] SVD — relate to low-rank approximation
- [ ] Positive semi-definite matrices — where they appear (kernels, covariances)
- [ ] Derivative of xᵀAx w.r.t. x

---

## Calculus / Optimization

- [ ] Chain rule through softmax + cross-entropy (derive once, remember structure)
- [ ] Gradient of log-likelihood
- [ ] Convex vs non-convex — what SGD still works for
- [ ] Lagrange multipliers — 1 simple constrained problem

---

## ML-Connected Derivations (do on paper)

1. **Softmax + cross-entropy gradient** — should reduce to (p − y)
2. **Linear regression closed form** — normal equations
3. **Gaussian log-likelihood → MSE** under i.i.d. noise

---

## Logic / Brain Teasers

Lower priority unless recruiter warns you. If so: practice 5–10 from past interview reports for that company.

---

## Session Template (30 min)

| Min | Activity |
|---|---|
| 0–10 | One derivation from scratch (no notes) |
| 10–20 | 3 probability problems |
| 20–30 | Review mistakes; add to formula sheet below |

---

## Formula Sheet (build your own one-pager)

Keep a single page you re-read the night before math interviews:

```
[Paste derivations and formulas you keep forgetting]
```

Reference: [Alisa math notes PDF](https://alisawuffles.github.io/assets/files/math_notes.pdf)
