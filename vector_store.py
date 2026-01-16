import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)
product_ids = []

def add_vector(vector, product_id):
    index.add(np.array([vector]).astype("float32"))
    product_ids.append(product_id)


def search_vector(vector, top_k=5):
    if index.ntotal == 0:
        return []

    vector = np.array([vector]).astype("float32")
    D, I = index.search(vector, top_k)

    valid_ids = []
    for idx in I[0]:
        if idx < len(product_ids):
            valid_ids.append(product_ids[idx])

    return valid_ids
