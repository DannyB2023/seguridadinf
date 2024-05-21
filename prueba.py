#!/usr/bin/env python
# coding: utf-8

# In[22]:


import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Función para desencriptar un mensaje usando el cifrado César
def desencriptar(mensaje_encriptado, clave):
    mensaje_desencriptado = ""
    for char in mensaje_encriptado:
        if char.isalpha():
            if char.islower():
                mensaje_desencriptado += chr((ord(char) - ord('a') - clave) % 26 + ord('a'))
            else:
                mensaje_desencriptado += chr((ord(char) - ord('A') - clave) % 26 + ord('A'))
        else:
            mensaje_desencriptado += char
    return mensaje_desencriptado

# Función para limpiar los campos de entrada
def limpiar_campos():
    texto_entry.delete(0, tk.END)
    resultado_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    clave_entry.delete(0, tk.END)

# Función para enviar el correo electrónico con el mensaje encriptado y la clave
def enviar_correo(mensaje_encriptado, clave):
    try:
        # Configurar el servidor SMTP y enviar el correo electrónico
        remitente = 'tu_correo@gmail.com'  # Pon aquí tu correo electrónico
        contraseña = 'tu_contraseña'  # Pon aquí tu contraseña
        destinatario = email_entry.get()

        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = destinatario
        msg['Subject'] = 'Mensaje Encriptado y Clave'

        # Cuerpo del correo con el mensaje encriptado y la clave
        cuerpo_correo = f"Mensaje encriptado:\n\n{mensaje_encriptado}\n\nClave para desencriptar: {clave}"
        msg.attach(MIMEText(cuerpo_correo, 'plain'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(remitente, contraseña)
            servidor.sendmail(remitente, destinatario, msg.as_string())

        messagebox.showinfo("Éxito", "Correo enviado exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al enviar el correo: {str(e)}")

# Función para encriptar el mensaje ingresado y enviarlo por correo electrónico
def encriptar_y_enviar():
    mensaje = texto_entry.get()
    clave = clave_entry.get()
    
    if not mensaje or not clave:
        messagebox.showwarning("Advertencia", "Por favor, ingrese el mensaje y la clave.")
        return

    try:
        # Encriptar el mensaje usando el cifrado César
        mensaje_encriptado = encriptar(mensaje, int(clave))

        # Enviar el mensaje encriptado y la clave por correo electrónico
        enviar_correo(mensaje_encriptado, clave)
    except Exception as e:
        messagebox.showerror("Error", f"Error al encriptar y enviar el mensaje: {str(e)}")

# Función para desencriptar el mensaje ingresado
def desencriptar_mensaje():
    mensaje_encriptado = texto_entry.get()
    clave = clave_entry.get()
    
    if not mensaje_encriptado or not clave:
        messagebox.showwarning("Advertencia", "Por favor, ingrese el mensaje encriptado y la clave.")
        return

    try:
        # Desencriptar el mensaje usando el cifrado César
        mensaje_desencriptado = desencriptar(mensaje_encriptado, int(clave))

        # Mostrar el mensaje desencriptado
        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(0, mensaje_desencriptado)
    except Exception as e:
        messagebox.showerror("Error", f"Error al desencriptar el mensaje: {str(e)}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Encriptar y Desencriptar Mensajes")

# Estilos para los labels
label_estilo = {
    "bg": "lightgrey",
    "font": ("Helvetica", 12, "bold")
}

# Crear y colocar widgets
tk.Label(ventana, text="Mensaje (Encriptado/Desencriptado):", **label_estilo).grid(row=0, column=0, padx=10, pady=10)
texto_entry = tk.Entry(ventana, width=50)
texto_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Clave:", **label_estilo).grid(row=1, column=0, padx=10, pady=10)
clave_entry = tk.Entry(ventana, width=50)
clave_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Enviar a (Email):", **label_estilo).grid(row=2, column=0, padx=10, pady=10)
email_entry = tk.Entry(ventana, width=50)
email_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(ventana, text="Resultado:", **label_estilo).grid(row=3, column=0, padx=10, pady=10)
resultado_entry = tk.Entry(ventana, width=50)
resultado_entry.grid(row=3, column=1, padx=10, pady=10)

# Estilos para los botones
boton_estilo = {
    "bd": 4,
    "relief": tk.RAISED,
    "bg": "lightblue",
    "activebackground": "lightgreen",
    "font": ("Helvetica", 12, "bold")
}

encriptar_boton = tk.Button(ventana, text="Encriptar y Enviar", command=encriptar_y_enviar, **boton_estilo)
encriptar_boton.grid(row=4, column=0, padx=10, pady=10)

desencriptar_boton = tk.Button(ventana, text="Desencriptar", command=desencriptar_mensaje, **boton_estilo)
desencriptar_boton.grid(row=4, column=1, padx=10, pady=10)

limpiar_boton = tk.Button(ventana, text="Limpiar Datos", command=limpiar_campos, **boton_estilo)
limpiar_boton.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()


# In[ ]:





# In[ ]:




