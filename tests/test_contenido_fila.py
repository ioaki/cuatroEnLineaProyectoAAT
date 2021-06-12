from src.cuatroEnLinea import contenidoFila

def test_tablero_contenido_fila():
        tablero = [
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [1,0,0,0,0,0,0],
   [1,2,0,0,0,0,0],
   [1,2,0,0,0,0,0],
   [1,2,0,0,0,0,0],
  ]

        assert [1,2,0,0,0,0,0] == contenidoFila(6,tablero)
    
