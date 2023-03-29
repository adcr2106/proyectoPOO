import random
from typing import Optional


class BancoPAD:
    def __init__(self):
        self.cuentas: dict = {}

    def crear_cuenta(self, nombre, saldo_inicial, contrasena) -> str:
        cuenta_id = str(random.randrange(10 ** 9, 10 ** 10))
        cuenta = CuentaBancaria(cuenta_id, nombre, saldo_inicial, contrasena)
        self.cuentas[cuenta_id] = cuenta
        return cuenta_id

    def iniciar_sesion(self, cuenta_id, contrasena) -> Optional[str]:
        if cuenta_id in self.cuentas and self.cuentas[cuenta_id].contrasena == contrasena:
            return self.cuentas[cuenta_id]
        else:
            return None

    def depositar(self, cuenta_id1, cuenta_id2, cantidad) -> bool:
        if cuenta_id1 in self.cuentas and cuenta_id2 in self.cuentas:
            self.cuentas[cuenta_id1].saldo -= cantidad
            self.cuentas[cuenta_id2].saldo += cantidad
            return True
        else:
            return False


class CuentaBancaria:
    def __init__(self, cuenta_id, nombre, saldo_inicial, contrasena):
        self.cuenta_id: str = cuenta_id
        self.nombre: str = nombre
        self.saldo: int = saldo_inicial
        self.contrasena: str = contrasena
