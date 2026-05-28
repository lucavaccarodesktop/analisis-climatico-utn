"""
Análisis de Datos Climáticos — Escenario A
TUP UTN 2026 · Organización Empresarial
Autores: Luca Vaccaro (lucavaccarodeskstop) (P1), Rosario Guadalupe Mallón (Colab22/Guadaa18) (P2)
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # necesario en entornos sin GUI (Colab, servidor)
import matplotlib.pyplot as plt
import os

# --- Configuración de rutas relativas ---
# Usamos rutas relativas para garantizar reproducibilidad en cualquier entorno
RUTA_DATOS = "datos/dataset_climatico.csv"
RUTA_RESULTADOS = "resultados"

os.makedirs(RUTA_RESULTADOS, exist_ok=True)


def cargar_datos(ruta: str) -> pd.DataFrame:
    """
    Carga el dataset climático desde un archivo CSV.
    Se valida que las columnas esperadas existan para evitar
    errores silenciosos en el análisis posterior.
    """
    df = pd.read_csv(ruta, parse_dates=["fecha"])
    columnas_requeridas = {"fecha", "temperatura_c", "precipitacion_mm"}
    if not columnas_requeridas.issubset(df.columns):
        raise ValueError(f"El dataset debe tener: {columnas_requeridas}")
    return df


def calcular_indicadores(df: pd.DataFrame) -> dict:
    """
    Calcula los indicadores estadísticos básicos del análisis climático.
    Se calculan sobre la serie completa para obtener una visión global
    del período analizado (2015-2024).
    """
    indicadores = {
        "temp_promedio": round(df["temperatura_c"].mean(), 2),
        "temp_maxima":   round(df["temperatura_c"].max(), 2),
        "temp_minima":   round(df["temperatura_c"].min(), 2),
        "precip_promedio": round(df["precipitacion_mm"].mean(), 2),
        "precip_total":  round(df["precipitacion_mm"].sum(), 2),
        "anio_inicio":   df["fecha"].dt.year.min(),
        "anio_fin":      df["fecha"].dt.year.max(),
        "n_registros":   len(df)
    }
    return indicadores


def guardar_resumen(indicadores: dict, ruta: str):
    """
    Exporta los indicadores calculados a un archivo CSV.
    Esto permite que otros integrantes o etapas del proyecto
    consuman los resultados sin re-ejecutar el análisis.
    """
    pd.DataFrame([indicadores]).to_csv(
        os.path.join(ruta, "resumen_indicadores.csv"), index=False
    )
    print("Resumen de indicadores guardado en /resultados")


def graficar_temperatura(df: pd.DataFrame, ruta: str):
    """
    Genera un gráfico de línea de la temperatura mensual.
    Se agrega una media móvil de 12 meses para suavizar la serie
    y visualizar la tendencia a largo plazo con mayor claridad.
    """
    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(df["fecha"], df["temperatura_c"],
            color="#5DCAA5", linewidth=0.9, alpha=0.7,
            label="Temperatura mensual (°C)")

    # Media móvil anual — reduce el ruido estacional para ver la tendencia
    media_movil = df["temperatura_c"].rolling(window=12, center=True).mean()
    ax.plot(df["fecha"], media_movil,
            color="#0F6E56", linewidth=2.2,
            label="Tendencia (media móvil 12 meses)")

    ax.set_title("Evolución de la Temperatura Mensual — 2015 a 2024",
                 fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Año", fontsize=11)
    ax.set_ylabel("Temperatura (°C)", fontsize=11)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle="--", alpha=0.4)
    fig.tight_layout()

    ruta_grafico = os.path.join(ruta, "grafico_temperatura.png")
    fig.savefig(ruta_grafico, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Gráfico guardado en {ruta_grafico}")


def graficar_precipitaciones(df: pd.DataFrame, ruta: str):
    """
    Genera un gráfico de barras con precipitaciones anuales totales.
    El agrupamiento anual facilita la comparación entre años
    y detectar períodos de sequía o exceso hídrico.
    """
    df_anual = df.groupby(df["fecha"].dt.year)["precipitacion_mm"].sum()

    fig, ax = plt.subplots(figsize=(10, 4))
    bars = ax.bar(df_anual.index, df_anual.values,
                  color="#378ADD", alpha=0.8, edgecolor="white")

    # Etiquetas sobre cada barra para facilitar la lectura
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 5,
                f"{bar.get_height():.0f}",
                ha="center", va="bottom", fontsize=9)

    ax.set_title("Precipitaciones Totales Anuales — 2015 a 2024",
                 fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Año", fontsize=11)
    ax.set_ylabel("Precipitación total (mm)", fontsize=11)
    ax.grid(True, axis="y", linestyle="--", alpha=0.4)
    fig.tight_layout()

    ruta_grafico = os.path.join(ruta, "grafico_precipitaciones.png")
    fig.savefig(ruta_grafico, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Gráfico guardado en {ruta_grafico}")


if __name__ == "__main__":
    print("=" * 50)
    print("Iniciando análisis climático...")
    print("=" * 50)

    df = cargar_datos(RUTA_DATOS)
    print(f"Dataset cargado: {len(df)} registros")

    indicadores = calcular_indicadores(df)
    print("\n--- Indicadores calculados ---")
    for k, v in indicadores.items():
        print(f"  {k}: {v}")

    guardar_resumen(indicadores, RUTA_RESULTADOS)
    graficar_temperatura(df, RUTA_RESULTADOS)
    graficar_precipitaciones(df, RUTA_RESULTADOS)

    print("\n✓ Análisis completado exitosamente.")
    print(f"  Resultados en: /{RUTA_RESULTADOS}/")
