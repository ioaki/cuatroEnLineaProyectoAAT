# Devuelve un tablero vacio
def generarTablero():
  return [
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
  ]

def contenidoColumna(nro_columna, tablero):
  columna = []
  for fila in tablero:
    celda = fila[nro_columna - 1]
    columna.append(celda)
  return columna

def contenidoFila(nro_fila, tablero):
  fila = []
  for celda in tablero[nro_fila-1]:
    fila.append(celda)
  return fila

def filas(tablero):
  return tablero

def columnas(tablero):
  columnas=[]
  for i in range(len(tablero)):
    columnas.insert(-1,contenidoColumna(i,tablero))
  return columnas


def soltarFichaEnColumna(ficha, columna, tablero):
 for fila in range(6,0,-1):
    if tablero[fila-1][columna-1]==0:
      tablero[fila-1][columna-1]=ficha
      return tablero

def completarTablero(secuencia,tablero):
  jugador=0
  for jugada in secuencia:
    tablero=soltarFichaEnColumna(jugador%2+1,jugada,tablero)
    jugador+=1
  return tablero

def dibujarTablero(tablero):
  for fila in range(0,6):
    print("|",end="")
    for columna in range(0,7):
      if tablero[fila][columna]==0:
          print(" ",end="")
      else:
          print(tablero[fila][columna],end="")
    print("|",end="")
    print();
  print("+-------+",end="")
  return

def validarFichas(secuencia):
  for element in secuencia:
    if element<1 or element>7:
      return False
  return True
        
secuencia = [1,2,3,1,3,4]
tablero = []
if(validarFichas(secuencia)):
  tablero = completarTablero(secuencia,generarTablero())
  dibujarTablero(tablero)
else:
    print("El valor de las columnas debe ir del 1 al 7")

print(contenidoColumna(2, tablero))
print(contenidoFila(6, tablero))
print(filas(tablero))
print()
print(columnas(tablero))
