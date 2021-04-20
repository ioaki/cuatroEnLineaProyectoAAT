def generarTablero():
  return [
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
  ]

def soltarFichaEnColumna(ficha, columna, tablero):
 for fila in range(6,0,-1):
    if tablero[fila-1][columna-1]==0:
      tablero[fila-1][columna-1]=ficha
      return tablero

def completarTablero(secuencia,tablero):
  jugador=0
  for jugada in secuencia:
    if validaColumna(jugada): #Si se inserta una ficha en una columna incorrecta, se ignorara
      tablero=soltarFichaEnColumna(jugador%2+1,jugada,tablero)
      jugador+=1
  return tablero

def dibujarTablero(tablero):
  for fila in range(0,6):
    for columna in range(0,7):
        print(tablero[fila][columna],end="")
    print();
  return

def validaColumna(columna):
  if columna>0 and columna<7:
    return True
    return False

secuencia = [1,2,3,1,3,4,7,8,9,10]
dibujarTablero(completarTablero(secuencia,generarTablero()))
