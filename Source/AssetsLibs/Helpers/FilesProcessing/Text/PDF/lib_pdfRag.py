# Copyright 2022 S2DesignsTeam (㊙️anonimo㊙️).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## 1. Ingest PDF Files
#  2. Extract Text from PDF Files and split into small chunks
#  3. Send the chunks to the embedding model
#  4. Save the embeddings to a vector database
#  5. Perform a similarity search on the vector database to find similar documents
#  6. Retrieve the similar documents and present them to the user
## run pip install -r requirements.txt to install the required packages

import ollama
ollama.pull("nomic-embbed-text")

from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.embeddings       import OllamaEmbedding
from langchain_text_splitters             import RecursiveCharacterTextSplitter

#  4. Save the embeddings to a vector database
from langchain_community.vectorstores     import Chroma

#  5. Perform a similarity search on the vector database to find similar documents
#  6. Retrieve the similar documents and present them to the user
from langchain.prompts                    import ChatPromptTemplate, PromptTemplate
from langchain.retrievers.multi_query     import MultiQueryRetriever
from langchain_core.output_parsers        import StrOutputParser
from langchain_core.runnables             import RunnablePassthrough
from langchain_ollama                     import ChatOllama

class PDF_RAG():
    _LLM:ChatOllama            = None
    _doc_path:str              = None
    _llm_model                 = None
    _current_document_path:str = None
    _current_document_chunks   = None 
    _chunk_size:int            = 1200
    _chunk_overlap:int         = 300
    _vector_db:Chroma          = None
    _embedding_model_name:str  = None

    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self, par_vector_DB:Chroma=None):
        self._doc_path                = "./data/"
        self._llm_model               = "llama3.2"
        self._embedding_model_name    = "nomics-embbed-text"
        self._current_document_chunks = []
        self._vector_db               = par_vector_DB
        # Setup our model to use
        self._LLM                     = ChatOllama(self._llm_model)
        pass

    def ingestDocument(self, par_doc_path:str = None):
        """
        """
        if par_doc_path == None:
            print("No document path provided.")
            return
        
        if self.par_doc_path:
            loader = UnstructuredPDFLoader(file_path = self.par_doc_path)
            data = loader.load()
            print("Done loading.....")
        else:
            print("Upload a PDF File")

        content = data[0].page_content
        print(content[:100])
        pass

    def extractTextFromDocument(self):
        """
        Extract text from PDF files and Split into small chunks.
        """
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1200, chunk_overlap=300)
        self._current_document_chunks = text_splitter.split_documents(data)
        print("Data Split Done.")
        print(f"Number of chunks: {len(self._current_document_chunks)}")
        print(f"Example chunk: {self._current_document_chunks[0]}")
        pass

    def addToVectorDB(self, par_vector_DB:Chroma= None):  
        """
        Add to vector database
        """
        ollama.pull(self._embedding_model_name)
        par_vector_DB = Chroma.from_documents(
            documents=self._current_document_chunks,
            embedding= OllamaEmbedding(model= self._embedding_model_name),
            collection_name="shortTermMemoryRag",
        )
        print("Adding to the vector database... Done")
        pass

    def retrieveSimilarDocuments(self, par_vector_DB:Chroma= None):
        """
        Perform a similarity search on the vector database to find similar documents
        """
        # A simple technique to generate multiple questions from a singlr prompt
        # baserd on those questions, getting the best of both worlds.
        QUERY_PROMPT = PromptTemplate(
            input_variables = ["question"],
            template        = """
                              You are an AI language model assistant. Your task is to
                              generate five different questions of the given user question
                              to retrieve relevant documents from a vector database. 
                              By generating nultiple perspectives on the user question, your
                              goal is to help the user to overcome some of the limitations of
                              the distance-based similarity search. Provide these alternative 
                              questions separated by newlines.
                              Original question: {question}
                              """,
        )
        retriever = MultiQueryRetriever.from_llm(
            par_vector_DB.as_retriever(),
            self._LLM,
            prompt=QUERY_PROMPT,
        )

        similar_documents = par_vector_DB.search("shortTermMemoryRag", self._current_document_chunks[0], top_k=5)
        print("Retrieving similar documents... Done")
        print(f"Similar documents: {similar_documents}")
        pass

