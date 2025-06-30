# tests/test_usuarios.py

from app.usuarios import nombre_completo

def test_nombre_completo_normal():
    usuario = {"nombre": "Carlos", "apellido": "Vásquez"}
    assert nombre_completo(usuario) == "Carlos Vásquez"

def test_nombre_completo_sin_apellido():
    usuario = {"nombre": "Carlos", "apellido": ""}
    assert nombre_completo(usuario) == "Carlos"
