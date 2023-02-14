class DispositivoEntrada:

    def __init__(self, tipoEntrada , marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    def __str__(self):
        return f'tipoEntrada: {self.tipoEntrada}, marca: {self.marca}'

    def mostrar_detalles(self):
        return self.__str__()