# app/ingestion.py
from llama_index.core.node_parser import TokenTextSplitter, SentenceWindowNodeParser
from app.config import settings

def get_parser():
    if settings.chunk_strategy == "sentence_window":
        return SentenceWindowNodeParser.from_defaults(
            window_size=3, window_metadata_key="window",
            original_text_metadata_key="original_text")
    return TokenTextSplitter(chunk_size=512, chunk_overlap=50)   # the article's 'first crack'