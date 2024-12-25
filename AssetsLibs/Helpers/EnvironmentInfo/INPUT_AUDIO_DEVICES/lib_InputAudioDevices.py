import pyaudio
import audioop
class InputAudioDevices:
    """
    A helper class to retrieve input audio devices informations and manage device configuration.
    """
    @staticmethod
    def get_pyaudio():
        """
        Imports the pyaudio module and checks its version. Throws exceptions if pyaudio can't be found or a wrong version is installed
        """
        try:
            import pyaudio
        except ImportError:
            raise AttributeError("Could not find PyAudio; check installation")
        from distutils.version import LooseVersion
        if LooseVersion(pyaudio.__version__) < LooseVersion("0.2.11"):
            raise AttributeError("PyAudio 0.2.11 or later is required (found version {})".format(pyaudio.__version__))
        return pyaudio
    
    @staticmethod
    def list_microphone_names():
        """
        Returns a list of the names of all available microphones. For microphones where the name can't be retrieved, the list entry contains ``None`` instead.

        The index of each microphone's name in the returned list is the same as its device index when creating a ``Microphone`` instance - if you want to use the microphone at index 3 in the returned list, use ``Microphone(device_index=3)``.
        """
        audio = InputAudioDevices.get_pyaudio().PyAudio()
        try:
            result = []
            for i in range(audio.get_device_count()):
                device_info = audio.get_device_info_by_index(i)
                result.append(device_info.get("name"))
        finally:
            audio.terminate()
        return result
    
    @staticmethod
    def list_working_microphones():
        """
        Returns a dictionary mapping device indices to microphone names, for microphones that are currently hearing sounds. When using this function, ensure that your microphone is unmuted and make some noise at it to ensure it will be detected as working.

        Each key in the returned dictionary can be passed to the ``Microphone`` constructor to use that microphone. For example, if the return value is ``{3: "HDA Intel PCH: ALC3232 Analog (hw:1,0)"}``, you can do ``Microphone(device_index=3)`` to use that microphone.
        """
        pyaudio_module = InputAudioDevices.get_pyaudio()
        audio = pyaudio_module.PyAudio()
        try:
            result = {}
            for device_index in range(audio.get_device_count()):
                device_info = audio.get_device_info_by_index(device_index)
                device_name = device_info.get("name")
                assert isinstance(device_info.get("defaultSampleRate"), (float, int)) and device_info["defaultSampleRate"] > 0, "Invalid device info returned from PyAudio: {}".format(device_info)
                try:
                    # read audio
                    pyaudio_stream = audio.open(
                        input_device_index=device_index, channels=1, format=pyaudio_module.paInt16,
                        rate=int(device_info["defaultSampleRate"]), input=True
                    )
                    try:
                        buffer = pyaudio_stream.read(1024)
                        if not pyaudio_stream.is_stopped(): pyaudio_stream.stop_stream()
                    finally:
                        pyaudio_stream.close()
                except Exception:
                    continue

                # compute RMS of debiased audio
                energy = -audioop.rms(buffer, 2)
                energy_bytes = bytes([energy & 0xFF, (energy >> 8) & 0xFF])
                debiased_energy = audioop.rms(audioop.add(buffer, energy_bytes * (len(buffer) // 2), 2), 2)

                if debiased_energy > 30:  # probably actually audio
                    result[device_index] = device_name
        finally:
            audio.terminate()
        return result

    @staticmethod
    def get_default_input_device():
        """
        Identifica il dispositivo audio di input predefinito.
        """
        audio = pyaudio.PyAudio()
        try:
            default_device_index = audio.get_default_input_device_info()
            print("Dispositivo di input predefinito:")
            print(default_device_index)
            return default_device_index
        except Exception as e:
            print(f"Errore: {e}")
        finally:
            audio.terminate()

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

    @staticmethod    
    def select_device(input_device_index = 0, device_format=16, device_channels=1, device_rate=44100, is_input_device=True, frames_per_buffer=1024):
        """
        """
        try:
            my_input_audio_devices_manager = pyaudio.PyAudio()
            my_selected_device = my_input_audio_devices_manager.open(format=device_format,
                                                                     channels=device_channels,
                                                                     rate=device_rate,
                                                                     input=is_input_device,
                                                                     input_device_index=input_device_index,
                                                                     frames_per_buffer=frames_per_buffer)
            return my_selected_device
        except Exception as e:
            raise (f"Error retrieving the input audio device {input_device_index}: {e}")