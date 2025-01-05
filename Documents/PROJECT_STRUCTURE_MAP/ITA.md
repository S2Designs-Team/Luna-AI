<PRE>
LUNA-AI/
├── requirements.txt                                      # Dipendenze globali
├── README.md                                             # INTRODUZIONE AL PROGETTO
│                                                         #-----------------------------------------------------------------------------------------
├── DevTools/                                             #
│   └── __init__.py                                       #
│                                                         #-----------------------------------------------------------------------------------------
├── Documents/                                            # Directory del progetto contenente la documentazione.
│   ├── GGUF/                                             #
│   │   ├── ENG.md                                        # Documento introduttivo (versione inglese).
│   │   └── ITA.md                                        # Documento introduttivo (versione italiana).
│   ├── LIBROSA/                                          #
│   │   ├── ENG.md                                        # Documento introduttivo (versione inglese).
│   │   └── ITA.md                                        # Documento introduttivo (versione italiana).
│   ├── LICENSES/                                         #
│   │   ├── ENG.md                                        # Documento della licenza del progetto (versione inglese).
│   │   └── ITA.md                                        # Documento della licenza del progetto (versione italiana).
│   ├── PROJECT_INTRODUCTION/                             #
│   │   ├── ENG.md                                        # Documento introduttivo (versione inglese).
│   │   └── ITA.md                                        # Documento introduttivo (versione italiana).
│   ├── PROJECT_SETUP/                                    #
│   │   ├── ENG.md                                        # Documento introduttivo (versione inglese).
│   │   └── ITA.md                                        # Documento introduttivo (versione italiana).
│   ├── RAG/                                              #
│   │   ├── ENG.md                                        # Documento introduttivo (versione inglese).
│   │   └── ITA.md                                        # Documento introduttivo (versione italiana).
│   └── TENSOR_RT/                                        # 
│       ├── ENG.md                                        # Documento introduttivo (versione inglese).
│       ├── ITA.md                                        # Documento introduttivo (versione italiana).
│       └── TensorRT-Quick-Start-Guide.pdf                # Guida rapida a TensorRT (da NVIDIA).
│                                                         #-----------------------------------------------------------------------------------------
├── Source/                                               #
│   ├── AssetsLibs/                                       # Directory del progetto contenente tutte le risorse di basso livello utilizzate da Luna-AI.
│   │   │                                                 #-----------------------------------------------------------------------------------------
│   │   ├── Abstraction/                                  # Directory del progetto contenente le classi astratte di Luna-AI.
│   │   │   │                                             #
│   │   │   └── Process/                                  # Directory del progetto contenente l'astrazione di base dei processi di Luna-AI. 
│   │   │       ├── README.md                             # Documento introduttivo al processo base astratto di Luna-AI.
│   │   │       ├── __init__.py                           # File segnaposto Python per trattare tutti gli script in questa cartella come moduli.
│   │   │       └── lib_NeuralProcess.py                  # Processo astratto base ereditato da tutti i Brain layers e gli engine di basso livello di Luna-AI.
│   │   │                                                 #
│   │   ├── AI_Models/                                    # Directory del progetto contenente tutti i modelli AI addestrati e i moduli.
│   │   │   ├── README.md                                 # Documento introduttivo al processo base astratto di Luna-AI.
│   │   │   └── __init__.py                               # File segnaposto Python per trattare tutti gli script in questa cartella come moduli.
│   │   │                                                 #
│   │   └── Helpers/                                      #
│   │       ├── README.md                                 #
│   │       ├── __init__.py                               # File segnaposto Python per trattare tutti gli script in questa cartella come moduli.
│   │       ├── message_queue.py                          #
│   │       ├── async_utils.py                            #
│   │       ├── logger.py                                 #
│   │       │                                             #
│   │       └── Configuration/                            #
│   │           ├── README.md                             #
│   │           ├── __init__.py                           # File segnaposto Python per trattare tutti gli script in questa cartella come moduli.
│   │           └── lib_Configuration.py                  #
│   │                                                     #-----------------------------------------------------------------------------------------
│   ├── GUI/                                              #         
│   │                                                     #-----------------------------------------------------------------------------------------
│   ├── MySelf/                                           #
│   │   │                                                 #
│   │   ├── Body/                                         #
│   │   │   ├── Arms/                                     #
│   │   │   │   ├── Left/                                 # Contiene la posizione 3D e i vettori sensoriali (valori termici e aptici) per il braccio sinistro.
│   │   │   │   │   └── ForeArm/                          # Contiene la posizione 3D e i vettori sensoriali (valori termici e aptici) per l'avambraccio sinistro.
│   │   │   │   │       └── Hand/                         # Contiene la posizione 3D e i vettori sensoriali (valori termici e aptici) per la mano sinistra.
│   │   │   │   │                                         #
│   │   │   │   └── Right/                                # Contiene la posizione 3D e i vettori sensoriali (valori termici e aptici) per il braccio destro.
│   │   │   │       └── ForeArm/                          # Contiene la posizione 3D e i vettori sensoriali (valori termici e aptici) per l'avambraccio destro.
│   │   │   │           └── Hand/                         # Contiene la posizione 3D e i vettori sensoriali (valori termici e aptici) per la mano destra.
│   │   │   │                                             #
│   │   │   ├── Chest/                                    # Contiene la posizione 3D e i vettori sensoriali (valori termici e aptici) per il torace.
│   │   │   │                                             #
│   │   │   ├── Head/                                     # Contiene la posizione 3D e i vettori sensoriali (valori termici e aptici) per la testa.
│   │   │   │   ├── HeadPivot/                            # Contiene il vettore di rotazione direzione frontale 3D per la testa.
│   │   │   │   ├── LeftEye/                              # Contiene il vettore di rotazione direzione frontale 3D per la testa.
│   │   │   │   ├── Mouth/                                #
│   │   │   │   ├── Nose/                                 #
│   │   │   │   ├── RightEye/                             #
│   │   │   │   └── Tongue/                               # 
│   │   │   │                                             #-----------------------------------------------------------------------------------------
│   │   │   └── Legs/                                     #
│   │   │       ├── Left/                                 #
│   │   │       │   └── Thigh/                            #
│   │   │       │       └── Shin/                         #
│   │   │       │           └── Foot/                     #
│   │   │       │                                         #-----------------------------------------------------------------------------------------
│   │   │       └── Right/                                #
│   │   │           └── Thigh/                            #
│   │   │               └── Shin/                         #
│   │   │                   └── Foot/                     #
│   │   │                                                 #-----------------------------------------------------------------------------------------
│   │   ├── Brain/                                        #
│   │   │   ├── Knowledge/                                #
│   │   │   │   ├── AuditoryMem/                          # Contiene i dati audio rilevanti utilizzati per riconoscere le fonti sonore, i tipi di suono e i timbri vocali.
│   │   │   │   ├── ConceptualMem/                        # Contiene i dati relativi ai nuovi concetti assimilati dall'ultimo addestramento.
│   │   │   │   ├── EmotionalalMem/                       # Contiene i dati relativi ai nuovi stati emotivi assimilati dall'ultimo addestramento.
│   │   │   │   ├── LongTermMem/                          # Contiene i collegamenti relativi ai dati e agli eventi assimilati nelle sessioni di addestramento precedenti.
│   │   │   │   ├── SelfExperiencesMem/                   # Contiene i collegamenti relativi ai dati e agli eventi associati alle esperienze passate e assimilati negli addestramenti precedenti.
│   │   │   │   ├── ShortTermMem/                         # Contiene i collegamenti relativi ai dati e agli eventi assimilati dall'ultimo addestramento.
│   │   │   │   └── VisualMem/                            # Contiene i dati visivi rilevanti utilizzati per riconoscere volti e oggetti.
│   │   │   │                                             #
│   │   │   └── Layers/                                   #
│   │   │       ├── AutoReflection/                       #
│   │   │       │   ├── __init__.py                       #
│   │   │       │   ├── config.yaml                       #
│   │   │       │   ├── lib_AutoReflectionLayer.py        # Layer of Luna-AI's personal and introspective reflections.
│   │   │       │   └── README.md                         # Introduction document to the logical layer of Luna-AI's personal and introspective reflections.
│   │   │       │                                         #
│   │   │       ├── Cognitive/                            #
│   │   │       │   ├── __init__.py                       #
│   │   │       │   ├── config.yaml                       #
│   │   │       │   ├── lib_CognitiveLayer.py             # Luna-AI's cognitive layer.
│   │   │       │   └── README.md                         # Introduction document to Luna-AI's cognitive logical layer.
│   │   │       │                                         #
│   │   │       ├── Emotional/                            #
│   │   │       │   ├── __init__.py                       #
│   │   │       │   ├── config.yaml                       #
│   │   │       │   ├── lib_EmotionalLayer.py             # Luna-AI's emotional/empathetic layer.
│   │   │       │   └── README.md                         # Introduction document to Luna-AI's emotional/empathetic layer.
│   │   │       │                                         #
│   │   │       ├── Imaginary/                            #
│   │   │       │   ├── __init__.py                       #
│   │   │       │   ├── config.yaml                       #
│   │   │       │   ├── lib_ImaginaryLayer.py             # Luna-AI's imagination layer.
│   │   │       │   └── README.md                         # Introduction document to Luna-AI's imaginary thoughts layer
│   │   │       │                                         #
│   │   │       ├── Logical/                              # 
│   │   │       │   ├── __init__.py                       #
│   │   │       │   ├── config.yaml                       #
│   │   │       │   ├── lib_LogicalLayer.py               # Luna-AI's logical thoughts layer.
│   │   │       │   └── README.md                         # Introduction document to Luna-AI's logical thoughts layer.
│   │   │       │                                         #
│   │   │       ├── Mnemonic/                             #
│   │   │       │   ├── __init__.py                       #
│   │   │       │   ├── config.yaml                       #
│   │   │       │   ├── lib_MnemonicLayer.py              # Luna-AI's mnemonic thoughts layer.
│   │   │       │   └── README.md                         # Introduction document to Luna-AI's mnemonic thoughts layer.
│   │   │       │                                         #
│   │   │       ├── Subconscious/                         #
│   │   │       │   ├── __init__.py                       #
│   │   │       │   ├── config.yaml                       #
│   │   │       │   ├── lib_SubconsciousLayer.py          # Luna-AI's unconscious thoughts layer.
│   │   │       │   └── README.md                         # Introduction document to Luna-AI's unconscious thoughts layer.
│   │   │       │                                         #
│   │   │       └── README.md                             #
│   │   │                                                 #
│   │   ├── Senses/                                       #
│   │   │   ├── _ExternalStimuli/                         # 
│   │   │   │   ├── Aptic/                                #
│   │   │   │   │   ├── __init__.py                       #
│   │   │   │   │   └── README.md                         #
│   │   │   │   │                                         #
│   │   │   │   ├── Audible/                              #
│   │   │   │   │   ├── __init__.py                       #
│   │   │   │   │   └── README.md                         #
│   │   │   │   │                                         #
│   │   │   │   ├── Olfactory/                            #
│   │   │   │   │   ├── __init__.py                       #
│   │   │   │   │   └── README.md                         #
│   │   │   │   │                                         #
│   │   │   │   ├── Visive/                               #
│   │   │   │   │   ├── __init__.py                       #
│   │   │   │   │   └── README.md                         #
│   │   │   │   │                                         #
│   │   │   │   └── __init__.py                           #
│   │   │   │                                             #
│   │   │   ├── HearingSense/                             #
│   │   │   │   ├── __init__.py                           #
│   │   │   │   ├── config.yaml                           #
│   │   │   │   ├── lib_HearingEngine.py                  #
│   │   │   │   └── README.md                             #
│   │   │   │                                             #
│   │   │   ├── OlfactorySense/                           #
│   │   │   │   ├── __init__.py                           #
│   │   │   │   ├── config.yaml                           #
│   │   │   │   ├── lib_OlfactoryEngine.py                #
│   │   │   │   └── README.md                             #
│   │   │   │                                             #
│   │   │   ├── SpeechSense/                              #
│   │   │   │   ├── __init__.py                           #
│   │   │   │   ├── config.yaml                           #
│   │   │   │   ├── lib_SpeechEngine.py                   #
│   │   │   │   └── README.md                             #
│   │   │   │                                             #
│   │   │   ├── TouchSense/                               #
│   │   │   │   ├── __init__.py                           #
│   │   │   │   ├── config.yaml                           #
│   │   │   │   ├── lib_TouchEngine.py                    #
│   │   │   │   └── README.md                             #
│   │   │   │                                             #
│   │   │   └── VisiveSense/                              #
│   │   │       ├── __init__.py                           #
│   │   │       ├── config.yaml                           #
│   │   │       ├── lib_VisionEngine.py                   #
│   │   │       └── README.md                             #
│   │   │                                                 #
│   │   └── Spine/                                        #
│   │       └── _MovementStimuli/                         #
│   │           └── __init__.py                           #
│   │                                                     #
│   └── startLuna-AI.py                                   #
│                                                         #
└── TestEnv/                                              #
    ├── TestMain.py                                       # Punto di ingresso per l'esecuzione dei test
    ├── config_test.yaml                                  # File di configurazione per i test
    │                                                     #
    ├── Test_HearEngine/                                  # Cartella con i test specifici per Hear_Engine
    │   └── test_hear_engine.py                           # File con i test definiti
    │                                                     #
    ├── Test_AnotherModule/                               # Altra cartella per test di altri moduli
    │   └── test_another_module.py                        #
    │                                                     #
    └── TestData/                                         # Cartella con file di test audio o altri dati di test
        └── dummy_audio.wav
</PRE>