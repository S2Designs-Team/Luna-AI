
# <CENTER>![alt text](GUI/Resources/LUNA-A_001.png)</CENTER>

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

 - Layer Interaction: Gli strati di basso livello (come il riconoscimento vocale (ASR), lo la trascrizione del "parlato" (STT), la conversione del testo in audio (TTS) etc...)interagiscono direttamente con gli strati superiori come la memoria e l'emotività. Ad esempio, se Luna riconosce un tono di tristezza, lo strato emotivo lo comunica al sistema, che attiverà risposte più empatiche.
 
 - Dynamic Memory: Lo strato della memoria aggiornerà costantemente il suo contenuto in base alle risposte di Luna, creando un sistema che si evolve nel tempo.

 - Ragionamento contestuale: Quando Luna affronta un problema complesso, lo strato del ragionamento logico interviene, mentre il layer emotivo può determinare la modalità di risposta (empatica, razionale, etc.).

# Project Structure
La struttura delle cartelle del progetto Luna-AI è stata progettata per separare chiaramente i vari engine, layers e i moduli di supporto (helpers). 
Ogni sezione ha uno scopo specifico e ogni file contiene il codice per implementare una funzionalità ben definita. La struttura finale è la seguente:
<PRE>
LUNA-AI/
├── startLuna-AI.py                                       # Main project file
├── requirements.txt                                      # Global dependencies
├── README.md                                             # PROJECT INTRODUCTION (questo file)
│   
├── Documentss/                                           # Project directory contenente la documentazione.
│   ├── PROJECT_SETUP.md                                  # Documentation di guida al setup del progetto.
│   └── TTS_SETUP.md
│
├── AssetsLibs/                                           # Directory del progetto contenente gli assets di basso livello nececessari.
│   │
│   ├── Abstraction/                                      # Directory del progetto contenente gli assets e le classi Astratte di Luna-AI
│   │   └── Process/                                      # Directory del progetto contenente l'Astrazione di base dei processi di Luna-AI 
│   │       ├── README.md                                 # Documento di introduzione al processBase astratto di Luna-AI
│   │       ├── __init__.py
│   │       └── lib_NeuralProcess.py                      # Base abstract process ereditato da tutti i Brain layers e gli engines di basso livello di Luna-AI
│   │
│   ├── AI_Models/                                        # Directory contenitore per i modelli addestrati e moduli specifici
│   │   ├── README.md
│   │   └── __init__.py
│   │
│   ├── Helpers/
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── message_queue.py
│   │   ├── async_utils.py
│   │   ├── logger.py
│   │   │
│   │   └── Configuration/
│   │       ├── README.md
│   │       ├── __init__.py
│   │       └── lib_Configuration.py
│   │
├── DevTools/
│   └── __init__.py
│   
├── Documentss/                                       # Project directory contenente la documentazione.
│   ├── PROJECT_SETUP.md                              # Documentation di guida al setup del progetto.
│   └── TODO_TASKS.md
│
├── MySelf/
│   │
│   ├── Body/
│   │   ├── Arms/
│   │   │   ├── Left/                                 # Contains data di posizionamento 3D e sensoriali (aptici e termici) del braccio sinistro
│   │   │   │   └── ForeArm/                          # Contains data di posizionamento 3D e sensoriali (aptici e termici) dell'avambraccio sinistro
│   │   │   │       └── Hand/                         # Contains data di posizionamento 3D e sensoriali (aptici e termici) della mano sinistra
│   │   │   │
│   │   │   └── Right/                                # Contains data di posizionamento 3D e sensoriali (aptici e termici) del braccio destro
│   │   │       └── ForeArm/                          # Contains data di posizionamento 3D e sensoriali (aptici e termici) dell'avambraccio destro
│   │   │           └── Hand/                         # Contains data di posizionamento 3D e sensoriali (aptici e termici) della mano destro
│   │   │
│   │   ├── Chest/
│   │   │
│   │   ├── Head/
│   │   │   ├── HeadPivot/                            #
│   │   │   ├── LeftEye/                              #
│   │   │   ├── Mouth/                                #
│   │   │   ├── Nose/                                 #
│   │   │   ├── RightEye/                             #
│   │   │   └── Tongue/                               #
│   │   │
│   │   └── Legs/
│   │       ├── Left/                                 #
│   │       │   └── Thigh/                            #
│   │       │       └── Shin/                         #
│   │       │           └── Foot/                     #
│   │       └── Right/                                #
│   │           └── Thigh/                            #
│   │               └── Shin/                         #
│   │                   └── Foot/                     #
│   │
│   ├── Brain/ 
│   │   ├── Knowledge/
│   │   │   ├── AuditoryMem/                          # Contains data uditivi rilevanti per il riconoscimento delle sorgenti sonore e dei timbri vocali
│   │   │   ├── ConceptualMem/                        # Contains data relativi ai nuovi concetti assimilati dall'ultimo training
│   │   │   ├── EmotionalalMem/                       # Contains data relativi ai nuovi stati emozionali assimilati dall'ultimo training
│   │   │   ├── LongTermMem/                          # Contiene i collegamenti relativi a dati ed eventi assimilate nelle sessioni di training precedenti
│   │   │   ├── SelfExperiencesMem/                   # Contiene i collegamenti relativi a dati ed eventi associati ad esperienze passate e assimilate nelle sessioni di training precedenti
│   │   │   ├── ShortTermMem/                         # Contiene i collegamenti relativi a dati ed eventi assimilati dall'ultimo training
│   │   │   └── VisualMem/                            # Contains data visivi di rilevanza per il riconoscimento di volti e oggetti
│   │   │
│   │   └── Layers/
│   │       ├── AutoReflection/
│   │       │   ├── __init__.py
│   │       │   ├── config.yaml
│   │       │   ├── lib_AutoReflectionLayer.py        # Layer delle riflessioni personali e introspettive di Luna-AI
│   │       │   └── README.md                         # Documento di introduzione al layer logico delle riflessioni personali e introspettive di Luna-AI
│   │       │
│   │       ├── Cognitive/
│   │       │   ├── __init__.py
│   │       │   ├── config.yaml
│   │       │   ├── lib_CognitiveLayer.py             # Layer cognitivo di Luna-AI
│   │       │   └── README.md                         # Documento di introduzione al layer logico cognitivo di Luna-AI
│   │       │
│   │       ├── Emotional/
│   │       │   ├── __init__.py
│   │       │   ├── config.yaml
│   │       │   ├── lib_EmotionalLayer.py             # Layer emozionale/empatico di Luna-AI
│   │       │   └── README.md                         # Documento di introduzione al layer emozionale/empatico di Luna-AI
│   │       │
│   │       ├── Imaginary/
│   │       │   ├── __init__.py
│   │       │   ├── config.yaml
│   │       │   ├── lib_ImaginaryLayer.py             # Layer dell'immaginazione di Luna-AI
│   │       │   └── README.md                         # Documento di introduzione al layer dei pensieri immaginari di Luna-AI
│   │       │
│   │       ├── Logical/
│   │       │   ├── __init__.py
│   │       │   ├── config.yaml
│   │       │   ├── lib_LogicalLayer.py               # Layer dei pensieri logici di Luna-AI
│   │       │   └── README.md                         # Documento di introduzione al layer dei pensieri logici di Luna-AI
│   │       │
│   │       ├── Mnemonic/
│   │       │   ├── __init__.py
│   │       │   ├── config.yaml
│   │       │   ├── lib_MnemonicLayer.py              # Layer dei pensieri memonici di Luna-AI
│   │       │   └── README.md                         # Documento di introduzione al layer dei pensieri memonici di Luna-AI
│   │       │
│   │       ├── Subconscious/                         
│   │       │   ├── __init__.py
│   │       │   ├── config.yaml
│   │       │   ├── lib_SubconsciousLayer.py          # Layer dei pensieri inconsci di Luna-AI
│   │       │   └── README.md                         # Documento di introduzione al layer dei pensieri inconsci di Luna-AI
│   │       │
│   │       └── README.md
│   │
│   ├── Senses/
│   │   ├── _ExternalStimuli/
│   │   │   ├── Aptic/
│   │   │   │   ├── __init__.py
│   │   │   │   └── README.md
│   │   │   │
│   │   │   ├── Audible/
│   │   │   │   ├── __init__.py
│   │   │   │   └── README.md
│   │   │   │
│   │   │   ├── Olfactory/
│   │   │   │   ├── __init__.py
│   │   │   │   └── README.md
│   │   │   │
│   │   │   ├── Visive/
│   │   │   │   ├── __init__.py
│   │   │   │   └── README.md
│   │   │   │
│   │   │   └── __init__.py
│   │   │
│   │   ├── HearingSense/
│   │   │   ├── __init__.py
│   │   │   ├── config.yaml
│   │   │   ├── lib_HearingEngine.py
│   │   │   └── README.md
│   │   │
│   │   ├── OlfactorySense/
│   │   │   ├── __init__.py
│   │   │   ├── config.yaml
│   │   │   ├── lib_OlfactoryEngine.py
│   │   │   └── README.md
│   │   │
│   │   ├── SpeechSense/
│   │   │   ├── __init__.py
│   │   │   ├── config.yaml
│   │   │   ├── lib_SpeechEngine.py
│   │   │   └── README.md
│   │   │
│   │   ├── TouchSense/
│   │   │   ├── __init__.py
│   │   │   ├── config.yaml
│   │   │   ├── lib_TouchEngine.py
│   │   │   └── README.md
│   │   │
│   │   └── VisiveSense/
│   │       ├── __init__.py
│   │       ├── config.yaml
│   │       ├── lib_VisionEngine.py
│   │       └── README.md
│   │
│   └── Spine/
│       └── _MovementStimuli/
│           └── __init__.py
│    
└── TestEnv/
    ├── TestMain.py                                       # Punto di ingresso per l'esecuzione dei test
    ├── config_test.yaml                                  # File di configurazione per i test
    │
    ├── Test_HearEngine/                                  # Cartella con i test specifici per Hear_Engine
    │   └── test_hear_engine.py                           # File con i test definiti
    │
    ├── Test_AnotherModule/                               # Altra cartella per test di altri moduli
    │   └── test_another_module.py
    │
    └── TestData/                                         # Cartella con file di test audio o altri dati di test
        └── dummy_audio.wav
