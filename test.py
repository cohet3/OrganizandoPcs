from Computadora import Computadora
from Monitor import Monitor
from Orden import Orden
from Raton import Raton
from Teclado import Teclado

teclado3 = Teclado('MoonGaming', 'USB')
raton3 = Raton('Racer', 'USB')
monitoe3 = Monitor('samsumg', 15)
computadora1 = Computadora('Hp', monitoe3, teclado3, raton3)

teclado4 = Teclado('MoonGaming', 'USB')
raton4 = Raton('Racer', 'USB')
monitoe4 = Monitor('samsumg', 15)
computadora2 = Computadora('Hp', monitoe4, teclado3, raton3)

computadora6= Computadora('Pepino','pantallote','superteclado','ratonPepino')

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)

orden1.agregar_computadora(computadora6)
print(orden1)