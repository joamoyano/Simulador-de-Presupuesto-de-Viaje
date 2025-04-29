import customtkinter as ctk
from PIL import Image
from calculos import calcular_presupuesto
from graficos import generar_grafico_torta, generar_grafico_barras, generar_grafico_linea

# --- Configuración general ---
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

COLOR_FONDO = "#FCFAFA"
COLOR_INPUT = "#FCFAFA"
COLOR_SECCION = "#A4B8C4"
COLOR_TEXTO = "#222222"
COLOR_BOTON = "#6E8387"
COLOR_PANEL = "#F0F2F5"

app = ctk.CTk()
app.title("Simulador de Presupuesto de Viaje")
app.geometry("1200x750")
app.configure(fg_color=COLOR_FONDO)

# --- Paneles principales ---
panel_izquierdo = ctk.CTkFrame(app, width=500, height=750, corner_radius=10, border_width=1, border_color="#6E8387")
panel_izquierdo.pack(side="left", fill="both")

panel_derecho = ctk.CTkFrame(app, corner_radius=10, border_width=1, border_color="#6E8387", fg_color=COLOR_SECCION)
panel_derecho.pack(side="left", fill="both", expand=True, padx=20, pady=20)

# --- Imagen inicial ---
imagen_inicial = Image.open("assets/MontaIMG.png").resize((500, 750))
imagen_tk = ctk.CTkImage(light_image=imagen_inicial, size=(500, 750))
imagen_widget = ctk.CTkLabel(panel_izquierdo, image=imagen_tk, text="")
imagen_widget.pack(expand=True)

# --- Formulario ---
def crear_input(frame, texto):
    label = ctk.CTkLabel(frame, text=texto, font=("Poppins", 15), text_color=COLOR_TEXTO)
    label.pack(anchor="center", pady=(5, 2))
    entry = ctk.CTkEntry(frame, width=300, height=40, font=("Poppins", 14), fg_color=COLOR_INPUT, text_color="black")
    entry.pack(pady=5, anchor="center")
    return entry

titulo = ctk.CTkLabel(
    panel_derecho,
    text="Simulador de Presupuesto",
    font=("Poppins", 28, "bold"),
    text_color=COLOR_TEXTO,
    anchor="center"
)
titulo.pack(pady=(10, 20))

entrada_presupuesto = crear_input(panel_derecho, "Presupuesto total (ARS):")
entrada_dias = crear_input(panel_derecho, "Cantidad de días de viaje:")
entrada_alojamiento = crear_input(panel_derecho, "Alojamiento (ARS):")
entrada_transporte = crear_input(panel_derecho, "Transporte (ARS):")
entrada_comida = crear_input(panel_derecho, "Gasto diario en comida:")
entrada_ocio = crear_input(panel_derecho, "Gasto diario en ocio / actividades:")

resultado_label = ctk.CTkLabel(panel_derecho, text="", font=("Poppins", 14), text_color=COLOR_TEXTO, wraplength=450, justify="left")
resultado_label.pack(pady=10)

# --- Botones ---
botones_frame = ctk.CTkFrame(panel_derecho, fg_color="transparent")
botones_frame.pack(pady=10)

def destruir_layout_inicial():
    panel_derecho.destroy()
    panel_izquierdo.destroy()

def mostrar_layout_resultado(gastos, presupuesto_total, dias, gasto_comida, gasto_ocio):
    layout_resultado = ctk.CTkFrame(app, fg_color=COLOR_PANEL)
    layout_resultado.pack(fill="both", expand=True)

    titulo_resultado = ctk.CTkLabel(layout_resultado, text="Resultado del Presupuesto", font=("Poppins", 28, "bold"), text_color=COLOR_TEXTO)
    titulo_resultado.pack(pady=20)

    resumen_frame = ctk.CTkFrame(layout_resultado, fg_color="transparent")
    resumen_frame.pack(pady=10)

    ctk.CTkLabel(resumen_frame, text=f"Total presupuestado: ${presupuesto_total:,.2f}", font=("Poppins", 16), text_color=COLOR_TEXTO).pack(side="left", padx=20)
    ctk.CTkLabel(resumen_frame, text=f"Gasto total: ${sum(gastos.values()):,.2f}", font=("Poppins", 16), text_color=COLOR_TEXTO).pack(side="left", padx=20)
    ctk.CTkLabel(resumen_frame, text=f"Sobrante: ${presupuesto_total - sum(gastos.values()):,.2f}", font=("Poppins", 16), text_color=COLOR_TEXTO).pack(side="left", padx=20)

    graficos_frame = ctk.CTkFrame(layout_resultado, fg_color="transparent")
    graficos_frame.pack(expand=True, fill="both", padx=30, pady=20)

    # Grilla 2x2
    graficos_frame.grid_rowconfigure((0, 1), weight=1)
    graficos_frame.grid_columnconfigure((0, 1), weight=1)

    generar_grafico_barras(graficos_frame, gastos)
    generar_grafico_linea(graficos_frame, presupuesto_total, dias, gasto_comida + gasto_ocio)
    generar_grafico_torta(graficos_frame, gastos)

def calcular():
    resultado_label.configure(text="")

    valor_presupuesto = entrada_presupuesto.get()
    valor_dias = entrada_dias.get()
    valor_alojamiento = entrada_alojamiento.get()
    valor_transporte = entrada_transporte.get()
    valor_comida = entrada_comida.get()
    valor_ocio = entrada_ocio.get()

    ok, mensaje = calcular_presupuesto(
        valor_presupuesto,
        valor_dias,
        valor_alojamiento,
        valor_transporte,
        valor_comida,
        valor_ocio
    )
    resultado_label.configure(text=mensaje)

    if ok:
        try:
            dias = int(valor_dias)
            gastos = {
                'Alojamiento': float(valor_alojamiento),
                'Transporte': float(valor_transporte),
                'Comida': float(valor_comida) * dias,
                'Ocio': float(valor_ocio) * dias,
            }
            presupuesto_total = float(valor_presupuesto)
            sobrante = presupuesto_total - sum(gastos.values())
            if sobrante > 0:
                gastos['Sobrante'] = sobrante

            destruir_layout_inicial()
            mostrar_layout_resultado(gastos, presupuesto_total, dias, float(valor_comida), float(valor_ocio))

        except Exception as e:
            print("Error generando gráficos:", e)

# --- Botones ---
ctk.CTkButton(
    botones_frame,
    text="Calcular",
    command=calcular,
    font=("Poppins", 17),
    fg_color=COLOR_BOTON,
    hover_color="#5a6e71",
    border_width=2,
    border_color="#4d5c61",
    width=170,
    height=40,
    corner_radius=12
).pack(side="left", padx=10)

ctk.CTkButton(
    botones_frame,
    text="Salir",
    command=app.destroy,
    font=("Poppins", 17),
    fg_color=COLOR_BOTON,
    hover_color="#5a6e71",
    border_width=2,
    border_color="#4d5c61",
    width=170,
    height=40,
    corner_radius=12
).pack(side="left", padx=10)

app.mainloop()
