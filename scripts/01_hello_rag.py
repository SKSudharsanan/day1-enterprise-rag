# scripts/01_hello_rag.py
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
Settings.llm = Anthropic(model="claude-haiku-4-5-20251001", temperature=0.1)

docs = SimpleDirectoryReader("data", required_exts=[".pdf"], recursive=True).load_data()
print(f"Loaded {len(docs)} document objects")

index = VectorStoreIndex.from_documents(docs)          # default chunking, in-memory
engine = index.as_query_engine(similarity_top_k=3)

resp = engine.query("What is the free-look period and how do I cancel within it?")
print(resp.response)
for n in resp.source_nodes:
    print(f"  {n.metadata.get('file_name')} p{n.metadata.get('page_label')} score={n.score:.3f}")