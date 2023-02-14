class Orden:
    contadorOrdenes= 0
    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._id_orden = Orden.contadorOrdenes
        self._contadorOrdenes= computadoras
        self._computadoras = computadoras

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f'''
            Orden: {self._id_orden}
            Computadoras: {computadoras_str}
'''
