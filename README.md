# Sistema Predictivo de Riesgo de Rotacion Laboral
TFM: Sistema predictivo de riesgo de rotación laboral mediante ML y NLP aplicado a datos de encuestas organizacionales

### Trabajo de Fin de Master - Julio 2026

**Mario Fernandez Hierro** - Master en Data Science
**Kalil Koury** - Master en Business Analytics

---

## Descripcion

Pipeline de Machine Learning y NLP para predecir el riesgo de rotacion
de empleados a partir de datos de encuestas organizacionales.

El sistema combina variables estructuradas (datos de RRHH) con variables
no estructuradas (respuestas abiertas de encuestas) para generar un score
de riesgo de rotacion por empleado, con enfasis en la interpretabilidad
y la traduccion de resultados en valor empresarial medible.

Incluye comparativa de 5 modelos (Logistic Regression, Random Forest,
XGBoost, SVM, MLP), analisis de sentimiento con HuggingFace,
interpretabilidad con SHAP/LIME, y cuantificacion del valor empresarial.

## Requisitos del Sistema

- Python 3.13
- RAM: minimo 8 GB (HuggingFace Transformers requiere memoria)
- GPU: opcional (acelera el pipeline NLP pero no es obligatorio)
- Sistema operativo: Windows, Linux o macOS

## Instalacion

```bash
git clone https://github.com/MarioFernandezH/TFM-Employee-Attrition.git
cd TFM-Employee-Attrition
python -m venv venv
.\venv\Scripts\activate         # Windows
# source venv/bin/activate      # Linux/macOS
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Descarga de Datos

Los datasets no estan incluidos por terminos de uso de Kaggle.
Ver instrucciones completas en [data/raw/DOWNLOAD_INSTRUCTIONS.md](data/raw/DOWNLOAD_INSTRUCTIONS.md).

**Opcion rapida (requiere Kaggle CLI configurado):**

```bash
kaggle datasets download pavansubhasht/ibm-hr-analytics-attrition-dataset -p data/raw/ --unzip
kaggle datasets download vjchoudhary7/hr-analytics-case-study -p data/raw/ --unzip
kaggle datasets download davidgauthier/glassdoor-job-reviews -p data/raw/ --unzip
```

**Opcion manual:** descargar desde los enlaces en DOWNLOAD_INSTRUCTIONS.md y colocar los CSV en data/raw/.

## Ejecucion

Ejecutar los notebooks en orden numerico:

| Notebook | Descripcion | Tiempo estimado |
|----------|-------------|-----------------|
| 00_data_loading | Carga y exploracion inicial | ~5 min |
| 01_EDA | Analisis exploratorio completo | ~10 min |
| 02_NLP_sentiment | Analisis de sentimiento | ~15 min (sin GPU) |
| 03_NLP_topics | Clasificacion tematica | ~10 min |
| 04_models_comparison | Entrenamiento de 5 modelos ML | ~20 min |
| 05_explainability_SHAP | Interpretabilidad SHAP | ~15 min |
| 06_explainability_LIME | Interpretabilidad LIME | ~10 min |
| 07_results_summary | Resumen consolidado | ~2 min |

## Estructura del Proyecto

```
TFM-Employee-Attrition/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- LICENSE
|
|-- data/
|   |-- raw/                          <-- datasets originales (no incluidos)
|   |   |-- DOWNLOAD_INSTRUCTIONS.md
|   |-- processed/                    <-- datos limpios para modelado
|   |-- nlp/                          <-- datos NLP procesados
|
|-- notebooks/
|   |-- 00_data_loading.ipynb         <-- Semana 1
|   |-- 01_EDA.ipynb                  <-- Semana 2
|   |-- 02_NLP_sentiment.ipynb        <-- Semana 3
|   |-- 03_NLP_topics.ipynb           <-- Semana 3
|   |-- 04_models_comparison.ipynb    <-- Semana 3-4
|   |-- 05_explainability_SHAP.ipynb  <-- Semana 4
|   |-- 06_explainability_LIME.ipynb  <-- Semana 4
|   |-- 07_results_summary.ipynb      <-- Semana 4
|
|-- src/
|   |-- config.py                     <-- configuracion centralizada
|   |-- preprocessing.py              <-- funciones de limpieza
|   |-- feature_engineering.py        <-- encoding, scaling, SMOTE
|   |-- models.py                     <-- entrenamiento y evaluacion
|   |-- nlp_pipeline.py               <-- sentimiento y clasificacion
|   |-- explainability.py             <-- SHAP y LIME
|   |-- utils.py                      <-- funciones auxiliares
|
|-- reports/
|   |-- figures/                      <-- graficas del EDA
|   |-- shap/                         <-- plots SHAP y LIME
|   |-- tables/                       <-- tablas comparativas
|
|-- outputs/
|   |-- risk_scores.csv               <-- output final del modelo
|
|-- tests/                            <-- tests unitarios
|-- docs/                             <-- diccionario de variables y notas

