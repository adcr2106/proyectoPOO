from bancoClass import BancoPAD

if __name__ == '__main__':
    banco = BancoPAD()

    print("BIENVENIDO A BANCO PAD.")
    while True:
        print("\nPresione 1 para crear una cuenta nueva")
        print("Presione 2 para iniciar sesión")
        print("Presione 3 depositar dinero")
        print("Presione 0 para finalizar")

        opc = int(input("\nDigite la opcion a realizar: "))

        if opc == 0:
            print("\nProceso finalizado...")
            break

        if opc == 1:
            name = input("Digite su nombre: ")
            saldo = int(input("Con cuanto dinero vienes a nuestro banco: "))
            contrasena = input("Digita una contrasena: ")
            nueva_cuenta_id = banco.crear_cuenta(name, saldo, contrasena)
            print("Cuenta creada con éxito. Su número de cuenta es:", nueva_cuenta_id)

        elif opc == 2:
            cuenta_id = input("Digite su número de cuenta: ")
            contrasena = input("Digite su contrasena: ")
            cuenta = banco.iniciar_sesion(cuenta_id, contrasena)
            if cuenta is not None:
                print("\nInicio de sesión exitoso. Bienvenido,", cuenta.nombre)
            else:
                print("\nNúmero de cuenta o contrasena incorrectos.")

        elif opc == 3:
            cuenta_id1 = input("Digite su número de cuenta: ")
            cuenta_id2 = input("Digite el número de cuenta de destino: ")
            cantidad = int(input("Digite la cantidad a depositar: "))
            if banco.depositar(cuenta_id1, cuenta_id2, cantidad):
                print("Depósito exitoso. Su nuevo saldo es de:", banco.cuentas[cuenta_id1].saldo)
                print("(Prueba de que se le suma a la cuenta de destino):", banco.cuentas[cuenta_id2].saldo)
            else:
                print("Número de cuenta incorrecto.")