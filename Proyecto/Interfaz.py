import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from Proyecto.Registrar_usuario import RegisterWindow
from Proyecto.informacion_usuario import Usuario


class PrincipalWindow(tk.Tk):
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

        encabezado_texto = f"Bienvenido a BANCO PAD, {nombre_usuario} {apellido_usuario}!"
        encabezado = tk.Label(self, text=encabezado_texto, font=("Arial", 16), bg="blue", fg="white")
        encabezado.pack(pady=20)

        ver_saldo_btn = tk.Button(self, text="Ver saldo", width=20, command=self.ver_saldo)
        ver_saldo_btn.pack(pady=10, anchor="center")

        hacer_transferencia_btn = tk.Button(self, text="Hacer transferencia", width=20,
                                            command=self.hacer_transferencia)
        hacer_transferencia_btn.pack(pady=10, anchor="center")

        hacer_retiro_btn = tk.Button(self, text="Hacer retiro", width=20, command=self.hacer_retiro)
        hacer_retiro_btn.pack(pady=10, anchor="center")

        cerrar_sesion_btn = tk.Button(self, text="Cerrar sesión", width=20, command=self.cerrar_sesion, bg="red",
                                      fg="white")
        cerrar_sesion_btn.pack(side=tk.LEFT, padx=10, pady=10, anchor="sw")

        numero_cuenta = self.usuario.datos.get("numero_cuenta")
        numero_cuenta_label = tk.Label(self, text=f"# de cuenta: {numero_cuenta}", font=("Arial", 12), bg="blue",
                                       fg="white")
        numero_cuenta_label.place(relx=1, rely=1, anchor="se", x=-10, y=-10)

        actualizar_datos_btn = tk.Button(self, text="Actualizar Datos", width=20, command=self.actualizar_datos)
        actualizar_datos_btn.pack(pady=10, anchor="center")

    def ver_saldo(self):
        saldo = self.usuario.obtener_saldo()
        messagebox.showinfo("Saldo", f"Tu saldo es de: {saldo}$")

    def hacer_transferencia(self):
        transferencia_window = TransferenciaWindow(self)
        transferencia_window.mainloop()

    def hacer_retiro(self):
        retiro_window = VentanaRetiro(self)
        retiro_window.mainloop()

    def actualizar_datos(self):
        actualizar_window = ActualizarDatosWindow(self)
        actualizar_window.mainloop()

    def cerrar_sesion(self):
        self.destroy()
        PrincipalWindow()


class TransferenciaWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.usuario = parent.usuario
        self.title("Realizar transferencia")
        self.geometry("600x300")
        self.configure(bg="blue")

        tk.Label(self, text="Destinatario:", font=("Arial", 12), bg="blue", fg="white").pack()
        self.destinatario_entry = tk.Entry(self, font=("Arial", 12))
        self.destinatario_entry.pack()

        tk.Label(self, text="Monto:", font=("Arial", 12), bg="blue", fg="white").pack()
        self.monto_entry = tk.Entry(self, font=("Arial", 12))
        self.monto_entry.pack()

        transferir_button = tk.Button(self, text="Transferir", command=self.transferir, bg="blue", fg="white",
                                      font=("Arial", 12))
        transferir_button.pack()
        volver_button = tk.Button(self, text="Volver", command=self.volver, bg="blue", fg="white", font=("Arial", 12))
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
                self.usuario.realizar_transferencia(destinatario, monto)
                messagebox.showinfo("Transferencia exitosa",
                                    f"Se ha transferido {monto}$ al destinatario {destinatario}.")
                self.destinatario_entry.delete(0, tk.END)
                self.monto_entry.delete(0, tk.END)

    def volver(self):
        self.destroy()


