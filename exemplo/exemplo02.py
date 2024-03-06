# ------- Exemplo de uso do Pandera para inferir o esquema de um DataFrame -------
import pandas as pd
import pandera as pa

from pandera import Check, Column, DataFrameSchema

df = pd.DataFrame({
    "column1": [5, 10, 20],
    "column2": ["a", "b", "c"],
    "column3": pd.to_datetime(["2020-01-01", "2020-02-01", "2020-03-01"])
})
schema = pa.infer_schema(df)

# Gerar o esquema do DataFrame em um arquivo
with open("inferred_schema.py", "w") as f:
    f.write(pa.infer_schema(df).to_script())

print(schema)