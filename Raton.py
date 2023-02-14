from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contadorRatones = 0
    def __init__(self, tipoEntrada, marca):
        Raton.contadorRatones += 1
        self._id_raton = Raton.contadorRatones
        super().__init__(tipoEntrada, marca)



    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self._marca}, Tipo_entrada: {self._tipoEntrada}'


if __name__ == '__main__':
    raton2 = Raton('bluetooth', 'Asus')
    raton1 = Raton('USB', 'HP')
    print(raton1)
    print(raton2)