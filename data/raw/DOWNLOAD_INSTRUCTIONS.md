# Instrucciones de Descarga de Datos

Los datasets no estan incluidos en el repositorio por terminos de uso de Kaggle.
Se requiere una cuenta gratuita en Kaggle para descargarlos.

## Datasets necesarios

| Dataset | URL |
|---------|-----|
| IBM HR Analytics (Principal) | https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset |
| HR Extended (Validacion) | https://www.kaggle.com/datasets/vjchoudhary7/hr-analytics-case-study |
| Glassdoor Reviews (NLP) | https://www.kaggle.com/datasets/andreshg/employee-reviews |

## Descarga con Kaggle CLI

```bash
kaggle datasets download pavansubhasht/ibm-hr-analytics-attrition-dataset -p . --unzip
kaggle datasets download vjchoudhary7/hr-analytics-case-study -p . --unzip
kaggle datasets download andreshg/employee-reviews -p . --unzip
```

Coloca los archivos CSV en esta carpeta (data/raw/).

Fecha de descarga original: 15 de junio de 2026.
