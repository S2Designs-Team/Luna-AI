import os
from typing import Optional
import whisper
import pyaudio
import wave
import speech_recognition as SpeechRecognition

from AssetsLibs.Abstraction.lib_NeuralProcess           import ANeuralProcess

class HearingEngine(ANeuralProcess):

    _INPUT_AUDIO_SENSOR:pyaudio.PyAudio         = None
    _INPUT_AUDIO_SENSOR_INDEX:int               = None
    _INPUT_AUDIO_SENSOR_FORMAT:int              = pyaudio.paInt16  # 16-bit per sample
    _INPUT_AUDIO_SENSOR_CHANNELS:int            = 1                # Audio mono
    _INPUT_AUDIO_SENSOR_RATE:int                = 44100            # Frequenza di campionamento (Hz)
    _INPUT_AUDIO_SENSOR_CHUNK:int               = 1024             # Dimensione dei blocchi di lettura
    _INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION:int = 5                # Durata della registrazione (secondi)
    _INPUT_AUDIO_SENSOR_OUTPUT_PATH:str         = "heared_sounds.wav"

    _STT_MODEL                                  = None
    _STT_MODEL_NAME                             = ""
    _speech_recognizer                          = None
    
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
    def INPUT_AUDIO_SENSOR_OUTPUT_PATH(self, value:int):
        """
        File audio che rappresenta lo stimolo uditivo (by default 'heared_sounds.wav')
        """
        self._INPUT_AUDIO_SENSOR_OUTPUT_PATH = value


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
    def __init__(self, senseName="HearingSense"):
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
            self.logger.warning("ATTENTION: No configuration key %s has been setted in the config.yaml file.", ' -> '.join(keys))
            return None

    def parseConfiguration(self):
        """
        Carica la configurazione letta dal file di configurazione 'config.yaml'
        """
        self.logger.info("[HearingEngine] => using configuration defined in %s ", self.config_path)

        # Parametri di registrazione
        self.INPUT_AUDIO_SENSOR_INDEX               = self.get_config_value("input_audio_sensor", "input_audio_sensor_index")
        self.INPUT_AUDIO_SENSOR_FORMAT              = self.get_config_value("input_audio_sensor", "input_audio_sensor_bits_format")
        self.INPUT_AUDIO_SENSOR_CHANNELS            = self.get_config_value("input_audio_sensor", "input_audio_sensor_channels")
        self.INPUT_AUDIO_SENSOR_RATE                = self.get_config_value("input_audio_sensor", "input_audio_sensor_rate")
        self.INPUT_AUDIO_SENSOR_CHUNK               = self.get_config_value("input_audio_sensor", "input_audio_sensor_chunk")
        self.INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION = self.get_config_value("input_audio_sensor", "input_audio_sensor_max_record_duration")
        self.INPUT_AUDIO_SENSOR_OUTPUT_PATH         = os.path.join(self.external_stimuli_directory, "Audible\\", (self.get_config_value("input_audio_sensor", "input_audio_sensor_output_path")))
        self.logger.info("    |==> INPUT AUDIO SENSOR::INDEX:               %s", self.INPUT_AUDIO_SENSOR_INDEX)
        self.logger.info("    |==> INPUT AUDIO SENSOR::FORMAT:              %s", self.INPUT_AUDIO_SENSOR_FORMAT)
        self.logger.info("    |==> INPUT AUDIO SENSOR::CHANNELS:            %s", self.INPUT_AUDIO_SENSOR_CHANNELS)
        self.logger.info("    |==> INPUT AUDIO SENSOR::RATE:                %s", self.INPUT_AUDIO_SENSOR_RATE)
        self.logger.info("    |==> INPUT AUDIO SENSOR::CHUNK:               %s", self.INPUT_AUDIO_SENSOR_CHUNK)
        self.logger.info("    |==> INPUT AUDIO SENSOR::MAX_RECORD_DURATION: %s", self.INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION)
        self.logger.info("    |==> INPUT AUDIO SENSOR::OUTPUT_PATH:         %s", self.INPUT_AUDIO_SENSOR_OUTPUT_PATH)

        self.STT_MODEL_NAME                         = self.get_config_value("transcription", "whisper_model_name")
        self.logger.info("    |==> STT_MODEL::NAME:                         %s", self.STT_MODEL_NAME)


    async def initialize(self):
        """
        Inizializza il motore di Speech-to-Text.
        self.asrModel1 = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-xvect-voxceleb", savedir="tmpdir")
        self.asrModel2 = SpeakerRecognition.from_hparams(source="speechbrain/asr-wav2vec2-libri",    savedir="tmpdir")
        """
        
        self.parseConfiguration()
        
        self.logger.info("[HearingEngine] => Loading Whisper model '%s'....", self.STT_MODEL_NAME)
        self.STT_MODEL = whisper.load_model(self.STT_MODEL_NAME)
        self.logger.info("[HearingEngine] => Whisper model '%s' correctly loaded!", self.STT_MODEL_NAME)
        self.logger.info("[HearingEngine] => SpeechToTextEngine: initialized.")

        self.__initialize_speech_recognizer()


    def __initialize_speech_recognizer(self):
        """
        """
        self._speech_recognizer = SpeechRecognition.Recognizer()

        self.INPUT_AUDIO_SENSOR = pyaudio.PyAudio()

        if self.INPUT_AUDIO_SENSOR_INDEX is None:
            self.logger.error("[HearingEngine] => No INPUT_AUDIO_SENSOR_INDEX configuration parameter has been setted in the config.yaml file. Please provide it and retry!")
            return
        
        device_info = self.INPUT_AUDIO_SENSOR.get_device_info_by_index(self.INPUT_AUDIO_SENSOR_INDEX)
        self.logger.info("[HearingEngine] => Selected input audio sensor:  ID: %s, Name: %s", self.INPUT_AUDIO_SENSOR_INDEX, device_info['name'] )

        # Apre il flusso audio con il dispositivo selezionato
        stream = self.INPUT_AUDIO_SENSOR.open(format             = self.INPUT_AUDIO_SENSOR_FORMAT,
                                              channels           = self.INPUT_AUDIO_SENSOR_CHANNELS,
                                              rate               = self.INPUT_AUDIO_SENSOR_RATE,
                                              input              = True,
                                              input_device_index = self.INPUT_AUDIO_SENSOR_INDEX,
                                              frames_per_buffer  = self.INPUT_AUDIO_SENSOR_CHUNK)
        
        with self._speech_recognizer as source:
            self.logger.info("[HearingEngine] => Calibrating hearing sense from microphone...Please wait.")
            # listen for 5 seconds and calculate the ambient noise energy level
            self._speech_recognizer.adjust_for_ambient_noise(source, duration=5)




    async def __record_audio(self):
        """
        Avvia la registrazione audio in un thread separato in modo asincrono.
        """
        try: 
            if self.INPUT_AUDIO_SENSOR_INDEX is None:
                self.logger.error("[HearingEngine] => No INPUT_AUDIO_SENSOR_INDEX configuration has been setted in the config.yaml file. Please provide it and retry!")
                return
            

            # Apre il flusso audio con il dispositivo selezionato
            stream = self.INPUT_AUDIO_SENSOR.open(format             = self.INPUT_AUDIO_SENSOR_FORMAT,
                                                  channels           = self.INPUT_AUDIO_SENSOR_CHANNELS,
                                                  rate               = self.INPUT_AUDIO_SENSOR_RATE,
                                                  input              = True,
                                                  input_device_index = self.INPUT_AUDIO_SENSOR_INDEX,
                                                  frames_per_buffer  = self.INPUT_AUDIO_SENSOR_CHUNK)

            self.logger.info("[HearingEngine] => Input audio recording...")
            frames = []

            for _ in range(0, int(self.INPUT_AUDIO_SENSOR_RATE / self.INPUT_AUDIO_SENSOR_CHUNK * self.INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION)):
                data = stream.read(self.INPUT_AUDIO_SENSOR_CHUNK)
                frames.append(data)

            self.logger.info("[HearingEngine] => Input audio recording finished.")
            stream.stop_stream()
            stream.close()
            self.INPUT_AUDIO_SENSOR.terminate()

            # Salva la registrazione in un file
            with wave.open(self.INPUT_AUDIO_SENSOR_OUTPUT_PATH, 'wb') as wf:
                wf.setnchannels(self.INPUT_AUDIO_SENSOR_CHANNELS)
                wf.setsampwidth(self.INPUT_AUDIO_SENSOR.get_sample_size(self.INPUT_AUDIO_SENSOR_FORMAT))
                wf.setframerate(self.INPUT_AUDIO_SENSOR_RATE)
                wf.writeframes(b''.join(frames))
        except Exception as e:
            self.logger.error("Error while recording audio: %s", str(e))

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

        focusedSpeaker_id = "001"

        # Identifica il parlante attuale dall'audio
        identifiedSpeaker_id = self.identify_speaker(message)

        # Verifica se l'audio proviene dal parlante su cui Luna è focalizzata
        if identifiedSpeaker_id != focusedSpeaker_id:
            print(f"Hear_Engine => Ignored: Audio is not from the focused speaker (expected: {focusedSpeaker_id}, got: {identifiedSpeaker_id}).")
            return None
        
        print(f"Hear_Engine => Recognized speaker '{focusedSpeaker_id}'. Proceeding with transcription...")
        print(f"Hear_Engine => SpeechToTextEngine: processing audio from speaker '{focusedSpeaker_id}' ")

        # Esegue la trascrizione dell'audio
        result = self.model.transcribe(message)
        transcription = result["text"]
        print(f"Hear_Engine => Transcription result: {transcription}")
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
            self.logger.info("Speaker %s recognized. Proceeding with audio transcription...", identifiedSpeaker_id)
            transcription = await self.HandleSelfStimuli(self._INPUT_AUDIO_SENSOR_OUTPUT_PATH)
            return transcription
        else:
            self.logger.info("Speaker %s not recognized. Audio ignored.", identifiedSpeaker_id)
            return None
        
