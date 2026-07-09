from app.stores import build_qdrant_index
from app.query import build_query_engine
import sys

engine = build_query_engine(build_qdrant_index())
print(engine.query(sys.argv[1]))