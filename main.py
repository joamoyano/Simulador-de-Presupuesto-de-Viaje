import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from calculos import calcular_presupuesto

# Configuración
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

COLOR_FONDO = "#A4B8C4"
COLOR_INPUT = "#FCFAFA"
COLOR_TEXTO = "#222222"
COLOR_BOTON = "#6E8387"
COLOR_PANEL = "#C8D3D5"

app = ctk.CTk()
app.title("Simulador de Presupuesto de Viaje")
app.geometry("1000x650")
app.configure(fg_color=COLOR_FONDO)

canvas_widget = None
imagen_widget = None

# --- Panel Izquierdo: Imagen o gráfico ---
panel_izquierdo = ctk.CTkFrame(app, width=400, height=650, corner_radius=0)
panel_izquierdo.pack(side="left", fill="both")

imagen_inicial = Image.open("assets/imglogo.jpg")
imagen_inicial = imagen_inicial.resize((400, 650))
imagen_tk = ImageTk.PhotoImage(imagen_inicial)

imagen_widget = ctk.CTkLabel(panel_izquierdo, image=imagen_tk, text="")
imagen_widget.pack(expand=True)

# --- Panel Derecho: Formulario ---
panel_derecho = ctk.CTkFrame(app, corner_radius=0, fg_color=COLOR_FONDO)
panel_derecho.pack(side="left", fill="both", expand=True, padx=30, pady=30)

def crear_input(frame, texto):
    label = ctk.CTkLabel(frame, text=texto, font=("Helvetica", 15), text_color=COLOR_TEXTO)
    label.pack(anchor="w", pady=(8, 2))
    entry = ctk.CTkEntry(frame, height=35, font=("Helvetica", 14), fg_color=COLOR_INPUT, text_color="black")
    entry.pack(fill="x")
    return entry

titulo = ctk.CTkLabel(panel_derecho, text="Simulador de Presupuesto", font=("Helvetica", 24, "bold"), text_color=COLOR_TEXTO)
titulo.pack(pady=(10, 20))

entrada_presupuesto = crear_input(panel_derecho, "Presupuesto total (ARS):")
entrada_dias = crear_input(panel_derecho, "Cantidad de días de viaje:")
entrada_alojamiento = crear_input(panel_derecho, "Alojamiento (ARS):")
entrada_transporte = crear_input(panel_derecho, "Transporte (ARS):")
entrada_comida = crear_input(panel_derecho, "Gasto diario en comida:")
entrada_ocio = crear_input(panel_derecho, "Gasto diario en ocio / actividades:")

resultado_label = ctk.CTkLabel(panel_derecho, text="", font=("Helvetica", 14), text_color=COLOR_TEXTO, wraplength=450)
resultado_label.pack(pady=10)

# --- Mostrar gráfico embebido ---
def mostrar_grafico_embed(gastos):
    global canvas_widget, imagen_widget

    if imagen_widget:
        imagen_widget.destroy()
        imagen_widget = None
    if canvas_widget:
        canvas_widget.get_tk_widget().destroy()

    etiquetas = list(gastos.keys())
    valores = list(gastos.values())

    fig, ax = plt.subplots(figsize=(4, 4))
    colores = plt.get_cmap('Set3').colors
    ax.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140, colors=colores)
    ax.axis('equal')

    canvas = FigureCanvasTkAgg(fig, master=panel_izquierdo)
    canvas.draw()
    canvas_widget = canvas
    canvas.get_tk_widget().pack(expand=True)

# --- Cálculo ---
def calcular():
    resultado_label.configure(text="")
    ok, mensaje = calcular_presupuesto(
        entrada_presupuesto.get(),
        entrada_dias.get(),
        entrada_alojamiento.get(),
        entrada_transporte.get(),
        entrada_comida.get(),
        entrada_ocio.get()
    )
    resultado_label.configure(text=mensaje)

    if ok:
        try:
            gastos = {
                'Alojamiento': float(entrada_alojamiento.get()),
                'Transporte': float(entrada_transporte.get()),
                'Comida': float(entrada_comida.get()) * int(entrada_dias.get()),
                'Ocio': float(entrada_ocio.get()) * int(entrada_dias.get()),
            }
            presupuesto_total = float(entrada_presupuesto.get())
            sobrante = presupuesto_total - sum(gastos.values())
            if sobrante > 0:
                gastos['Sobrante'] = sobrante

            mostrar_grafico_embed(gastos)
        except:
            print("Error generando gráfico.")

# --- Botones ---
botones_frame = ctk.CTkFrame(panel_derecho, fg_color="transparent")
botones_frame.pack(pady=15)

ctk.CTkButton(botones_frame, text="Calcular", command=calcular, font=("Helvetica", 15), fg_color=COLOR_BOTON, width=130).pack(side="left", padx=10)
ctk.CTkButton(botones_frame, text="Salir", command=app.destroy, font=("Helvetica", 15), fg_color=COLOR_BOTON, width=130).pack(side="left", padx=10)

app.mainloop()
