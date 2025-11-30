# Lab 5 Experimentação

## 1. Desenho do Experimento

### Hipóteses

**RQ1. Respostas GraphQL são mais rápidas que respostas REST?**\
- H0: Não existe diferença significativa no tempo de resposta entre REST
e *GraphQL*.\
- H1: O tempo de resposta de *GraphQL* é significativamente menor que o
de REST.

**RQ2. Respostas GraphQL têm tamanho menor que respostas REST?**\
- H0: Não existe diferença significativa no tamanho das respostas entre
REST e *GraphQL*.\
- H1: As respostas de *GraphQL* têm tamanho significativamente menor que
as respostas REST.

### Variáveis Dependentes

-   Tempo de resposta das requisições.\
-   Tamanho das respostas retornadas.

### Variáveis Independentes

-   Tipo da API utilizada (REST ou *GraphQL*).

### Tratamentos

-   Execução de consultas REST da API pública do GitHub.\
-   Execução de consultas *GraphQL* da API pública do GitHub.

### Objetos Experimentais

O experimento utilizará a mesma fonte de dados disponibilizada pelo
GitHub nos dois formatos.

Consultas REST:\
- `GET https://api.github.com/users/<username>`\
- `GET https://api.github.com/users/<username>/repos`

Consulta GraphQL:

    {
      user(login: "<username>") {
        name
        followers {
          totalCount
        }
        repositories(first: 100) {
          nodes {
            name
            stargazerCount
          }
        }
      }
    }

### Tipo de Projeto Experimental

Experimento controlado com medições repetidas.

### Quantidade de Medições

-   30 requisições REST.\
-   30 requisições *GraphQL*.

### Ameaças à Validade

-   Variação da rede.\
-   Rate limit da API.\
-   Diferenças de infraestrutura.\
-   Cache interno da API.\
-   Amostra limitada.

------------------------------------------------------------------------

## 2. Preparação do Experimento

### Ferramentas Utilizadas

-   Python\
-   Biblioteca *requests*\
-   Biblioteca `gql` ou `requests`\
-   `time.perf_counter()`\
-   CSV para armazenamento

### API Pública Escolhida

A API do GitHub:\
- REST: `https://api.github.com/`\
- GraphQL: `https://api.github.com/graphql`

### Scripts Preparados

#### Script REST

-   Consulta `/users/<username>` e `/users/<username>/repos`.\
-   Mede tempo e tamanho.\
-   Salva em CSV.

#### Script GraphQL

-   Envia consulta equivalente via POST.\
-   Mede tempo e tamanho.\
-   Salva em CSV.

### Ambiente Experimental

-   Linux\
-   Mesma máquina para todos os testes\
-   Execuções sequenciais\
-   Cuidados com limites da API
