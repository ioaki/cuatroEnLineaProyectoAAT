from src.cuatroEnLinea import contenidoColumna

def test_contenido_columna():
    tablero = [
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [1,0,0,0,0,0,0],
   [1,2,0,0,0,0,0],
   [1,2,0,0,0,0,0],
   [1,2,0,0,0,0,0],
  ]

    assert [0,0,1,1,1,1] == contenidoColumna(1,tablero)
    assert [0,0,0,2,2,2] == contenidoColumna(2,tablero)
