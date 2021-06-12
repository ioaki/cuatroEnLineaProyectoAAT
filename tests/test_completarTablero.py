from src.cuatroEnLinea import completarTablero

def test_completarTablero():
    tablero = [
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
  ]

    secuencia = [1,2,1,2,1,2,1]

    tableroEsperado = [
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [1,0,0,0,0,0,0],
   [1,2,0,0,0,0,0],
   [1,2,0,0,0,0,0],
   [1,2,0,0,0,0,0],
  ]

    assert completarTablero(secuencia,tablero) == tableroEsperado
