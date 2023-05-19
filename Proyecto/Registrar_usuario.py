import random
import tkinter as tk
from PIL import ImageTk, Image
from Proyecto.Informacion_usuario import Usuario


class RegisterWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.usuario = Usuario()
        self.title("Registro")
        self.geometry("600x300")


        fondo_image = Image.open("R.jpeg")
        fondo_photo = ImageTk.PhotoImage(fondo_image)

        fondo_label = tk.Label(self, image=fondo_photo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

        info_label = tk.Label(
            self,
            text="Regístrate en Banco PAD y comienza a disfrutar de los beneficios",
            wraplength=250,
            justify="left",
            font=("Times New Roman", 12, "bold"),
            fg="white",
            bg="blue",
            relief="solid"
        )
        info_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        boton_estilo = {
            "background": "blue",
            "foreground": "white",
            "font": ("Arial", 12),
            "width": 15
        }

        etiqueta_estilo = {
            "background": "blue",
            "foreground": "white",
            "font": ("Times New Roman", 12, "bold"),
            "relief": "solid"
        }

        tk.Label(self, text="Nombre:", **etiqueta_estilo).grid(row=0, column=1, padx=5, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self, text="Apellido:", **etiqueta_estilo).grid(row=1, column=1, padx=5, pady=5)
        self.apellido_entry = tk.Entry(self)
        self.apellido_entry.grid(row=1, column=2, padx=5, pady=5)

        tk.Label(self, text="Email:", **etiqueta_estilo).grid(row=2, column=1, padx=5, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=2, column=2, padx=5, pady=5)

        tk.Label(self, text="Contraseña:", **etiqueta_estilo).grid(row=3, column=1, padx=5, pady=5)
        self.contraseña_entry = tk.Entry(self)
        self.contraseña_entry.grid(row=3, column=2, padx=5, pady=5)


        tk.Label(self, text="Confirmar contraseña:", **etiqueta_estilo).grid(row=4, column=1, padx=5, pady=5)
        self.verificar_contraseña_entry = tk.Entry(self)
        self.verificar_contraseña_entry.grid(row=4, column=2, padx=5, pady=5)

        tk.Label(self, text="Saldo de cuenta:", **etiqueta_estilo).grid(row=5, column=1, padx=5, pady=5)
        self.saldo_btn = tk.Entry(self)
        self.saldo_btn.grid(row=5, column=2, padx=5, pady=5)

        guardar_info = tk.Button(self, text="Registrarme", command=self.registrar_usuario, **boton_estilo)
        guardar_info.grid(row=6, column=2, padx=5, pady=5)
        self.fondo_photo = fondo_photo

    def validar_correo(self, correo):
        dominios_permitidos = ["gmail", "outlook"]
        for dominio in dominios_permitidos:
            if dominio in correo:
                return True
        return False

    def registrar_usuario(self):
        nombre  = self.name_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        contraseña = self.contraseña_entry.get()
        verificar_contraseña = self.verificar_contraseña_entry.get()
        saldo = self.saldo_btn.get()

        if not all([nombre, apellido, email, contraseña, verificar_contraseña, saldo]):
            tk.messagebox.showerror("Error", "Todos los campos son obligatorios")
        elif not saldo.isdigit():
            tk.messagebox.showerror("Error", "El saldo debe ser un valor entero")
        elif not self.validar_correo(email):
            tk.messagebox.showerror("Error", "Solo se permiten correos de Gmail y Outlook")
        elif Usuario.correo_existe(email):
            tk.messagebox.showerror("Error", "El correo electrónico ya está en uso")
        elif contraseña != verificar_contraseña:
            tk.messagebox.showerror("Error", "Las contraseñas no coinciden")
        else:
            numero_cuenta = random.randrange(1000000000, 9999999999)
            saldo = int(saldo)
            if self.usuario.guardar_datos(nombre, apellido, email, contraseña, verificar_contraseña, saldo,
                                          numero_cuenta):
                tk.messagebox.showinfo("Registro exitoso", "Se ha registrado con éxito")
                self.destroy()
