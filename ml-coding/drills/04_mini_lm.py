"""
Drill 04 — Mini language model forward + loss
Target: 45 min. Tiny vocab/dim is fine.

Run: python3 ml-coding/drills/04_mini_lm.py
"""
from __future__ import annotations

import torch
import torch.nn as nn


class MiniLM(nn.Module):
    """Decoder-only: embed → N blocks → lm_head."""

    def __init__(
        self,
        vocab_size: int,
        d_model: int,
        num_heads: int,
        num_layers: int,
        max_seq_len: int,
    ) -> None:
        super().__init__()
        raise NotImplementedError

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        """Return logits (B, T, V)."""
        raise NotImplementedError


def lm_loss(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    """Causal LM cross-entropy with correct shift."""
    raise NotImplementedError


def _test() -> None:
    B, T, V = 2, 8, 100
    model = MiniLM(vocab_size=V, d_model=64, num_heads=4, num_layers=2, max_seq_len=32)
    ids = torch.randint(0, V, (B, T))
    logits = model(ids)
    assert logits.shape == (B, T, V)
    loss = lm_loss(logits, ids)
    assert loss.ndim == 0
    print("ok", float(loss))


if __name__ == "__main__":
    _test()
