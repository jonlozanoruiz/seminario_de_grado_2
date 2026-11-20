import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path

# 1. Se crea la carpeta data/processed si todavía no existe
carpeta_salida = Path("models")
carpeta_salida.mkdir(parents=True, exist_ok=True)

mlflow.set_experiment("Proyecto_Final_Grado")

with mlflow.start_run():
    n_estimators = 100
    mlflow.log_param("n_estimators", n_estimators)
    
    # Se cargan los datos procesados
    train = pd.read_csv('data/procesados/train.csv')
    X_train = train.drop('species', axis=1)
    y_train = train['species']
    
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)
    
    # Se evalúa con test
    test = pd.read_csv('data/procesados/test.csv')
    X_test = test.drop('species', axis=1)
    y_test = test['species']
    accuracy = model.score(X_test, y_test)
    
    mlflow.log_metric("accuracy", accuracy)
    #mlflow.sklearn.log_model(model, "iris_model")
    mlflow.sklearn.log_model(sk_model=model, artifact_path="iris_model", skops_trusted_types=["sklearn.tree._tree.Tree"])
    
    # Se guarda el modelo localmente para pipeline
    joblib.dump(model, 'models/model.pkl')
    
    print(f"Paso 3 listo: Modelo entrenado con accuracy: {accuracy}")

    
    