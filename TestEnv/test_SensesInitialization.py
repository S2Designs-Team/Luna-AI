import pytest

from MySelf.Senses.HearingSense.lib_HearingEngine      import HearingEngine
#from MySelf.Senses.OlfactorySense.lib_OlfactoryEngine  import OlfactoryEngine
#from MySelf.Senses.SpeechSense.lib_SpeechEngine        import SpeechEngine
#from MySelf.Senses.TouchSense.lib_TouchEngine          import TouchEngine
#from MySelf.Senses.VisiveSense.lib_VisionEngine        import VisionEngine

@pytest.fixture
def setup_BrainSenses():
    """
    Fixture per inizializzare tutte le istanze degli engine.
    """
    brainSenses = {
        "hearingEngine"  : HearingEngine("HearingSense")
        # , "olfactoryEngine": OlfactoryEngine("OlfactorySense")
        # , "speechEngine"   : SpeechEngine("SpeechSense")
        # , "touchEngine"    : TouchEngine("TouchSense")
        # , "visionEngine"   : VisionEngine("VisionSense")
    }
    return brainSenses
 
def test_InitializeBrainSenses(setup_BrainSenses):
    """
    Testa il metodo wakeUp per tutti gli engine, verificando che non sollevi eccezioni.
    """
    for name, brainSense in setup_BrainSenses.items():
        try:
            brainSense.wakeUp()
        except Exception as e:
            pytest.fail(f"{name} failed to initialize with exception: {e}")

def test_ProcessSenses(setup_Senses):
    """
    Esempio di test su metodi di process per ogni layer (esempio generico).
    """
    for name, brainSense in setup_BrainSenses.items():
        result = brainSense.process("test data")  # Presupponendo che ogni engine abbia un metodo `process`.
        assert result == "EXPECTED OUTPUT", f"{name} did not return the expected output."

    def test_initialize(self):
        self.hearingEngine.wakeUp()
        # self.olfactoryEngine.wakeUp()
        # self.speechEngine.wakeUp()
        # self.touchEngine.wakeUp()
        # self.VisionEngine.wakeUp()
        self.assertTrue(True, "Test Initialization did not raise any exception")

