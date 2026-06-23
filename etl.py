import psycopg
import pandas as pd

conn = psycopg.connect(
    host="localhost",
    dbname="seme",
    user="seme_user",
    password="seme123"
)

# EXTRACT
df = pd.read_sql("SELECT * FROM ventas", conn)

# TRANSFORM
df["ingreso_calculado"] = df["cantidad"] * df["precio_unitario"]
df["margen_estimado"] = df["ingreso_calculado"] * 0.30

print(df)

# LOAD (archivo para R / Power BI)
df.to_csv("exports/ventas_limpias.csv", index=False)

conn.close()

print("ETL SEME completado ✔️")
