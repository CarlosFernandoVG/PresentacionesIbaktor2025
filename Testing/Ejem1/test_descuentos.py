#from descuentos import calcular_descuento

#def test_descuento_premium():
#    resultado = calcular_descuento({"tipo": "premium"})
#    assert resultado == 80.0

#def test_descuento_regular():
#    cliente = {"tipo": "regular", "total": 200}
#    resultado = calcular_descuento(cliente)
#    assert resultado == 180.0

import pytest
from descuentos import calcular_descuento

@pytest.fixture
def cliente_base():
    return {"tipo": "regular", "total": 100}

def test_descuento_regular(cliente_base):
    cliente_base["tipo"] = "regular"
    cliente_base["total"] = 200
    resultado = calcular_descuento(cliente_base)
    assert resultado == 180.0

def test_descuento_premium(cliente_base):
    cliente_base["tipo"] = "premium"
    cliente_base["total"] = 100
    resultado = calcular_descuento(cliente_base)
    assert resultado == 80.0

def test_descuento_sin_tipo(cliente_base):
    cliente_base["tipo"] = "otro"
    cliente_base["total"] = 150
    resultado = calcular_descuento(cliente_base)
    assert resultado == 150.0