``` 

## Outputs

- reports/figures/ -- Graficas del EDA
- reports/shap/ -- Plots SHAP y LIME
- reports/tables/ -- Tablas comparativas de modelos
- outputs/risk_scores.csv -- Score de riesgo por empleado + factores principales

## Tecnologias

- **ML:** scikit-learn, XGBoost, imbalanced-learn
- **NLP:** HuggingFace Transformers, spaCy, NLTK
- **Interpretabilidad:** SHAP, LIME
- **Visualizacion:** matplotlib, seaborn, Power BI
- **Infraestructura:** Git/GitHub, Python 3

## Autores

| Nombre | Master | Rol principal |
|--------|--------|---------------|
| Mario Fernandez Hierro | Data Science | Pipeline ML/NLP, SHAP, validacion tecnica, dashboard |
| Kalil Koury | Business Analytics | Valor empresarial, interpretacion de negocio, storytelling |

## Contexto Academico

TFM Interdisciplinar - Entrega: Julio 2026

## Licencia

MIT License - ver archivo LICENSE
'@ | Out-File -Encoding utf8 "README.md"

## Datasets Utilizados

### 1. IBM HR Analytics Employee Attrition & Performance ★ PRINCIPAL

| Campo | Detalle |
|-------|---------|
| **URL** | https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset |
| **Archivo** | `WA_Fn-UseC_-HR-Employee-Attrition.csv` |
| **Filas × Columnas** | 1,470 × 35 |
| **Target** | `Attrition` (Yes/No) — desbalanceado 84/16 |
| **Licencia** | CC0: Public Domain |
| **Fecha de descarga** | 2026-06-17 |
| **Limitaciones** | Dataset **sintético** generado por IBM Watson Analytics. Los patrones pueden no reflejar realidades organizacionales específicas. Muestra de una sola empresa ficticia con posible sesgo cultural USA. Ampliamente citado en la literatura académica como benchmark del sector. |

### 2. HR Analytics Case Study (Validación Externa)

| Campo | Detalle |
|-------|---------|
| **URL** | https://www.kaggle.com/datasets/vjchoudhary7/hr-analytics-case-study |
| **Archivos** | Múltiples CSV unidos por `EmployeeID` (`general_data.csv`, `employee_survey_data.csv`, `manager_survey_data.csv`, `in_time.csv`, `out_time.csv`) |
| **Filas × Columnas** | 4,410 × ~28 (tras join) |
| **Target** | `Attrition` (Yes/No) |
| **Licencia** | CC BY-NC-SA 4.0 |
| **Fecha de descarga** | 2026-06-17 |
| **Limitaciones** | Requiere join de múltiples archivos. Estructura diferente al IBM HR — necesita preprocesamiento adicional. Se usa exclusivamente como conjunto de validación externa para verificar que los modelos no overfittean en el dataset principal. |

### 3. Glassdoor Employee Reviews (NLP)

| Campo | Detalle |
|-------|---------|
| **URL** | https://www.kaggle.com/datasets/davidgauthier/glassdoor-job-reviews |
| **Archivo** | `glassdoor_reviews.csv` |
| **Filas × Columnas** | ~67,000 × 18 |
| **Target** | Sentimiento implícito (no hay label explícito) |
| **Licencia** | CC0: Public Domain |
| **Fecha de descarga** | 2026-06-17 |
| **Limitaciones** | Datos scrapeados de Glassdoor — sesgo de autoselección (empleados insatisfechos tienden a dejar más reseñas). No tiene variable `Attrition` directa; se usa para entrenar/validar el pipeline NLP de análisis de sentimiento y clasificación temática. Textos en inglés. |

> **Nota:** Los archivos CSV no se incluyen en el repositorio por términos de licencia y tamaño.
> Descárgalos desde las URLs indicadas y colócalos en `data/raw/` antes de ejecutar los notebooks.
