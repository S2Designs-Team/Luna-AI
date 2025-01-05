from pymilvus import (
    connections,
    FieldSchema, CollectionSchema, DataType,
    Collection, utility
)
import numpy as np

class MilvusHandler:
    """
    Classe per la gestione del database vettoriale Milvus.
    Consente l'inserimento, il recupero e l'aggiornamento degli embedding.
    """
    def __init__(self, collection_name, host="localhost", port="19530"):
        """
        Inizializza il gestore per Milvus.

        :param collection_name: Nome della collezione nel database.
        :param host: Indirizzo host del server Milvus.
        :param port: Porta del server Milvus.
        """
        self.collection_name = collection_name
        self.host = host
        self.port = port

        # Connessione al server Milvus
        connections.connect(alias="default", host=self.host, port=self.port)
        print(f"Connesso a Milvus su {self.host}:{self.port}")

        # Controlla se la collezione esiste; altrimenti, creala
        if not utility.has_collection(self.collection_name):
            self._create_collection()

        self.collection = Collection(self.collection_name)

    def _create_collection(self):
        """
        Crea una nuova collezione in Milvus con schema predefinito.
        """
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128),
        ]
        schema = CollectionSchema(fields, description="Collezione per pesi ed embedding")
        Collection(name=self.collection_name, schema=schema)
        print(f"Collezione '{self.collection_name}' creata.")

    def insert_embedding(self, embeddings):
        """
        Inserisce uno o più embedding nella collezione.

        :param embeddings: Lista di embedding (array NumPy) da inserire.
        :return: IDs degli embedding inseriti.
        """
        if not isinstance(embeddings, np.ndarray):
            embeddings = np.array(embeddings)

        data = [
            None,  # ID auto-generato
            embeddings.tolist()  # Converti in lista per l'inserimento
        ]
        ids = self.collection.insert(data)
        print(f"Inseriti {len(ids.primary_keys)} embedding nella collezione '{self.collection_name}'.")
        return ids.primary_keys

    def query_embedding(self, embedding, top_k=5):
        """
        Recupera i vettori più vicini a un embedding dato.

        :param embedding: Embedding da utilizzare per la ricerca (array NumPy).
        :param top_k: Numero di risultati da restituire.
        :return: Risultati della query.
        """
        if not isinstance(embedding, np.ndarray):
            embedding = np.array(embedding)

        self.collection.load()  # Assicurati che la collezione sia caricata
        results = self.collection.search(
            data=[embedding.tolist()],
            anns_field="embedding",
            param={"metric_type": "L2", "params": {"nprobe": 10}},
            limit=top_k,
        )
        print(f"Query completata. Restituiti i top {top_k} risultati.")
        return results

    def delete_by_id(self, ids):
        """
        Elimina uno o più record dalla collezione tramite ID.

        :param ids: Lista di ID dei record da eliminare.
        """
        self.collection.delete(expr=f"id in {ids}")
        print(f"Eliminati {len(ids)} record dalla collezione '{self.collection_name}'.")

    def update_embedding(self, id, new_embedding):
        """
        Aggiorna l'embedding di un record specifico.

        :param id: ID del record da aggiornare.
        :param new_embedding: Nuovo embedding (array NumPy).
        """
        self.delete_by_id([id])
        self.insert_embedding(new_embedding)
        print(f"Aggiornato l'embedding con ID {id}.")
