# Luna_AI_main.py
import datetime
import tracemalloc
import os
import asyncio
import sys

import tkinter as tk
from tkinter import scrolledtext
import multiprocessing

class LunaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Luna-AI Console")
        self.root.geometry("800x600")

        # Area dei log di LUNA (ScrolledText)
        self.log_area = scrolledtext.ScrolledText(self.root, width=100, height=20, wrap=tk.WORD, state=tk.DISABLED)
        self.log_area.grid(row=0, column=0, padx=10, pady=10)

        # Area per l'input dell'utente (Entry)
        self.command_area = tk.Entry(self.root, width=80)
        self.command_area.grid(row=1, column=0, padx=10, pady=10)
        self.command_area.bind("<Return>", self.handle_command)

        # Variabili di stato
        self.LUNA = None
        self.running = False

        # Avvio della memoria tracemalloc
        tracemalloc.start()

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
        else:
            self.log(f"User: {user_input}")
        self.command_area.delete(0, tk.END)

    def stop_luna(self):
        """Ferma LUNA e chiude l'applicazione"""
        if self.LUNA:
            self.LUNA.am_i_active = False  # Termina il ciclo di LUNA
            self.log("Stopping LUNA...")
        self.root.quit()

    def start_luna(self):
        """Avvia il processo di LUNA"""
        self.LUNA = MySelf()
        asyncio.run(self.run_luna())

    async def run_luna(self):
        """Esegui il ciclo di vita di LUNA"""
        self.running = True
        try:
            self.log("Initializing LUNA...")
            await self.LUNA.async_init()
            await self.LUNA.wakeUp()

            # Simuliamo il processo di LUNA
            while self.running:
                await asyncio.sleep(1)
                # Logica di aggiornamento LUNA (simulata per ora)
                self.log("LUNA is processing...")
        except Exception as e:
            self.log(f"Error occurred: {e}")
        finally:
            self.LUNA.TurnOff()
            self.log("LUNA has been turned off.")