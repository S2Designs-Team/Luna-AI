# INTRODUZIONE:
Ti sei mai chiesto come fa Siri a riconoscere le parole che dici? O il fatto che Spotify sappia di che genere è una canzone 
senza che venga menzionato da nessuna parte.
<BR>
Tutto questo è possibile grazie all'Analisi Audio :)
<BR>
In questo documento verranno esaminati alcuni aspetti importanti dell'analisi audio e degli strumenti utilizzati per fare lo 
stesso.
<BR>

<BR>

# Introduzione all'analisi audio
L'analisi audio è il processo di elaborazione dei segnali audio per estrarre informazioni vitali, consentendo un'ampia gamma di 
applicazioni, dalla classificazione dei generi musicali al riconoscimento vocale, dall'identificazione dei suoni ambientali al 
rilevamento delle emozioni nella voce.
<BR>

In questo caso, sfruttando le solide librerie di Python come Librosa, possiamo elaborare e analizzare in modo efficiente i dati
audio, trasformando il suono grezzo in informazioni fruibili.
<BR>

# Impostazione dell'ambiente
Per iniziare a usare Librosa puoi usare il seguente comando pip per installare librosa nel tuo attuale ambiente Python.
```console
pip install librosa
```

# Nozioni di base di Librosa
Diamo un'occhiata veloce ad alcune delle caratteristiche più importanti di Librosa che lo rendono così utile per varie attività 
di analisi audio.

    - Conversioni nel dominio del tempo e della frequenza
    - Caratteristiche spettrali
    - Monitoraggio del tempo e del beat
    - Strumenti di visualizzazione

Per saperne di più consulta la [documentazione ufficiale di Librosa](https://librosa.org/doc/latest/index.html)

# Caricamento e visualizzazione audio
Andiamo subito al dunque, va bene?<BR>
Come si carica un file audio utilizzando librosa?                                                                                <BR>
```console
audio_path = 'your_audio_file.wav'
 y, sr = librosa.load (audio_path)
 ```

 Qui 'y' rappresenta i dati della serie temporale audio che sono array numpy 1D. Contiene i valori di ampiezza del segnale audio.<BR>
 Ogni elemento corrisponde a un campione della forma d'onda audio

 'sr' rappresenta la frequenza di campionamento per il file audio.                                                               <BR>
 La frequenza di campionamento indica quanti campioni al secondo sono contenuti nel file audio.