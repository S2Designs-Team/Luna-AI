# Luna_AI_main.py
import datetime
import tkinter as tk
import asyncio
import tracemalloc
import sys
import os

from GUI.Desktop.gui_Console import LunaApp
from AssetsLibs.Helpers.EnvironmentInfo.GPU.lib_GPU_Info import GPUInfo
from MySelf.lib_MySelf import MySelf

# Starts the monitoring of the memory allocation
tracemalloc.start()

# Global termination Event
shutdown_event = asyncio.Event()
Luna_AI_Process:MySelf = MySelf()

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

    except asyncio.CancelledError:
        print("[INFO] Memory monitor coroutine has been cancelled.")
    except Exception as monitor_current_memory_exeption:
        print(f"An error occurred in monitor_current_memory: {monitor_current_memory_exeption}")

async def run_luna_gui():
    """
    GUI mode: starts a graphic user interface Tkinter (if supported).
    """      
    try:
        root = tk.Tk()
        app = LunaApp(root)
        app.start_luna()
        root.mainloop()        
        print("Graphic Interfaced Mode...started.")
    except ImportError:
        print("Error: tkinter not installed.")

async def run_luna_being():
    """
    Main async function that initializes and manages the main loop.
    """ 
    #Use GPUInfo to retrieve the GPU device"
    #my_process_unit_device = GPUInfo.check_gpu_availability()    

    try:
        _ = await Luna_AI_Process.async_init()
        await Luna_AI_Process.wakeUp()

    finally:
        await Luna_AI_Process.TurnOff()
        print("Luna has been gracefully turned off.")

async def handle_mode_async(mode):
    """
    Handles the execution mode based on starting call arguments.
    """
    tasks = []
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
                tasks.append(asyncio.create_task(run_luna_gui()))
                tasks.append(asyncio.create_task(run_luna_being()))
                tasks.append(asyncio.create_task(monitor_current_memory()))
                await asyncio.gather(*tasks)
            case "help":
                show_command_help()
            case _:
                print("Parameter(s) not valid. Use 'gui' to start Luna in Graphic Interfaced Mode or 'console' for the Console Mode.")
                sys.exit(1)
    except asyncio.CancelledError:
        for task in tasks:
            task.cancel()  # Properly clear the tasks.
        await asyncio.gather(*tasks, return_exceptions=True)
        print("[INFO] All tasks have been cleared.")        
    finally:
        for task in tasks:
            task.cancel()  # Cancels all the tasks                

def show_command_help():
    """
    Shows the instructions to correctly use this script.
    """    
    print("Usage Help: python startLunaAI.py [gui|console]")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("╔═════════════════════════════════════════════════════════════════════════════╗")
    print("║ Welcome to Luna-AI project!                                                 ║")
    print("╚═════════════════════════════════════════════════════════════════════════════╝") 
    
    if len(sys.argv) != 2:
        print("Usage Help: python startLunaAI.py [gui|console]")
        sys.exit(1)

    par_mode = sys.argv[1].lower()
    
    try:
        asyncio.run(handle_mode_async(par_mode))
    except KeyboardInterrupt:
        print("[INFO] Manual interruption detected. Closing the program...")
    except Exception as app_exception:
        print(f"[ERROR] An unexpected error occurred: {app_exception}")
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
