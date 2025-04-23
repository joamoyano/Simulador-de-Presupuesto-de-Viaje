import customtkinter as ctk

ctk.set_appearance_mode("light")  # o "dark"
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Simulador de Presupuesto")
root.geometry("500x400")

titulo = ctk.CTkLabel(root, text="Presupuesto Total:", font=("Helvetica", 18))
titulo.pack(pady=20)

entrada = ctk.CTkEntry(root)
entrada.pack(pady=10)

boton = ctk.CTkButton(root, text="Calcular")
boton.pack(pady=20)

root.mainloop()
