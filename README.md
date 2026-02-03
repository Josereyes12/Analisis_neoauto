# 📊 Análisis del Mercado de Autos Usados en Lima (NeoAuto)

## 📌 Descripción del proyecto

Este proyecto analiza el mercado de autos usados publicados en **NeoAuto** para la ciudad de **Lima, Perú**, con el objetivo de identificar patrones de precios y entender qué factores influyen en la valorización de los vehículos.

El flujo completo del proyecto abarca:

- Web scraping de anuncios reales  
- Limpieza y estructuración de datos  
- Análisis exploratorio (EDA)  
- Visualización interactiva mediante **Power BI**

El resultado final es un dashboard que permite explorar el mercado de autos usados desde distintas perspectivas: precio, kilometraje, año, transmisión, combustible y marca.

---

## 🎯 Objetivos del análisis

- Analizar cómo influyen el **kilometraje** y el **año** en el precio de los vehículos.  
- Comparar precios según **tipo de transmisión** y **combustible**.  
- Identificar diferencias de precio entre **marcas**.  
- Proporcionar una visión general y exploratoria del mercado de autos usados en Lima.

---

## 🗂️ Dataset

- **Fuente:** https://neoauto.com  
- **Método de obtención:** Web scraping con Selenium  
- **Cobertura:** Anuncios activos de autos usados en Lima  
- **Fecha de scraping:** 30/01/2026  
- **Total de registros:** 550 vehículos  

### Variables principales

| Columna | Descripción |
|-------|-------------|
| `Marca_Modelo` | Texto original del anuncio (marca, modelo y año) |
| `Precio` | Precio del vehículo en USD |
| `Km` | Kilometraje del vehículo |
| `Transmision` | Tipo de transmisión |
| `Combustible` | Tipo de combustible |
| `Anio` | Año de fabricación |
| `Marca` | Marca del vehículo |
| `Modelo` | Modelo del vehículo |
| `URL` | Enlace al anuncio original |

---

## 🧹 Limpieza y preparación de datos

El proceso de limpieza incluyó:

- Tratamiento de valores nulos en `Km`, identificados como vehículos nuevos (0 km).  
- Normalización y conversión de variables numéricas (`Precio`, `Km`).  
- Estandarización de categorías truncadas (ej. **Automática - Secuencial**).  
- Identificación y conservación de categorías poco frecuentes sin imputación forzada.  
- Separación de la variable compuesta `Marca_Modelo` en:
  - `Marca`
  - `Modelo`
  - `Anio`

El resultado es un dataset limpio y consistente, listo para análisis y visualización.

---

## 🔍 Análisis Exploratorio (EDA)

Se realizó un análisis exploratorio ligero con los siguientes objetivos:

- Validar la calidad del dataset final.  
- Verificar distribuciones básicas de variables numéricas.  
- Analizar la frecuencia de variables categóricas clave.  
- Explorar relaciones entre precio, kilometraje y año.

Este paso permitió confirmar la coherencia de los datos antes de su visualización en Power BI.

---

## 📈 Dashboard en Power BI

El dashboard se construyó en una sola página e incluye:

### KPIs principales

- Precio promedio  
- Kilometraje promedio  
- Total de vehículos analizados  

### Visualizaciones

- **Precio vs Kilometraje** (gráfico de dispersión)  
- **Precio promedio por año**  
- **Precio promedio por tipo de transmisión**  
- **Distribución de vehículos por tipo de combustible**  
- **Top 10 marcas por precio promedio**  

El dashboard permite aplicar filtros por:

- Marca  
- Año  
- Transmisión  
- Combustible  

---

## 🧠 Principales insights

- Existe una **relación inversa clara entre kilometraje y precio**, evidenciando la depreciación del vehículo.  
- Los **autos más recientes** tienden a mantener un mayor valor.  
- Los vehículos con **transmisión automática** presentan precios promedio más altos.  
- El mercado está dominado por vehículos a **gasolina**, mientras que los combustibles alternativos representan nichos pequeños.  
- Las marcas premium concentran los precios promedio más elevados.

---

## ⚠️ Limitaciones del análisis

- El dataset representa una muestra del mercado en un momento específico.  
- No se incluyen variables como ubicación exacta, fecha de publicación o estado del vehículo.  
- Los resultados son exploratorios y no deben interpretarse como precios de mercado oficiales.

---

## 🛠️ Tecnologías utilizadas

- Python (Pandas, NumPy)  
- Selenium  
- Jupyter Notebook  
- Power BI  

---

## 📬 Contacto

Proyecto desarrollado como parte de un portafolio personal de **Analista de Datos**.

---

### 🔚 Nota final

Este proyecto tiene fines **educativos y demostrativos**, mostrando un flujo completo de análisis de datos aplicado a un caso real del mercado peruano.

