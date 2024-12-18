# Luna_AI_main.py
import tracemalloc
import os
import asyncio
import sys

from MySelf.lib_MySelf import MySelf

# Starts the monitoring of the memory allocation
tracemalloc.start()

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


async def monitor_memory():
    while True:
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')
        print("\n[ Memory usage update ]")
        for stat in top_stats[:5]:
            print(stat)
        await asyncio.sleep(5)  # Controlla la memoria ogni 5 secondi


async def main():
    # Avvia il monitoraggio continuo della memoria
    asyncio.create_task(monitor_memory())

    # Qui inizieremo a sviluppare le funzionalità del progetto
    LUNA = MySelf()
    LUNA.turnOn()
    _ = await LUNA.wakeUp()
    pass

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("╔═════════════════════════════════════════════════════════════════════════════╗")
    print("║ Benvenuto nel progetto Luna-AI!                                             ║")
    print("╚═════════════════════════════════════════════════════════════════════════════╝")

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

    # Al termine del programma, prendi uno snapshot di tracemalloc
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    snapshot.dump(".\\DevTools\\TraceMAlloc_dumps\\LunaTraceMAlloc.pkl")

    print("\n[ Top 10 memory allocation ]")
    for stat in top_stats[:100]:
        print(stat)

