# Body/__init__.py
from .Arms.lib_Arms import Arms

class Body:

    arms:Arms = None

    def __init__(self):

        self.arms = Arms()
        print("Luna's arms body parts have been initialized.")