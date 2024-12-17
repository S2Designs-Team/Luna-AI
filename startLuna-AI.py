# Luna_AI_main.py
import os
import asyncio
import sys

from MySelf.Brain  import *
from MySelf.Senses import *
from MySelf.Spine  import *
from MySelf.Senses.HearingSense.lib_HearingEngine import HearingEngine


def run_console():
    print("Console Mode...started.")
    while True:
        user_input = input("Insert a command (or '[exit]' to terminate): ")
        if user_input.lower() == "[exit]":
            print("The console mode is going to be closed.")
            break
        else:
            print(f"You've wrote: {user_input}")

def run_gui():
    try:
        print("Graphic Interfaced Mode...started.")
    except ImportError:
        print("Error: tkinter not installed.")

def showCommandHelp():
    print("Usage Help: python startLunaAI.py [gui|console]")


async def main():
    print("╔═════════════════════════════════════════════════════════════════════════════╗")
    print("║ Benvenuto nel progetto Luna-AI!                                             ║")
    print("╚═════════════════════════════════════════════════════════════════════════════╝")
    
    # Qui inizieremo a sviluppare le funzionalità del progetto
    hearingSense = HearingEngine()
    _ = await hearingSense.wakeUp()
    #body = Body()
    pass

if __name__ == "__main__":
   
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(sys.argv) != 2:
        print("Usage Help: python startLunaAI.py [gui|console]")
        sys.exit(1)
    
    par_guiMode = sys.argv[1].lower()
    asyncio.run(main())

    match par_guiMode:
        case "console":
            run_console()
        case "gui":
            run_gui()
        case "help":
            showCommandHelp()
        case _:
            print("Parameter(s) not valid. Use 'gui' to start Luna in Graphic Interfaced Mode or 'console' for the Console Mode.")
            sys.exit(1)