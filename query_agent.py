def rewrite_query(query):
    if "cheap" in query:
        query += " affordable budget"
    if "gaming" in query:
        query += " high performance graphics"
    if "laptop" in query:
        query += " notebook computer"
    return query
