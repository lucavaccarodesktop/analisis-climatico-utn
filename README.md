# Sistema de Análisis de Datos Climáticos Históricos 
### Trabajo Práctico Integrador — Organización Empresarial
**Tecnicatura Universitaria en Programación (TUP) — UTN** *Ciclo Lectivo: 2026*

---

##  1. Descripción del Proyecto
Este proyecto consiste en el desarrollo de un sistema automatizado en Python para el procesamiento, análisis estadístico y visualización de series de datos climáticos históricos (período 2015-2024). El objetivo de negocio es proporcionar una herramienta ágil que permita identificar tendencias térmicas de largo plazo y anomalías en los regímenes de precipitaciones anuales para optimizar la toma de decisiones en sectores productivos dependientes del clima.

---

##  2. Integrantes y Roles (Simulación Scrum)
Para cumplir con los estándares de metodologías ágiles y control de versiones profesional, el equipo distribuyó sus responsabilidades bajo los siguientes roles:

| Integrante | Rol Ágil / Git | Responsabilidades Principales |
| :--- | :--- | :--- |
| **Luca Vaccaro (lucavaccarodesktop)** (P1) | Líder de Proyecto y Supervisor| Inicialización del repositorio, definición del entorno, arquitectura de carpetas, revisión de código (*Peer Review*) y aprobación final de integraciones (*Merge*). |
| **Rosario Guadalupe Mallón (Guadaa18/Colab22)** (P2) | Desarrolladora del código y visualización de ejecución| Configuración del entorno en Google Colab, desarrollo del script de análisis estadístico core, exportación de resultados y generación de gráficos de tendencias. |


---

##  3. Metodología y Flujo de Trabajo (Git & Jira)
La gestión de este proyecto se realizó bajo el marco de trabajo **Scrum**, utilizando **Jira** como herramienta centralizadora para el sprint. 

### Ciclo de Ramificación (Feature Branch Workflow)
Para el desarrollo del código no se trabajó directamente sobre la rama principal, garantizando la estabilidad del software:
* **`main`**: Contiene únicamente versiones estables, limpias y aprobadas para producción.
* **`feature/desarrollo-analisis`**: Rama secundaria utilizada por el equipo de desarrollo para codificar el script y generar las métricas visuales sin alterar la línea principal.

Todos los commits realizados en Git fueron vinculados de manera estricta al tablero de Jira utilizando la clave del proyecto como prefijo (`CLIM-4`, `CLIM-2`, `CLIM-3`). La integración final se realizó mediante un **Pull Request (PR)**, el cual requirió debate técnico cruzado y aprobación formal previa fusión.

---

## 4. Estructura del Repositorio
El proyecto mantiene una arquitectura de archivos limpia y modular:

```text
├── datos/
│   └── dataset_climatico.csv      # Dataset histórico con registros mensuales (2015-2024)
├── scripts/
│   └── analisis_datos.py          # Script principal de procesamiento y análisis en Python
├── resultados/
│   ├── resumen_indicadores.csv    # Tabla con promedios, máximos y mínimos calculados
│   ├── grafico_temperatura.png    # Visualización lineal de la tendencia térmica
│   └── grafico_precipitaciones.png# Histograma de barras de acumulación pluvial anual
├── .gitignore                     # Archivo de exclusión para entornos locales y temporales
└── README.md                      # Documentación general del proyecto (este archivo)
