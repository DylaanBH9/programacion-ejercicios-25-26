import pytest
from main import procesamiento

@pytest.mark.parametrize("entrada, esperado",
[
    ("23:45", 15),
    ("21:30", 150),
    ("00:01", 1439),
])
def test_procesar_linea(entrada, esperado):
    assert procesamiento(entrada) == esperado