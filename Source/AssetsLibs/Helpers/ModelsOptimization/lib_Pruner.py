import torch

class Pruner:
    """
    Classe per il pruning dei pesi del modello.
    Elimina i pesi meno significativi per ridurre la complessità.
    """
    def __init__(self, model, pruning_percentage=0.2):
        """
        Inizializza il Pruner con il modello e la percentuale di pruning.
        
        :param model: Modello PyTorch da ottimizzare.
        :param pruning_percentage: Percentuale di pesi da rimuovere (default: 20%).
        """
        self.model = model
        self.pruning_percentage = pruning_percentage

    def prune(self):
        """
        Esegue il pruning dei pesi del modello.
        """
        for name, param in self.model.named_parameters():
            if 'weight' in name:
                mask = self._compute_mask(param.data)
                param.data *= mask
                print(f"Pruned layer {name}, rimosso il {self.pruning_percentage * 100}% dei pesi.")

    def _compute_mask(self, tensor):
        """
        Calcola la maschera binaria per i pesi da eliminare.
        
        :param tensor: Tensore dei pesi.
        :return: Maschera binaria per il pruning.
        """
        threshold = torch.quantile(tensor.abs(), self.pruning_percentage)
        return (tensor.abs() > threshold).float()
