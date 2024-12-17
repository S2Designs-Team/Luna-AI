# HearEngine (Simulates the Hearing sense)

## Cosa fa il codice:

### Registrazione audio: 
Il metodo record_audio attiva il microfono e salva i dati audio in un file WAV. E' possibile regolare la durata della registrazione tramite il parametro duration definito nel file di configurazione ".\config.yaml"



### Identificazione dello speaker: 
Dopo aver registrato l'audio, il metodo identify_speaker simula un processo di riconoscimento vocale. Se lo speaker è già stato registrato, il sistema prosegue con la trascrizione dell'audio.<BR>



### Elaborazione e trascrizione: 
Se lo speaker è riconosciuto, il file audio viene passato al metodo HandleSelfStimuli che utilizza il modello Whisper per trascrivere il testo.
Gestione stimoli esterni: Il metodo HandleExternalStimuli richiama la registrazione dell'audio, identifica lo speaker e, se lo speaker è già stato riconosciuto, chiama HandleSelfStimuli per la trascrizione.<BR>



## Considerazioni:
Il riconoscimento dello speaker è ancora un placeholder e deve essere implementato con un sistema di riconoscimento vocale (ad esempio, tramite modelli di speaker recognition come pyAudio o SpeechBrain).
L'audio viene registrato per una durata definita da INPUT_AUDIO_SENSOR_MAX_RECORD_DURATION (default 5 secondi).
Whisper processa i file WAV e restituisce una trascrizione.