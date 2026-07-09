from llama_index.core import SimpleDirectoryReader

from app.ingestion import get_parser
from app.stores import build_qdrant_index


docs = SimpleDirectoryReader("data", required_exts=[".pdf"]).load_data()
nodes = get_parser().get_nodes_from_documents(docs)   # your Commit 3 sentence-window parser
build_qdrant_index(nodes)
print(f"Ingested {len(docs)} docs → {len(nodes)} nodes")