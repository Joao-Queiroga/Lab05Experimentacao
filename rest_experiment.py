import requests
import time
import csv

USERNAME = "Gaburieru35" 
TOKEN = ""
N = 30

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}"
}

def medir_requisicao(url):
    """Mede tempo e tamanho de uma requisição GET."""
    inicio = time.perf_counter()
    response = requests.get(url, headers=headers)
    fim = time.perf_counter()

    tempo_ms = (fim - inicio) * 1000
    tamanho = len(response.content)

    return tempo_ms, tamanho, response.status_code

def executar_rest():
    with open("rest_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["trial", "tipo", "tempo_ms", "tamanho_bytes", "status"])

        for i in range(1, N + 1):
            print(f"[REST] Execução {i}/{N}")

            # Endpoint 1
            url_user = f"https://api.github.com/users/{USERNAME}"
            tempo1, tam1, st1 = medir_requisicao(url_user)

            # Endpoint 2
            url_repos = f"https://api.github.com/users/{USERNAME}/repos"
            tempo2, tam2, st2 = medir_requisicao(url_repos)

            # Tempo total e tamanho total
            tempo_total = tempo1 + tempo2
            tamanho_total = tam1 + tam2

            writer.writerow([i, "REST", tempo_total, tamanho_total, f"{st1}/{st2}"])

    print("Arquivo rest_results.csv gerado com sucesso!")

if __name__ == "__main__":
    executar_rest()
