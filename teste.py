from models.cliente import Cliente
from models.conta import Conta


felicty: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', '123.456.789-01', '02/09/1987')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '234.567.890-09', '08/07/1978')

# print(felicty)
# print(angelina)

contaf: Conta = Conta(felicty)
contaa: Conta = Conta(angelina)

# print(contaf)
# print(contaa)

