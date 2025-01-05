import whisper
import torch
import librosa

class WhisperWrapper:
    """
    Classe wrapper per il modello Whisper di OpenAI.
    Fornisce funzionalità di trascrizione audio in testo.
    """
    def __init__(self, model_name="base", device=None):
        """
        Inizializza il wrapper per il modello Whisper.

        :param model_name: Nome del modello Whisper (es. "base", "small", "medium", "large").
        :param device: Dispositivo su cui eseguire il modello (es. "cpu" o "cuda").
        """
        self.model_name = model_name
        self.device = device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = whisper.load_model(self.model_name, device=self.device)
        print(f"Modello Whisper '{self.model_name}' caricato su {self.device}.")

    def transcribe(self, audio_path, language="en", suppress_silence=True):
        """
        Trascrive un file audio in testo.

        :param audio_path: Percorso del file audio da trascrivere.
        :param language: Lingua del file audio (es. "en", "it", "es").
        :param suppress_silence: Sopprime la trascrizione di sezioni silenziose.
        :return: Trascrizione in formato stringa.
        """
        try:
            # Caricamento dell'audio e resampling
            audio, sr = librosa.load(audio_path, sr=16000)
            options = {
                "language": language,
                "suppress_silence": suppress_silence,
            }
            # Trascrizione
            result = self.model.transcribe(audio, **options)
            print(f"Trascrizione completata per '{audio_path}'.")
            return result["text"]
        except Exception as e:
            print(f"Errore durante la trascrizione: {e}")
            return None

    def transcribe_audio_array(self, audio_array, language="en", suppress_silence=True):
        """
        Trascrive un array NumPy rappresentante un file audio.

        :param audio_array: Array NumPy contenente i dati audio.
        :param language: Lingua del file audio (es. "en", "it", "es").
        :param suppress_silence: Sopprime la trascrizione di sezioni silenziose.
        :return: Trascrizione in formato stringa.
        """
        try:
            options = {
                "language": language,
                "suppress_silence": suppress_silence,
            }
            result = self.model.transcribe(audio_array, **options)
            print("Trascrizione completata per audio array.")
            return result["text"]
        except Exception as e:
            print(f"Errore durante la trascrizione: {e}")
            return None

    def detect_language(self, audio_path):
        """
        Rileva la lingua di un file audio.

        :param audio_path: Percorso del file audio.
        :return: Codice della lingua rilevata.
        """
        try:
            # Caricamento dell'audio e resampling
            audio, sr = librosa.load(audio_path, sr=16000)
            result = self.model.detect_language(audio)
            language = max(result["language"], key=result["language"].get)
            print(f"Lingua rilevata: {language}")
            return language
        except Exception as e:
            print(f"Errore durante il rilevamento della lingua: {e}")
            return None
