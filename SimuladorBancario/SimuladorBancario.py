__author__ = "Ana Maria Ruales"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "ana.rualesr@campusucc.edu.co"

#----------------------------------------------------------------
# Importaciones
#----------------------------------------------------------------

from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __cedula = ''
    __nombre = ''
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Asociaciones
    #----------------------------------------------------------------
    
    __cuentaAhorros=CuentaAhorros()
    __cuentaCorriente=CuentaCorriente()
    __cdt=CDT()
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite depositar en la cuenta corriente"

    def DepositarCuentaCorriente(self, monto):
        # Aqui inicia mi codigo
        self.__cuentaCorriente.ConsignarSaldo(monto)
    
    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__ = "Metodo que permite calcular el saldo total actual en todas las cuentas"

    def CalcularSaldoTotal(self):
        # Aqui inicia mi codigo
        # Metodo 1
        # total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        # return total
        # Metodo 2
        return self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
    
    __method__ = "PasarAhorroACorriente"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Metodo que permite pasar saldo de la cuenta de ahorrros a la cuenta corriente"

    def PasarAhorroACorriente(self):
        # Aqui inicia mi codigo
        saldoAhorros = self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarSaldo(saldoAhorros)
        self.__cuentaCorriente.ConsignarSaldo(saldoAhorros)

    __method__ = "Ahorrar"
    __parameter__ = "Monto"
    __returns__ = "Ninguna"
    __Description__ = "Metodo que permite Pasar saldo de la cuenta corriente a la cuenta de ahorros"

    def Ahorrar(self, monto):
        # Aqui inicia mi codigo
        self.__cuentaCorriente.RetirarSaldo(monto)
        self.__cuentaAhorros.ConsignarSaldo(monto)

    __method__ = "retirarAhorro"
    __parameter__ = "Monto"
    __returns__ = "Saldo de la cuenta de ahorros"
    __Description__ = "Metodo que permite Retirar un valor dado de la cuenta de ahorros"

    def retirarAhorro(self, monto):
        # Aqui inicia mi codigo
        return self.__cuentaAhorros.DarSaldo()-monto
    
    __method__ = "darSaldoCorriente"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo de la cuenta de la cuenta corriente"
    __Description__ = "Metodo que permite Retornar el saldo que hay en la cuenta corriente."

    def darSaldoCorriente(self):
        # Aqui inicia mi codigo
        return self.__cuentaCorriente.DarSaldo()
    
    __method__ = "retirarTodo"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite Retirar todo el dinero que hay en la cuenta corriente y en la cuenta de ahorros."

    def retirarTodo(self):
        # Aqui inicia mi codigo
        saldoAhorros = self.__cuentaAhorros.DarSaldo()
        saldoCorriente = self.__cuentaCorriente.DarSaldo()
        self.__cuentaCorriente.RetirarSaldo(saldoCorriente)
        self.__cuentaAhorros.RetirarSaldo(saldoAhorros) 
    

    __method__ = "duplicarAhorro"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo duplicado"
    __Description__ = "Metodo que permite Duplica la cantidad de dinero que hay en la cuenta de ahorros."

    def duplicarAhorro(self):
        # Aqui inicia mi codigo
        return self.__cuentaAhorros.DarSaldo()*2
        