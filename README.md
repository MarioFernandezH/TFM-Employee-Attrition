# Sistema Predictivo de Riesgo de Rotacion Laboral
TFM: Sistema predictivo de riesgo de rotación laboral mediante ML y NLP aplicado a datos de 
encuestas organizacionales

### Trabajo de Fin de Master - Julio 2026

**Mario Fernández Hierro** - Master en Data Science
**Kalil Koury** - Master en Business Analytics
**Rafael Concepción** - Master en Business Analytics

---

## Descripcion

Este proyecto desarrolla un sistema predictivo para identificar empleados con
riesgo de rotación (attrition) en una organización, combinando modelos de
clasificación de Machine Learning, análisis de texto con NLP, e
interpretabilidad explicable (XAI). Con un objetivo doble: predecir qué 
empleados presentan mayor riesgo de abandono y explicar los factores que 
impulsan ese riesgo, de forma que RRHH pueda tomar decisiones accionables.

El sistema combina variables estructuradas (datos de RRHH) con variables
no estructuradas (respuestas abiertas de encuestas) para generar un score
de riesgo de rotacion por empleado, con enfasis en la interpretabilidad
y la traduccion de resultados en valor empresarial medible.

Incluye comparativa de 5 modelos (Logistic Regression, Random Forest,
XGBoost, SVM, MLP), analisis de sentimiento con HuggingFace,
interpretabilidad con SHAP/LIME, y cuantificacion del valor empresarial.

El enfoque prioriza la **detección (Recall)** de los empleados en riesgo sobre
la precisión, dado el coste asimétrico de los errores: no anticipar la marcha
de un empleado es más costoso que una falsa alerta, que se resuelve con una
conversación de seguimiento de valor para el empleado.

---

## Resultado principal

Tras entrenar y comparar cinco modelos de clasificación bajo la misma
estrategia de manejo del desbalanceo, el modelo seleccionado es la
**Regresión Logística**:

| Métrica | Valor |
|---------|-------|
| Recall (clase abandono) | 0.68 |
| AUC-ROC | 0.816 |
| Validación cruzada (5-fold) | AUC 0.821 ± 0.050 |

El modelo más simple resultó el más eficaz, con la ventaja añadida de ofrecer
interpretabilidad nativa a través de sus coeficientes, reforzada visualmente
con SHAP y LIME.

---

## Estructura del Proyecto

```
TFM-Employee-Attrition/

|-- README.md

|-- requirements.txt

|-- .gitignore

|-- LICENSE

|-- data/

|   |-- raw/                         <-- datasets originales (ver DOWNLOAD_INSTRUCTIONS)

|   |-- processed/                   <-- datos limpios (se generaron en EDA)

|   |-- nlp/                   		 <-- datasets del análisis de textos

|-- notebooks/

|   |-- 00_data_loading.ipynb        <-- carga y exploración inicial
|   |-- 01_EDA.ipynb                 <-- análisis exploratorio de los datos
|   |-- 02_NLP_sentiment.ipynb       <-- análisis de sentimiento (DistilBERT)
|   |-- 03_NLP_topics.ipynb          <-- clasificación temática zero-shot
|   |-- 04_models_comparison.ipynb   <-- entrenamiento y comparativa de los modelos
|   |-- 05_SHAP_LIME.ipynb           <-- interpretabilidad
|   |-- 06_validacion_externa.ipynb  <-- análisis de compatibilidad con dataset externo

|-- reports/

|   |-- Diccionario_Variables_IBM_HR.xlsx
|   |-- Dashboard_TFM.pdf
|   |-- figures/					 <-- gráficos del EDA y modelos
|   |-- shap/					     <-- plots de interpretabilidad
|   |-- tables/					     <-- tablas de métricas y coeficientes

|-- outputs/

|   |-- risk_scores.csv				 <-- predicciones de riesgo para el dashbpard
|   |-- shap_local.csv				 <-- contribuciones SHAP por empleado (drivers individuales)
|   |-- empleados_contexto.csv		 <-- variables de contexto por empleado (Department, etc.)
|   |-- importancia_global_shap.csv	 <-- importancia global (media |SHAP|)

``` 

---

## Datasets utilizados

- **IBM HR Analytics** (1.470 registros, 35 variables) — dataset principal para
  el entrenamiento y evaluación de los modelos.
- **Glassdoor Reviews** (~67.000 reseñas) — corpus textual para el pipeline de
  NLP (sentimiento y clasificación temática).
