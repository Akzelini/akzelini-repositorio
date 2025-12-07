import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_data = {
    "gameid": ["g1","g2","g3","g4","g5","g6"],
    "title": ["cyber-punk 2078","elder scrolls vi",
              "llama tycoon","super mario odyssey2",
              "fifa 2026","dark souls iv"],
    "genre": ["rpg","rpg","simulation","platform","sports","rpg"],
    "publisher": ["dev-studios","bethesda","llama-soft",
                  "nintendo","ea","fromsoft"],
    "units_sold_millions": [15.5,20.1,8.0,12.3,18.2,19.6]
}

sales_df = pd.DataFrame(sales_data)

reviews_data = {
    "gameid": ["g1","g2","g3","g4","g5","g7"],
    "critic_score": [7.5,9.5,8.8,9.7,6.1,8.0],
    "user_score": [5.1,9.1,8.5,9.2,np.nan,7.5]
}

reviews_df = pd.DataFrame(reviews_data)

print("--- datos de ventas (crudos) ---")
print(sales_df)
print("--- datos de reseñas (crudos) ---")
print(reviews_df)

mean_user_score = reviews_df["user_score"].mean()
reviews_df["user_score"] = reviews_df["user_score"].fillna(mean_user_score)

print(f"\n--- reseñas (limpias,nan rellenado con {mean_user_score})---")
print(reviews_df)

df = pd.merge(sales_df, reviews_df, on="gameid", how="inner")

print("\n--- tabla fusionada de ventas+reseñas ---")
print(df)

df["revenue_estimate_billions"] = (df["units_sold_millions"] * 50) / 1000
df["score_gap"] = df["critic_score"] - df["user_score"]
df["critic_score_100"] = df["critic_score"] * 10

print("\n--- tabla transformada (con nuevas columnas) ---")
print(df)

