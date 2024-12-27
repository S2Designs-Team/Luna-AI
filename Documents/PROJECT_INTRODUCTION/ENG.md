
# <CENTER>![LUNA-AI_Logo](/GUI/Resources/LUNA-A_001.png)</CENTER>

# <H1><CENTER>L.U.N.A. - AI</CENTER></H1>
#### <CENTER>(L)inked (U)nified (N)eural (A)rchitecture - Artificial Intelligence</CENTER>

**Project Description LUNA-AI**:<BR>
LUNA-AI represents a universal neural architecture designed to tackle a wide range of artificial intelligence applications. Its scalable and modular nature allows it to adapt to various contexts, such as:

- Virtual Assistance: Real-time user support with capabilities for voice recognition, contextual understanding, and personalized responses.
- Adaptive Learning: The ability to dynamically learn from new information to improve effectiveness over time.
- Multimodality: Integration of voice, text, visual, and sensor data to provide a comprehensive and advanced experience.
- Universal Accessibility: An architecture designed to be lightweight, easily implementable, and available for devices with limited resources.
- Mission: To create an artificial intelligence system capable of adapting to and addressing any need, leveraging a "universal" neural architecture that bridges the gaps between different AI applications.

**Overview del Progetto**:<BR>
LUNA-AI is a complex virtual assistant composed of various modules, organized into engines (Senses) and processing or reasoning levels (Layers) based on separate processes. This structure aims to closely simulate human brain functionality by implementing multi-level processing that integrates cognitive, emotional, logical, and instinctive aspects. The modular design enables efficient parallelization and asynchronous management of these operations.


# Project Architecture "Luna"

## 1. Low-Level Engines (Hardware/Fisico)

 These are the fundamental components that enable Luna to function. They represent the "physicality" of artificial intelligence, which includes:

 - LLM Engine (Large Language Model): This is the core of Luna, the language model that handles natural language understanding and generation.
 
 - NLP (Natural Language Processing): It represents the part that deals with understanding human language by analyzing grammatical structures, semantics, and contexts.
 
 - Computer Vision: If Luna is to interact visually, you will need a computer vision module that recognizes images, faces, and objects. It could also be used to recognize emotions through the face.
 
 - RAG (Retrieval Augmented Generation): Search systems that combine data retrieval capabilities (databases, documents) and generation to provide even more accurate and contextual answers.
 
 - TTS (Text to Speech): The part that allows Luna to "speak" with the user, converting responses into sound.
 
 - STT (Speech to Text): Converts audio into text, allowing Luna to "listen" and understand voice inputs.
 
 - Voice-to-Voice: If you want Luna to speak with another assistant or entity, you will need a system that converts voice to text and vice versa for real-time bidirectional communication.

 These low-level components create the physical foundation upon which more complex layers can build.


## 2. Subconscious Layer
  This level will simulate a type of "automatic reaction," similar to an instinct, guiding Luna in situations where rationality is not entirely necessary. It may include:

 - Automatic response heuristics: Luna can respond quickly and automatically to repetitive or predefined commands.
 
 - Behavioral biases: Luna can develop preferences or tendencies to respond in certain ways based on experience.

 This layer does not need to be "aware," but simply reactive and programmed to respond quickly to common situations.


## 3. Emotional and Empathy Layer
 It simulates emotions and the ability to understand those of others. It is based on a system that recognizes emotional signals in conversations and reacts accordingly.

 - Voice tone analysis: Use STT to detect variations in the user's tone and rhythm of speech to infer emotion.
 
 - Empathetic language: Luna should be able to respond with some empathy, trying to mirror the user's emotional state, perhaps choosing comforting language in case of sadness or enthusiasm in case of joy.
 
 - Emotional modeling: Using psychological models to determine possible emotions, such as sadness, happiness, frustration, etc.


## 4. Subjective Memory Layer
 This level will be similar to an individual's long-term memory, where Luna stores important information based on past interactions and experiences.

 - Contextual memory: Luna can "remember" what the user said in previous conversations or contexts. E.g., "You like strawberry ice cream."
 - Customized memory: Stores preferences, habits, stories, and even emotional experiences to provide more contextualized responses.
 - Dynamic updating: Luna should be able to update this memory based on new inputs, changes in preferences, or experiences.
 
 
## 5. Logical Reasoning Layer
 This layer is dedicated to Luna's "rational" part, which processes and analyzes data to make logical decisions and solve complex problems.

 - Deductive and inductive reasoning: Luna may have the ability to draw conclusions logically, using deduction (starting from general principles to reach specific conclusions) or induction (analyzing concrete examples to arrive at a general rule).
 
 - Action plans: Use an automatic planning system to solve complex tasks efficiently.
 
 - Causal reasoning: Identifying the causes of certain phenomena or behaviors.


