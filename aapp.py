import pandas as pd


def generar_tabla_trading_mensual():
    print("--- Configuración de Trading Mensual ---")
    try:
        # Entradas del usuario
        capital_inicial = float(input("Ingresa el capital inicial: "))
        porcentaje_mensual = (
            float(input("Ingresa el porcentaje de ganancia mensual (ej. 10 para 10%): "))
            / 100
        )
        retiro_input = input("Ingresa el retiro diario (%) (ej. 2 para 2% - por defecto 2): ")
        retiro_fijo = float(retiro_input) if retiro_input.strip() else 2.0  # ahora trata como porcentaje

        datos = []
        capital_actual = capital_inicial

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

        for mes_nombre, dias in meses_2026:
            saldo_inicial = capital_actual
            ganancia_mes = 0.0
            retiro_mes = 0.0

            # Convertir porcentaje mensual a tasa diaria compuesta para el mes
            tasa_diaria = (1 + porcentaje_mensual) ** (1 / dias) - 1 if porcentaje_mensual >= 0 else 0

            # Simular día a día dentro del mes
            for _ in range(dias):
                ganancia_dia = capital_actual * tasa_diaria
                ganancia_mes += ganancia_dia
                capital_con_ganancia = capital_actual + ganancia_dia

                retiro_diario = capital_con_ganancia * (retiro_fijo / 100.0)
                retiro_mes += retiro_diario

                capital_actual = max(0, capital_con_ganancia - retiro_diario)

            saldo_final_mes = capital_actual

            datos.append(
                {
                    "Mes": f"{mes_nombre} 2026",
                    "Saldo Inicial": round(saldo_inicial, 2),
                    "Ganancia (+)": round(ganancia_mes, 2),
                    "Retiro (-)": round(retiro_mes, 2),
                    "Saldo Final": round(saldo_final_mes, 2),
                }
            )

        # Crear DataFrame
        df = pd.DataFrame(datos)

        # Mostrar tabla
        print("\n" + "=" * 30)
        print(" TRADING DE GANANCIA MENSUAL (2026) ")
        print("=" * 30)
        print(df.to_string(index=False))

        print("\nResumen tras 12 meses:")
        print("Capital Final:", round(capital_actual, 2))

    except ValueError:
        print("Por favor, ingresa números válidos.")


if __name__ == "__main__":
    generar_tabla_trading_mensual()
