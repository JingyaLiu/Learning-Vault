"""
Drill 03 — Transformer Block (pre-norm decoder block)
Target: 35 min from blank, no AI.

Run: python3 ml-coding/drills/03_transformer_block.py
"""
from __future__ import annotations

import torch
import torch.nn as nn


class TransformerBlock(nn.Module):
  """Pre-norm: LN → attn → residual → LN → FFN → residual."""

  def __init__(self, d_model: int, num_heads: int, ffn_dim: int) -> None:
    super().__init__()
    raise NotImplementedError

  def forward(
    self,
    x: torch.Tensor,  # (B, T, D)
    mask: torch.Tensor | None = None,
  ) -> torch.Tensor:
    raise NotImplementedError


def _test() -> None:
  block = TransformerBlock(d_model=64, num_heads=8, ffn_dim=256)
  x = torch.randn(2, 5, 64)
  causal = torch.tril(torch.ones(5, 5)).unsqueeze(0).expand(2, -1, -1)
  out = block(x, mask=causal)
  assert out.shape == x.shape
  print("ok", out.shape)


if __name__ == "__main__":
  _test()
