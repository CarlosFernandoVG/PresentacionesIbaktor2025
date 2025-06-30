import unittest
from unittest.mock import Mock
from cliente import registrar_usuario

class TestRegistro(unittest.TestCase):

    def test_registro_exitoso(self):
        api_mock = Mock()
        base_mock = Mock()

        api_mock.obtener.return_value = {"nombre": "Carlos"}

        registrar_usuario(api_mock, base_mock)

        api_mock.obtener.assert_called_once()
        base_mock.guardar.assert_called_once_with({"nombre": "Carlos"})

if __name__ == '__main__':
    unittest.main()
