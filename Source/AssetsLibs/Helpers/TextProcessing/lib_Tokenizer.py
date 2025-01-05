from transformers import AutoTokenizer

class Tokenizer:
    """
    Classe per la tokenizzazione del testo e il preprocessing.
    Utilizza un modello pre-addestrato di Hugging Face.
    """
    def __init__(self, model_name="bert-base-uncased"):
        """
        Inizializza il Tokenizer.

        :param model_name: Nome del modello pre-addestrato da utilizzare.
        """
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        print(f"Tokenizer basato su '{self.model_name}' caricato.")

    def tokenize(self, text, padding=True, truncation=True, max_length=512):
        """
        Tokenizza il testo in input.

        :param text: Testo da tokenizzare.
        :param padding: Applica il padding alle sequenze (default: True).
        :param truncation: Tronca il testo che supera il max_length (default: True).
        :param max_length: Lunghezza massima delle sequenze (default: 512).
        :return: Dizionario contenente i token e i relativi ID.
        """
        tokens = self.tokenizer(
            text,
            padding=padding,
            truncation=truncation,
            max_length=max_length,
            return_tensors="pt"
        )
        print(f"Testo tokenizzato: {text}")
        return tokens

    def decode(self, token_ids):
        """
        Decodifica una lista di ID di token in una stringa di testo.

        :param token_ids: Lista di ID di token.
        :return: Testo decodificato.
        """
        text = self.tokenizer.decode(token_ids, skip_special_tokens=True)
        print(f"Token decodificati in: {text}")
        return text

    def get_vocab_size(self):
        """
        Restituisce la dimensione del vocabolario del tokenizer.

        :return: Dimensione del vocabolario.
        """
        vocab_size = len(self.tokenizer)
        print(f"Dimensione del vocabolario: {vocab_size}")
        return vocab_size

    def get_special_tokens(self):
        """
        Restituisce i token speciali del tokenizer (es. [CLS], [SEP], [PAD]).

        :return: Dizionario dei token speciali.
        """
        special_tokens = self.tokenizer.special_tokens_map
        print(f"Token speciali: {special_tokens}")
        return special_tokens
