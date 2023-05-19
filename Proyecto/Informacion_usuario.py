import re
import tkinter as tk
from tkinter import messagebox
usuarios_global = []


class Usuario:
    UserName = ''
    UserLastName = ''
    UserSaldo = 0
    UserNumber = 0
    datos = {}

    def guardar_datos(self, nombre, apellido, email, contraseña, contraseña_verificacion, saldo, numero_cuenta):
        if not re.match("^[a-zA-Z]+$", nombre):
            messagebox.showerror("Error", "El nombre solo debe contener letras")
        elif not re.match("^[a-zA-Z]+$", apellido):
            messagebox.showerror("Error", "El apellido solo debe contener letras")
        elif len(contraseña) < 6:
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres")
        elif contraseña != contraseña_verificacion:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
        elif 'email' in self.__class__.datos and self.__class__.datos['email'] == email:
            messagebox.showerror("Error", "El correo electrónico ya está registrado")
        else:
            self.__class__.datos['nombre'] = nombre
            self.__class__.datos['apellido'] = apellido
            self.__class__.datos['email'] = email
            self.__class__.datos['contraseña'] = contraseña_verificacion
            self.__class__.datos["saldo"] = saldo
            self.__class__.datos["numero_cuenta"] = numero_cuenta
            self.UserName = nombre
            self.UserLastName = apellido
            self.UserSaldo = saldo
            self.UserNumber = numero_cuenta

            # Almacenar el usuario en la variable global
            global usuario_global
            usuario_global = self
            print(usuario_global.datos)
            return True
    def actualizar_datos(self, email, contraseña, contraseña_verificacion):
        if len(contraseña) < 6:
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres")
        elif contraseña != contraseña_verificacion:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
        elif 'email' in self.__class__.datos and self.__class__.datos['email'] == email:
            messagebox.showerror("Error", "El correo electrónico ya está registrado")
        else:
            self.__class__.datos['email'] = email
            self.__class__.datos['contraseña'] = contraseña_verificacion
            return True

    @classmethod
    def correo_existe(cls, email):
        return email in cls.datos

    def validar_datos(self, email, contraseña):
        if not self.__class__.datos:
            messagebox.showerror("Acceso denegado", "El correo electrónico o la contraseña son incorrectos")
        else:
            stored_email = self.__class__.datos.get('email')
            stored_password = self.__class__.datos.get('contraseña')

            if stored_email is None or stored_password is None:
                messagebox.showerror("Acceso denegado", "Ingresa la información, no dejes espacios en blanco")
                return False
            elif email == stored_email and contraseña == stored_password:
                messagebox.showinfo("Acceso concedido", "¡Inicio de sesión exitoso!")
                return True
            else:
                messagebox.showerror("Acceso denegado", "El correo electrónico o la contraseña son incorrectos")
                return False

    def obtener_saldo(self, monto = 0):
        saldo = (self.__class__.datos.get("saldo") - monto)
        return saldo

    def obetener_contraseña(self):
        contraseña = self.__class__.datos.get("contraseña")
        return contraseña
    def actualizar_saldo(self, nuevo_saldo):
        self.__class__.datos["saldo"] = nuevo_saldo
    def realizar_transferencia(self, monto):
        saldo_actual = self.obtener_saldo()
        if saldo_actual >= monto:
                nuevo_saldo_origen = saldo_actual - monto

                self.actualizar_saldo(nuevo_saldo_origen)

                messagebox.showinfo("Transferencia exitosa",
                                    f"Se transfirió {monto} $")
                return True
        else:
            messagebox.showerror("Error", "Saldo insuficiente para realizar la transferencia")
            return False

    @staticmethod
    def obtener_usuario_por_correo(correo):
        if correo in Usuario.datos:
            return Usuario()
        else:
            return None

usuario = Usuario()
usuario.guardar_datos("John", "Doe", "johndoe@gmail.com", "123456", "123456", 1000, 1234567890)

