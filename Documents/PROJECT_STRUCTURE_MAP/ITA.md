<PRE>
LUNA-AI/
├── startLuna-AI.py                                       # Main project file
├── requirements.txt                                      # Global dependencies
├── README.md                                             # PROJECT INTRODUCTION
│                                                         #-----------------------------------------------------------------------------------------
├── DevTools/                                             #
│   └── __init__.py                                       #
│                                                         #-----------------------------------------------------------------------------------------
├── AssetsLibs/                                           # Project directory containing all the low level assets used by Luna-AI.
│   │                                                     #-----------------------------------------------------------------------------------------
│   ├── Abstraction/                                      # Project directory containing the abstract classes of Luna-AI.
│   │   │                                                 #
│   │   └── Process/                                      # Project directory containing the basic abstraction of Luna-AI processes. 
│   │       ├── README.md                                 # Introduction document to the Luna-AI's abstract base process.
│   │       ├── __init__.py                               # Python placeholder file to let all scripts inside this folder to be treated as modules.
│   │       └── lib_NeuralProcess.py                      # Base abstract process ereditato da tutti i Brain layers e gli engines di basso livello di Luna-AI.
│   │                                                     #
│   ├── AI_Models/                                        # Project directory Directory containing all the trained AI models and modules.
│   │   ├── README.md                                     # Documento di introduzione al processBase astratto di Luna-AI.
│   │   └── __init__.py                                   # Python placeholder file to let all scripts inside this folder to be treated as modules.
│   │                                                     #
│   └── Helpers/                                          #
│       ├── README.md                                     #
│       ├── __init__.py                                   # Python placeholder file to let all scripts inside this folder to be treated as modules.
│       ├── message_queue.py                              #
│       ├── async_utils.py                                #
│       ├── logger.py                                     #
│       │                                                 #
│       └── Configuration/                                #
│           ├── README.md                                 #
│           ├── __init__.py                               # Python placeholder file to let all scripts inside this folder to be treated as modules.
│           └── lib_Configuration.py                      #
│                                                         #
├── DevTools/                                             # Project directory contenente la documentazione.
│                                                         #-----------------------------------------------------------------------------------------
├── Documents/                                            # Project directory containing the documentation.
│   ├── GGUF/                                             #
│   │   ├── ENG.md                                        # Introduction document (English version).
│   │   └── ITA.md                                        # Introduction document (Italian version).
│   ├── LIBROSA/                                          #
│   │   ├── ENG.md                                        # Introduction document (English version).
│   │   └── ITA.md                                        # Introduction document (Italian version).
│   ├── LICENSES/                                         #
│   │   ├── ENG.md                                        # Project License Document (English version).
│   │   └── ITA.md                                        # Project License Document (Italian version).
│   ├── PROJECT_INTRODUCTION/                             #
│   │   ├── ENG.md                                        # Introduction document (English version).
│   │   └── ITA.md                                        # Introduction document (Italian version).
│   ├── PROJECT_SETUP/                                    #
│   │   ├── ENG.md                                        # Introduction document (English version).
│   │   └── ITA.md                                        # Introduction document (Italian version).
│   ├── RAG/                                              #
│   │   ├── ENG.md                                        # Introduction document (English version).
│   │   └── ITA.md                                        # Introduction document (Italian version).
│   └── TENSOR_RT/                                        # 
│       ├── ENG.md                                        # Introduction document (English version).
│       ├── ITA.md                                        # Introduction document (Italian version).
│       └── TensorRT-Quick-Start-Guide.pdf                # TensorRT quick start (from NVIDIA).
│                                                         #-----------------------------------------------------------------------------------------
├── MySelf/                                               #
│   │                                                     #
│   ├── Body/                                             #
│   │   ├── Arms/                                         #
│   │   │   ├── Left/                                     # Contains the 3d position and the sensorial vectors (thermal and aptic values) for the left arm.
│   │   │   │   └── ForeArm/                              # Contains the 3d position and the sensorial vectors (thermal and aptic values) for the left fore-arm.
│   │   │   │       └── Hand/                             # Contains the 3d position and the sensorial vectors (thermal and aptic values) for the left hand.
│   │   │   │                                             #
│   │   │   └── Right/                                    # Contains the 3d position and the sensorial vectors (thermal and aptic values) for the right arm.
│   │   │       └── ForeArm/                              # Contains the 3d position and the sensorial vectors (thermal and aptic values) for the right fore-arm.
│   │   │           └── Hand/                             # Contains the 3d position and the sensorial vectors (thermal and aptic values) for the right hand.
│   │   │                                                 #
│   │   ├── Chest/                                        # Contains the 3d position and the sensorial vectors (thermal and aptic values) for the chest.
│   │   │                                                 #
│   │   ├── Head/                                         # Contains the 3d position and the sensorial vectors (thermal and aptic values) for the head.
│   │   │   ├── HeadPivot/                                # Contains the rotation vector front direction 3D for the head.
│   │   │   ├── LeftEye/                                  # Contains the rotation front direction 3D for the head.
│   │   │   ├── Mouth/                                    #
│   │   │   ├── Nose/                                     #
│   │   │   ├── RightEye/                                 #
│   │   │   └── Tongue/                                   # 
│   │   │                                                 #-----------------------------------------------------------------------------------------
│   │   └── Legs/                                         #
│   │       ├── Left/                                     #
│   │       │   └── Thigh/                                #
│   │       │       └── Shin/                             #
│   │       │           └── Foot/                         #
│   │       │                                             #-----------------------------------------------------------------------------------------
│   │       └── Right/                                    #
│   │           └── Thigh/                                #
│   │               └── Shin/                             #
│   │                   └── Foot/                         #
│   │                                                     #-----------------------------------------------------------------------------------------
│   ├── Brain/                                            #
│   │   ├── Knowledge/                                    #
│   │   │   ├── AuditoryMem/                              # Contains relevant audio data used to recognize the sound sources, sounds types and vocal timbers.
│   │   │   ├── ConceptualMem/                            # Contains data concerning the new concepts assimilated from the latest training.
│   │   │   ├── EmotionalalMem/                           # Contains data related to the new emotional states assimilated from the latest training.
│   │   │   ├── LongTermMem/                              # Contains the links related to data and events assimilated in previous training sessions.
│   │   │   ├── SelfExperiencesMem/                       # Contains the links related to data and events associated with past experiences and assimilated in previous training sessions.
│   │   │   ├── ShortTermMem/                             # Contains the links related to data and events assimilated from the latest training.
│   │   │   └── VisualMem/                                # Contains relevant visual data used to recognize faces and objects.
│   │   │                                                 #
│   │   └── Layers/                                       #
│   │       ├── AutoReflection/                           #
│   │       │   ├── __init__.py                           #
│   │       │   ├── config.yaml                           #
│   │       │   ├── lib_AutoReflectionLayer.py            # Layer of Luna-AI's personal and introspective reflections.
│   │       │   └── README.md                             # Introduction document to the logical layer of Luna-AI's personal and introspective reflections.
│   │       │                                             #
│   │       ├── Cognitive/                                #
│   │       │   ├── __init__.py                           #
│   │       │   ├── config.yaml                           #
│   │       │   ├── lib_CognitiveLayer.py                 # Luna-AI's cognitive layer.
│   │       │   └── README.md                             # Introduction document to Luna-AI's cognitive logical layer.
│   │       │                                             #
│   │       ├── Emotional/                                #
│   │       │   ├── __init__.py                           #
│   │       │   ├── config.yaml                           #
│   │       │   ├── lib_EmotionalLayer.py                 # Luna-AI's emotional/empathetic layer.
│   │       │   └── README.md                             # Introduction document to Luna-AI's emotional/empathetic layer.
│   │       │                                             #
│   │       ├── Imaginary/                                #
│   │       │   ├── __init__.py                           #
│   │       │   ├── config.yaml                           #
│   │       │   ├── lib_ImaginaryLayer.py                 # Luna-AI's imagination layer.
│   │       │   └── README.md                             # Introduction document to Luna-AI's imaginary thoughts layer
│   │       │                                             #
│   │       ├── Logical/                                  # 
│   │       │   ├── __init__.py                           #
│   │       │   ├── config.yaml                           #
│   │       │   ├── lib_LogicalLayer.py                   # Luna-AI's logical thoughts layer.
│   │       │   └── README.md                             # Introduction document to Luna-AI's logical thoughts layer.
│   │       │                                             #
│   │       ├── Mnemonic/                                 #
│   │       │   ├── __init__.py                           #
│   │       │   ├── config.yaml                           #
│   │       │   ├── lib_MnemonicLayer.py                  # Luna-AI's mnemonic thoughts layer.
│   │       │   └── README.md                             # Introduction document to Luna-AI's mnemonic thoughts layer.
│   │       │                                             #
│   │       ├── Subconscious/                             #
│   │       │   ├── __init__.py                           #
│   │       │   ├── config.yaml                           #
│   │       │   ├── lib_SubconsciousLayer.py              # Luna-AI's unconscious thoughts layer.
│   │       │   └── README.md                             # Introduction document to Luna-AI's unconscious thoughts layer.
│   │       │                                             #
│   │       └── README.md                                 #
│   │                                                     #
│   ├── Senses/                                           #
│   │   ├── _ExternalStimuli/                             # 
│   │   │   ├── Aptic/                                    #
│   │   │   │   ├── __init__.py                           #
│   │   │   │   └── README.md                             #
│   │   │   │                                             #
│   │   │   ├── Audible/                                  #
│   │   │   │   ├── __init__.py                           #
│   │   │   │   └── README.md                             #
│   │   │   │                                             #
│   │   │   ├── Olfactory/                                #
│   │   │   │   ├── __init__.py                           #
│   │   │   │   └── README.md                             #
│   │   │   │                                             #
│   │   │   ├── Visive/                                   #
│   │   │   │   ├── __init__.py                           #
│   │   │   │   └── README.md                             #
│   │   │   │                                             #
│   │   │   └── __init__.py                               #
│   │   │                                                 #
│   │   ├── HearingSense/                                 #
│   │   │   ├── __init__.py                               #
│   │   │   ├── config.yaml                               #
│   │   │   ├── lib_HearingEngine.py                      #
│   │   │   └── README.md                                 #
│   │   │                                                 #
│   │   ├── OlfactorySense/                               #
│   │   │   ├── __init__.py                               #
│   │   │   ├── config.yaml                               #
│   │   │   ├── lib_OlfactoryEngine.py                    #
│   │   │   └── README.md                                 #
│   │   │                                                 #
│   │   ├── SpeechSense/                                  #
│   │   │   ├── __init__.py                               #
│   │   │   ├── config.yaml                               #
│   │   │   ├── lib_SpeechEngine.py                       #
│   │   │   └── README.md                                 #
│   │   │                                                 #
│   │   ├── TouchSense/                                   #
│   │   │   ├── __init__.py                               #
│   │   │   ├── config.yaml                               #
│   │   │   ├── lib_TouchEngine.py                        #
│   │   │   └── README.md                                 #
│   │   │                                                 #
│   │   └── VisiveSense/                                  #
│   │       ├── __init__.py                               #
│   │       ├── config.yaml                               #
│   │       ├── lib_VisionEngine.py                       #
│   │       └── README.md                                 #
│   │                                                     #
│   └── Spine/                                            #
│       └── _MovementStimuli/                             #
│           └── __init__.py                               #
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