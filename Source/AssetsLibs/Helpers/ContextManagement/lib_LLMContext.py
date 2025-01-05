from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

class LLMContext:
    """
    Classe per la gestione del contesto tramite un Large Language Model (LLM).
    Genera embedding contestuali e coordina le operazioni legate al contesto.
    """
    def __init__(self, model_name="bert-base-uncased", embedding_dim=768):
        """
        Inizializza il gestore del contesto basato su LLM.

        :param model_name: Nome del modello pre-addestrato da utilizzare.
        :param embedding_dim: Dimensione degli embedding generati.
        """
        self.model_name = model_name
        self.embedding_dim = embedding_dim

        # Carica il tokenizer e il modello
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModel.from_pretrained(self.model_name)

        # Metti il modello in modalità valutazione
        self.model.eval()
        print(f"Modello LLM '{self.model_name}' caricato.")

    def generate_context_embedding(self, text):
        """
        Genera un embedding contestuale per un testo dato.

        :param text: Testo da analizzare.
        :return: Embedding contestuale come array NumPy.
        """
        with torch.no_grad():
            # Tokenizza il testo
            tokens = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
            output = self.model(**tokens)
            
            # Usa l'output del [CLS] token per l'embedding contestuale
            embedding = output.last_hidden_state[:, 0, :].squeeze().numpy()
            return embedding

    def evaluate_context_similarity(self, embedding1, embedding2):
        """
        Valuta la similarità tra due embedding contestuali.

        :param embedding1: Primo embedding (array NumPy).
        :param embedding2: Secondo embedding (array NumPy).
        :return: Similarità (valore scalare).
        """
        embedding1 = torch.tensor(embedding1)
        embedding2 = torch.tensor(embedding2)

        # Calcola la similarità coseno tra gli embedding
        similarity = torch.nn.functional.cosine_similarity(embedding1, embedding2, dim=0)
        return similarity.item()

    def suggest_updates(self, context_embedding, database_handler, threshold=0.85):
        """
        Suggerisce aggiornamenti basati sulla similarità contestuale.

        :param context_embedding: Embedding contestuale generato.
        :param database_handler: Istanza della classe MilvusHandler per interagire con il database.
        :param threshold: Soglia di similarità per aggiornamenti.
        :return: Lista di record da aggiornare.
        """
        results = database_handler.query_embedding(context_embedding, top_k=10)
        updates = []

        for result in results:
            similarity = self.evaluate_context_similarity(
                context_embedding, result.entity.get("embedding")
            )
            if similarity < threshold:
                updates.append(result.id)

        print(f"{len(updates)} record identificati per aggiornamenti.")
        return updates

    def update_context(self, new_context, database_handler, record_id=None):
        """
        Aggiorna il contesto nel database vettoriale.

        :param new_context: Nuovo contesto sotto forma di testo o embedding.
        :param database_handler: Istanza della classe MilvusHandler per interagire con il database.
        :param record_id: ID del record da aggiornare, se specificato.
        """
        # Genera un embedding per il nuovo contesto se è un testo
        if isinstance(new_context, str):
            new_embedding = self.generate_context_embedding(new_context)
        else:
            new_embedding = new_context

        if record_id:
            database_handler.update_embedding(record_id, new_embedding)
            print(f"Contesto aggiornato per il record con ID {record_id}.")
        else:
            database_handler.insert_embedding([new_embedding])
            print("Nuovo contesto inserito nel database.")