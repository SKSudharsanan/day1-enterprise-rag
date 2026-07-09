# app/stores.py
from qdrant_client import QdrantClient
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from app.config import settings

def build_qdrant_index(nodes=None):
    client = QdrantClient(url="http://localhost:6333")
    store = QdrantVectorStore(
        client=client, collection_name="policy_chunks",
        enable_hybrid=True,                       # dense + sparse in one collection
        fastembed_sparse_model="Qdrant/bm25",
    )
    ctx = StorageContext.from_defaults(vector_store=store)
    if nodes is not None:
        return VectorStoreIndex(nodes, storage_context=ctx)
    return VectorStoreIndex.from_vector_store(store)