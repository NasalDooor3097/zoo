import tkinter as tk
import time
import requests

def alimentar_animales():
    boton_alimentar.config(bg="red", text="¡Alimentando!")
    estructura_tiempo = time.localtime()
    fecha = time.strftime("%Y-%m-%d", estructura_tiempo)
    hora = time.strftime("%H:%M:%S", estructura_tiempo)

    url = "http://localhost:4000/createRegister"
    datos = {"fecha": fecha, "hora": hora}

    try:
        response = requests.post(url, json=datos)
        response.raise_for_status()
        
        if response.status_code == 201:
            print("Registro enviado con éxito")
            obtener_registros()  
        else:
            print(f"Error al enviar el registro: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

    root.after(2000, resetear_boton)

def resetear_boton():
    boton_alimentar.config(bg="lightgray", text="Alimentar Animales")

def obtener_registros():
    url = "http://localhost:4000/getRegisters"

    try:
        response = requests.get(url)
        response.raise_for_status()
        registros = response.json()

        for widget in frame.winfo_children():
            widget.destroy()

    
        encabezados = ["Fecha", "Hora"]
        for i, encabezado in enumerate(encabezados):
            tk.Label(frame, text=encabezado, font=("Arial", 12, "bold"), borderwidth=1, relief="solid").grid(row=0, column=i, padx=5, pady=5)

        for i, registro in enumerate(registros, start=1):
            tk.Label(frame, text=registro["fecha"], borderwidth=1, relief="solid").grid(row=i, column=0, padx=5, pady=5)
            tk.Label(frame, text=registro["hora"], borderwidth=1, relief="solid").grid(row=i, column=1, padx=5, pady=5)

    except requests.exceptions.RequestException as e:
        error_label.config(text=f"Error al obtener registros: {e}")


root = tk.Tk()
root.title("Sistema de Alimentación de Animalitos 🐾")
root.geometry("700x700")

boton_alimentar = tk.Button(root, text="Alimentar Animales", command=alimentar_animales, font=("Arial", 14))
boton_alimentar.pack(pady=10)

frame = tk.Frame(root)  
frame.pack(pady=10)

btn_obtener = tk.Button(root, text="Obtener Registros", command=obtener_registros, font=("Arial", 12))
btn_obtener.pack(pady=10)

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()