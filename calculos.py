
def calcular_presupuesto(presupuesto, dias, alojamiento, transporte, comida_dia, ocio_dia):
    try:
        presupuesto = float(presupuesto)
        dias = int(dias)
        alojamiento = float(alojamiento)
        transporte = float(transporte)
        comida_dia = float(comida_dia)
        ocio_dia = float(ocio_dia)

        total_gastos = alojamiento + transporte + ((comida_dia + ocio_dia) * dias)
        sobrante = presupuesto - total_gastos

        msg = f"🧾 Gastos estimados: ${total_gastos:,.2f}\n"
        msg += f"💰 Sobrante: ${sobrante:,.2f}" if sobrante >= 0 else f"❌ Te faltan ${-sobrante:,.2f}"
        return True, msg

    except (ValueError, TypeError):
        return False, "⚠️ Ingresá todos los valores numéricos correctamente."
