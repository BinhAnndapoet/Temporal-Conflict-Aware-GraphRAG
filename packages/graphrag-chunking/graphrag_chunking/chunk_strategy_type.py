"""Chunk strategy type enumeration."""

from enum import StrEnum


class ChunkerType(StrEnum):
    """ChunkerType class definition."""

    Tokens = "tokens"
    Sentence = "sentence"
