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
from AssetsLibs.Helpers.Configuration.lib_Configuration import loadConfiguration



class HearingEngine(ANeuralProcess):
    def __init__(self, senseName):
        self.script_path = Path(__file__).parent.resolve()            # Determina la directory corrente dello script
        super().__init__()
        config_path = self.script_path / "config.yaml"                # Percorso del file di configurazione

        if not config_path.exists(): raise FileNotFoundError(f"File di configurazione non trovato: {config_path}")

        # Carica la configurazione
        self.config                 = loadConfiguration(self.script_dir)  # Carica il file config.yaml dalla propria directory
        self.audio_settings         = self.config["audio_settings"]
        self.transcription_settings = self.config["transcription"]
        self.speaker_settings       = self.config["speaker_recognition"]
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
    
    # async def wakeUp(self):
    #    """
    #    Attiva il Processo Neurale e fa partire il thread della propria logica
    #    (definita nella classe concreta all'interno del metodo handleStimuli).
    #    """
    #    self.logger.info(f"[{self.__class__.__name__}] Avvio del Processo Neurale...")

    #    if self._am_i_active:
    #        raise RuntimeError("Il Processo Neurale è già attivo.")
         
        # Metodo astratto implementato dalla classe concreta
    #    await self.initialize()
    #    self._am_i_active = True

        # Avvia il task asincrono per gestire gli stimoli
    #    self._incomingStimuliEvaluationTask = asyncio.create_task(self._evaluateIncomingStimuli())