</PRE>

# Decisioni strutturali e Motivationi

## 1. Sottocartella AssetsLibs/Abstaction:

 - Descrizione: Ogni classe di astrazione di base è contenuta in una propria sottocartella con un file .py per il codice operativo, e un file README.md che ne descrive la funzione e la configurazione.

 - Motivazione: Gli engine e i brain_layers sono processi che compongono Luna-AI, ognuno dei quali gestisce specifiche funzionalità proprie ma che ereditano da classi astratte definite all'interno della sottocartella 'abstraction'.

## 2. Sottocartella AassetsLibs/Helpers/:

 - Descrizione: Include file Python come message_queue.py, async_utils.py, config_loader.py, e logger.py, che forniscono supporto generico per la gestione dei dati, la configurazione e la logica asincrona.

 - Motivazione: Gli helper sono moduli di supporto che gestiscono funzionalità comuni e utili tra gli engine, come la gestione della coda dei messaggi, l'asincronia, il logging e il caricamento della configurazione.

## 3. Sottocartella AassetsLibs/AI_Modules/:

 - Descrizione: Include file Python come message_queue.py, async_utils.py, config_loader.py, e logger.py, che forniscono supporto generico per la gestione dei dati, la configurazione e la logica asincrona.

 - Motivazione: Gli helper sono moduli di supporto che gestiscono funzionalità comuni e utili tra gli engine, come la gestione della coda dei messaggi, l'asincronia, il logging e il caricamento della configurazione.

