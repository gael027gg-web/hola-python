import pytest
from hola import saludar, sumar


class TestSaludar:
    """Pruebas para la función saludar"""
    
    def test_saludar_con_nombre(self):
        """Verifica que saludar devuelva el saludo correcto"""
        assert saludar("Python") == "¡Hola, Python!"
    
    def test_saludar_contiene_hola(self):
        """Verifica que el saludo contiene 'Hola'"""
        resultado = saludar("Juan")
        assert "Hola" in resultado
    
    def test_saludar_contiene_nombre(self):
        """Verifica que el saludo contiene el nombre proporcionado"""
        nombre = "María"
        resultado = saludar(nombre)
        assert nombre in resultado


class TestSumar:
    """Pruebas para la función sumar"""
    
    def test_sumar_positivos(self):
        """Verifica la suma de dos números positivos"""
        assert sumar(2, 3) == 5
    
    def test_sumar_negativos(self):
        """Verifica la suma con números negativos"""
        assert sumar(-2, -3) == -5
    
    def test_sumar_mixtos(self):
        """Verifica la suma de números positivos y negativos"""
        assert sumar(5, -3) == 2
    
    def test_sumar_ceros(self):
        """Verifica la suma con ceros"""
        assert sumar(0, 0) == 0
    
    def test_sumar_decimales(self):
        """Verifica la suma con números decimales"""
        assert sumar(1.5, 2.5) == 4.0
