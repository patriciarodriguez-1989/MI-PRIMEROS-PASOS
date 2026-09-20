import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.main import saludar


def test_saludar():
    assert saludar("Patricia") == "Hola, Patricia"