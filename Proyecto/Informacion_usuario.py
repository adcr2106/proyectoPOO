import tkinter as tk
from abc import ABC
from tkinter import messagebox


class Usuario(ABC):

    def guardar_datos(self, nombre, apellido, email, contraseña, contraseña_verificacion):
        datos = []
        if len(contraseña) < 6:
            tk.messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres")
        else:
            if contraseña != contraseña_verificacion:
                tk.messagebox.showerror("Error, las contraseñas no coinciden")
            else:
                datos.append(nombre)
                datos.append(apellido)
                datos.append(email)
                datos.append(contraseña_verificacion)
                tk.messagebox.showinfo("Usuario creado con exito")
                print(datos)
