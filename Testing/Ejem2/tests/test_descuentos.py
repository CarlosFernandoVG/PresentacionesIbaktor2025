# tests/test_descuentos.py

import pytest
from app.descuentos import calcular_descuento

@pytest.fixture
def cliente_base():
    return {"tipo": "regular", "total": 100}

def test_descuento_regular(cliente_base):
    cliente_base["tipo"] = "regular"
    cliente_base["total"] = 200
    assert calcular_descuento(cliente_base) == 180.0

def test_descuento_premium(cliente_base):
    cliente_base["tipo"] = "premium"
    cliente_base["total"] = 100
    assert calcular_descuento(cliente_base) == 80.0

def test_sin_descuento(cliente_base):
    cliente_base["tipo"] = "otro"
    cliente_base["total"] = 150
    assert calcular_descuento(cliente_base) == 150.0
