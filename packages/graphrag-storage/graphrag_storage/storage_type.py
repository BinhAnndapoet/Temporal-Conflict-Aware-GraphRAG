"""Builtin storage implementation types."""

from enum import StrEnum


class StorageType(StrEnum):
    """Enum for storage types."""

    File = "file"
    Memory = "memory"
    AzureBlob = "blob"
    AzureCosmos = "cosmosdb"