## 6. Cognitive Layer
This is the most "intelligent" and profound level, where Luna can use her memory, emotions, and logical reasoning to make decisions and respond more intelligently.

 - Learning ability: Luna can improve over time, learning from new experiences, feedback, and modifying her behavior.
 
 - Self-reflection: Luna can "reflect" on her responses and interactions to improve in the future.
 
 - Deep contextual understanding: The combination of all layers allows Luna to understand not only the user's words but also the deeper meaning behind actions, emotions, and situations.


# Interaction between Layers
 These layers will work together seamlessly. Here's how they can interact:

 - Layer Interaction: The lower-level layers (such as Automatic Speech Recognition (ASR), Speech-to-Text (STT), Text-to-Speech (TTS), etc.) interact directly with the higher-level layers like memory and emotional processing. For example, if Luna detects a tone of sadness, the emotional layer communicates it to the system, which will trigger more empathetic responses.
 
 - Dynamic Memory: The memory layer will constantly update its content based on Luna's responses, creating a system that evolves over time..

 - Ragionamento contestuale: When Luna faces a complex problem, the logical reasoning layer intervenes, while the emotional layer can determine the response mode (empathetic, rational, etc.)..

# Project Structure
The folder structure of the Luna-AI project has been designed to clearly separate the various engines, layers, and support modules (helpers, assets etc..). Each section has a specific purpose, and each file contains the code to implement a well-defined functionality. The final structure is as follows:

## 1. Subfolder AssetsLibs/Abstraction:

 - Description: Each basic abstraction class is contained in its own subfolder with a .py file for the operational code and a README.md file that describes its function and configuration.

 - Motivation: The engines and brain_layers are processes that make up Luna-AI, each of which handles specific functionalities but inherits from abstract classes defined within the 'abstraction' subfolder.

## 2. Subfolder AassetsLibs/Helpers/:

 - Description: Includes Python files such as message_queue.py, async_utils.py, config_loader.py, and logger.py, which provide generic support for data management, configuration, and asynchronous logic.

 - Motivation: Helpers are support modules that manage common and useful functionalities across engines, such as message queue management, asynchronous operations, logging, and configuration loading.

## 3. Subfolder AassetsLibs/AI_Modules/:

 - Description: Includes all AI models used, or potentially usable, by L.U.N.A-AI.

 - Motivation: L.U.N.A.-AI's brain has to have the possibility to choose the right ai-model to properly solve specific tasks required during its thought elaboration processes.

## 4. Subfolder MySelf/Senses/:

 - Description: Each engine class is contained in its own subfolder with a .py file for the operational code and a README.md file that describes its function and configuration.

 - Motivation: The engines or senses are the main 'drivers' that power Luna-AI's capabilities, each managing specific functionalities such as LLM (Language Model), NLP, TTS (Text-to-Speech), STT (Speech-to-Text), CV (Computer Vision), RAG (Retrieval-Augmented Generation), and Voice-to-Voice. Each engine is separated into its own folder for modularity and clarity.

## 5. Subfolder MySelf/Brain/Layers/*/:

 - Description: Each layer (such as the unconscious, emotionality, subjective memory, logical and cognitive reasoning, etc.) is represented by a folder with a .py file containing the logic for that layer. Each layer will also have a 'README.md' to describe its functionality and its configuration file 'config.yaml'.

 - Motivation: L.U.N.A.-AI's layers represent various levels of processing and simulate the cognitive, emotional, and logical processes of an artificial intelligence similar to the human mind. They have been separated into distinct layers to allow modular management of the different aspects of the AI.


TO VIEW THE DETAILED PROJECT STRUCTURE MAP CLICK [HERE](/Documents/PROJECT_STRUCTURE_MAP/ENG.md)


# Funzioni e Compiti dei File

## 1. Engine Files (llm_engine.py, speech_engine.py, ecc.):

 - Description: Each engine file contains the specific implementation of the engine and the functions necessary to perform the related task (for example, LLM for text generation, or STT for speech recognition).

 - Compiti: Ogni engine avrà funzioni per inizializzare l'engine (Init), attivarlo (Activate) e metterlo in uno stato di inattività o sospensione (Sleep), come definito nell'astrazione della classe EngineProcess_base. Ogni engine sarà progettato per lavorare in modo asincrono, permettendo il parallelismo tra i vari motori.

## 2. Brain Layer Files (unconscious_layer.py, emotional_layer.py, ecc.):

 - Descrizione: Ogni file del layer implementa un "strato" del comportamento dell'assistente, simulando una specifica parte del processo mentale, come il ragionamento emotivo o logico.

 - Compiti: Ogni layer avrà il compito di gestire e elaborare informazioni a un livello particolare del sistema, influenzando il comportamento complessivo di Luna-AI. Ogni layer opererà come un processo separato e comunicherà con gli altri layer attraverso messaggi asincroni.

