# Implemented Features

## Contextual Embedding Generation:

- Uses an LLM (e.g., BERT) to transform text into contextual embeddings.
- Leverages the [CLS] token vector to represent the context.

## Contextual Similarity Evaluation:

- Computes cosine similarity between two embeddings.

## Update Suggestions:

- Queries the database (via MilvusHandler) and compares the similarity between the current context and existing embeddings.
- Suggests which records to update based on a similarity threshold.

## Context Update:

- Updates or inserts new embeddings into the vector database.
- Allows both the insertion of new data and the modification of existing data.