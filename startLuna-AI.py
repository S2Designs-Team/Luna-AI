#import asyncio
#from Assets.CognitiveEngines.HearingSense.lib_HearingEngine import HearingEngine
#from BrainLayers.CognitiveLayer.cognitive_layer import CognitiveLayer
#from BrainLayers.EmotionalLayer.emotional_layer import Emotional_Layer

#import whisper

#model = whisper.load_model("base")
#print("Modello Whisper caricato correttamente!")

#async def main():
    #hearingSense = HearingEngine()
    # Crea i vari processi neurali (layer del cervello)
    #cognitive_layer = CognitiveLayer("Sistema cognitivo")
    #emotive_layer   = Emotional_Layer("Sistema emotivo - empatico")

    # Risveglia i processi neurali
    #hearingSense.wakeUp()
    #await cognitive_layer.wakeUp()
    #await emotive_layer.wakeUp()
    
    # Comunica tra i processi neurali
    #await cognitive_layer.send_stimulus("Messaggio dalla Corteccia cerebrale")
    #await emotive_layer.send_stimulus("Messaggio dal Sistema limbico")

    # Attendere che i processi lavorino per un po'
    #await asyncio.sleep(5)

    # Mette a riposo i processi neurali
    #hearingSense.sleep()
    #await cognitive_layer.sleep()
    #await emotive_layer.sleep()

    #print("Tutti i processi neurali sono stati messi a riposo.")

# Avvia la funzione main
#asyncio.run(main())


# Luna_AI_main.py

import asyncio
import sys

from MySelf.Body.lib_Body  import *
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
        print("Errore: tkinter non è installato.")

def showCommandHelp():
    print("Usage Help: python startLunaAI.py [gui|console]")


async def main():
    print("Benvenuto nel progetto Luna-AI!")
    # Qui inizieremo a sviluppare le funzionalità del progetto
    hearingSense = HearingEngine("Udito")
    hearingSense.wakeUp()
    body = Body()
    body.legs.leftLeg
    pass

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage Help: python startLunaAI.py [gui|console]")
        sys.exit(1)
    
    par_guiMode = sys.argv[1].lower()

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

    # asyncio.run(main())