from langchain_ollama                     import ChatOllama

class LUNA_LLM():
    _LLM_INSTANCE:ChatOllama = None

    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        self._LLM_INSTANCE  = ChatOllama("llama3.2")