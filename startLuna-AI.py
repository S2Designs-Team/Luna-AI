# Luna_AI_main.py
import datetime
import tracemalloc
import os
import asyncio
import sys

from AssetsLibs.Helpers.EnvironmentInfo.GPU.lib_GPU_Info import GPUInfo
from MySelf.lib_MySelf import MySelf

# Starts the monitoring of the memory allocation
tracemalloc.start()

async def main():
    """
    Main async function that initializes and manages the main loop.
    """
    print("╔═════════════════════════════════════════════════════════════════════════════╗")
    print("║ Welcome to Luna-AI project!                                                 ║")
    print("╚═════════════════════════════════════════════════════════════════════════════╝")  
 
    # Utilizza GPUInfo per ottenere il dispositivo
    my_process_unit_device = GPUInfo.check_gpu_availability()    
    
    LUNA = MySelf()
    _ = await LUNA.async_init()
    _ = await LUNA.wakeUp()

    # Starts the continuous memory allocation monitoring
    my_monitor_task = asyncio.create_task(monitor_current_memory())

    try:
        # Simulates some other async operations just to test the monitoring
        await asyncio.sleep(10)  # Time to test the monitoring
    finally:
        my_monitor_task.cancel()
        try:
            await my_monitor_task
        except asyncio.CancelledError:
            print("Memory monitor coroutine has been cancelled.")

def handle_mode(mode):
    """
    Handles the execution mode based on starting call arguments.
    """
    match mode:
        case "console":
            run_console()
        case "gui":
            run_gui()
        case "help":
            show_command_help()
        case _:
            print("Parameter(s) not valid. Use 'gui' to start Luna in Graphic Interfaced Mode or 'console' for the Console Mode.")
            sys.exit(1)

def run_console():
    """
    Console mode: lets the user to type commands directly from the terminal.
    """
    print("Console Mode...started.")
    try:
        while True:
            my_user_input = input("Insert a command (or '[exit]' to terminate): ")
            if my_user_input.lower() == "[exit]":
                print("The console mode is going to be closed.")
                break
            else:
                print(f"You've wrote: {my_user_input}")
    except KeyboardInterrupt:
        print("\nConsole mode interrupted by user.")                

def run_gui():
    """
    GUI mode: starts a graphic user interface (if supported).
    """      
    try:
        print("Graphic Interfaced Mode...started.")
    except ImportError:
        print("Error: tkinter not installed.")

def show_command_help():
    """
    Shows the instructions to correctly use this script.
    """    
    print("Usage Help: python startLunaAI.py [gui|console]")

async def monitor_current_memory():
    """
    Monitoring of the memory by using tracemalloc and display of statistics.
    """    
    try:
        while True:
            my_current_snapshot     = tracemalloc.take_snapshot()
            my_current_memory_stats = my_current_snapshot.statistics('lineno')
            print("\n[ Memory usage update ]")

            for my_processed_top_memory_stat in my_current_memory_stats[:5]:
                print(my_processed_top_memory_stat)

            await asyncio.sleep(5)  # Checks memory allocation each 5 seconds

    except asyncio.CancelledError:
        print("Memory monitor coroutine has been cancelled.")
    except Exception as monitor_current_memory_exeption:
        print(f"An error occurred in monitor_current_memory: {monitor_current_memory_exeption}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(sys.argv) != 2:
        print("Usage Help: python startLunaAI.py [gui|console]")
        sys.exit(1)

    par_mode = sys.argv[1].lower()
    
    try:
        asyncio.run(main())
        handle_mode(par_mode)
        
    except Exception as app_exception:
        print(f"An unexpected error occurred: {app_exception}")
    finally:
        # AT the end (before the exit execution has been completed), takes a snapshot of tracemalloc
        my_final_snapshot     = tracemalloc.take_snapshot()
        my_final_memory_stats = my_final_snapshot.statistics('lineno')
        my_timestamp          = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        my_dump_file_path     = os.path.join("DevTools", "TraceMAlloc_dumps", f"[{my_timestamp}] LunaTraceMAlloc.pkl")        
        my_final_snapshot.dump(my_dump_file_path)

        print("\n[ Top 10 memory allocation ]")
        for my_processed_top_final_memory_stat in my_final_memory_stats[:10]:
            print(my_processed_top_final_memory_stat)

