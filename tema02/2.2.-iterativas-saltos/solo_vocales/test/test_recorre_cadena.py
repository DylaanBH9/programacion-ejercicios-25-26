import pytest
from main import saca_vocales

@pytest.mark.parametrize("cadena, esperado", [
    ("hola", "oa"),
    ("", ""),
    ("jrk", ""),
    ("aAron", "aao"),
    ("juan", "ua"),
    ("aaaa", "aaaa"),
    ("77", ""),
    ("María", "aía"),
    ("aarón", "aaó"),
])

def test_recorrer_cadena(cadena, esperado):
    assert saca_vocales(cadena) == esperado