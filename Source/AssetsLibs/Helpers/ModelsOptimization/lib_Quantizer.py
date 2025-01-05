import torch

class Quantizer:
    """
    Classe per la quantizzazione dei modelli.
    Riduce i pesi del modello a una rappresentazione a 4 bit per ottimizzare le prestazioni.
    """
    def __init__(self, model):
        """
        Inizializza il Quantizer con il modello da quantizzare.
        
        :param model: Modello PyTorch da ottimizzare.
        """
        self.model = model

    def quantize(self):
        """
        Applica la quantizzazione a 4 bit sui pesi del modello.
        """
        for name, param in self.model.named_parameters():
            if 'weight' in name:
                # Conversione dei pesi in una rappresentazione a 4 bit
                param.data = self._quantize_tensor(param.data)
                print(f"Quantizzato layer {name} a 4 bit.")

    def _quantize_tensor(self, tensor):
        """
        Quantizza un tensore in formato a 4 bit.
        
        :param tensor: Tensore da quantizzare.
        :return: Tensore quantizzato.
        """
        scale = tensor.abs().max() / (2**3 - 1)  # Calcola il fattore di scala
        quantized = torch.round(tensor / scale).clamp(-8, 7)  # Limita i valori tra -8 e 7
        return quantized * scale
