import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def generar_grafico_torta(frame, datos):
    etiquetas = list(datos.keys())
    valores = list(datos.values())
    colores = plt.get_cmap('Set3').colors

    fig, ax = plt.subplots(figsize=(5.5, 4))
    ax.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140, colors=colores)
    ax.axis('equal')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=10)


def generar_grafico_barras(frame, datos):
    etiquetas = list(datos.keys())
    valores = list(datos.values())
    colores = plt.get_cmap('Set3').colors

    fig, ax = plt.subplots(figsize=(5.5, 4))
    ax.bar(etiquetas, valores, color=colores)
    ax.set_title("Distribución de Gastos")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)


def generar_grafico_linea(frame, presupuesto_total, dias, gasto_diario):
    x_dias = list(range(1, dias + 1))
    restante = [presupuesto_total - gasto_diario * d for d in x_dias]

    fig, ax = plt.subplots(figsize=(5.5, 4))
    ax.plot(x_dias, restante, color="#6E8387")
    ax.set_title("Presupuesto restante por día")
    ax.set_xlabel("Días")
    ax.set_ylabel("Pesos")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=10)
