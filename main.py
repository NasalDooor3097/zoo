import tkinter as tk

def alimentar_animales():
    boton_alimentar.config(bg="red", text="¡Alimentando!")
    root.update()
    root.after(2000, resetear_boton)  # Después de 2 segundos vuelve a su estado normal

def resetear_boton():
    boton_alimentar.config(bg="SystemButtonFace", text="Alimentar Animales")

root = tk.Tk()
root.title("Sistema de Alimentación Manual")

boton_alimentar = tk.Button(root, text="Alimentar Animales", command=alimentar_animales, font=("Arial", 14))
boton_alimentar.pack(pady=20)

root.mainloop()