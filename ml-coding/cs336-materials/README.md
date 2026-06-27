# CS336 lecture materials (local copies)

Executable lecture scripts from [Stanford CS336 Spring 2026](https://cs336.stanford.edu/).

## Why does the `.py` file look weird in Cursor?

These are **not normal scripts**. Percy writes lectures as Python that calls `edtrace`:

```python
def welcome():
    text("## CS336: Language Models From Scratch")
    image("images/course-staff.png", width=600)
    text("- Same 'from scratch' philosophy")
```

| Where you open it | What you see |
|---|---|
| **Cursor / raw `.py`** | Hundreds of imports + `text()` / `link()` / `image()` — looks like broken code |
| **Course trace viewer** | Rendered **slides**: markdown, images, links — step line-by-line |

**For studying:** use the **online trace viewer** (or YouTube). Keep the local `.py` as a searchable reference (`def tokenization`, `train_bpe`, etc.).

### View exactly like the webpage

**Option A — use the course site (zero setup, identical UI)**

Open: **https://cs336.stanford.edu/lectures/?trace=lecture_01**

This *is* the rendered trace. The local `.py` in this folder is only source code, not the viewer.

**Option B — run the trace viewer on your machine**

You need the **full** [stanford-cs336/lectures](https://github.com/stanford-cs336/lectures) repo (not just `lecture_01.py` — it depends on `lecture_util`, `references`, `images/`, `execute.py`).

```bash
# 1. Clone (sibling folders)
cd ~/code   # or wherever you keep repos
git clone https://github.com/stanford-cs336/lectures.git cs336-lectures
cd cs336-lectures
git clone https://github.com/percyliang/edtrace

# 2. Python env (install uv if missing: https://docs.astral.sh/uv/)
uv sync

# 3. Compile lecture → JSON trace (downloads/caches images)
uv run python execute.py -m lecture_01
# → creates var/traces/lecture_01.json

# 4. Frontend (needs Node.js + npm)
npm run --prefix=edtrace/frontend dev
```

Then open in browser:

**http://localhost:5173/?trace=var/traces/lecture_01.json**

Use **→ / ←** to step — same interaction as the Stanford site.

**Troubleshooting**
- `ModuleNotFoundError: edtrace` → run from repo root after `uv sync`; `edtrace/` folder must exist
- Blank page → check terminal for the exact port (5173) and that `var/traces/lecture_01.json` exists
- For prep you usually **don't need Option B** — Option A is the same UI

### Lec 1 — jump to these sections (local or trace)

| Function | Topic |
|---|---|
| `tokenization()` | Main unit for today |
| `intro_to_tokenization()` | Motivation |
| `character_tokenizer()` / `byte_tokenizer()` / `word_tokenizer()` | Baselines |
| `bpe_tokenizer()` / `train_bpe()` | BPE — interview-relevant |

---

## Files

| File | Interactive viewer | Refresh |
|---|---|---|
| [lecture_01.py](lecture_01.py) | [trace](https://cs336.stanford.edu/lectures/?trace=lecture_01) | `curl -L -o lecture_01.py https://cs336.stanford.edu/lectures/lecture_01.py` |
| [lecture_02.py](lecture_02.py) | [trace](https://cs336.stanford.edu/lectures/?trace=lecture_02) | `curl -L -o lecture_02.py https://cs336.stanford.edu/lectures/lecture_02.py` |

**Run locally (optional):** clone [stanford-cs336/lectures](https://github.com/stanford-cs336/lectures) + [edtrace](https://github.com/percyliang/edtrace) — not needed for interview prep.

**PDF lectures** (Lec 3+): download from [schedule](https://cs336.stanford.edu/) — not mirrored here yet.
