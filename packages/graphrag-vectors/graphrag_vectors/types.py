"""Common types for vector stores."""

from collections.abc import Callable

TextEmbedder = Callable[[str], list[float]]