- **Extended HR** (~4.410 registros) — planteado para validación externa. El
  análisis de compatibilidad (notebook 06) reveló que carece de variables
  predictivas claves del modelo (OverTime y las dimensiones de satisfacción),
  por lo que la validación externa directa no resultó viable. Se documenta como
  limitación del estudio.

- Los datasets no se incluyen en el repositorio por su tamaño y licencia.
- **Nota:** El IBM HR es un dataset sintetico generado por IBM Watson Analytics. 
  Es el benchmark estandar del sector para modelos de attrition.

---

## Metodología

1. **Carga y limpieza** de los datos, eliminación de variables constantes y
   codificación (one-hot encoding).
2. **Análisis exploratorio (EDA)** con pruebas de significancia estadística.
3. **Pipeline de NLP** sobre reseñas: análisis de sentimiento con DistilBERT y
   clasificación temática zero-shot con BART.
4. **Entrenamiento de 5 modelos**: Regresión Logística, Random Forest, XGBoost,
   SVM (kernel RBF) y MLP (red neuronal). Manejo homogéneo del desbalanceo
   mediante `class_weight='balanced'` (o `scale_pos_weight` en XGBoost).
5. **Selección del modelo** priorizando el Recall, con análisis del umbral de
   decisión (0.55 operativo / 0.35 para cobertura máxima).
6. **Validación cruzada estratificada** (5-fold) para confirmar la robustez.
7. **Interpretabilidad** con SHAP (global e individual) y LIME.
8. **Generación del output** (`risk_scores.csv` y `shap_local.csv`) desde el mismo
   conjunto de test, para garantizar la trazabilidad empleado a empleado en el dashboard.

---

## Stack técnico

- **Lenguaje:** Python 3
- **ML / Datos:** scikit-learn, XGBoost, pandas, numpy
- **NLP:** HuggingFace Transformers (DistilBERT, BART)
- **Interpretabilidad:** SHAP, LIME
- **Visualización:** matplotlib, Power BI
- **Entorno:** Jupyter Notebook, entorno virtual (venv)

---

## Reproducción

Para reproducir los resultados:

```bash
# 1. Clonar el repositorio
git clone https://github.com/MarioFernandezH/TFM-Employee-Attrition.git
cd TFM-Employee-Attrition

# 2. Crear y activar el entorno virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Colocar los datasets en data/raw/
```

- **Nota:** Todos los modelos usan `random_state=42` para garantizar la 
  reproducibilidad.

---

## Interpretabilidad y valor de negocio

El sistema no se limita a predecir, explica. Mediante SHAP se identifican los
principales impulsores de la rotación (horas extra, antigüedad, estado civil,
rol) tanto a nivel global como individual. El gráfico waterfall permite a RRHH
comprender por qué un empleado en concreto está en riesgo y qué factor abordar en
una conversación de seguimiento, convirtiendo un score abstracto en una acción
concreta.

---

## Dashboard (Power BI)

Los resultados se presentan en un dashboard interactivo de 4 páginas
(Portada, Vista Ejecutiva, Voz del Empleado, Alerta y Acción) construido
sobre el output del modelo.

- **Enlace (solo lectura):** 
https://app.powerbi.com/view?r=eyJrIjoiYWU5MzVmMjUtNGZmYS00ZWMzLTgwNWItN2IzOWZjMzE0ZTgxIiwidCI6Ijc4NWM5NmYxLTZkMmItNGNmZC1hMTQ3LTUzMTU5NWU1Yjg0NiJ9
- Respaldo en PDF disponible en `reports/` (`Dashboard_TFM.pdf`).

El dashboard combina el score de riesgo por empleado, los drivers globales
e individuales (SHAP), y la voz del empleado (NLP), respetando la
triangulación entre fuentes independientes (IBM HR y Glassdoor no se cruzan
a nivel individual).

---

## Limitaciones y trabajo futuro

- La validación externa con el dataset Extended no fue viable por incompatibilidad
  de esquemas (variables claves ausentes), limitación común entre datasets
  públicos de People Analytics. La robustez del modelo se sustenta en la
  validación cruzada interna.
- Se propone como trabajo futuro la validación en datos organizacionales con
  esquema homogéneo, así como la integración de las features de NLP en el modelo
  predictivo estructurado.

---

## Autores

| Nombre | Master | Rol principal |
|--------|--------|---------------|
| Mario Fernandez Hierro | Data Science | Pipeline técnico, modelos, NLP, XAI |
| Kalil Koury | Business Analytics | EDA, interpretación de negocio |
| Rafael Concepción | Business Analytics | Marco teórico, ROI, dashboard |

TFM Interdisciplinar - Entrega: Julio 2026