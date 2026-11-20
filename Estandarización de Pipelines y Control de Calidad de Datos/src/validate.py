import pandas as pd


def validar_dataset(ruta_csv):
    # 1. Se carga el archivo CSV
    df = pd.read_csv("data/procesados/train.csv")

    # 2. Se verifican columnas esperadas
    columnas_esperadas = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "species",
    ]
    assert list(df.columns) == columnas_esperadas, (
        f"Columnas incorrectas en {ruta_csv}: {list(df.columns)}"
    )

    # 3. Se verifica que NO haya valores nulos (vacíos)
    assert not df.isna().any().any(), f"Se encontraron valores nulos en {ruta_csv}"

    # 4. Se verifican tipos de datos correctos
    for col in [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]:
        assert pd.api.types.is_numeric_dtype(df[col]), (
            f"La columna '{col}' debe ser numérica en {ruta_csv}"
        )

    assert pd.api.types.is_integer_dtype(df["species"]), (
        f"La columna 'species' debe ser entera en {ruta_csv}"
    )

    # 5. Verificamos rangos lógicos para las variables de Iris
    assert df["sepal length (cm)"].between(4.0, 8.0).all(), (
        "Valor fuera de rango en 'sepal length (cm)' [4.0, 8.0]"
    )
    assert df["sepal width (cm)"].between(2.0, 4.5).all(), (
        "Valor fuera de rango en 'sepal width (cm)' [2.0, 4.5]"
    )
    assert df["petal length (cm)"].between(1.0, 7.0).all(), (
        "Valor fuera de rango en 'petal length (cm)' [1.0, 7.0]"
    )
    assert df["petal width (cm)"].between(0.1, 2.5).all(), (
        "Valor fuera de rango en 'petal width (cm)' [0.1, 2.5]"
    )
    assert df["species"].isin([0, 1, 2]).all(), (
        "La columna 'species' debe contener solo valores 0, 1 o 2"
    )

    print(f"Validación exitosa en {ruta_csv}")


if __name__ == "__main__":
    # Ajusta la ruta si en tu prepare.py guardaste los CSV en otra carpeta
    validar_dataset("data/processed/train.csv")
    validar_dataset("data/processed/test.csv")

    print("Paso 2 listo: se validaron los datos de train.csv")



