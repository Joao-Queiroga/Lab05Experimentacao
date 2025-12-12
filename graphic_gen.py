import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("imagens", exist_ok=True)

# ================================
# 1. Carregar o CSV existente
# ================================
df = pd.read_csv("experiment_full.csv")

# ================================
# 2. Separar REST e GraphQL
# ================================
rest = df[df["tipo"] == "REST"]
gql = df[df["tipo"] == "GraphQL"]

# ================================
# 3. Gráfico: Tempo de Resposta
# ================================
plt.figure(figsize=(8, 5))
plt.boxplot([rest["tempo_ms"], gql["tempo_ms"]], labels=["REST", "GraphQL"])
plt.ylabel("Tempo (ms)")
plt.title("Comparação de Tempo de Resposta")
plt.tight_layout()
plt.savefig("imagens/tempo_resposta.png", dpi=300)
plt.close()  # fecha a figura após salvar

# ================================
# 4. Gráfico: Tamanho das Respostas
# ================================
plt.figure(figsize=(8, 5))
plt.boxplot([rest["tamanho_bytes"], gql["tamanho_bytes"]], labels=["REST", "GraphQL"])
plt.ylabel("Tamanho da Resposta (bytes)")
plt.title("Comparação do Tamanho das Respostas")
plt.tight_layout()
plt.savefig("imagens/tamanho_resposta.png", dpi=300)
plt.close()
