from langchain.tools import tool

@tool
def retrieve_context(query: str, database, collection_name , repo) -> str:
    """Retrieve data and information from the database, Args:
        query (str): The query string to search for relevant context."""
    
    # Example query vector (this should be replaced with an actual vector)
    query_vector = [query]
    
    # Search the collection for relevant context
    results = repo.search_collection(collection_name=collection_name, query_vector=query_vector, n_results=5)
    
    return results