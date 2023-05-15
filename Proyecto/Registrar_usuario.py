import tkinter as tk
from Proyecto.informacion_usuario import Usuario


class RegisterWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.usuario = Usuario()
        self.title("Registro")
        self.geometry("600x300")

        tk.Label(self, text="Nombre:").grid(row=0, column=1, padx=5, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self, text="Apellido:").grid(row=1, column=1, padx=5, pady=5)
        self.apellido_entry = tk.Entry(self)
        self.apellido_entry.grid(row=1, column=2, padx=5, pady=5)

        tk.Label(self, text="Email:").grid(row=2, column=1, padx=5, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=2, column=2, padx=5, pady=5)

        tk.Label(self, text="Contraseña:").grid(row=3, column=1, padx=5, pady=5)
        self.contraseña_entry = tk.Entry(self)
        self.contraseña_entry.grid(row=3, column=2, padx=5, pady=5)

        tk.Label(self, text="Confirmar contraseña :").grid(row=4, column=1, padx=5, pady=5)
        self.verificar_contraseña_entry = tk.Entry(self)
        self.verificar_contraseña_entry.grid(row=4, column=2, padx=5, pady=5)

        tk.Label(self, text="Saldo de cuenta").grid(row=5, column=1, padx=5, pady=5)
        self.saldo_btn = tk.Entry(self)
        self.saldo_btn.grid(row=5, column=2, padx=5, pady=5)

        guardar_info = tk.Button(self, text="Registrarme", command=self.registrar_usuario, width=20)
        guardar_info.grid(row=6, column=2, padx=5, pady=5)

    def registrar_usuario(self):
        nombre = self.name_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        contraseña = self.contraseña_entry.get()
        verificar_contraseña = self.verificar_contraseña_entry.get()
        saldo = self.saldo_btn.get()

        if not saldo.isdigit():
            tk.messagebox.showerror("Error", "El saldo debe ser un valor entero")
        else:
            if self.usuario.guardar_datos(nombre, apellido, email, contraseña, verificar_contraseña, saldo):
                self.destroy()
