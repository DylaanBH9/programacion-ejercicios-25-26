import pytest
from main import procesamiento

@pytest.mark.parametrize("numero, esperado", [
    (3, "IZQUIERDA"),   # Ejemplo: impar
    (10, "DERECHA"),    # Ejemplo: par
    (41, "IZQUIERDA"),  # Ejemplo: impar
    (1, "IZQUIERDA"),    # Caso base impar
    (2, "DERECHA"),    # Caso base par
    (999, "IZQUIERDA"),   # Límite superior impar
    (1000, "DERECHA"),  # Límite superior par
])
def test_determinar_lado(numero, esperado):
    assert procesamiento(numero) == esperado
