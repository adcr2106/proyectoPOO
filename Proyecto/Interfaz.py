import tkinter as tk
from tkinter import messagebox

from Proyecto.Registrar_usuario import RegisterWindow
from Proyecto.informacion_usuario import Usuario


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.usuario = Usuario()
        self.title("Inicio de sesión")
        self.geometry("600x300")

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

    def open_register_window(self):
        register_window = RegisterWindow(self)
        register_window.mainloop()

    def login(self):
        email = self.email_entry.get()
        contraseña = self.password_entry.get()
        if self.usuario.comparar_datos(email, contraseña):
            self.destroy()
            AccountWindow()


class AccountWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.usuario = Usuario()
        self.title("Cuenta bancaria")
        self.geometry("600x300")
        self.configure(bg="blue")  # Establecer el color de fondo en azul

        # Obtener el nombre del usuario del diccionario datos
        nombre_usuario = self.usuario.datos.get("nombre")
        apellido_usuario = self.usuario.datos.get("apellido")

        # Agregar un encabezado con el nombre del usuario
        encabezado_texto = f"Bienvenido a BANCO PAD, {nombre_usuario}, {apellido_usuario}!"
        encabezado = tk.Label(self, text=encabezado_texto, font=("Arial", 16), bg="blue", fg="white")
        encabezado.pack(pady=20)

        ver_saldo_btn = tk.Button(self, text="Ver saldo", width=20, command=self.ver_saldo)
        ver_saldo_btn.pack()

        cerrar_sesion_btn = tk.Button(self, text="Cerrar sesión", width=20, command=self.cerrar_sesion, bg="red", fg="white")
        cerrar_sesion_btn.place(relx=1, rely=1, anchor="se", x=-10, y=-10)

    def ver_saldo(self):
        # Lógica para mostrar el saldo
        saldo = self.usuario.obtener_saldo()  # Ejemplo: función para obtener el saldo del usuario
        messagebox.showinfo("Saldo", f"Tu saldo es de: {saldo}$")

    def cerrar_sesion(self):
        # Destruir la ventana actual
        self.destroy()

        # Volver a la pantalla de inicio de sesión
        LoginWindow()




if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()
