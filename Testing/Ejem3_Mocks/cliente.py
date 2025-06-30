def registrar_usuario(api, base):
    usuario = api.obtener()
    base.guardar(usuario)