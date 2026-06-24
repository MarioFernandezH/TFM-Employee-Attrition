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

| Notebook | Descripcion | Estado |
|----------|-------------|-----------------|
| 00_data_loading | Carga y exploracion inicial | Completado |
| 01_EDA | Analisis exploratorio completo | En proceso |
| 02_NLP_sentiment | Analisis de sentimiento | Pendiente |
| 03_NLP_topics | Clasificacion tematica | Pendiente |
| 04_models_comparison | Entrenamiento de 5 modelos ML | Pendiente |
| 05_explainability_SHAP | Interpretabilidad SHAP | Pendiente |
| 06_explainability_LIME | Interpretabilidad LIME | Pendiente |
| 07_results_summary | Resumen consolidado | Pendiente |

## Estructura del Proyecto

```
TFM-Employee-Attrition/

|-- README.md

|-- requirements.txt

|-- .gitignore

|-- LICENSE

|-- data/

|   |-- raw/                     <-- datasets originales (ver DOWNLOAD_INSTRUCTIONS)

|   |-- processed/               <-- datos limpios (se genera en EDA)

|-- notebooks/

|   |-- 00_data_loading.ipynb    <-- carga y exploracion inicial

|-- reports/

|   |-- Diccionario_Variables_IBM_HR.xlsx

``` 
*La estructura se ampliará a medida que avance el proyecto (src/, reports/figures/, etc.)*

## Tecnologias

- **ML:** scikit-learn, XGBoost, imbalanced-learn
- **NLP:** HuggingFace Transformers, spaCy, NLTK
- **Interpretabilidad:** SHAP, LIME
- **Visualizacion:** matplotlib, seaborn, Power BI
- **Infraestructura:** Git/GitHub, Python 3

## Datasets

| Dataset | Filas | Target | Uso en el proyecto |
|---------|-------|--------|--------------------|
| [IBM HR Analytics](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) -principal- | 1,470 | Attrition (Yes/No) | Dataset principal - entrenamiento ML |
| [HR Analytics Case Study](https://www.kaggle.com/datasets/vjchoudhary7/hr-analytics-case-study) | 4,410 | Attrition (Yes/No) | Validacion externa |
| [Glassdoor Job Reviews](https://www.kaggle.com/datasets/davidgauthier/glassdoor-job-reviews) | ~67,000 | Sentimiento implicito | Pipeline NLP |

**Nota:** El IBM HR es un dataset sintetico generado por IBM Watson Analytics. Es el benchmark estandar del sector para modelos de attrition y esta ampliamente citado en la literatura academica, pero sus patrones pueden no reflejar realidades organizacionales especificas. Los datos de Glassdoor tienen sesgo de autoseleccion (empleados insatisfechos tienden a dejar mas reseñas).

## Autores

| Nombre | Master | Rol principal |
|--------|--------|---------------|
| Mario Fernandez Hierro | Data Science | Pipeline ML/NLP, SHAP, validacion tecnica, dashboard |
| Kalil Koury | Business Analytics | Valor empresarial, interpretacion de negocio, storytelling |

TFM Interdisciplinar - Entrega: Julio 2026

## Licencia

MIT License - ver archivo LICENSE
