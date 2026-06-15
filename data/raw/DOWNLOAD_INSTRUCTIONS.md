# Instrucciones de Descarga de Datos

Los datasets no estan incluidos en el repositorio por terminos de uso de Kaggle.
Se requiere una cuenta gratuita en Kaggle para descargarlos.

## Datasets necesarios

| Dataset | Rol en el TFM | URL |
|---------|---------------|-----|
| IBM HR Analytics (Principal) | Entrenar 5 modelos ML + SHAP/LIME | https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset |
| HR Analytics Case Study (Validacion) | Validacion externa de generalizacion | https://www.kaggle.com/datasets/vjchoudhary7/hr-analytics-case-study |
| Glassdoor Job Reviews (NLP) | Pipeline NLP: sentimiento y clasificacion tematica | https://www.kaggle.com/datasets/davidgauthier/glassdoor-job-reviews |

## Descarga con Kaggle CLI

```bash
kaggle datasets download pavansubhasht/ibm-hr-analytics-attrition-dataset -p . --unzip
kaggle datasets download vjchoudhary7/hr-analytics-case-study -p . --unzip
kaggle datasets download davidgauthier/glassdoor-job-reviews -p . --unzip
```

## Archivos esperados en esta carpeta

- WA_Fn-UseC_-HR-Employee-Attrition.csv (IBM HR - 1,470 filas)
- general_data.csv + employee_survey_data.csv + manager_survey_data.csv (Extended - 4,410 filas)
- glassdoor_reviews.csv (Glassdoor - textos de resenas)

## Fecha de descarga original

Los datos fueron descargados el 15 de junio de 2026.