## 4. Sottocartella MySelf/Senses/:

 - Descrizione: Ogni classe engine è contenuta in una propria sottocartella con un file .py per il codice operativo, e un file README.md che ne descrive la funzione e la configurazione.

 - Motivazione: Gli engine o sensi sono i "motori" principali che alimentano le capacità di Luna-AI, ognuno dei quali gestisce specifiche funzionalità come LLM (Language Model), NLP, TTS (Text-to-Speech), STT (Speech-to-Text), CV (Computer Vision), RAG (Retrieval-Augmented Generation) e Voice-to-Voice. Ogni engine è separato in una propria cartella per modularità e chiarezza.

## 5. Sottocartella MySelf/Brain/Layers/*/:

 - Descrizione: Ogni layer (come l'inconscio, l'emotività, la memoria soggettiva, il ragionamento logico e cognitivo etc..) è rappresentato da una cartella con un file .py che contiene la logica di quel layer. Ogni layer avrà anche un "README.md" per descriverne il funzionamento e il proprio file di configurazione "config.yaml".

 - Motivazione: I layers di Luna-AI rappresentano vari livelli di elaborazione e simulano i processi cognitivi, emotivi e logici di un'intelligenza artificiale simile alla mente umana. Sono stati separati in layer distinti per permettere una gestione modulare dei vari aspetti dell'AI.


# Funzioni e Compiti dei File

## 1. Engine Files (llm_engine.py, speech_engine.py, ecc.):

 - Descrizione: Ogni file di engine contiene l'implementazione specifica del motore e le funzioni necessarie per eseguire il task relativo (ad esempio, generazione del testo nel caso del LLM, o riconoscimento vocale per STT).

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



# Future Developments and Improvements

 ## Scalability: 
 La struttura modulare e asincrona del sistema è progettata per essere scalabile. In futuro, sarà possibile aggiungere nuovi engine e layer senza compromettere il funzionamento del sistema esistente.

 ## Layer Expansion: 
 I layer cognitivi ed emotivi possono essere ulteriormente raffinati, aggiungendo comportamenti più complessi e realistici basati sull'analisi dei dati provenienti da sensori esterni o interazioni con l'utente.

 ## Integrazione di Nuove Tecnologie: 
 Potrebbero essere integrati nuovi engine per tecnologie emergenti, come il riconoscimento delle emozioni tramite analisi vocale o il miglioramento delle capacità di ragionamento tramite modelli di deep learning avanzati.

 ## Ottimizzazione delle Risorse: 
 In futuro, sarà possibile migliorare ulteriormente la gestione delle risorse, ottimizzando l'uso della message queue e migliorando l'interazione tra i vari engine per ridurre il carico sui processori.


# Conclusions
Il progetto Luna-AI è stato progettato per essere un sistema complesso e modulare che simula vari aspetti del comportamento umano, utilizzando un'architettura basata su engine e layer separati. Ogni componente è pensato per funzionare come un processo indipendente, migliorando l'efficienza e la scalabilità del sistema. La struttura del progetto e le scelte architetturali consentono una rapida espansione, manutenzione e aggiornamenti futuri, rendendo Luna-AI una base solida per lo sviluppo di un assistente virtuale avanzato.
