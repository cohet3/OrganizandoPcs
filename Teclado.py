from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorTeclado = 0
    def __init__(self, tipoEntrada, marca):
        Teclado.contadorTeclado += 1
        self._id_teclado = Teclado.contadorTeclado
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'Id: {self._id_teclado}, Marca: {self._marca}, Tipo Entrada: {self._tipoEntrada}'


if __name__ == '__main__':
    teclado2 = Teclado('bluetooth', 'Asus')
    teclado1 = Teclado('USB', 'HP')
    print(teclado1)
    print(teclado2)