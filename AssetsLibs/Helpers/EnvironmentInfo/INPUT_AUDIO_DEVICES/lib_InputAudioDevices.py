import pyaudio

class InputAudioDevices:
    """
    A helper class to retrieve input audio devices informations and manage device configuration.
    """

    @staticmethod
    def get_device_infos(index = 0):
        """
        """
        try:
            my_input_audio_devices_manager = pyaudio.PyAudio()
            my_device_info = my_input_audio_devices_manager.get_device_info_by_index(index)
            return my_device_info
        except Exception as e:
            raise (f"Error retrieving information for input audio device {index}: {e}")