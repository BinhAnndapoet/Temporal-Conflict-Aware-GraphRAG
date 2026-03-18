"""Builtin cache implementation types."""

from enum import StrEnum


class CacheType(StrEnum):
    """Enum for cache types."""

    Json = "json"
    Memory = "memory"
    Noop = "none"
