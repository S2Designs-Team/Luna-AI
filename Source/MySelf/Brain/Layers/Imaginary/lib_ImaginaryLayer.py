import asyncio
from AssetsLibs.Abstraction.lib_NeuralProcess import ANeuralProcess

# Classe derivata che simula il layer del processo di immaginazione del cervello
class ImaginaryLayer(ANeuralProcess):
    def __init__(self, layer_name):
        super().__init__()
        self.layer_name = layer_name