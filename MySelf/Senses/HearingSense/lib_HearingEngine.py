# import webrtcvad
import asyncio
import sys
from pathlib import Path
# Aggiunge la directory principale del progetto al sys.path
sys.path.append(str(Path(__file__).parent.parent.parent))

import os
import json
import whisper
from datetime import datetime

from AssetsLibs.Abstraction.lib_NeuralProcess           import ANeuralProcess

class HearingEngine(ANeuralProcess):
    def __init__(self, senseName="HearingSense"):
                                             # Determina la directory corrente dello script
        super().__init__()
    
        self.script_name      = __name__
        self.script_directory = Path(os.path.dirname(__file__)).resolve()
        self.script_path      = Path(os.path.join(self.script_directory, self.script_name)).resolve()
        print(f"Hear_Engine => DEBUG: PERCORSO DELLO SCRIPT = {self.script_path}.")
        print(f"Hear_Engine => DEBUG: PERCORSO DELLA CONFIGURAZIONE = {self.config_path}.")
    
        # Carica la configurazione
        self.configuration          = self._loadConfiguration()                                   # Carica il file config.yaml dalla propria directory
        self.audio_settings         = self.configuration["audio_settings"]
        self.transcription_settings = self.configuration["transcription"]
        self.speaker_settings       = self.configuration["speaker_recognition"]
        self.model                  = None
        # self.vad                    = webrtcvad.Vad()
        #self.vad.set_mode(self.audio_settings["vad_mode"])

    async def initialize(self):
        """Inizializza il motore di Speech-to-Text."""

        print("Modello Whisper caricato correttamente!")
        print("Hear_Engine => SpeechToTextEngine: Caricamento modello Whisper...")
        self.model = whisper.load_model(self.transcription_settings["whisper_model"])
        print("Hear_Engine => SpeechToTextEngine: initialized.")

    def identify_speaker(self, audioStimuli):
        """ Metodo fittizio per identificare il parlante dall'audio.
            Deve essere implementato utilizzando un sistema di riconoscimento vocale."""
        
        # TODO: Logica per identificare lo speaker (placeholder)
        # Supponiamo che restituisca un ID speaker
        return "001"        
    
    async def handleSelfStimuli(self, message):
        """Elabora audio simulando l'udito."""

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
    
    async def handleExternalStimuli(self, message):
        """Elabora audio simulando l'udito."""

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