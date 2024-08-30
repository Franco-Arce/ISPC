import unittest
from fundidora import Fundidora

class TestFundidora(unittest.TestCase):
    def setUp(self):
        """Configura el entorno de prueba inicial."""
        self.fundidora = Fundidora(capacidad=5000, temperatura_maxima=1800)

    def test_seleccionar_metal_valido(self):
        """Prueba la selección de un metal válido."""
        self.fundidora.seleccionar_metal('oro')
        self.assertEqual(self.fundidora.tipo_metal, 'oro')
        self.assertEqual(self.fundidora.temperatura_necesaria, 1064)

    def test_seleccionar_metal_no_soportado(self):
        """Prueba la selección de un metal no soportado."""
        with self.assertRaises(ValueError):
            self.fundidora.seleccionar_metal('cobre')

    def test_calentar_temperatura_valida(self):
        """Prueba calentar la fundidora a una temperatura válida."""
        self.fundidora.seleccionar_metal('plata')
        self.fundidora.calentar()
        # Usamos métodos públicos para verificar el estado después de calentar
        self.assertEqual(self.fundidora._Fundidora__temperatura_actual, 961)

    def test_calentar_temperatura_excedida(self):
        """Prueba calentar la fundidora a una temperatura que excede el máximo."""
        self.fundidora.temperatura_maxima = 900  # Redefinimos temperatura máxima para la prueba
        self.fundidora.seleccionar_metal('platino')
        with self.assertRaises(ValueError):
            self.fundidora.calentar()

    def test_fundir_material_valido(self):
        """Prueba fundir una cantidad válida de material."""
        self.fundidora.seleccionar_metal('oro')
        self.fundidora.calentar()
        self.fundidora.fundir_material(2000)
        self.assertEqual(self.fundidora.material_fundido, 2000)

    def test_fundir_material_excedido(self):
        """Prueba fundir una cantidad de material que excede la capacidad."""
        self.fundidora.seleccionar_metal('plata')
        self.fundidora.calentar()
        with self.assertRaises(ValueError):
            self.fundidora.fundir_material(6000)

    def test_verificar_pureza(self):
        """Prueba la verificación de la pureza del material fundido."""
        self.fundidora.seleccionar_metal('paladio')
        self.fundidora.calentar()
        self.fundidora.fundir_material(1000)
        pureza = self.fundidora.verificar_pureza()
        self.assertEqual(pureza, 99.9)

    def test_verificar_pureza_baja(self):
        """Prueba la verificación de la pureza cuando la temperatura es baja."""
        self.fundidora.__temperatura_actual = 800  # Redefinimos la temperatura para la prueba
        pureza = self.fundidora.verificar_pureza()
        self.assertEqual(pureza, 90.0)

if __name__ == "__main__":
    unittest.main()
