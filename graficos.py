import matplotlib.pyplot as plt

def mostrar_grafico_gastos(datos):
    """
    Muestra un gráfico de torta con la distribución de gastos.
    :param datos: Diccionario con claves = categorías y valores = montos
    """
    etiquetas = []
    valores = []

    for categoria, monto in datos.items():
        if monto > 0:
            etiquetas.append(categoria)
            valores.append(monto)

    if not valores:
        print("No hay datos para graficar.")
        return

    colores = plt.get_cmap('Set3').colors
    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140, colors=colores)
    plt.title('Distribución de gastos del viaje')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()