from src.cuatroEnLinea import generarTablero

def test_tablero_vacio_tiene_6_filas():
    tablero = generarTablero()
    assert len(tablero) == 6

def test_tablero_vacio_tiene_7_columnas():
    tablero = generarTablero()
    assert len(tablero[0]) == 7
