import os
import whisper
import pyaudio
import speech_recognition as SpeechRecognition
from typing         import Optional
from pydub          import AudioSegment
from pydub.playback import play
from AssetsLibs.Abstraction.lib_NeuralProcess                                     import NeuralProcess
from AssetsLibs.Helpers.EnvironmentInfo.INPUT_AUDIO_DEVICES.lib_InputAudioDevices import InputAudioDevices


class HearingSense(NeuralProcess):

    _input_audio_sensor:pyaudio.PyAudio               = None
    _input_audio_sensor_index:int                     = None
    _input_audio_sensor_format:int                    = pyaudio.paInt32  # 32-bit per sample
    _input_audio_sensor_channels:int                  = 1                # Audio mono
    _input_audio_sensor_rate:int                      = 44100            # Frequenza di campionamento (Hz)
    _input_audio_sensor_chunk:int                     = 1024             # Dimensione dei blocchi di lettura
    _input_audio_sensor_max_record_duration:int       = 5                # Durata della registrazione (secondi)
    _input_audio_sensor_output_path:str               = "heared_sounds.wav"

    _speech_recognitiion_energy_threshold:int         = 300
    _speech_recognitiion_dyn_energy_threshold:bool    = True
    _speech_recognitiion_dyn_energy_adj_damping:float = 0.15
    _speech_recognitiion_dyn_energy_ratio:float       = 1.5
    _speech_recognitiion_pause_threshold:float        = 0.8
    _speech_recognitiion_operation_timeout:int        = None

    _STT_MODEL                                        = None
    _STT_MODEL_NAME                                   = ""
    _speech_recognizer                                = None
    _STREAM                                           = None
    _selected_input_audio_device_info                 = None
    
    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------------
    @property
    def conf_input_audio_sensor_index(self):
        """
        Property: index of the input audio sensor.\n\n
        """
        return self._input_audio_sensor_index
    @conf_input_audio_sensor_index.setter
    def conf_input_audio_sensor_index(self, value:int):
        """
        Args:
            value (int): The index value to set for the input audio sensor.
        """
        self._input_audio_sensor_index = value

    @property
    def conf_input_audio_sensor(self):
        """
        Property: the logical device used for the audio input.
        """      
        return self._input_audio_sensor
    @conf_input_audio_sensor.setter
    def conf_input_audio_sensor(self, value:pyaudio):
        """
        Args:
            value (pyaudio): The logical device used for the audio input.
        """      
        self._input_audio_sensor = value

    @property
    def conf_input_audio_sensor_format(self):
        """
        Property: The number of bits per sample for the input audio sensor.
        """
        return self._input_audio_sensor_format
    @conf_input_audio_sensor_format.setter
    def conf_input_audio_sensor_format(self, value:int):
        """
        Args:
            value (int): Bits per sample for the audio sensor.
        """
        self._input_audio_sensor_format = value

    @property
    def conf_input_audio_sensor_channels(self):
        """
        Property: Number of channels of the audio.
        """
        return self._input_audio_sensor_channels
    @conf_input_audio_sensor_channels.setter
    def conf_input_audio_sensor_channels(self, value:int):
        """
        Args:
            value (int): The number of audio sensor channels to be set.
        """
        self._input_audio_sensor_channels = value

    @property
    def conf_input_audio_sensor_rate(self):
        """
        Property: The input audio sensor sampling rate (in hz).
        """
        return self._input_audio_sensor_rate
    @conf_input_audio_sensor_rate.setter
    def conf_input_audio_sensor_rate(self, value:int):
        """
        Args:
            value (int): The rate value to set for the input audio sensor (in hz).
        """
        self._input_audio_sensor_rate = value    

    @property
    def conf_input_audio_sensor_chunk(self):
        """
        The size of the audio sensor input chunks (bytes).
        """
        return self._input_audio_sensor_chunk
    @conf_input_audio_sensor_chunk.setter
    def conf_input_audio_sensor_chunk(self, value:int):
        """
        Args:
            value (int): The size of the audio sensor input chunk (bytes).
        """
        self._input_audio_sensor_chunk = value          

    @property
    def conf_input_audio_sensor_max_record_duration(self):
        """
        Durata della registrazione in secondi (by default 5)
        """
        return self._input_audio_sensor_max_record_duration

    @conf_input_audio_sensor_max_record_duration.setter
    def conf_input_audio_sensor_max_record_duration(self, value:int):
        """
        Durata della registrazione in secondi (by default 5)
        """
        self._input_audio_sensor_max_record_duration = value

    @property
    def conf_input_audio_sensor_output_path(self):
        """
        File audio che rappresenta lo stimolo uditivo (by default 'heared_sounds.wav')
        """
        return self._input_audio_sensor_output_path

    @conf_input_audio_sensor_output_path.setter
    def conf_input_audio_sensor_output_path(self, value:str):
        self._input_audio_sensor_output_path = value

    @property
    def conf_speech_recognitiion_energy_threshold(self):
        return self._speech_recognitiion_energy_threshold

    @conf_speech_recognitiion_energy_threshold.setter
    def conf_speech_recognitiion_energy_threshold(self, value:int):
        self._speech_recognitiion_energy_threshold = value

    @property
    def conf_speech_recognitiion_dyn_energy_threshold(self):
        return self._speech_recognitiion_dyn_energy_threshold
    
    @conf_speech_recognitiion_dyn_energy_threshold.setter
    def conf_speech_recognitiion_dyn_energy_threshold(self, value:bool):
        self._speech_recognitiion_dyn_energy_threshold = value

    @property
    def conf_speech_recognitiion_dyn_energy_adj_damping(self):
        return self._speech_recognitiion_dyn_energy_adj_damping
    
    @conf_speech_recognitiion_dyn_energy_adj_damping.setter
    def conf_speech_recognitiion_dyn_energy_adj_damping(self, value:float):
        self._speech_recognitiion_dyn_energy_adj_damping = value

    @property
    def conf_speech_recognitiion_dyn_energy_ratio(self):
        return self._speech_recognitiion_dyn_energy_ratio
    
    @conf_speech_recognitiion_dyn_energy_ratio.setter
    def conf_speech_recognitiion_dyn_energy_ratio(self, value:float):
        self._speech_recognitiion_dyn_energy_ratio = value

    @property
    def conf_speech_recognitiion_pause_threshold(self):
        return self._speech_recognitiion_pause_threshold
    
    @conf_speech_recognitiion_pause_threshold.setter
    def conf_speech_recognitiion_pause_threshold(self, value:float):
        self._speech_recognitiion_pause_threshold = value

    @property
    def conf_speech_recognitiion_operation_timeout(self):
        return self._speech_recognitiion_operation_timeout
    
    @conf_speech_recognitiion_operation_timeout.setter
    def conf_speech_recognitiion_operation_timeout(self, value:int):
        self._speech_recognitiion_operation_timeout = value

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
        """
        Initializes the HearingSense class.

        This constructor initializes the base class and sets up the database
        for recognized speakers. The database is a dictionary where the key
        is the speaker_id and the value is the embedding.

        Attributes:
            speaker_db (dict): A dictionary containing recognized speakers.
                               The key is the speaker_id and the value is the embedding.
        """
        super().__init__()
        # Database degli speaker riconosciuti (chiave: speaker_id, valore: embedding)
        self.speaker_db = {"001"}
        
    def initialize(self):
        """
        Initializes the Speech-to-Text engine and other components.
        This method performs the following steps:
        1. Parses the configuration.
        2. Logs the initialization process.
        3. Initializes the Speech-to-Text engine.
        4. Initializes the speech recognizer.
        If an error occurs during initialization, it logs the error and sets the 
        process initialization flag to False.\n\n
        Raises:
            Exception: If an error occurs during the initialization process.
        """
        """
        self.asrModel1 = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-xvect-voxceleb", savedir="tmpdir")
        self.asrModel2 = SpeakerRecognition.from_hparams(source="speechbrain/asr-wav2vec2-libri",    savedir="tmpdir")
        """
        try:
            self.__parseConfiguration()
        
            self.LOGGER.info("[HearingSense]::[initialize]")
            self.__initialize_speech_to_text()
            self.__initialize_speech_recognizer()

            self.is_process_initialized = True
        except Exception as e:
            self.LOGGER.error("[HearingSense]::[initialize] => Error during initialization: %s", e, exc_info=True)
            self.is_process_initialized = False


    #- [CONCRETIZATION OF ABSTRACT METHODS SPECIFIC TO THIS CLASS]
    #--------------------------------------------------------------------------------------------------
    async def elaboration(self):
        """
        Main elaboration logic for NeuralProcess.
        """
        try:
            self.LOGGER.info("Starting neural process elaboration.")
            self._am_i_active = True

            # Step 1: Process Inputs
            _ = await self.processInputs()

            # Step 2: Execute Inference
            _ = await self.execute_inference()

            # Step 3: Handle Outputs
            _ = await self.handle_outputs()

            self.LOGGER.info("Neural process elaboration completed.")
        except Exception as e:
            self.LOGGER.error(f"Error during neural process elaboration: {e}")
            raise e

    async def processInputs(self):
        """
        Processes input data and prepares it for neural network inference.
        """
        # Passo 1: Registra l'audio
        _ = await self.__record_audio()

        # Passo 2: Identifica lo speaker
        identifiedSpeaker_id = self.__identify_speaker(self.conf_input_audio_sensor_output_path)

        # Passo 3: Verifica se lo speaker è già riconosciuto
        if identifiedSpeaker_id in self.speaker_db:
            self.LOGGER.info("[HearingSense]::[processInputs] => Speaker %s recognized. Proceeding with audio transcription...", identifiedSpeaker_id)
            transcription = await self.__transcribe_audio()
            return transcription
        else:
            self.LOGGER.info("[HearingSense]::[processInputs] => Speaker %s not recognized. Audio ignored.", identifiedSpeaker_id)
            return None

    async def execute_inference(self):
        """
        Executes the neural network inference using the processed inputs.
        This method must be implemented by the subclasses.
        """
        print("execute_inference")        
        pass

    async def handle_outputs(self):
        """
        Handles the output data generated by the neural network inference.
        This method must be implemented by the subclasses.
        """
        print("handle_outputs")           
        pass

    def __parseConfiguration(self):
        """
        Parses the configuration from the 'config.yaml' file and sets the corresponding attributes.
        This method reads various configuration parameters related to recording, speech recognition, 
        and speech-to-text functionalities. It also logs the configuration details for debugging purposes.\n\n
        Attributes:
            conf_input_audio_sensor_index (int):.................... Index of the input audio sensor.
            conf_input_audio_sensor_format (str):................... Format of the input audio sensor bits.
            conf_input_audio_sensor_channels (int):................. Number of channels of the input audio sensor.
            conf_input_audio_sensor_rate (int):..................... Rate of the input audio sensor.
            conf_input_audio_sensor_chunk (int):.................... Chunk size of the input audio sensor.
            conf_input_audio_sensor_max_record_duration (int):...... Maximum record duration of the input audio sensor.
            conf_input_audio_sensor_output_path (str):.............. Output path for the input audio sensor recordings.
            conf_speech_recognitiion_energy_threshold (float):...... Energy threshold for speech recognition.
            conf_speech_recognitiion_dyn_energy_threshold (bool):... Dynamic energy threshold for speech recognition.
            conf_speech_recognitiion_dyn_energy_adj_damping (float): Dynamic energy adjustment damping for speech recognition.
            conf_speech_recognitiion_dyn_energy_ratio (float):...... Dynamic energy ratio for speech recognition.
            conf_speech_recognitiion_pause_threshold (float):....... Pause threshold for speech recognition.
            conf_speech_recognitiion_operation_timeout (float):..... Operation timeout for speech recognition.
            STT_MODEL_NAME (str):................................... Name of the speech-to-text model.
        Logs:
            Logs the configuration details including input audio sensor parameters, speech recognition parameters, 
            and speech-to-text model name.
        Raises:
            ValueError: If the input audio sensor index is not set in the configuration file.
        """
        try: 
            #----------------------------
            #- Recording parameters
            #----------------------------
            self.conf_input_audio_sensor_index                   = self.getConfigValue("input_audio_sensor", "input_audio_sensor_index")
            self.conf_input_audio_sensor_format                  = self.getConfigValue("input_audio_sensor", "input_audio_sensor_bits_format")
            self.conf_input_audio_sensor_channels                = self.getConfigValue("input_audio_sensor", "input_audio_sensor_channels")
            self.conf_input_audio_sensor_rate                    = self.getConfigValue("input_audio_sensor", "input_audio_sensor_rate")
            self.conf_input_audio_sensor_chunk                   = self.getConfigValue("input_audio_sensor", "input_audio_sensor_chunk")
            self.conf_input_audio_sensor_max_record_duration     = self.getConfigValue("input_audio_sensor", "input_audio_sensor_max_record_duration")
            self.conf_input_audio_sensor_output_path             = os.path.join(self.external_stimuli_directory, "Audible\\", (self.getConfigValue("input_audio_sensor", "input_audio_sensor_output_path")))
            #------------------------------------        
            #- Speech Recognition parameters
            #------------------------------------
            self.conf_speech_recognitiion_energy_threshold       = self.getConfigValue("speech_recognition", "energy_threshold")
            self.conf_speech_recognitiion_dyn_energy_threshold   = self.getConfigValue("speech_recognition", "dynamic_energy_threshold")
            self.conf_speech_recognitiion_dyn_energy_adj_damping = self.getConfigValue("speech_recognition", "dynamic_energy_adjustment_damping")
            self.conf_speech_recognitiion_dyn_energy_ratio       = self.getConfigValue("speech_recognition", "dynamic_energy_ratio")
            self.conf_speech_recognitiion_pause_threshold        = self.getConfigValue("speech_recognition", "pause_threshold")
            self.conf_speech_recognitiion_operation_timeout      = self.getConfigValue("speech_recognition", "operation_timeout")
            #--------------------------------        
            #- Speech To Text parameters
            #--------------------------------
            self.STT_MODEL_NAME                                  = self.getConfigValue("transcription", "whisper_model_name")
            #-------------------------------------        
            #- Selected input audio device name
            #-------------------------------------
            if self.conf_input_audio_sensor_index is None:
                self.LOGGER.error("[HearingEngine] => No INPUT_AUDIO_SENSOR_INDEX configuration parameter has been setted in the config.yaml file. Please provide it and retry!")
                return
            self._selected_input_audio_device_info                              = InputAudioDevices.getDeviceInfos(self.conf_input_audio_sensor_index)

            self.LOGGER.info("[HearingEngine]::[parseConfiguration] => reading   '%s'", self.config_path)        
            self.LOGGER.debug("    ├ INPUT AUDIO SENSOR::INDEX:.................  %s" , self.conf_input_audio_sensor_index)
            self.LOGGER.debug("    ├ INPUT AUDIO SENSOR::NAME::................. '%s'", self._selected_input_audio_device_info['name'] )          
            self.LOGGER.debug("    ├ INPUT AUDIO SENSOR::FORMAT::...............  %s" , self.conf_input_audio_sensor_format)
            self.LOGGER.debug("    ├ INPUT AUDIO SENSOR::CHANNELS:..............  %s" , self.conf_input_audio_sensor_channels)
            self.LOGGER.debug("    ├ INPUT AUDIO SENSOR::RATE:..................  %s" , self.conf_input_audio_sensor_rate)
            self.LOGGER.debug("    ├ INPUT AUDIO SENSOR::CHUNK:.................  %s" , self.conf_input_audio_sensor_chunk)
            self.LOGGER.debug("    ├ INPUT AUDIO SENSOR::MAX_RECORD_DURATION:...  %s" , self.conf_input_audio_sensor_max_record_duration)
            self.LOGGER.debug("    ├ INPUT AUDIO SENSOR::OUTPUT_PATH:........... '%s'", self.conf_input_audio_sensor_output_path)
            self.LOGGER.debug("    ├ STT_MODEL::NAME:........................... '%s'", self.STT_MODEL_NAME)
            self.LOGGER.debug("    ├ SPEECH RECOGNITION::ENERGY_THRESHOLD:......  %s" , self.conf_speech_recognitiion_energy_threshold)
            self.LOGGER.debug("    ├ SPEECH RECOGNITION::DYN_ENERGY_THRESHOLD:..  %s" , self.conf_speech_recognitiion_dyn_energy_threshold)
            self.LOGGER.debug("    ├ SPEECH RECOGNITION::DYN_ENERGY_ADJ_DAMPING:  %s" , self.conf_speech_recognitiion_dyn_energy_adj_damping)
            self.LOGGER.debug("    ├ SPEECH RECOGNITION::DYN_ENERGY_RATIO:......  %s" , self.conf_speech_recognitiion_dyn_energy_ratio)
            self.LOGGER.debug("    ├ SPEECH RECOGNITION::PAUSE_THRESHOLD:.......  %s" , self.conf_speech_recognitiion_pause_threshold)
            self.LOGGER.debug("    ├ SPEECH RECOGNITION::OPERATION_TIMEOUT:.....  %s" , self.conf_speech_recognitiion_operation_timeout)
        except Exception as e:
            raise RuntimeError(f"\n[self.class_name]::[__parseConfiguration] => {e}")
        
    def __initialize_speech_to_text(self):
        """
        """
        self.LOGGER.info("    ├──> Initializing STT Whisper model '%s'....", self.STT_MODEL_NAME)
        self.LOGGER.info("    ├──> Initializing the selected INPUT AUDIO SENSOR....(%s)", self._selected_input_audio_device_info['name'])        
        try:
            self.STT_MODEL = whisper.load_model(self.STT_MODEL_NAME, device="cpu")
            self.conf_input_audio_sensor = pyaudio.PyAudio()
        except Exception as e:
            self.LOGGER.error("    └──> [ERROR] %s", e, exc_info=True)

    def __initialize_speech_recognizer(self):
        """
        """        
        #- SPEECH RECOGNIZER INITIALIZATION
        #----------------------------------
        try:
            self.LOGGER.info("    ├──> Initializing the speech recognizer....Please wait.")        
            self._speech_recognizer = SpeechRecognition.Recognizer()
        except Exception as e:
            self.LOGGER.error("        └──> [ERROR] %s", e, exc_info=True)
        
        try:
            self.LOGGER.info("    ├──> Calibrating hearing sense from microphone...Please wait.")
            with SpeechRecognition.Microphone(device_index=self.conf_input_audio_sensor_index) as source:
                # listen for 5 seconds and calculate the ambient noise energy level
                self._speech_recognizer.adjust_for_ambient_noise(source, duration=1)
        except Exception as e:
            self.LOGGER.error("        └──> [ERROR] %s", e, exc_info=True)
    
    def __identify_speaker(self, audioStimuli:str = None):
        """ 
        Metodo da utilizzare per identificare il parlante dall'audio.
        """
    
        # TODO: Logica per identificare lo speaker (placeholder)
        # Supponiamo che restituisca un ID speaker
        return "001"
    
    async def __record_audio(self):
        """
        Records the input audio and saves it to a file.
        """
        self.LOGGER.info("[HearingEngine]::[__record_audio]")
        try:
            try:
                # Open the audio stream with the selected device.
                self._STREAM = self.conf_input_audio_sensor.open(format             = self.conf_input_audio_sensor_format,
                                                                 channels           = self.conf_input_audio_sensor_channels,
                                                                 rate               = self.conf_input_audio_sensor_rate,
                                                                 input              = True,
                                                                 input_device_index = self.conf_input_audio_sensor_index,
                                                                 frames_per_buffer  = self.conf_input_audio_sensor_chunk)
            except Exception as e:
                self.LOGGER.error("    └──> [ERROR]  Error opening the input audio stream: %s", e)
                return

            my_speechRecognizer = SpeechRecognition.Recognizer()
            my_speechRecognizer.energy_threshold                  = self.conf_speech_recognitiion_energy_threshold
            my_speechRecognizer.dynamic_energy_threshold          = self.conf_speech_recognitiion_dyn_energy_threshold
            my_speechRecognizer.dynamic_energy_adjustment_damping = self.conf_speech_recognitiion_dyn_energy_adj_damping
            my_speechRecognizer.dynamic_energy_ratio              = self.conf_speech_recognitiion_dyn_energy_ratio
            my_speechRecognizer.pause_threshold                   = self.conf_speech_recognitiion_pause_threshold
            my_speechRecognizer.operation_timeout                 = self.conf_speech_recognitiion_operation_timeout
            self.LOGGER.info("    ├    ├──> Device ID:......................... %s", self.conf_input_audio_sensor_index)
            self.LOGGER.info("    ├    ├──> Selected device:................... %s", self._selected_input_audio_device_info['name'])
            self.LOGGER.info("    ├    ├──> Input channels:.................... %s", self._selected_input_audio_device_info['maxInputChannels'])
            self.LOGGER.info("    ├    ├──> Supported sampling rate:........... %s", self._selected_input_audio_device_info['defaultSampleRate'])
            self.LOGGER.info("    ├    ├──> Energy threshold:.................. %s", my_speechRecognizer.energy_threshold)
            self.LOGGER.info("    ├    ├──> Dynamic energy threshold:.......... %s", my_speechRecognizer.dynamic_energy_threshold)
            self.LOGGER.info("    ├    ├──> Dynamic energy adjustment damping:. %s", my_speechRecognizer.dynamic_energy_adjustment_damping)
            self.LOGGER.info("    ├    ├──> Dynamic energy ratio:.............. %s", my_speechRecognizer.dynamic_energy_ratio)
            self.LOGGER.info("    ├    ├──> Pause threshold:................... %s", my_speechRecognizer.pause_threshold)
            self.LOGGER.info("    ├    └──> Operation timeout:................. %s", my_speechRecognizer.operation_timeout)
            
            # Use the microphone as the audio source
            with SpeechRecognition.Microphone() as source:

                self.LOGGER.info("    ├──> Input audio recording...")
                try:

                    # Option to reduce background noise
                    my_speechRecognizer.adjust_for_ambient_noise(source, duration=1)                 
                    
                    self.LOGGER.info("    ├    ├──> Noise reduction active...")
                    audio = my_speechRecognizer.listen(source, timeout=10)  # Timeout dopo 10 secondi
                    self.LOGGER.info("    ├    └──> Input audio recording completeted.")

                    # Salva l'audio in un file WAV
                    with open(self.conf_input_audio_sensor_output_path, "wb") as f:
                         f.write(audio.get_wav_data())

                         self.LOGGER.info("    └──> Input audio saved as '%s'.", self.conf_input_audio_sensor_output_path)

                except Exception as e:
                    self.LOGGER.error("    └──> [ERROR] Error occurred during the outcoming sound recording: %s", e)

            # Opzionale: Riproduci l'audio registrato
            audio = AudioSegment.from_file(self.conf_input_audio_sensor_output_path, format="wav")
            play(audio)

        except KeyboardInterrupt:
            print("[INFO] Manual interruption during incoming audio recording.")
            raise
        except Exception as e:
            self.LOGGER.error("[ERROR][HearingEngine]::[__record_audio] => Error during input audio recording: %s", e)
    
    async def __transcribe_audio(self):
        """
        Transcribes the recorded audio file using the Whisper model.
        """
        if not os.path.exists(self.conf_input_audio_sensor_output_path):
            self.LOGGER.error("[HearingSense] => Audio file '%s' does not exist.", self.conf_input_audio_sensor_output_path)
            return None
        try:
            self.LOGGER.info("[HearingSense] => Transcribing audio file '%s'...", self.conf_input_audio_sensor_output_path)
            my_transcription_result = self.STT_MODEL.transcribe(self.conf_input_audio_sensor_output_path, fp16=False)
            my_transcription_text = my_transcription_result['text']
            self.LOGGER.info("[HearingSense] => Transcription completed: %s", my_transcription_text)
            return my_transcription_text
        except Exception as e:
            self.LOGGER.error("Error during transcription: %s", e)
            return None   
    
    def sleep(self):
        self.am_i_active = False