from chromadb import chromadb
from chromadb.config import Settings
import os

tenant = os.environ.get("TENANT", "default_tenant")

class ChromaModule:
    def __init__(self, tenant = tenant):
        self._tenant = tenant
        self._client = None

    def connect_in_memory(self, database):
        if self._tenant is None:
            raise ValueError("TENANT environment variable must be set or explicitly provided")
        self._client = chromadb.Client(tenant=self._tenant)
        return self._client.get_database(database)
    
    
    def connect_http_client(self, database, host, port, ssl=False, settings=Settings()):
        if self._tenant is None:
            raise ValueError("TENANT environment variable must be set or explicitly provided")
        self._client = chromadb.HttpClient(
            host=host,
            port=port,
            ssl=ssl,
            settings=settings,
            tenant=self._tenant, 
            database=database,
        )
        return self._client.get_database(database)

    def connect_persistent(self, database, persist_directory, settings=Settings()):
        if self._tenant is None:
            raise ValueError("TENANT environment variable must be set or explicitly provided")
        self._client = chromadb.PersistentClient(
            path=persist_directory,
            settings=settings,
            tenant=self._tenant,
            database=database,
        )
        return self._client.get_database(database)

    def get_client(self):
        if self._client is None:
            raise ValueError("Client not connected. Please call connect() first.")
        
        return self._client
    