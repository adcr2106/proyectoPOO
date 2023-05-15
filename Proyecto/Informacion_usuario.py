import tkinter as tk
from tkinter import messagebox


class Usuario:
    datos: dict = {}

    def guardar_datos(self, nombre, apellido, email, contraseña, contraseña_verificacion, saldo):
        if len(contraseña) < 6:
            tk.messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres")
        else:
            if contraseña != contraseña_verificacion:
                tk.messagebox.showerror("Error", "Las contraseñas no coinciden")
            else:
                self.__class__.datos['nombre'] = nombre
                self.__class__.datos['apellido'] = apellido
                self.__class__.datos['email'] = email
                self.__class__.datos['contraseña'] = contraseña_verificacion
                self.__class__.datos["saldo"] = saldo
                tk.messagebox.showinfo("Usuario creado con éxito")
                return True

    def comparar_datos(self, email, contraseña):
        if not self.__class__.datos:
            tk.messagebox.showerror("Acceso denegado", "El correo electrónico o la contraseña son incorrectos")
        else:
            stored_email = self.__class__.datos.get('email')
            stored_password = self.__class__.datos.get('contraseña')

            if stored_email is None or stored_password is None:
                tk.messagebox.showerror("Acceso denegado", "Ingresa la informacion ,no dejes espacios en blanco")
                return False
            elif email == stored_email and contraseña == stored_password:
                tk.messagebox.showinfo("Acceso concedido", "¡Inicio de sesión exitoso!")
                return True
            else:
                tk.messagebox.showerror("Acceso denegado", "El correo electrónico o la contraseña son incorrectos")
                return False

    def obtener_saldo(self):
        saldo = self.__class__.datos.get("saldo")
        return saldo
