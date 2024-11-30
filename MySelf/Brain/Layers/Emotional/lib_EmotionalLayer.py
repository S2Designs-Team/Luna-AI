import asyncio
from AssetsLibs.Abstraction.lib_NeuralProcess import ANeuralProcess

# Classe derivata che simula il layer del processo Emozionale/Emptatico del cervello
class EmotionalLayer(ANeuralProcess):
    def __init__(self, layer_name):
        super().__init__()
        self.layer_name = layer_name