from romannumbers import romano_a_entero, RomanNumberError
import pytest

def tes_palito_es_uno():
    assert romano_a_entero("I") == 1
    assert romano_a_entero("L") == 50

def test_sumando():
    assert romano_a_entero("CXXIII") == 123

def test_resta_normal():
    assert romano_a_entero("IV") == 4
    assert romano_a_entero("IX") == 9

def test_composicion_numero():
    assert romano_a_entero("MMCMXLIX") == 2949
    

def test_de_no_mas_de_tres_repeticiones():
    with pytest.raises(RomanNumberError):
        romano_a_entero("CCCC") 

def test_de_no_repetir_VLD():
    with pytest.raises(RomanNumberError):
        romano_a_entero("VV")
    with pytest.raises(RomanNumberError):
        romano_a_entero("LL")
    with pytest.raises(RomanNumberError):
        romano_a_entero("DD")

def test__restas_permitidas():
    with pytest.raises(RomanNumberError):
        romano_a_entero("IC")
    with pytest.raises(RomanNumberError):
        romano_a_entero("IL")
    with pytest.raises(RomanNumberError):
        romano_a_entero("XD")
    with pytest.raises(RomanNumberError):
        romano_a_entero("XM")

    with pytest.raises(RomanNumberError): #PENDIENTE 
        romano_a_entero("CM")