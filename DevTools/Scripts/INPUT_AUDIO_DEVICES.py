import pyaudio
import logging
import os

def clear_console():
    """Cancella il terminale per un output pulito."""
    os.system('cls' if os.name == 'nt' else 'clear')

def ListAll_Input_Audio_Devices():
    INPUT_AUDIO_SENSOR = pyaudio.PyAudio()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    logger = logging.getLogger()
    
    # Elenca tutti i dispositivi audio disponibili
    logger.info("[DEV TOOL] => LIST ALL INPUT AUDIO DEVICES:")
    for i in range(INPUT_AUDIO_SENSOR.get_device_count()):
        device_info = INPUT_AUDIO_SENSOR.get_device_info_by_index(i)            
        if i < INPUT_AUDIO_SENSOR.get_device_count() - 1:
            logger.info("   ├── Device ID: %s, Name: %s", i, device_info['name'])
        else:
            logger.info("   └── Device ID: %s, Name: %s", i, device_info['name'])

if __name__ == "__main__":
    clear_console()  # Cancella l'output precedente
    ListAll_Input_Audio_Devices()