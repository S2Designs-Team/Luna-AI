import unittest
import os
from AssetsLibs.Abstraction.lib_BasicProcess import BasicProcess

# Classe concreta per i test
class ConcreteProcess(BasicProcess):
    def __init__(self):
        super().__init__()

class TestBasicProcess(unittest.TestCase):

    def setUp(self):
        self.process = ConcreteProcess()

    def test_class_properties(self):
        expected_name = "ConcreteProcess"
        self.assertEqual(self.process.CLASS_NAME, expected_name)

    def test_class_paths(self):
        expected_file = os.path.basename(__file__)
        self.assertEqual(self.process.CLASS_FILE_NAME, expected_file)

if __name__ == "__main__":
    unittest.main()