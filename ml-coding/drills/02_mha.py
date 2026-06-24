"""
Drill 02 — Multi-Head Attention
Target: 30 min from blank, no AI.

Run: python3 ml-coding/drills/02_mha.py
"""
from __future__ import annotations

import torch
import torch.nn as nn


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model: int, num_heads: int) -> None:
        super().__init__()
        assert d_model % num_heads == 0
        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        # TODO: define projections
        raise NotImplementedError

    def forward(
        self,
        x: torch.Tensor,  # (B, T, D)
        mask: torch.Tensor | None = None,
    ) -> torch.Tensor:
        raise NotImplementedError


def _test() -> None:
    mha = MultiHeadAttention(d_model=64, num_heads=8)
    x = torch.randn(2, 5, 64)
    out = mha(x)
    assert out.shape == x.shape
    print("ok", out.shape)


if __name__ == "__main__":
    _test()
