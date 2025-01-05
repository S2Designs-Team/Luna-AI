# Implemented Features

## Model Loading:

Allows selecting the Whisper model from the available versions (e.g., base, small, medium, large).  
Automatically configures the device (CPU or GPU) based on availability.

## Transcription from Audio Files:

Supports transcription of local audio files.  
Automatically suppresses silent sections if configured.

## Transcription from Audio Arrays:

Enables transcription directly from a NumPy array containing audio data.

## Language Detection:

Analyzes the audio to determine the spoken language.

## Usage example:
```python
from AssetsLibs.TextProcessing.lib_WhisperWrapper import WhisperWrapper

# Inizializza il wrapper per il modello Whisper
whisper_wrapper = WhisperWrapper(model_name="base")

# Percorso del file audio da trascrivere
audio_path = "sample_audio.wav"

# Trascrizione
transcription = whisper_wrapper.transcribe(audio_path, language="en")
print("Trascrizione:", transcription)

# Rilevamento della lingua
detected_language = whisper_wrapper.detect_language(audio_path)
print("Lingua rilevata:", detected_language)
```
