from __future__ import annotations
from tinyhnsw.index import Index

import numpy


class HNSWIndex(Index):
    def __init__(self, d: int) -> None:
        super().__init__(d)

    def add(self, vectors: numpy.ndarray) -> None:
        return

    def search(
        self, query: numpy.ndarray, k: int
    ) -> tuple[numpy.ndarray, numpy.ndarray]:
        return ()
