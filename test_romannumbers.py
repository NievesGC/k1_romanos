from romannumbers import entero_a_romano,sacar_unidad,decimales

def test_uno_es_palito():
    assert entero_a_romano(1) == "I"

def test_dos_es_palito_palito():
    assert entero_a_romano(2) == "II"

def test_tres_es_palito_tres_veces():
    assert entero_a_romano(3) == "III"

def test_cuadro_es_palito_uve():
    assert entero_a_romano(4) == "IV"

def test_cinco_es_uve():
    assert entero_a_romano(5) == "V"

def test_seis_es_uve_paliro():
    assert entero_a_romano(6) == "VI"

def test_sietes_es_uve_y_dos_palitos():
    assert entero_a_romano(7) == "VII"

def test_ocho_es_uve_y_tres_palitos():
    assert entero_a_romano(8) == "VIII"

def test_nueve_es_palito_equis():
    assert entero_a_romano(9) == "IX"

def test_diez_es_equis():
    assert entero_a_romano(10) == "X"

def test_once_es_equis_equis_palito():
    assert entero_a_romano(11) == "XI"


def test_pruebas_sacarDecimal():
    assert sacar_unidad(22) == 2

def test_decimales():
    assert decimales(96) == "XCVI"