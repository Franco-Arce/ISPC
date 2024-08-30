
import unittest
from fundidora import Fundidora

class TestFundidora(unittest.TestCase):
    def setUp(self):
        """Configura una instancia de Fundidora para cada prueba."""
        self.fundidora = Fundidora(capacidad=5000, temperatura_maxima=1800)

    def test_seleccionar_metal_oro(self):
        """Prueba la selección del metal 'oro'."""
        self.fundidora.seleccionar_metal('oro')
        self.assertEqual(self.fundidora.temperatura_necesaria, 1064)

    def test_seleccionar_metal_plata(self):
        """Prueba la selección del metal 'plata'."""
        self.fundidora.seleccionar_metal('plata')
        self.assertEqual(self.fundidora.temperatura_necesaria, 961)

    def test_seleccionar_metal_invalido(self):
        """Prueba la selección de un metal no soportado."""
        with self.assertRaises(ValueError):
            self.fundidora.seleccionar_metal('cobre')

    def test_calentar(self):
        """Prueba el calentamiento de la fundidora."""
        self.fundidora.seleccionar_metal('platino')
        self.fundidora.calentar()
        self.assertEqual(self.fundidora.temperatura_actual, 1768)

    def test_calentar_exceso_temperatura(self):
        """Prueba el intento de calentar a una temperatura mayor a la máxima permitida."""
        self.fundidora.temperatura_maxima = 1000
        self.fundidora.seleccionar_metal('platino')
        with self.assertRaises(ValueError):
            self.fundidora.calentar()

    def test_fundir_material(self):
        """Prueba la fundición de material."""
        self.fundidora.seleccionar_metal('paladio')
        self.fundidora.calentar()
        self.fundidora.fundir_material(1000)
        self.assertEqual(self.fundidora.material_fundido, 1000)

    def test_fundir_material_excedido(self):
        """Prueba el intento de fundir una cantidad de material que excede la capacidad."""
        self.fundidora.seleccionar_metal('oro')
        self.fundidora.calentar()
        with self.assertRaises(ValueError):
            self.fundidora.fundir_material(6000)

    def test_verificar_pureza_alta(self):
        """Prueba la verificación de la pureza cuando la temperatura es alta."""
        self.fundidora.temperatura_actual = 1100
        self.assertEqual(self.fundidora.verificar_pureza(), 99.9)

    def test_verificar_pureza_baja(self):
        """Prueba la verificación de la pureza cuando la temperatura es baja."""
        self.fundidora.temperatura_actual = 900
        self.assertEqual(self.fundidora.verificar_pureza(), 90.0)

if __name__ == '__main__':
    unittest.main()
