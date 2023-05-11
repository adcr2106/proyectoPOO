import tkinter as tk
from Proyecto.Informacion_usuario import Usuario


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Inicio de sesión")
        self.geometry("500x300")

        tk.Label(self, text="Correo electrónico:").grid(row=0, column=1, padx=5, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self, text="Contraseña:").grid(row=1, column=1, padx=5, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=2, padx=5, pady=5)

        self.login_button = tk.Button(self, text="Iniciar sesión", command=self.login, width=20)
        self.login_button.grid(row=2, column=2, padx=5, pady=5)

        self.register_button = tk.Button(self, text="Registrarte aquí", command=self.open_register_window, width=20)
        self.register_button.grid(row=3, column=2, padx=5, pady=5)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def open_register_window(self):
        register_window = RegisterWindow(self)
        register_window.mainloop()


class RegisterWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

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

        guardar_info = tk.Button(self, text="Registrarme", command=self.registrar_usuario, width=20)
        guardar_info.grid(row=5, column=2, padx=5, pady=5)

    def registrar_usuario(self):
        nombre = self.name_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        contraseña = self.contraseña_entry.get()
        verificar_contraseña = self.verificar_contraseña_entry.get()
        Usuario.guardar_datos(self, nombre, apellido, email, contraseña, verificar_contraseña)


class AccountWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cuenta bancaria")
        self.geometry("300x200")
        tk.Label(self, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        # Agregar elementos de la interfaz de usuario de la cuenta bancaria aquí, pendiente


if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()
