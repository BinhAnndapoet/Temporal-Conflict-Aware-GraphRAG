"""LLMEmbedding module for graphrag_llm."""

from graphrag_llm.embedding.embedding import LLMEmbedding
from graphrag_llm.embedding.embedding_factory import (
    create_embedding,
    register_embedding,
)

__all__ = [
    "LLMEmbedding",
    "create_embedding",
    "register_embedding",
]
