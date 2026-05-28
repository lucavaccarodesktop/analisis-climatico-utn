import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
datos = pd.read_csv("datos/dataset_climatico.csv")
datos["fecha"] = pd.to_datetime(datos["fecha"])

# Cálculos básicos
temp_promedio = datos["temperatura_c"].mean()
temp_maxima = datos["temperatura_c"].max()
temp_minima = datos["temperatura_c"].min()
precip_promedio = datos["precipitacion_mm"].mean()
precip_total = datos["precipitacion_mm"].sum()

# Guardar CSV de resumen
resumen = {
    "Año Inicio": [datos["fecha"].dt.year.min()],
    "Año Fin": [datos["fecha"].dt.year.max()],
    "Temperatura Promedio": [round(temp_promedio, 2)],
    "Temperatura Máxima": [temp_maxima],
    "Temperatura Mínima": [temp_minima],
    "Precipitación Promedio": [round(precip_promedio, 2)],
    "Precipitación Total": [round(precip_total, 2)]
}
pd.DataFrame(resumen).to_csv("resultados/resumen_indicadores.csv", index=False)

# Gráfico 1
plt.figure(figsize=(10, 5))
plt.plot(datos["fecha"], datos["temperatura_c"], color="green", alpha=0.6)
plt.title("Evolución de la Temperatura Mensual (2015-2024)")
plt.grid(True)
plt.savefig("resultados/grafico_temperatura.png")
plt.close()

# Gráfico 2
datos["anio"] = datos["fecha"].dt.year
precip_por_anio = datos.groupby("anio")["precipitacion_mm"].sum()
plt.figure(figsize=(10, 5))
plt.bar(precip_por_anio.index, precip_por_anio.values, color="blue", alpha=0.7)
plt.title("Precipitaciones Totales por Año")
plt.grid(True)
plt.savefig("resultados/grafico_precipitaciones.png")
plt.close()

print("-> Script ejecutado internamente con éxito.")
