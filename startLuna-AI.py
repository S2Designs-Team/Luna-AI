# Luna_AI_main.py
import datetime
import threading
import tkinter as tk
import asyncio
import tracemalloc
import sys
import os

from GUI.Desktop.gui_Console import LunaApp
from AssetsLibs.Helpers.LogManager.lib_LogManager import LoggerManager
from AssetsLibs.Helpers.EnvironmentInfo.GPU.lib_GPU_Info import GPUInfo
from MySelf.lib_MySelf import MySelf

# Starts the monitoring of the memory allocation
tracemalloc.start()

# Global termination Event
shutdown_event = asyncio.Event()
# LUNA AI Main Process
Luna_AI_Process:MySelf       = None 
# Centralized Logger
Logger_Manager:LoggerManager = None
# App Global main Tasks
Tasks:list                   = []

Gui_Thread:threading.Thread  = None

async def monitor_current_memory():
    """
    Monitoring of the memory by using tracemalloc and display of statistics.
    """    
    try:
        while True:
            my_current_snapshot     = tracemalloc.take_snapshot()
            my_current_memory_stats = my_current_snapshot.statistics('lineno')
            print("\n[Memory usage update]")

            for my_processed_top_memory_stat in my_current_memory_stats[:5]:
                print(my_processed_top_memory_stat)

            await asyncio.sleep(5)  # Checks memory allocation each 5 seconds
    except Exception as monitor_current_memory_exeption:
        Logger_Manager.info(f"An error occurred in monitor_current_memory: {monitor_current_memory_exeption}")

async def run_luna_gui():
    """
    GUI mode: starts a graphic user interface Tkinter (if supported).
    """      
    try:
        def start_gui():
            main_root = tk.Tk()
            app = LunaApp(main_root, Logger_Manager)
            app.startGui()

        Gui_Thread = threading.Thread(target=start_gui, daemon=True)
        Gui_Thread.start()
        print("Graphic Interfaced Mode...started.")

        # Aspetta la fine del thread GUI per sincronizzarlo con asyncio
        while Gui_Thread.is_alive():
            await asyncio.sleep(0.1)

        print("Graphic Interfaced Mode...started.")
    except ImportError:
        print("Error: tkinter not installed.")
    except Exception as e:
        print(f"Error in run_luna_gui: {e}")

async def run_luna_being():
    """
    Main async function that initializes and manages the main loop.
    """ 
    global Luna_AI_Process
    #Use GPUInfo to retrieve the GPU device"
    #my_process_unit_device = GPUInfo.check_gpu_availability()    

    try:
        Luna_AI_Process = MySelf(Logger_Manager)
        _ = await Luna_AI_Process.async_init()
        await Luna_AI_Process.wakeUp()
    except Exception as app_exception:
        Logger_Manager.error(f"An unexpected error occurred: {app_exception}")
    finally:
        await Luna_AI_Process.turnOff()
        print("Luna has been gracefully turned off.")

async def handle_mode_async(mode):
    """
    Handles the execution mode based on starting call arguments.
    """
    try:
        match mode:
            case "console":
                # Starts the GUI process
                #LunaGUI_process   = multiprocessing.Process(target=run_luna_gui)
                #LunaGUI_process.start()
                #LunaGUI_process.join()
                # Starts the Luna Being process
                #LunaBeing_process = multiprocessing.Process(target=run_luna_being)
                #LunaBeing_process.start()
                #LunaBeing_process.join()
                # Starts the continuous memory allocation monitoring process
                #AppMemory_process = multiprocessing.Process(target=monitor_current_memory)
                #AppMemory_process.start()
                #AppMemory_process.join()
                print ("NOT YET IMPLEMENTED")
            case "gui":
                Tasks.append(asyncio.create_task(run_luna_gui()))
                Tasks.append(asyncio.create_task(run_luna_being()))
                Tasks.append(asyncio.create_task(monitor_current_memory()))
                await asyncio.gather(*Tasks)
            case "help":
                show_command_help()
            case _:
                print("Parameter(s) not valid. Use 'gui' to start Luna in Graphic Interfaced Mode or 'console' for the Console Mode.")
                sys.exit(1)
    except Exception as app_exception:
        Logger_Manager.error(f"An unexpected error occurred: {app_exception}")
    finally:
        for task in Tasks:
            task.cancel()  # Cancels all the tasks                

def show_command_help():
    """
    Shows the instructions to correctly use this script.
    """    
    print("Usage Help: python startLunaAI.py [gui|console]")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    Logger_Manager = LoggerManager()
    Logger_Manager.info("╔═════════════════════════════════════════════════════════════════════════════╗")
    Logger_Manager.info("║ Welcome to Luna-AI project!                                                 ║")
    Logger_Manager.info("╚═════════════════════════════════════════════════════════════════════════════╝") 
    
    if len(sys.argv) != 2:
        Logger_Manager.info("Usage Help: python startLunaAI.py [gui|console|help]")
        sys.exit(1)

    par_mode = sys.argv[1].lower()
    
    try:
        asyncio.run(handle_mode_async(par_mode))

    except KeyboardInterrupt:
        Logger_Manager.info("Manual interruption detected. Closing the program...")

        for task in Tasks:
            task.cancel()  # Properly clear all the tasks.

        # Closing the Gui_Thread if it is running
        if Gui_Thread and Gui_Thread.is_alive():
            Logger_Manager.info("Closing the GUI...")
            tk.Tk().quit()
            Gui_Thread.join()

        if Luna_AI_Process:
            asyncio.run(Luna_AI_Process.turnOff())
            Logger_Manager.info("Luna AI has been gracefully turned off.")

        Logger_Manager.info("All tasks have been cleared.")

    except Exception as app_exception:
        Logger_Manager.error(f"An unexpected error occurred: {app_exception}")

    finally:
        # At the end (before the exit execution has been completed), takes a snapshot of tracemalloc
        my_final_snapshot     = tracemalloc.take_snapshot()
        my_final_memory_stats = my_final_snapshot.statistics('lineno')
        my_timestamp          = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        my_dump_file_path     = os.path.join("DevTools", "TraceMAlloc_dumps", f"[{my_timestamp}] LunaTraceMAlloc.pkl")        
        my_final_snapshot.dump(my_dump_file_path)

        print("\n[ Top 10 memory allocation ]")
        for my_processed_top_final_memory_stat in my_final_memory_stats[:10]:
            print(my_processed_top_final_memory_stat)

        print("[INFO] All resources have been correctly deallocated.")
