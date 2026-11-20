# Actividad 2.1 – Estandarización de Pipelines y Control de Calidad de Datos

## Objetivo
Implementar una línea base (Baseline) utilizando un modelo de Machine Learning con el conjunto de datos Iris. Este proyecto toma el modelo de clasificación de flores Iris con Random Forest y lo organiza en pasos reproducibles con validación de datos, registro en MLflow, pruebas con `pytest` y ejecución automatizada con `Makefile`.
---

# Requisitos
Antes de iniciar, verificar que se encuentre instalado:
- Python 3.10 o superior
- Visual Studio Code / Antigravity o el editor de código de su preferencia.
- Extensión de Python para VS Code / Antigravity o el editor de código de su preferencia.
- Git (Opcional)
---

# 1. Preparar el entorno desde cero

- Abre una terminal en la carpeta del proyecto.
- Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Linux / macOS:
   source .venv/bin/activate
---

# 2. Instalar las librerías:

```powershell
pip install -r requirements.txt
```
---

# 3. Ejecutar el Makefile

- Desde la terminal ejecutar:

```powershell
make all
```
- Si el entrenamiento fue exitoso aparecerá un resultado similar a:
```
Modelo registrado con accuracy: 1.0
Run ID:
xxxxxxxxxxxxxxxxxxxxxxxx
```
---

# 4. Abrir MLflow UI
- Abrir una **segunda terminal** en Visual Studio Code.

- Activar nuevamente el entorno virtual (de ser necesario):

```powershell
venv\Scripts\activate
```

- Ejecutar:
```powershell
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

- Abrir el navegador en:
```
http://127.0.0.1:5000
```
---

