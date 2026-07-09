# app/query.py (first version)
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from app.config import settings

def build_retriever(index):
    return index.as_retriever(
        vector_store_query_mode="hybrid",
        similarity_top_k=settings.retrieve_k,
        sparse_top_k=settings.retrieve_k,
        alpha=settings.alpha,
    )

def build_query_engine(index):
    return index.as_query_engine(
        similarity_top_k=settings.retrieve_k,
        node_postprocessors=[
            MetadataReplacementPostProcessor(target_metadata_key="window"),
        ],
    )