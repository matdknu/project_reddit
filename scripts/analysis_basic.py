# ========================================
# 1️⃣ Importar librerías
# ========================================
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ========================================
# 2️⃣ Cargar datos
# ========================================
path = "raw_data/reddit_comentarios.csv"
df = pd.read_csv(path, low_memory=False)

print("Shape:", df.shape)
print(df.head())
print(df.info())

# ========================================
# 3️⃣ Procesar fechas (si existe columna de fecha)
# ========================================
if "post_created" in df.columns:
    df["post_created"] = pd.to_datetime(df["post_created"], errors="coerce")
    daily = df.groupby(df["post_created"].dt.date).size().reset_index(name="n_posts")

    # Crear carpeta de salida
    Path("data/reports").mkdir(parents=True, exist_ok=True)

    # ========================================
    # 4️⃣ Graficar posts por día
    # ========================================
    plt.figure(figsize=(10,5))
    plt.plot(daily["post_created"], daily["n_posts"], marker="o", linestyle="-")
    plt.title("Posts per day")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("data/reports/daily_posts_from_raw.png", dpi=150)
    print("Saved plot -> data/reports/daily_posts_from_raw.png")
else:
    print("⚠️ La columna 'post_created' no está en reddit_posts.csv")
