"""Builtin table storage implementation types."""

from enum import StrEnum


class TableType(StrEnum):
    """Enum for table storage types."""

    Parquet = "parquet"
    CSV = "csv"
