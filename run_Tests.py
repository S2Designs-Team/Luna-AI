import unittest
import sys
import os

def run_tests():
    # Aggiungi la directory del codice sorgente al percorso
    source_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "source"))
    if source_dir not in sys.path:
        sys.path.insert(0, source_dir)

    # Trova ed esegui i test nella cartella Tests
    loader = unittest.TestLoader()
    tests = loader.discover("Tests")
    test_runner = unittest.TextTestRunner(verbosity=2)
    
    # Esegue i test e salva i risultati
    result = test_runner.run(tests)
    
    # Riassunto finale
    print("\n" + "=" * 40)
    print("Test Summary")
    print("=" * 40)
    print(f"Total Tests: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    # Dettaglio dei fallimenti
    if result.failures or result.errors:
        print("\nDetails:")
        for failed_test, traceback in result.failures + result.errors:
            print(f"Test: {failed_test}")
            print(traceback)
    else:
        print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()