class VentanaRetiro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.usuario = parent.usuario
        self.title("Retirar dinero")
        self.geometry("600x300")
        self.configure(bg="blue")

        tk.Label(self, text="Monto a retirar:", font=("Arial", 12), bg="blue", fg="white").pack()
        self.monto_entry = tk.Entry(self, font=("Arial", 12))
        self.monto_entry.pack()

        retirar_button = tk.Button(self, text="Retirar", command=self.retirar, bg="blue", fg="white",
                                   font=("Arial", 12))
        retirar_button.pack()
        volver_button = tk.Button(self, text="Volver", command=self.volver, bg="blue", fg="white",
                                  font=("Arial", 12))
        volver_button.pack()

    def retirar(self):
        monto = self.monto_entry.get()

        # Verificar si el monto es válido
        if not monto:
            messagebox.showerror("Error", "Debe ingresar el monto a retirar.")
        elif not monto.isdigit():
            messagebox.showerror("Error", "El monto debe ser un valor numérico.")
        else:
            monto = int(monto)
            saldo_actual = self.usuario.obtener_saldo()

            # Verificar si hay suficiente saldo para el retiro
            if monto > saldo_actual:
                messagebox.showerror("Error", "No tienes suficiente saldo para realizar el retiro.")
            else:
                self.monto_entry.delete(0, tk.END)
                Ventana_despues_click_RETIRAR()

    def volver(self):
        self.destroy()


class Ventana_despues_click_RETIRAR(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Retiro sencillo")
        self.geometry("600x600")
        self.configure(bg="blue")

        mensaje = "Para retirar es muy sencillo.\nDirígete a un corresponsal bancario de Bancolombia y muestra este código QR.\nEl retiro se hará de acuerdo al monto que decidas."

        mensaje_label = tk.Label(self, text=mensaje, font=("Arial", 12), bg="blue", fg="white")
        mensaje_label.pack(pady=50)

        # Agregar la imagen
        imagen_path = "C:/Users/Daniel Lasso/PycharmProjects/proyectoPOO/Proyecto/qr_image.png"
        self.imagen = self.resize_image(imagen_path, width=300, height=300)
        imagen_label = tk.Label(self, image=self.imagen, bg="blue")
        imagen_label.pack()

        volver_button = tk.Button(self, text="Volver", command=self.volver, bg="blue", fg="white", font=("Arial", 12))
        volver_button.pack(side=tk.LEFT, padx=10, pady=10)

    def volver(self):
        self.destroy()

    def resize_image(self, path, width, height):
        original_image = Image.open(path)
        resized_image = original_image.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)


class ActualizarDatosWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.usuario = Usuario()
        self.title("Actualización de datos")
        self.geometry("600x300")

        fondo_image = Image.open("R.jpeg")
        fondo_photo = ImageTk.PhotoImage(fondo_image)

        fondo_label = tk.Label(self, image=fondo_photo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

        info_label = tk.Label(
            self,
            text="Actualiza tus datos de manera rápida",
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

        guardar_info = tk.Button(self, text="Actualizar", command=self.actualizar_usuario, **boton_estilo)
        guardar_info.grid(row=6, column=2, padx=5, pady=5)
        self.fondo_photo = fondo_photo

    def validar_correo(self, correo):
        dominios_permitidos = ["gmail", "outlook"]
        for dominio in dominios_permitidos:
            if dominio in correo:
                return True
        return False

    def actualizar_usuario(self):
        nombre = self.name_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        contraseña = self.contraseña_entry.get()
        verificar_contraseña = self.verificar_contraseña_entry.get()

        if not all([nombre, apellido, email, contraseña, verificar_contraseña]):
            tk.messagebox.showerror("Error", "Todos los campos son obligatorios")
        elif not self.validar_correo(email):
            tk.messagebox.showerror("Error", "Solo se permiten correos de Gmail y Outlook")
        elif Usuario.correo_existe(email):
            tk.messagebox.showerror("Error", "El correo electrónico ya está en uso")
        elif contraseña != verificar_contraseña:
            tk.messagebox.showerror("Error", "Las contraseñas no coinciden")
        else:
            if self.usuario.actualizar_datos(nombre, apellido, email, contraseña, verificar_contraseña):
                tk.messagebox.showinfo("Actualización Exitosa", "Se ha actualizado los datos con éxito")
                self.destroy()


if __name__ == "__main__":
    login_window = PrincipalWindow()
    login_window.mainloop()
