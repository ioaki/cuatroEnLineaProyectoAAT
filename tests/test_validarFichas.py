from src.cuatroEnLinea import validarFichas

def test_validarFichas():
    secuencia = [1,2,1,2,1,2,1]
    secuencia1 = [0,2,1,2,1,2,7]

    assert validarFichas(secuencia) == True
    assert validarFichas(secuencia1) == False
