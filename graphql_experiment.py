import requests
import time
import csv
import json

USERNAME = "Gaburieru35"
TOKEN = ""
N = 30

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

query = {
    "query": f"""
    {{
      user(login: "{USERNAME}") {{
        name
        followers {{
          totalCount
        }}
        repositories(first: 30) {{
          nodes {{
            name
            stargazerCount
          }}
        }}
      }}
    }}
    """
}

def executar_graphql():
    with open("graphql_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["trial", "tipo", "tempo_ms", "tamanho_bytes", "status"])

        for i in range(1, N + 1):
            print(f"[GraphQL] Execução {i}/{N}")

            inicio = time.perf_counter()
            response = requests.post(
                "https://api.github.com/graphql",
                headers=headers,
                data=json.dumps(query)
            )
            fim = time.perf_counter()

            tempo_ms = (fim - inicio) * 1000
            tamanho = len(response.content)

            writer.writerow([i, "GraphQL", tempo_ms, tamanho, response.status_code])

    print("Arquivo graphql_results.csv gerado com sucesso!")

if __name__ == "__main__":
    executar_graphql()
