import pandas as pd

rest = pd.read_csv("rest_results.csv")
graphql = pd.read_csv("graphql_results.csv")

full = pd.concat([rest, graphql], ignore_index=True)
full.to_csv("experiment_full.csv", index=False)

print("Arquivo experiment_full.csv gerado com todos os dados!")
