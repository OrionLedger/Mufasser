from configs.chroma import ChromaModule

class ChromaRepo:
    def __init__(self, 
                database: str, 
                module: ChromaModule = ChromaModule()
                ):
        
        self._module = module
        self._database = database
        self._db_instance = None
        self._client = self.get_module_client()

    def get_db_instance(self):
        if self._db_instance is None:
            raise ValueError("Database instance not connected. Please call connect() first.")
        
        return self._db_instance
    
    def get_module_client(self):
        return self._module.get_client()
    
    def add_collection(self, collection_name: str):
        return self._client.create_collection(name=collection_name)
    
    def get_collection(self, collection_name: str):
        return self._client.get_collection(name=collection_name)

    def search_collection(self, collection_name: str, query_vector, n_results: int = 5):
        collection = self.get_collection(collection_name)
        results = collection.query(query_embeddings=[query_vector], n_results=n_results)
        return results
    
    def insert_into_collection(self, collection_name: str, embeddings, metadatas=None, ids=None):
        collection = self.get_collection(collection_name)
        collection.add(
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )