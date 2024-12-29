# Luna_AI_main.py
import logging
import tkinter as tk
from tkinter import scrolledtext

from AssetsLibs.Helpers.LogManager.lib_LogManager import LoggerManager

class LunaApp:
    def __init__(self, root, logger:LoggerManager = None):
        self.root = root
        self.logger = logger
        self.root.title("Luna-AI Console")
        self.root.geometry("800x600")

        # Area dei log di LUNA (ScrolledText)
        self.log_area = scrolledtext.ScrolledText(self.root, width=100, height=20, wrap=tk.WORD, state=tk.DISABLED)
        self.log_area.grid(row=0, column=0, padx=10, pady=10)

        # Area per l'input dell'utente (Entry)
        self.command_area = tk.Entry(self.root, width=80)
        self.command_area.grid(row=1, column=0, padx=10, pady=10)
        self.command_area.bind("<Return>", self.handle_command)
       
        # Registra la GUI come consumer dei log
        self.logger.add_consumer(self.log, logging.DEBUG)

        # Variabili di stato
        self.running = False

    def log(self, message):
        """Visualizza i messaggi nei log di LUNA"""
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

    def stopGui(self):
        """
        Stops and closes the Application GUI.
        """
        self.log("Luna AI is going to be turned off...")
        self.running = False
        self.root.quit()     # Termnate the mainloop
        self.root.destroy()  # Close the windows

    def startGui(self):
        """
        Starts the Application GUI.
        """
        self.log("Welcome in Luna AI. Write 'help' to show all the available commands.")
        self.root.mainloop()

# Esegui l'app
if __name__ == "__main__":
    root = tk.Tk()
    app = LunaApp(root)
    app.start_luna()