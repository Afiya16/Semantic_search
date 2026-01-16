from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from models import Product
from db import SessionLocal, ProductTable
from vector_store import add_vector, search_vector
from query_agent import rewrite_query

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

@app.get("/health")
def health():
    return {"status": "API running"}

@app.post("/product")
def add_product(product: Product):
    db = SessionLocal()
    db_product = ProductTable(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    embedding = model.encode(product.description)
    add_vector(embedding, db_product.id)

    return {"message": "Product added successfully"}

@app.get("/search")
def search(query: str):
    refined_query = rewrite_query(query)
    query_embedding = model.encode(refined_query)

    ids = search_vector(query_embedding)

    if not ids:
        return {
            "original_query": query,
            "refined_query": refined_query,
            "results": []
        }

    db = SessionLocal()
    results = db.query(ProductTable).filter(ProductTable.id.in_(ids)).all()

    return {
        "original_query": query,
        "refined_query": refined_query,
        "results": results
    }
