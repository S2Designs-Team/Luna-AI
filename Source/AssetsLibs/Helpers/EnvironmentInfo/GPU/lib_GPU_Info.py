import torch

class GPUInfo:
    """
    A helper class to retrieve GPU information and manage device configuration.
    """

    @staticmethod
    def check_gpu_availability():
        """
        Checks and returns whether a GPU is available, along with the device information.

        Returns:
            torch.device: The available device (GPU or CPU).
        """
        try:
            if torch.cuda.is_available():
                my_device   = torch.device("cuda")
                my_gpu_name = torch.cuda.get_device_name(0)
                print(f"GPU detected: {my_gpu_name}")
                print(f"Using device: {my_device}")
                return my_device
            else:
                my_device = torch.device("cpu")
                print("No GPU detected. Falling back to CPU.")
                return my_device
        except Exception as e:
            print(f"Error detecting GPU: {e}")