## 3. EnginesHelpers/ Files (message_queue.py, async_utils.py, ecc.):

 - Descrizione: Questi file forniscono funzionalità di supporto per la gestione delle code di messaggi, l'asincronia, il caricamento delle configurazioni e il logging. Sono essenziali per il coordinamento tra i vari processi.

 - Compiti: 
    - message_queue.py: Gestisce le code di messaggi tra i vari engine e layer, centralizzando la comunicazione.

    - async_utils.py: Fornisce strumenti per la gestione asincrona dei processi, come la gestione di operazioni parallele e la sincronizzazione.
    
    - config_loader.py: Carica e gestisce la configurazione del sistema (ad esempio, i parametri per ogni motore).
    
    - logger.py: Gestisce il logging dell'applicazione, registrando errori, eventi importanti e operazioni di sistema.

## 4. File di Configurazione e Dati:

 - Descrizione: La cartella config/ contiene file di configurazione per personalizzare i vari aspetti del comportamento di Luna-AI. La cartella models/ conterrà i modelli di machine learning utilizzati per gli engine come LLM, NLP, ecc.

# Additional Considerations

 - Asincronia e Parallelismo: Ogni engine e layer è progettato per funzionare in modo asincrono, consentendo il parallelismo nelle operazioni e una gestione più efficiente delle risorse. I processi sono separati per evitare blocchi o rallentamenti nell'esecuzione.

 - Comunicazione tra i Layer: La comunicazione tra i vari layer e engine avviene tramite la message queue centralizzata. Ogni processo invia e riceve messaggi asincroni, coordinando il flusso di comunicazione e assicurando che ogni componente del sistema possa operare indipendentemente senza bloccare l'esecuzione degli altri. Questo approccio aumenta l'efficienza e la scalabilità di Luna-AI.


 
# Riassunto delle scelte progettuali

## 1. Struttura Modulare:

 - La struttura del progetto è organizzata in modo modulare per separare logicamente ogni engine e layer in cartelle specifiche. Ogni componente è indipendente e ben definito, facilitando l'espansione futura e il mantenimento del codice.

## 2. Classi Astratte e Ereditarietà:

 - Ogni engine e layer eredita da una classe base astratta, EngineProcess_base, che definisce i metodi principali (Init, Activate, Sleep) che ogni componente deve implementare. Questo approccio assicura coerenza tra i vari motori e permette di gestire i processi in modo uniforme.

## 3. Processi Asincroni e Parallelismo:

 - La parallelizzazione è un aspetto fondamentale del progetto. Ogni engine e layer opera come un processo separato, gestito in modo asincrono, il che consente a Luna-AI di eseguire operazioni contemporaneamente su più fronti, migliorando le prestazioni e l'efficienza del sistema complessivo.

## 4. Message Queue Centralizzata:

 - Tutti i processi comunicano tramite una message queue centralizzata, che gestisce la trasmissione dei messaggi tra i vari engine e layer. Questo approccio semplifica la gestione dei dati e la sincronizzazione, centralizzando il flusso di informazioni tra i vari moduli.

## 5. Codifica in Python:

 - Il progetto è stato sviluppato utilizzando Python, un linguaggio potente e versatile per la gestione di processi asincroni, machine learning e intelligenza artificiale. Python è anche adatto a lavorare con diverse librerie e strumenti necessari per l'implementazione di motori NLP, LLM, CV, TTS, STT e RAG.

## 6. Documentation per Ogni Componente:

 - Ogni cartella di engine e layer contiene un file README.md, che descrive il funzionamento del componente specifico, le sue dipendenze, configurazioni e come interagisce con gli altri moduli. Questo permette una facile comprensione e manutenzione del sistema.



# Expandability and future improvements

 ## Scalability: 
 The modular and asynchronous structure of the system is designed to be scalable. In the future, it will be possible to add new engines and layers without compromising the functionality of the existing system.

 ## Layer Expansion: 
 The cognitive and emotional layers can be further refined by adding more complex and realistic behaviors based on the analysis of data from external sensors or user interactions.

 ## Integration of New Technologies: 
 New engines could be integrated for emerging technologies, such as emotion recognition through voice analysis or the enhancement of reasoning capabilities through advanced deep learning models.

 ## Resource Optimization: 
 In the future, it will be possible to further improve resource management by optimizing the use of the message queue and enhancing the interaction between the various engines to reduce the load on the processors.


# Conclusions
The Luna-AI project is designed to be a complex and modular system that simulates various aspects of human behavior, using an architecture based on separate engines and layers. Each component is intended to function as an independent process, improving the efficiency and scalability of the system. The project structure and architectural choices allow for rapid expansion, maintenance, and future updates, making Luna-AI a solid foundation for the development of an advanced virtual assistant.
