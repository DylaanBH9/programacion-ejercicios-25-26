import pytest
from main import procesamiento

test_cases = [
    (entrada, esperado), #cambiar los valores
    ("1 10", (0, 0, 24, 0)),
    ("10 10", (0, 4, 0, 0)),
    ("25 25", (1, 1, 0, 0)),
    ("1 100", (0, 4, 0, 0)),
    ("365 1", (0, 14, 36, 0)),
    ("0 0", (0, 0, 0, 0)),
    ("1 1440", (2, 9, 36, 0))
]

@pytest.mark.parametrize("entrada, esperado", test_cases)
def test_procesamiento(entrada, esperado):
    assert procesamiento(entrada) == esperado