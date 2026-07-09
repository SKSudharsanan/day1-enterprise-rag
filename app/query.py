# app/query.py (first version)
from llama_index.core.postprocessor import MetadataReplacementPostProcessor

def build_query_engine(index):
    return index.as_query_engine(
        similarity_top_k=settings.retrieve_k,
        node_postprocessors=[
            MetadataReplacementPostProcessor(target_metadata_key="window"),
        ],
    )