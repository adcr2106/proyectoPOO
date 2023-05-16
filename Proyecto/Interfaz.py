import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from Proyecto.Registrar_usuario import RegisterWindow
from Proyecto.informacion_usuario import Usuario


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.usuario = Usuario()
        self.title("Inicio de sesión")
        self.geometry("600x300")

        fondo_image = Image.open("R.jpeg")
        fondo_photo = ImageTk.PhotoImage(fondo_image)

        # Crear un widget Label para mostrar la imagen de fondo
        fondo_label = tk.Label(self, image=fondo_photo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

        boton_estilo = {
            "background": "blue",  # Color de fondo en azul
            "foreground": "white",  # Color de texto en blanco
            "font": ("Arial", 12),  # Fuente en Arial, tamaño 12
            "width": 20
        }

        # Configurar estilo para las etiquetas
        etiqueta_estilo = {
            "background": "blue",  # Color de fondo en azul
            "foreground": "white",  # Color de texto en blanco
            "font": ("Times New Roman", 12, "bold"),  # Fuente en Times New Roman, tamaño 12, negrita
            "relief": "solid"  # Estilo de relieve sólido
        }

        tk.Label(self, text="Correo electrónico:", **etiqueta_estilo).grid(row=0, column=1, padx=5, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self, text="Contraseña:", **etiqueta_estilo).grid(row=1, column=1, padx=5, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=2, padx=5, pady=5)

        self.login_button = tk.Button(self, text="Iniciar sesión", command=self.login, **boton_estilo)
        self.login_button.grid(row=2, column=2, padx=5, pady=5)

        self.register_button = tk.Button(self, text="Registrarte aquí", command=self.open_register_window,
                                         **boton_estilo)
        self.register_button.grid(row=3, column=2, padx=5, pady=5)

        info_label = tk.Label(
            self,
            text="Tienes una cuenta en Banco PAD? Si no, regístrate y comienza a tener tu dinero asegurado con nosotros",
            wraplength=250,
            justify="right",
            **etiqueta_estilo
        )
        info_label.grid(row=0, column=3, rowspan=4, padx=10, pady=10,sticky="nsew")

        # Mantener una referencia al objeto fondo_photo
        self.fondo_photo = fondo_photo

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
