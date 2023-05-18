import re
import tkinter as tk


class Usuario:
    datos = {} #Esto será variable de clase para que todos los metodos puedan acceder a la info

    def guardar_datos(self, nombre, apellido, email, contraseña, contraseña_verificacion, saldo, numero_cuenta):
        if not re.match("^[a-zA-Z]+$", nombre):
            tk.messagebox.showerror("Error", "El nombre solo debe contener letras")
        elif not re.match("^[a-zA-Z]+$", apellido):
            tk.messagebox.showerror("Error", "El apellido solo debe contener letras")
        elif len(contraseña) < 6:
            tk.messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres")
        elif contraseña != contraseña_verificacion:
            tk.messagebox.showerror("Error", "Las contraseñas no coinciden")
        elif 'email' in self.__class__.datos and self.__class__.datos['email'] == email:
            tk.messagebox.showerror("Error", "El correo electrónico ya está registrado")
        else:
            self.__class__.datos['nombre'] = nombre
            self.__class__.datos['apellido'] = apellido
            self.__class__.datos['email'] = email
            self.__class__.datos['contraseña'] = contraseña_verificacion
            self.__class__.datos["saldo"] = saldo
            self.__class__.datos["numero_cuenta"] = numero_cuenta
            return True

    @classmethod
    def correo_existe(cls, email):
        return email in cls.datos

    def validar_datos(self, email, contraseña):
        if not self.__class__.datos:
            tk.messagebox.showerror("Acceso denegado", "El correo electrónico o la contraseña son incorrectos")
        else:
            stored_email = self.__class__.datos.get('email')
            stored_password = self.__class__.datos.get('contraseña')

            if stored_email is None or stored_password is None:
                tk.messagebox.showerror("Acceso denegado", "Ingresa la información, no dejes espacios en blanco")
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

    def actualizar_saldo(self, nuevo_saldo):
        self.__class__.datos["saldo"] = nuevo_saldo

    @staticmethod #No requiere tener una instancia de la clase para funcionar correctamente.
    def obtener_usuario_por_correo(correo):
            if correo in Usuario.datos:
                return Usuario()
            else:
                return None

