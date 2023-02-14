

class Monitor():
    contadorMonitores = 0
    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self._marca = marca
        self._id_Monitor = Monitor.contadorMonitores
        self._tamaño = tamaño

    def __str__(self):
        return f'Monitor: Id : {self._id_Monitor}, Marca: {self._marca}, Tamaño: {self._tamaño}"'
    # @property
    # def idMonitor(self):
    #     return self.idMonitor
    # @idMonitor.setter
    # def idMonitor(self, idMonitor):
    # @property
    # def marca(self):
    #     return self.marca
    # @marca.setter
    # def marca(self, marca):
    # @property
    # def contadorMonitores(self):
    #     return self.contadorMonitores
    # @contadorMonitores.setter
    # def contadorMonitores(self, contadorMonitores):
    # @property
    # def tamaño(self):
    #     return self.tamaño
    # @tamaño.setter
    # def tamaño(self, tamaño):
    #
    #
    # @classmethod
    # def generar_siguiene_valor(cls):
    #     cls.contadorMonitores += 1
    #     return cls.contadorMonitores

if __name__ == '__main__':
    monitor1 = Monitor('Lenovo', 18)
    print(monitor1)

    monitor2 = Monitor('Samsung', 50)
    print(monitor2)