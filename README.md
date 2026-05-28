# Análisis de Datos Climáticos — UTN TUP 2026

## 1. Descripción del Proyecto

Este proyecto es parte del trabajo práctico de Organización Empresarial de la Tecnicatura en Programación (UTN). Consiste en un script de Python que procesa datos climáticos históricos del período 2015-2024, calcula indicadores básicos de temperatura y precipitaciones, y genera gráficos para visualizar cómo evolucionaron a lo largo del tiempo.

## 2. Integrantes y Roles

| Integrante | Usuario GitHub | Rol |
|---|---|---|
| Luca Vaccaro | lucavaccarodesktop | P1 — Líder: creación del repo, estructura de carpetas, revisión del código y merge final |
| Rosario Guadalupe Mallón | Guadaa18 | P2 — Desarrollo: script de análisis, gráficos y exportación de resultados en Colab |

## 3. Cómo trabajamos

Usamos **Jira** para organizar las tareas y **Git con GitHub** para el control de versiones. Cada commit está vinculado a un Issue de Jira con el formato `CLIM-N: descripción`.

No trabajamos directo sobre `main`. El desarrollo se hizo en una rama separada (`feature/desarrollo-analisis`) y se integró a main mediante un Pull Request con revisión de código entre los dos.

## 4. Estructura del repositorio
├── datos/
│   └── dataset_climatico.csv       # Registros mensuales de temperatura y precipitaciones
├── scripts/
│   └── analisis_datos.py           # Script principal de análisis
├── resultados/
│   ├── resumen_indicadores.csv     # Tabla con los indicadores calculados
│   ├── grafico_temperatura.png     # Gráfico de evolución de temperatura
│   └── grafico_precipitaciones.png # Gráfico de precipitaciones por mes
├── .gitignore
└── README.md

## 5. Cómo ejecutar el script

1. Clonar el repositorio
2. Abrir `scripts/analisis_datos.py` en Google Colab
3. Ejecutar todas las celdas en orden
4. Los resultados se guardan automáticamente en `/resultados`

> Si el archivo CSV no está en `/datos`, el script genera un dataset de ejemplo para que puedas probar igual.

## 6. Dataset utilizado

Datos climáticos históricos obtenidos de [datahub.io/core/global-temp](https://datahub.io/core/global-temp). Registros mensuales de temperatura global en formato CSV, de acceso público.
