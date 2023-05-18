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
            "background": "blue",
            "foreground": "white",
            "font": ("Arial", 12),
            "width": 20
        }

        etiqueta_estilo = {
            "background": "blue",
            "foreground": "white",
            "font": ("Times New Roman", 12, "bold"),
            "relief": "solid"
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
        info_label.grid(row=0, column=3, rowspan=4, padx=10, pady=10, sticky="nsew")
        self.fondo_photo = fondo_photo

    def open_register_window(self):
        register_window = RegisterWindow(self)
        register_window.mainloop()

    def login(self):
        email = self.email_entry.get()
        contraseña = self.password_entry.get()
        if self.usuario.validar_datos(email, contraseña):
            self.destroy()
            AccountWindow()


class AccountWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.usuario = Usuario()
        self.title("Cuenta bancaria")
        self.geometry("600x300")
        self.configure(bg="blue")

        nombre_usuario = self.usuario.datos.get("nombre")
        apellido_usuario = self.usuario.datos.get("apellido")

        encabezado_texto = f"Bienvenido a BANCO PAD, {nombre_usuario}, {apellido_usuario}!"
        encabezado = tk.Label(self, text=encabezado_texto, font=("Arial", 16), bg="blue", fg="white")
        encabezado.pack(pady=20)

        ver_saldo_btn = tk.Button(self, text="Ver saldo", width=20, command=self.ver_saldo)
        ver_saldo_btn.pack(side=tk.LEFT, padx=10, pady=10)

        hacer_transferencia_btn = tk.Button(self, text="Hacer transferencia", width=20, command=self.hacer_transferencia)
        hacer_transferencia_btn.pack(side=tk.LEFT, padx=10, pady=10)

        cerrar_sesion_btn = tk.Button(self, text="Cerrar sesión", width=20, command=self.cerrar_sesion, bg="red",
                                      fg="white")
        cerrar_sesion_btn.pack(side=tk.RIGHT, padx=10, pady=10)

    def ver_saldo(self):
        saldo = self.usuario.obtener_saldo()
        messagebox.showinfo("Saldo", f"Tu saldo es de: {saldo}$")

    def hacer_transferencia(self):
        transferencia_window = TransferenciaWindow(self)
        transferencia_window.mainloop()

    def cerrar_sesion(self):
        self.destroy()
        LoginWindow()


class AccountWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.usuario = Usuario()
        self.title("Cuenta bancaria")
        self.geometry("600x300")
        self.configure(bg="blue")

        nombre_usuario = self.usuario.datos.get("nombre")
        apellido_usuario = self.usuario.datos.get("apellido")

        encabezado_texto = f"Bienvenido a BANCO PAD, {nombre_usuario}, {apellido_usuario}!"
        encabezado = tk.Label(self, text=encabezado_texto, font=("Arial", 16), bg="blue", fg="white")
        encabezado.pack(pady=20)

        ver_saldo_btn = tk.Button(self, text="Ver saldo", width=20, command=self.ver_saldo)
        ver_saldo_btn.pack(side=tk.LEFT, padx=10, pady=10)

        hacer_transferencia_btn = tk.Button(self, text="Hacer transferencia", width=20, command=self.hacer_transferencia)
        hacer_transferencia_btn.pack(side=tk.LEFT, padx=10, pady=10)

        cerrar_sesion_btn = tk.Button(self, text="Cerrar sesión", width=20, command=self.cerrar_sesion, bg="red",
                                      fg="white")
        cerrar_sesion_btn.pack(side=tk.RIGHT, padx=10, pady=10)

    def ver_saldo(self):
        saldo = self.usuario.obtener_saldo()
        messagebox.showinfo("Saldo", f"Tu saldo es de: {saldo}$")

    def hacer_transferencia(self):
        transferencia_window = TransferenciaWindow(self)
        transferencia_window.mainloop()

    def cerrar_sesion(self):
        self.destroy()
        LoginWindow()


class TransferenciaWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.usuario = parent.usuario
        self.title("Realizar transferencia")
        self.geometry("600x300")
        self.configure(bg="blue")

        nombre_usuario = self.usuario.datos.get("nombre")
        apellido_usuario = self.usuario.datos.get("apellido")

        encabezado_texto = f"Bienvenido a BANCO PAD, {nombre_usuario}, {apellido_usuario}!"
        encabezado = tk.Label(self, text=encabezado_texto, font=("Arial", 16), bg="blue", fg="white")
        encabezado.pack(pady=20)

        tk.Label(self, text="Destinatario:", font=("Arial", 12), bg="blue", fg="white").pack()
        self.destinatario_entry = tk.Entry(self, font=("Arial", 12))
        self.destinatario_entry.pack()

        tk.Label(self, text="Monto:", font=("Arial", 12), bg="blue", fg="white").pack()
        self.monto_entry = tk.Entry(self, font=("Arial", 12))
        self.monto_entry.pack()

        transferir_button = tk.Button(self, text="Transferir", command=self.transferir,
                                      bg="blue", fg="white", font=("Arial", 12))
        transferir_button.pack()

        volver_button = tk.Button(self, text="Volver", command=self.volver,
                                  bg="blue", fg="white", font=("Arial", 12))
        volver_button.pack()
    def transferir(self):
        destinatario = self.destinatario_entry.get()
        monto = self.monto_entry.get()

        # Verificar si el destinatario existe y si el monto es válido
        if not destinatario or not monto:
            messagebox.showerror("Error", "Debe ingresar el destinatario y el monto de la transferencia.")
        elif not monto.isdigit():
            messagebox.showerror("Error", "El monto debe ser un valor numérico.")
        else:
            monto = int(monto)
            saldo_actual = self.usuario.obtener_saldo()

            # Verificar si hay suficiente saldo para la transferencia
            if monto > saldo_actual:
                messagebox.showerror("Error", "No tienes suficiente saldo para realizar la transferencia.")
            else:
                # Restar el monto transferido al saldo actual
                saldo_nuevo = saldo_actual - monto
                self.usuario.actualizar_saldo(saldo_nuevo)

                # Realizar lógica adicional para completar la transferencia
                destinatario_usuario = Usuario.obtener_usuario_por_correo(destinatario)
                if destinatario_usuario:
                    saldo_destinatario = destinatario_usuario.obtener_saldo()
                    saldo_destinatario += monto
                    destinatario_usuario.actualizar_saldo(saldo_destinatario)
                    messagebox.showinfo("Transferencia", f"Se ha transferido {monto}$ a {destinatario}.")
                else:
                    messagebox.showerror("Error", "El destinatario no existe.")

    def volver(self):
        self.destroy()


if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()


