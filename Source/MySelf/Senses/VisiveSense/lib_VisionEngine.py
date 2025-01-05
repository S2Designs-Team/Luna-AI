#import cv2
from PIL import Image
import numpy as np
import asyncio
from pathlib import Path
from AssetsLibs.Abstraction.lib_NeuralProcess import NeuralProcess

class VisionEngine(NeuralProcess):

    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
        self.camera = None
        self.image_processing_tasks = []

    def initialize(self):
        """
        Initializes the Vision Engine.
        """
        self.logger.info("[VisionEngine]::[Initialize]")      
        self.camera = cv2.VideoCapture(0)  # Apre la webcam (ID 0 di default)  
        self.is_process_initialized = True
        self.logger.info(f"[{self.__class__.__name__}] Visual Sense Initialized.")

    async def handleSelfStimuli(self, message):
        """
        Elaborates the image stimuli simulating the vision sense.
        """
        self.logger.info("VisionEngine: processing vision image stimuli - %s", message)

        # Simulates the vision result
        result = f"Detected objects in image: {message}"
        self.logger.info("VisionEngine result: %s", result)
        return result
    
    async def handleExternalStimuli(self, message:str = ""):
        """
        Elaborates the image stimuli simulating the vision sense.
        """
        self.logger.info("VisionEngine: processing vision image stimuli - %s", message)

        # Simulates the vision result
        result = f"Detected objects in image: {message}"
        self.logger.info("VisionEngine result: %s", result)
        return result