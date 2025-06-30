# app/usuarios.py

def nombre_completo(usuario):
    return f"{usuario['nombre']} {usuario['apellido']}".strip()
