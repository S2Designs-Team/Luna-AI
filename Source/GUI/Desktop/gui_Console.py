import logging
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import cv2  # OpenCV per il video stream
from AssetsLibs.Helpers.LogManager.lib_LogManager import LoggerManager

class LunaApp:
    def __init__(self, gui_root, logger: LoggerManager = None):
        self.root = gui_root
        self.logger = logger
        self.root.title("Luna-AI Console")
        self.root.geometry("800x600")

        # Frame principale per la gestione del layout
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame per la webcam a destra
        self.video_frame = tk.Frame(self.main_frame, width=400, height=480)
        self.video_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # Canvas per il video stream della webcam
        self.canvas = tk.Canvas(self.video_frame, width=640, height=480)
        self.canvas.pack()

        # Frame per la chat e i comandi sulla sinistra
        self.chat_frame = tk.Frame(self.main_frame)
        self.chat_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

        # Area per l'input dell'utente (Entry)
        self.command_area = tk.Entry(self.chat_frame, width=80)
        self.command_area.grid(row=0, column=0, padx=10, pady=10)
        self.command_area.bind("<Return>", self.handle_command)

        # Area dei log (ScrolledText) nella parte inferiore della finestra
        self.log_area = scrolledtext.ScrolledText(self.chat_frame, width=100, height=20, wrap=tk.WORD, state=tk.DISABLED)
        self.log_area.grid(row=1, column=0, padx=10, pady=10)

        # Inizializza il video capture (webcam)
        self.cap = cv2.VideoCapture(0)
        
        if not self.cap.isOpened():
            self.log("Errore nell'aprire la webcam.")
        else:
            self.log("Webcam aperta correttamente.")
        
        self.update_video()

        # Registra la GUI come consumer dei log
        self.logger.add_consumer(self.log, logging.DEBUG)

        # Variabili di stato
        self.running = False

    def log(self, message):
        """Visualizza i messaggi nei log di LUNA"""
        self.root.after(0, self._update_log_area, message)

    def _update_log_area(self, message):
        """Metodo per aggiornare l'area di log nella GUI"""
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.yview(tk.END)
        self.log_area.config(state=tk.DISABLED)

    def handle_command(self, event):
        """Gestisce il comando inserito dall'utente"""
        user_input = self.command_area.get().strip()
        if user_input.lower() == "[exit]":
            self.stop_luna()
        elif user_input.lower() == "help":
            self.log("Comandi disponibili:\n[exit] - Per uscire dall'app\nhelp - Mostra questo messaggio di aiuto")
        else:
            # Risposta automatica per qualsiasi comando
            self.log(f"User: {user_input}")
            self.log("Luna: Non sono ancora programmata per rispondere a questo comando, ma sto imparando!")
        self.command_area.delete(0, tk.END)

    def stop_luna(self):
        """Ferma e chiude l'applicazione"""
        self.log("Luna AI is going to be turned off...")
        self.running = False
        self.cap.release()  # Rilascia la webcam
        self.root.quit()     # Termina il mainloop
        self.root.destroy()  # Chiude la finestra

    def startGui(self):
        """Avvia l'applicazione GUI"""
        self.log("Welcome in Luna AI. Write 'help' to show all the available commands.")
        self.root.mainloop()

    def update_video(self):
        """Acquisisce e visualizza i fotogrammi dalla webcam"""
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Converti il frame da BGR a RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Converti il frame in un formato compatibile con Tkinter
                img = Image.fromarray(frame_rgb)
                img_tk = ImageTk.PhotoImage(image=img)
                
                # Visualizza l'immagine sulla canvas
                self.canvas.create_image(0, 0, image=img_tk, anchor=tk.NW)
                self.canvas.image = img_tk  # Salva il riferimento all'immagine per evitare che venga distrutta
                self.root.after(10, self.update_video)  # Richiama la funzione ogni 10ms
            else:
                self.log("Errore nel leggere il fotogramma dalla webcam.")
        else:
            self.log("La webcam non è stata inizializzata correttamente.")

# Esegui l'app
if __name__ == "__main__":
    root = tk.Tk()
    # Qui, il logger viene passato come parametro
    logger = LoggerManager()  # Assicurati che il logger venga passato correttamente
    app = LunaApp(root, logger)
    app.startGui()