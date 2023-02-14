from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora:
    contadorComputadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras +=1
        self._id_computadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    def __str__(self):
       return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Ratón: {self._raton}
        '''

if __name__ == '__main__':
    teclado3 = Teclado('MoonGaming', 'USB')
    raton3= Raton('Racer', 'USB')
    monitoe3= Monitor('samsumg', 15)
    computadora1 = Computadora('Hp', monitoe3, teclado3, raton3)
    print(computadora1)
    teclado4 = Teclado('MoonGaming', 'USB')
    raton4= Raton('Racer', 'USB')
    monitoe4= Monitor('samsumg', 15)
    computadora2 = Computadora('Hp', monitoe4, teclado3, raton3)
    print(computadora2)