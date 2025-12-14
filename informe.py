import pandas as pd
import matplotlib.pyplot as plt
import pdfkit
from pathlib import Path

# =========================
# 1️⃣ Leer datos
# =========================
df = pd.read_csv("datos.csv")

# =========================
# 2️⃣ Métricas principales
# =========================
total_ventas = df["ventas"].sum()
promedio_ventas = int(df["ventas"].mean())



mejor_producto = df.groupby("producto")["ventas"].sum().idxmax()
mejor_region = df.groupby("region")["ventas"].sum().idxmax()
mejor_vendedor = df.groupby("vendedor")["ventas"].sum().idxmax()

# =========================
# 3️⃣ Gráficos
# =========================
plt.figure(figsize=(8, 5))
df.groupby("producto")["ventas"].sum().plot(kind="bar")
plt.title("Ventas por Producto")
plt.ylabel("Ventas")
plt.tight_layout()
plt.savefig("grafico_ventas_producto.png")
plt.close()

plt.figure(figsize=(8, 5))
df.groupby("region")["ventas"].sum().plot(kind="bar")
plt.title("Ventas por Región")
plt.ylabel("Ventas")
plt.tight_layout()
plt.savefig("grafico_ventas_region.png")
plt.close()

# =========================
# 4️⃣ Rutas absolutas (Windows safe)
# =========================
base_path = Path(__file__).parent.resolve()
grafico_producto = (base_path / "grafico_ventas_producto.png").as_uri()
grafico_region = (base_path / "grafico_ventas_region.png").as_uri()

# =========================
# 5️⃣ HTML + CSS profesional
# =========================
html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Informe Profesional de Ventas</title>
  <style>
    body {{
      font-family: Arial, Helvetica, sans-serif;
      background-color: #f2f4f7;
      margin: 0;
      padding: 40px;
      color: #333;
    }}

    .container {{
      background-color: #ffffff;
      padding: 40px;
      border-radius: 12px;
      max-width: 900px;
      margin: auto;
    }}

    h1 {{
      text-align: center;
      color: #1F4E79;
      margin-bottom: 10px;
    }}

    .subtitle {{
      text-align: center;
      color: #666;
      margin-bottom: 40px;
    }}

    h2 {{
      color: #1F4E79;
      margin-top: 40px;
    }}

    p {{
      font-size: 14px;
      line-height: 1.6;
      margin-bottom: 15px;
    }}

    .card {{
      background-color: #f9fafb;
      padding: 20px;
      border-left: 5px solid #1F4E79;
      border-radius: 6px;
      margin-top: 20px;
    }}

    img {{
      max-width: 100%;
      margin-top: 20px;
      border-radius: 6px;
    }}

    .footer {{
      margin-top: 50px;
      font-size: 12px;
      color: #777;
      text-align: center;
    }}
  </style>
</head>

<body>
  <div class="container">

    <h1>Informe Profesional de Ventas</h1>
    <div class="subtitle">
      Análisis automatizado generado con Python
    </div>

    <h2>Resumen Ejecutivo</h2>
    <div class="card">
      <p>
        En el período analizado, se registró un total de
        <strong>{total_ventas}</strong> unidades vendidas,
        con un promedio de <strong>{promedio_ventas}</strong>

        ventas por registro.
      </p>

      <p>
        El producto con mejor desempeño fue
        <strong>{mejor_producto}</strong>,
        destacándose por su consistencia en ventas.
      </p>

      <p>
        La región con mayor volumen de ventas fue
        <strong>{mejor_region}</strong>,
        indicando una alta concentración de demanda.
      </p>

      <p>
        El vendedor más destacado del período fue
        <strong>{mejor_vendedor}</strong>,
        con una contribución significativa al total.
      </p>
    </div>

    <h2>Ventas por Producto</h2>
    <img src="{grafico_producto}">

    <h2>Ventas por Región</h2>
    <img src="{grafico_region}">

    <div class="footer">
      Informe generado automáticamente con Python · Proyecto de Data Analytics
    </div>

  </div>
</body>
</html>
"""

# =========================
# 6️⃣ Generar PDF
# =========================
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)

options = {
    "enable-local-file-access": None
}

pdfkit.from_string(
    html_content,
    "informe_ventas.pdf",
    configuration=config,
    options=options
)

print("✅ Informe generado correctamente: informe_ventas.pdf")
