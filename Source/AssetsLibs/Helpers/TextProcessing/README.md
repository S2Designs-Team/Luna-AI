# Implemented Features

## Text Tokenization:

Converts text into tokens using a Hugging Face tokenizer.  
Supports padding, truncation, and a defined maximum length.

## Token Decoding:

Converts a list of token IDs into readable text.

## Vocabulary Information:

Returns the vocabulary size and special tokens of the model.

## LLM Compatibility:

Prepares the data in a format compatible with Transformer models, facilitating integration with other classes such as LLMContext.

## Usage example:
```python
from AssetsLibs.TextProcessing.lib_Tokenizer import Tokenizer

# Inizializza il tokenizer
tokenizer = Tokenizer(model_name="bert-base-uncased")

# Testo da tokenizzare
text = "Hello, how are you today?"

# Tokenizza il testo
tokens = tokenizer.tokenize(text)

# Decodifica i token in testo
decoded_text = tokenizer.decode(tokens['input_ids'][0])

# Ottieni dimensione del vocabolario
vocab_size = tokenizer.get_vocab_size()

# Ottieni token speciali
special_tokens = tokenizer.get_special_tokens()

```