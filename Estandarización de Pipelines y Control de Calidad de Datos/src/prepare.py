from pathlib import Path
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. Se crea la carpeta data/processed si todavía no existe
carpeta_salida = Path("data/procesados")
carpeta_salida.mkdir(parents=True, exist_ok=True)

# 2. Se cargan los datos de Iris y se crea una dataframw
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data["species"] = iris.target

# 3. Se dividen los datos para entrenar (80%) y para probar (20%)
train_df, test_df = train_test_split(data, test_size=0.2, random_state=42)

# 4. Se guardan ambos archivos en la carpeta creada (data/processed/)
train_df.to_csv(carpeta_salida / "train.csv", index=False)
test_df.to_csv(carpeta_salida / "test.csv", index=False)

print("Paso 1 listo: se crearon train.csv y test.csv en la carpeta procesados")