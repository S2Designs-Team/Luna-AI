import asyncio
from AssetsLibs.Abstraction.lib_NeuralProcess import ANeuralProcess

# Classe derivata che simula il layer del processo Mnemonico del cervello
class MnemonicLayer(ANeuralProcess):
    def __init__(self, layer_name):
        super().__init__()
        self.layer_name = layer_name