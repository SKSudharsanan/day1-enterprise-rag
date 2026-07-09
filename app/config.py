# app/config.py
from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    vector_backend: str = "qdrant"            # "qdrant" | "pgvector"
    anthropic_api_key: str = ""
    embed_model: str = "BAAI/bge-small-en-v1.5"
    embed_dim: int = 384
    llm_model: str = "claude-haiku-4-5-20251001"
    chunk_strategy: str = "fixed"             # "fixed" | "sentence_window"
    retrieve_k: int = 20
    rerank_top_n: int = 5
    alpha: float = 0.5
    refusal_score: float = 0.2
    class Config: env_file = ".env"

settings = AppSettings()