import pytest

from operaciones import agrupar, dividir, sumar


def test_sumar():
    assert sumar(2, 3) == 5


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_agrupar():
    assert agrupar([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]