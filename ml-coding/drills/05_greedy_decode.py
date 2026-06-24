"""
Drill 05 — Greedy decoding loop
Target: 20 min from blank, no AI.

Run: python3 ml-coding/drills/05_greedy_decode.py
"""
from __future__ import annotations

import torch


def greedy_decode(
  model: torch.nn.Module,
  input_ids: torch.Tensor,  # (B, T0) prompt
  max_new_tokens: int,
) -> torch.Tensor:
  """Return full sequence (B, T0 + max_new_tokens) via greedy argmax."""
  raise NotImplementedError


class _ToyLM(torch.nn.Module):
  def __init__(self, vocab_size: int = 8, d_model: int = 16) -> None:
    super().__init__()
    self.embed = torch.nn.Embedding(vocab_size, d_model)
    self.head = torch.nn.Linear(d_model, vocab_size)

  def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
    return self.head(self.embed(input_ids))


def _test() -> None:
  model = _ToyLM()
  prompt = torch.tensor([[1, 2, 3]])
  out = greedy_decode(model, prompt, max_new_tokens=4)
  assert out.shape == (1, 7), out.shape
  print("ok", out.shape)


if __name__ == "__main__":
  _test()
