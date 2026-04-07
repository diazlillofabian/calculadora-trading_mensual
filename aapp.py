import streamlit as st
import pandas as pd

st.set_page_config(page_title="Trading de Ganancia Mensual", layout="wide")

st.title("📈 Trading de Ganancia Mensual")

# Sidebar para controles
st.sidebar.header("Configuración de Capital (Mensual)")
cap_inicial = st.sidebar.number_input("Capital Inicial", value=500000, step=10000)
porcentaje = (
    st.sidebar.number_input(
        "Porcentaje Diario (%)",
        min_value=0.0,
        max_value=100.0,
        value=10.0,
        step=0.1,
        format="%.2f",
    )
    / 100
)
retiro = st.sidebar.number_input("Retiro Diario Fijo", value=10000, step=1000)

# Lógica de cálculo por meses (12 meses de 2026)
datos = []
saldo_actual = cap_inicial

# Días reales por mes para 2026
meses_2026 = [
    ("Enero", 31),
    ("Febrero", 28),
    ("Marzo", 31),
    ("Abril", 30),
    ("Mayo", 31),
    ("Junio", 30),
    ("Julio", 31),
    ("Agosto", 31),
    ("Septiembre", 30),
    ("Octubre", 31),
    ("Noviembre", 30),
    ("Diciembre", 31),
]

for mes_nombre, dias_mes in meses_2026:
    saldo_inicial = saldo_actual
    ganancia_mes_total = 0.0
    retiro_mes_total = retiro * dias_mes

    # Simular día a día dentro del mes usando el porcentaje diario y el retiro diario
    for _ in range(dias_mes):
        ganancia = saldo_actual * porcentaje
        ganancia_mes_total += ganancia
        saldo_con_ganancia = saldo_actual + ganancia
        saldo_actual = max(0, saldo_con_ganancia - retiro)

    saldo_final = saldo_actual

    datos.append(
        {
            "Mes": f"{mes_nombre} 2026",
            "Saldo Inicial": f"{saldo_inicial:,.0f}",
            "Ganancia (+)": f"{ganancia_mes_total:,.0f}",
            "Retiro (-)": f"{retiro_mes_total:,.0f}",
            "Retiro de Dinero": f"{retiro_mes_total:,.0f}",
            "Saldo Final": f"{max(0, saldo_final):,.0f}",
        }
    )

# Mostrar Tabla
df = pd.DataFrame(datos)
st.table(df)

# Gráfico de crecimiento
st.subheader("Evolución del Capital")
st.line_chart(df["Saldo Final"].str.replace(",", "").astype(float))
