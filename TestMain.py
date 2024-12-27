import pytest
import os

def discover_and_run_tests(test_directory="testenv"):
    """
    Scopre ed esegue tutti i test nella directory `testenv` usando pytest.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(current_dir, "TestEnv")
    
    # Esegui pytest sulla directory dei test
    pytest.main([test_dir, "--verbose", "--color=yes"])

if __name__ == "__main__":
    discover_and_run_tests()