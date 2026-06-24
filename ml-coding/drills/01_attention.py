"""
Drill 01 — Scaled Dot-Product Attention
Target: 20 min from blank, no AI.

Run: python3 ml-coding/drills/01_attention.py
"""
from __future__ import annotations

import torch
import torch.nn.functional as F


def scaled_dot_product_attention(
    q: torch.Tensor,  # (B, T, Dh)
    k: torch.Tensor,  # (B, T, Dh)
    v: torch.Tensor,  # (B, T, Dh)
    mask: torch.Tensor | None = None,  # (B, T, T) or broadcastable; 1=keep, 0=mask
) -> torch.Tensor:
    """Return (B, T, Dh)."""
    raise NotImplementedError


def _test() -> None:
    B, T, Dh = 2, 4, 8
    q = torch.randn(B, T, Dh)
    k = torch.randn(B, T, Dh)
    v = torch.randn(B, T, Dh)
    causal = torch.tril(torch.ones(T, T)).unsqueeze(0).expand(B, -1, -1)
    out = scaled_dot_product_attention(q, k, v, mask=causal)
    assert out.shape == (B, T, Dh), out.shape
    print("ok", out.shape)


if __name__ == "__main__":
    _test()
