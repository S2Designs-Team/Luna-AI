import os
from typing import Optional
import whisper
from pydub import AudioSegment
from pydub.playback import play
import pyaudio
import speech_recognition as SpeechRecognition

from AssetsLibs.Abstraction.lib_NeuralProcess                                     import ANeuralProcess
from AssetsLibs.Helpers.EnvironmentInfo.INPUT_AUDIO_DEVICES.lib_InputAudioDevices import InputAudioDevices


class HearingEngine(ANeuralProcess):

    _INPUT_AUDIO_SENSOR:pyaudio.PyAudio              = None
    _INPUT_AUDIO_SENSOR_INDEX:int                    = None
    _INPUT_AUDIO_SENSOR_FORMAT:int                   = pyaudio.paInt32  # 32-bit per sample
    _INPUT_AUDIO_SENSOR_CHANNELS:int                 = 1                # Audio mono
    _INPUT_AUDIO_SENSOR_RATE:int                     = 44100            # Frequenza di campionamento (Hz)
    _INPUT_AUDIO_SENSOR_CHUNK:int                    = 1024             # Dimensione dei blocchi di lettura
    _INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION:int      = 5                # Durata della registrazione (secondi)
    _INPUT_AUDIO_SENSOR_OUTPUT_PATH:str              = "heared_sounds.wav"

    _SPEECH_RECOGNITION_ENERGY_THRESHOLD:int         = 300
    _SPEECH_RECOGNITION_DYN_ENERGY_THRESHOLD:bool    = True
    _SPEECH_RECOGNITION_DYN_ENERGY_ADJ_DAMPING:float = 0.15
    _SPEECH_RECOGNITION_DYN_ENERGY_RATIO:float       = 1.5
    _SPEECH_RECOGNITION_PAUSE_THRESHOLD:float        = 0.8
    _SPEECH_RECOGNITION_OPERATION_TIMEOUT:int        = None


    _STT_MODEL                                  = None
    _STT_MODEL_NAME                             = ""
    _speech_recognizer                          = None
    _STREAM                                     = None
    _selected_input_audio_device_info           = None
    
    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------------
    @property
    def INPUT_AUDIO_SENSOR_INDEX(self):
        return self._INPUT_AUDIO_SENSOR_INDEX

    @INPUT_AUDIO_SENSOR_INDEX.setter
    def INPUT_AUDIO_SENSOR_INDEX(self, value):
        self._INPUT_AUDIO_SENSOR_INDEX = value

    @property
    def INPUT_AUDIO_SENSOR(self):
        """
        THE LOGICAL DEVICE USED FOR THE AUDIO INPUT
        """        
        return self._INPUT_AUDIO_SENSOR
    
    @INPUT_AUDIO_SENSOR.setter
    def INPUT_AUDIO_SENSOR(self, value):
        """
        THE LOGICAL DEVICE USED FOR THE AUDIO INPUT
        """
        self._INPUT_AUDIO_SENSOR = value

    @property
    def INPUT_AUDIO_SENSOR_FORMAT(self):
        """
        Bits per sample (by default 16 bits)
        """        
        return self._INPUT_AUDIO_SENSOR_FORMAT

    @INPUT_AUDIO_SENSOR_FORMAT.setter
    def INPUT_AUDIO_SENSOR_FORMAT(self, value:int):
        """
        Bits per sample (by default 16 bits)
        """
        self._INPUT_AUDIO_SENSOR_FORMAT = value

    @property
    def INPUT_AUDIO_SENSOR_CHANNELS(self):
        """
        Channels of the audio (by default 1 channel)
        """
        return self._INPUT_AUDIO_SENSOR_CHANNELS

    @INPUT_AUDIO_SENSOR_CHANNELS.setter
    def INPUT_AUDIO_SENSOR_CHANNELS(self, value:int):
        """
        Channels of the audio (by default 1 channel)
        """
        self._INPUT_AUDIO_SENSOR_CHANNELS = value

    @property
    def INPUT_AUDIO_SENSOR_RATE(self):
        """
        Frequenza di campionamento in Hz (by default 44100)
        """
        return self._INPUT_AUDIO_SENSOR_RATE

    @INPUT_AUDIO_SENSOR_RATE.setter
    def INPUT_AUDIO_SENSOR_RATE(self, value:int):
        """
        Frequenza di campionamento in Hz (by default 44100)
        """
        self._INPUT_AUDIO_SENSOR_RATE = value    

    @property
    def INPUT_AUDIO_SENSOR_CHUNK(self):
        """
        Dimensione dei blocchi di lettura (by default 1024)
        """
        return self._INPUT_AUDIO_SENSOR_CHUNK

    @INPUT_AUDIO_SENSOR_CHUNK.setter
    def INPUT_AUDIO_SENSOR_CHUNK(self, value:int):
        """
        Dimensione dei blocchi di lettura (by default 1024)
        """
        self._INPUT_AUDIO_SENSOR_CHUNK = value          

    @property
    def INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION(self):
        """
        Durata della registrazione in secondi (by default 5)
        """
        return self._INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION

    @INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION.setter
    def INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION(self, value:int):
        """
        Durata della registrazione in secondi (by default 5)
        """
        self._INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION = value

    @property
    def INPUT_AUDIO_SENSOR_OUTPUT_PATH(self):
        """
        File audio che rappresenta lo stimolo uditivo (by default 'heared_sounds.wav')
        """
        return self._INPUT_AUDIO_SENSOR_OUTPUT_PATH

    @INPUT_AUDIO_SENSOR_OUTPUT_PATH.setter
    def INPUT_AUDIO_SENSOR_OUTPUT_PATH(self, value:str):
        self._INPUT_AUDIO_SENSOR_OUTPUT_PATH = value

    @property
    def SPEECH_RECOGNITION_ENERGY_THRESHOLD(self):
        return self._SPEECH_RECOGNITION_DYN_ENERGY_THRESHOLD

    @SPEECH_RECOGNITION_ENERGY_THRESHOLD.setter
    def SPEECH_RECOGNITION_ENERGY_THRESHOLD(self, value:int):
        self._SPEECH_RECOGNITION_DYN_ENERGY_THRESHOLD = value

    @property
    def SPEECH_RECOGNITION_DYN_ENERGY_THRESHOLD(self):
        return self._SPEECH_RECOGNITION_DYN_ENERGY_THRESHOLD
    
    @SPEECH_RECOGNITION_DYN_ENERGY_THRESHOLD.setter
    def SPEECH_RECOGNITION_DYN_ENERGY_THRESHOLD(self, value:bool):
        self._SPEECH_RECOGNITION_DYN_ENERGY_THRESHOLD = value

    @property
    def SPEECH_RECOGNITION_DYN_ENERGY_ADJ_DAMPING(self):
        return self._SPEECH_RECOGNITION_DYN_ENERGY_ADJ_DAMPING
    
    @SPEECH_RECOGNITION_DYN_ENERGY_ADJ_DAMPING.setter
    def SPEECH_RECOGNITION_DYN_ENERGY_ADJ_DAMPING(self, value:float):
        self._SPEECH_RECOGNITION_DYN_ENERGY_ADJ_DAMPING = value

    @property
    def SPEECH_RECOGNITION_DYN_ENERGY_RATIO(self):
        return self._SPEECH_RECOGNITION_DYN_ENERGY_RATIO
    
    @SPEECH_RECOGNITION_DYN_ENERGY_RATIO.setter
    def SPEECH_RECOGNITION_DYN_ENERGY_RATIO(self, value:float):
        self._SPEECH_RECOGNITION_DYN_ENERGY_RATIO = value

    @property
    def SPEECH_RECOGNITION_PAUSE_THRESHOLD(self):
        return self._SPEECH_RECOGNITION_PAUSE_THRESHOLD
    
    @SPEECH_RECOGNITION_PAUSE_THRESHOLD.setter
    def SPEECH_RECOGNITION_PAUSE_THRESHOLD(self, value:float):
        self._SPEECH_RECOGNITION_PAUSE_THRESHOLD = value

    @property
    def SPEECH_RECOGNITION_OPERATION_TIMEOUT(self):
        return self._SPEECH_RECOGNITION_OPERATION_TIMEOUT
    
    @SPEECH_RECOGNITION_OPERATION_TIMEOUT.setter
    def SPEECH_RECOGNITION_OPERATION_TIMEOUT(self, value:int):
        self._SPEECH_RECOGNITION_OPERATION_TIMEOUT = value

    @property
    def STT_MODEL(self):
        """
        """
        return self._STT_MODEL

    @STT_MODEL.setter
    def STT_MODEL(self, value):
        """
        """
        self._STT_MODEL = value

    @property
    def STT_MODEL_NAME(self):
        """
        """
        return self._STT_MODEL_NAME

    @STT_MODEL_NAME.setter
    def STT_MODEL_NAME(self, value):
        """
        """
        self._STT_MODEL_NAME = value

        
    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
        # Database degli speaker riconosciuti (chiave: speaker_id, valore: embedding)
        self.speaker_db = {"001"}
        
    def get_config_value(self, *keys):
        """
        Recupera il valore dalla configurazione data una serie di chiavi.
        Se una chiave non esiste, stampa un messaggio di avviso e restituisce None.
        """
        try:
            config_value = self.configuration
            for key in keys:
                config_value = config_value[key]
            return config_value
        except KeyError:
            self.logger.warning("ATTENTION: No configuration key %s has been setted in the config.yaml file.", ' -> '.join(keys), exc_info=True)
            return None

    def parseConfiguration(self):
        """
        Carica la configurazione letta dal file di configurazione 'config.yaml'
        """
        #----------------------------
        #- Parametri di registrazione
        #----------------------------
        self.INPUT_AUDIO_SENSOR_INDEX                  = self.get_config_value("input_audio_sensor", "input_audio_sensor_index")
        self.INPUT_AUDIO_SENSOR_FORMAT                 = self.get_config_value("input_audio_sensor", "input_audio_sensor_bits_format")
        self.INPUT_AUDIO_SENSOR_CHANNELS               = self.get_config_value("input_audio_sensor", "input_audio_sensor_channels")
        self.INPUT_AUDIO_SENSOR_RATE                   = self.get_config_value("input_audio_sensor", "input_audio_sensor_rate")
        self.INPUT_AUDIO_SENSOR_CHUNK                  = self.get_config_value("input_audio_sensor", "input_audio_sensor_chunk")
        self.INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION    = self.get_config_value("input_audio_sensor", "input_audio_sensor_max_record_duration")
        self.INPUT_AUDIO_SENSOR_OUTPUT_PATH            = os.path.join(self.external_stimuli_directory, "Audible\\", (self.get_config_value("input_audio_sensor", "input_audio_sensor_output_path")))
        #------------------------------------        
        #- Parametri dello Speech Recognition
        #------------------------------------
        self.SPEECH_RECOGNITION_ENERGY_THRESHOLD       = self.get_config_value("speech_recognition", "energy_threshold")
        self.SPEECH_RECOGNITION_DYN_ENERGY_THRESHOLD   = self.get_config_value("speech_recognition", "dynamic_energy_threshold")
        self.SPEECH_RECOGNITION_DYN_ENERGY_ADJ_DAMPING = self.get_config_value("speech_recognition", "dynamic_energy_adjustment_damping")
        self.SPEECH_RECOGNITION_DYN_ENERGY_RATIO       = self.get_config_value("speech_recognition", "dynamic_energy_ratio")
        self.SPEECH_RECOGNITION_PAUSE_THRESHOLD        = self.get_config_value("speech_recognition", "pause_threshold")
        self.SPEECH_RECOGNITION_OPERATION_TIMEOUT      = self.get_config_value("speech_recognition", "operation_timeout")
        #--------------------------------        
        #- Parametri dello Speech To Text
        #--------------------------------
        self.STT_MODEL_NAME                            = self.get_config_value("transcription", "whisper_model_name")
        #-------------------------------------        
        #- Input audio device Name selezionato 
        #-------------------------------------
        if self.INPUT_AUDIO_SENSOR_INDEX is None:
            self.logger.error("[HearingEngine] => No INPUT_AUDIO_SENSOR_INDEX configuration parameter has been setted in the config.yaml file. Please provide it and retry!")
            return
        self._selected_input_audio_device_info                              = InputAudioDevices.get_device_infos(self.INPUT_AUDIO_SENSOR_INDEX)

        self.logger.info("[HearingEngine]::[parseConfiguration] => reading  '%s'", self.config_path)        
        self.logger.info("    ├ INPUT AUDIO SENSOR::INDEX:.................  %s" , self.INPUT_AUDIO_SENSOR_INDEX)
        self.logger.info("    ├ INPUT AUDIO SENSOR::NAME::................. '%s'", self._selected_input_audio_device_info['name'] )          
        self.logger.info("    ├ INPUT AUDIO SENSOR::FORMAT::...............  %s" , self.INPUT_AUDIO_SENSOR_FORMAT)
        self.logger.info("    ├ INPUT AUDIO SENSOR::CHANNELS:..............  %s" , self.INPUT_AUDIO_SENSOR_CHANNELS)
        self.logger.info("    ├ INPUT AUDIO SENSOR::RATE:..................  %s" , self.INPUT_AUDIO_SENSOR_RATE)
        self.logger.info("    ├ INPUT AUDIO SENSOR::CHUNK:.................  %s" , self.INPUT_AUDIO_SENSOR_CHUNK)
        self.logger.info("    ├ INPUT AUDIO SENSOR::MAX_RECORD_DURATION:...  %s" , self.INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION)
        self.logger.info("    ├ INPUT AUDIO SENSOR::OUTPUT_PATH:........... '%s'", self.INPUT_AUDIO_SENSOR_OUTPUT_PATH)
        self.logger.info("    ├ STT_MODEL::NAME:........................... '%s'", self.STT_MODEL_NAME)
        self.logger.info("    ├ SPEECH RECOGNITION::ENERGY_THRESHOLD:......  %s" , self.SPEECH_RECOGNITION_ENERGY_THRESHOLD)
        self.logger.info("    ├ SPEECH RECOGNITION::DYN_ENERGY_THRESHOLD:..  %s" , self.SPEECH_RECOGNITION_DYN_ENERGY_THRESHOLD)
        self.logger.info("    ├ SPEECH RECOGNITION::DYN_ENERGY_ADJ_DAMPING:  %s" , self.SPEECH_RECOGNITION_DYN_ENERGY_ADJ_DAMPING)
        self.logger.info("    ├ SPEECH RECOGNITION::DYN_ENERGY_RATIO:......  %s" , self.SPEECH_RECOGNITION_DYN_ENERGY_RATIO)
        self.logger.info("    ├ SPEECH RECOGNITION::PAUSE_THRESHOLD:.......  %s" , self.SPEECH_RECOGNITION_PAUSE_THRESHOLD)
        self.logger.info("    ├ SPEECH RECOGNITION::OPERATION_TIMEOUT:.....  %s" , self.SPEECH_RECOGNITION_OPERATION_TIMEOUT)       


    def initialize(self):
        """
        Inizializza il motore di Speech-to-Text.
        self.asrModel1 = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-xvect-voxceleb", savedir="tmpdir")
        self.asrModel2 = SpeakerRecognition.from_hparams(source="speechbrain/asr-wav2vec2-libri",    savedir="tmpdir")
        """
        try:
            self.parseConfiguration()
        
            self.logger.info("[HearingSense]::[initialize]")
            self.__initialize_speech_to_text()
            self.__initialize_speech_recognizer()

            self.is_process_initialized = True
        except Exception as e:
            self.logger.error("[HearingSense]::[initialize] => Error during initialization: %s", e, exc_info=True)
            self.is_process_initialized = False

    def __initialize_speech_to_text(self):
        """
        """
        self.logger.info("    ├──> Initializing STT Whisper model '%s'....", self.STT_MODEL_NAME)
        self.logger.info("    ├──> Initializing the selected INPUT AUDIO SENSOR....(%s)", self._selected_input_audio_device_info['name'])        
        try:
            self.STT_MODEL = whisper.load_model(self.STT_MODEL_NAME)
            self._INPUT_AUDIO_SENSOR = pyaudio.PyAudio()
        except Exception as e:
            self.logger.error("    └──> [ERROR] %s", e, exc_info=True)

    def __initialize_speech_recognizer(self):
        """
        """        
        #- SPEECH RECOGNIZER INITIALIZATION
        #----------------------------------
        try:
            self.logger.info("    ├──> Initializing the speech recognizer....Please wait.")        
            self._speech_recognizer = SpeechRecognition.Recognizer()
        except Exception as e:
            self.logger.error("        └──> [ERROR] %s", e, exc_info=True)
        
        try:
            self.logger.info("    ├──> Calibrating hearing sense from microphone...Please wait.")
            with SpeechRecognition.Microphone(device_index=self.INPUT_AUDIO_SENSOR_INDEX) as source:
                # listen for 5 seconds and calculate the ambient noise energy level
                self._speech_recognizer.adjust_for_ambient_noise(source, duration=1)
        except Exception as e:
            self.logger.error("        └──> [ERROR] %s", e, exc_info=True)

        
    async def __record_audio(self):
        """
        Records the input audio and saves it to a file.
        """
        self.logger.info("[HearingEngine]::[__record_audio]")
        try:
            try:
                # Apre il flusso audio con il dispositivo selezionato
                self._STREAM = self.INPUT_AUDIO_SENSOR.open(format             = self.INPUT_AUDIO_SENSOR_FORMAT,
                                                            channels           = self.INPUT_AUDIO_SENSOR_CHANNELS,
                                                            rate               = self.INPUT_AUDIO_SENSOR_RATE,
                                                            input              = True,
                                                            input_device_index = self.INPUT_AUDIO_SENSOR_INDEX,
                                                            frames_per_buffer  = self.INPUT_AUDIO_SENSOR_CHUNK)
            except Exception as e:
                self.logger.error("    └──> [ERROR]  Error opening the input audio stream: %s", e)
                return

            my_speechRecognizer = SpeechRecognition.Recognizer()
            my_speechRecognizer.energy_threshold                  = self.SPEECH_RECOGNITION_ENERGY_THRESHOLD
            my_speechRecognizer.dynamic_energy_threshold          = self.SPEECH_RECOGNITION_DYN_ENERGY_THRESHOLD
            my_speechRecognizer.dynamic_energy_adjustment_damping = self.SPEECH_RECOGNITION_DYN_ENERGY_ADJ_DAMPING
            my_speechRecognizer.dynamic_energy_ratio              = self.SPEECH_RECOGNITION_DYN_ENERGY_RATIO
            my_speechRecognizer.pause_threshold                   = self.SPEECH_RECOGNITION_PAUSE_THRESHOLD
            my_speechRecognizer.operation_timeout                 = self.SPEECH_RECOGNITION_OPERATION_TIMEOUT
            self.logger.info("    ├    ├──> ID Dispositivo:.................... %s", self.INPUT_AUDIO_SENSOR_INDEX)
            self.logger.info("    ├    ├──> Dispositivo selezionato:........... %s", self._selected_input_audio_device_info['name'])
            self.logger.info("    ├    ├──> Canali input:...................... %s", self._selected_input_audio_device_info['maxInputChannels'])
            self.logger.info("    ├    ├──> Freq. di campionamento supportata:. %s", self._selected_input_audio_device_info['defaultSampleRate'])
            self.logger.info("    ├    ├──> Energy threshold:.................. %s", my_speechRecognizer.energy_threshold)
            self.logger.info("    ├    ├──> Dynamic energy threshold:.......... %s", my_speechRecognizer.dynamic_energy_threshold)
            self.logger.info("    ├    ├──> Dynamic energy adjustment damping:. %s", my_speechRecognizer.dynamic_energy_adjustment_damping)
            self.logger.info("    ├    ├──> Dynamic energy ratio:.............. %s", my_speechRecognizer.dynamic_energy_ratio)
            self.logger.info("    ├    ├──> Pause threshold:................... %s", my_speechRecognizer.pause_threshold)
            self.logger.info("    ├    └──> Operation timeout:................. %s", my_speechRecognizer.operation_timeout)
            
            # Usa il microfono come sorgente audio
            with SpeechRecognition.Microphone() as source:

                self.logger.info("    ├──> Input audio recording...")
                try:

                    # Opzione per ridurre il rumore ambientale
                    my_speechRecognizer.adjust_for_ambient_noise(source, duration=1)                 
                    
                    self.logger.info("    ├    ├──> Noise reduction active...")
                    audio = my_speechRecognizer.listen(source, timeout=10)  # Timeout dopo 10 secondi
                    self.logger.info("    ├    └──> Input audio recording completeted.")

                    # Salva l'audio in un file WAV
                    with open(self.INPUT_AUDIO_SENSOR_OUTPUT_PATH, "wb") as f:
                         f.write(audio.get_wav_data())

                         self.logger.info("    └──> Input audio saved as '%s'.", self.INPUT_AUDIO_SENSOR_OUTPUT_PATH)

                except Exception as e:
                    self.logger.error("    └──> [ERROR] Error occurred during the outcoming sound recording: %s", e)

            # Opzionale: Riproduci l'audio registrato
            audio = AudioSegment.from_file(self.INPUT_AUDIO_SENSOR_OUTPUT_PATH, format="wav")
            play(audio)

        except KeyboardInterrupt:
            print("[INFO] Manual interruption during incoming audio recording.")
            raise
        except Exception as e:
            self.logger.error("[ERROR][HearingEngine]::[__record_audio] => Error during input audio recording: %s", e)

    def transcribe_audio(self):
        """
        Transcribes the recorded audio file using the Whisper model.
        """
        if not os.path.exists(self.INPUT_AUDIO_SENSOR_OUTPUT_PATH):
            self.logger.error("[HearingEngine] => Audio file '%s' does not exist.", self.INPUT_AUDIO_SENSOR_OUTPUT_PATH)
            return None
        try:
            self.logger.info("[HearingEngine] => Transcribing audio file '%s'...", self.INPUT_AUDIO_SENSOR_OUTPUT_PATH)
            my_transcription_result = self.STT_MODEL.transcribe(self.INPUT_AUDIO_SENSOR_OUTPUT_PATH)
            my_transcription_text = my_transcription_result['text']
            self.logger.info("[HearingEngine] => Transcription completed: %s", my_transcription_text)
            return my_transcription_text
        except Exception as e:
            self.logger.error("Error during transcription: %s", e)
            return None
        
    @staticmethod
    def identify_speaker(audioStimuli):
        """ 
        Metodo da utilizzare per identificare il parlante dall'audio.
        """
    
        # TODO: Logica per identificare lo speaker (placeholder)
        # Supponiamo che restituisca un ID speaker
        return "001"
    
    async def handleSelfStimuli(self, message):
        """
        Elabora audio simulando l'udito.
        """
        self.logger.info("[HearingEngine]::[handleSelfStimuli]")
        try: 
            focusedSpeaker_id = "001"

            # Identifica il parlante attuale dall'audio
            identifiedSpeaker_id = self.identify_speaker(message)

            # Verifica se l'audio proviene dal parlante su cui Luna è focalizzata
            if identifiedSpeaker_id != focusedSpeaker_id:
                self.logger.error("[HearingEngine]::[handleSelfStimuli] => Ignored: Audio is not from the focused speaker (expected: %s, got: %s).", focusedSpeaker_id, identifiedSpeaker_id)
                return None
        
            self.logger.info("[HearingEngine]::[handleSelfStimuli] => Recognized speaker '%s'. Proceeding with transcription...", focusedSpeaker_id)
            self.logger.info("[HearingEngine]::[handleSelfStimuli] => SpeechToTextEngine: processing audio from speaker '%s'.", focusedSpeaker_id)

            # Esegue la trascrizione dell'audio
            result = self._STT_MODEL.transcribe(message)
            transcription = result["text"]
            self.logger.info("[HearingEngine]::[handleSelfStimuli] => Transcription result: %s", transcription)

        except Exception as e:
            self.logger.error("    └──> [ERROR] Error occurred: %s", e)
        finally:
            pass
        return transcription
    
    async def handleExternalStimuli(self, message:str = ""):
        """
        Elabora l'audio esterno simulando l'udito, identifica lo speaker e rimanda lo stimolo uditivo al processamento degli stimoli interni
        (handleSelfStimuli) che utilizzerà uno STT (Whisper) per trascrivere l'audio analizzato.
        """
        # Passo 1: Registra l'audio
        _ = await self.__record_audio()

        # Passo 2: Identifica lo speaker
        identifiedSpeaker_id = self.identify_speaker(self._INPUT_AUDIO_SENSOR_OUTPUT_PATH)

        # Passo 3: Verifica se lo speaker è già riconosciuto
        if identifiedSpeaker_id in self.speaker_db:
            self.logger.info("[HearingEngine]::[handleExternalStimuli] => Speaker %s recognized. Proceeding with audio transcription...", identifiedSpeaker_id)
            transcription = await self.handleSelfStimuli(self._INPUT_AUDIO_SENSOR_OUTPUT_PATH)
            return transcription
        else:
            self.logger.info("[HearingEngine]::[handleExternalStimuli] => Speaker %s not recognized. Audio ignored.", identifiedSpeaker_id)
            return None