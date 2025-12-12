# LAB05 — GraphQL vs REST: Um Experimento Controlado  
## Sprint 2 — Execução, Análise e Relatório Final

---

# 1. Introdução

GraphQL surgiu como alternativa ao modelo tradicional de APIs REST, oferecendo consultas flexíveis e potencial para reduzir o volume de dados trafegados. Entretanto, seus benefícios de desempenho ainda precisam ser avaliados empiricamente em cenários reais.  

Este experimento controlado compara REST e GraphQL utilizando a API pública do GitHub, com foco em duas dimensões:

- **RQ1:** GraphQL é mais rápido que REST?  
- **RQ2:** GraphQL retorna respostas menores que REST?

Para responder a essas questões, coletamos 60 medições (30 REST e 30 GraphQL), aplicando ambos os tratamentos sobre o mesmo objeto experimental.

---

# 2. Metodologia

## 2.1 Hipóteses

### Tempo de resposta (RQ1)
- **H0₁:** Não existe diferença significativa entre os tempos de resposta de REST e GraphQL.  
- **H1₁:** O tempo de resposta de GraphQL é significativamente menor que o de REST.

### Tamanho da resposta (RQ2)
- **H0₂:** Não existe diferença significativa no tamanho das respostas entre REST e GraphQL.  
- **H1₂:** O tamanho das respostas GraphQL é significativamente menor.

---

## 2.2 Variáveis

- **Independente:** Tipo da API (REST ou GraphQL)  
- **Dependentes:**  
  - Tempo de resposta (ms)  
  - Tamanho da resposta (bytes)

---

## 2.3 Tratamentos

- **REST:**  
  - `GET /users/<username>`  
  - `GET /users/<username>/repos`  
  O tempo e tamanho são somados.

- **GraphQL:**  
  - Consulta única agregando os mesmos dados retornados por REST.

---

## 2.4 Objetos experimentais
Dados públicos de um mesmo usuário GitHub.

---

## 2.5 Tipo de experimento
Experimento controlado com **medições repetidas**.

---

## 2.6 Quantidade de medições
- 30 REST  
- 30 GraphQL  

---

## 2.7 Ambiente Experimental
- Linux  
- Python + `requests`  
- Métricas via `time.perf_counter()`  
- Armazenamento dos dados em CSV  
- Execução sequencial  
- Token GitHub utilizado

---

# 3. Execução do Experimento

A execução seguiu o plano definido na Sprint 1:

### REST
Para cada uma das 30 medições:
1. `GET /users/<username>`
2. `GET /users/<username>/repos`
3. Tempo total = soma das duas requisições  
4. Tamanho total = soma dos dois payloads

### GraphQL
Para cada uma das 30 medições:
1. Envio da consulta agregada
2. Medição do tempo
3. Registro do tamanho da resposta

Nenhuma requisição falhou e não houve rate limit.

---

# 4. Análise dos Resultados

Os dados reais do arquivo `experiment_full.csv` foram analisados estatisticamente.

---

## 4.1 Estatísticas Descritivas (dados reais)

### Tempo de resposta (ms)

| Métrica | REST | GraphQL |
|--------|-------|----------|
| **Média** | 1108.94 ms | 1580.48 ms |
| **Mediana** | 1086.98 ms | 1538.11 ms |
| **Desvio-padrão** | 104.38 | 245.59 |
| **Mínimo** | 988.08 | 1261.76 |
| **Máximo** | 1351.47 | 2260.41 |

### Tamanho das respostas (bytes)

| Métrica | REST | GraphQL |
|--------|-------|----------|
| **Média** | 134162 bytes | 1540 bytes |
| **Desvio-padrão** | 0 | 0 |
| **Mediana** | 134162 | 1540 |

> Observação: todos os tamanhos REST foram 134.162 bytes e todos os tamanhos GraphQL foram 1.540 bytes, indicando consistência total nos payloads.

---

## 4.2 Testes Estatísticos

Como os dados não são normalmente distribuídos (Shapiro-Wilk), utilizamos o **Wilcoxon pareado**.

### RQ1 – Tempo de resposta

**Teste:** Wilcoxon pareado  
**Hipótese alternativa:** GraphQL < REST  

**Resultado real:**  
- Estatística = 465.0  
- **p = 1.0**

**Interpretação:**  
Não há evidência estatística de que GraphQL seja mais rápido.  
Na verdade, os tempos **REST foram consistentemente menores** que os tempos GraphQL.

Portanto:
- **H0₁ NÃO é rejeitada.**
- **H1₁ é rejeitada.**

---

### RQ2 – Tamanho das respostas

**Teste:** Wilcoxon pareado  
**Hipótese alternativa:** GraphQL < REST  

**Resultado real:**  
- Estatística = 0.0  
- **p = 9.31e-10** (extremamente significativo)

**Interpretação:**  
GraphQL retorna respostas **drasticamente menores** que REST.

Portanto:
- **H0₂ é rejeitada.**
- **H1₂ é aceita.**

---

# 5. Resultados

Com base nos dados reais coletados:

- **GraphQL NÃO foi mais rápido** que REST.  
  - REST apresentou média **1108 ms**, enquanto GraphQL apresentou **1580 ms**.  
  - p = 1.0 → nenhuma evidência de ganho de tempo.

- **GraphQL retornou respostas muito menores**, com redução superior a 98%.  
  - REST: 134.162 bytes  
  - GraphQL: 1.540 bytes  
  - p ≈ 9e-10 → altamente significativo.

---

# 6. Discussão

Os resultados contradizem a expectativa comum de que GraphQL seja mais rápido.  
Ao contrário:

- **REST foi mais rápido e mais consistente**.
- **GraphQL foi mais lento**, possivelmente devido a:
  - processamento adicional de esquema
  - montagem da resposta em grafo
  - custo de validação da query

Entretanto, o ganho no **tamanho das respostas** é enorme e consistente, demonstrando que GraphQL:

- reduz drasticamente o tráfego de rede  
- evita overfetching típico de REST  
- retornou sempre o mesmo payload compacto

## 6.1 Ameaças à validade

### Validade interna
- Variabilidade de rede pode favorecer um dos métodos.
- GraphQL pode exigir tempo adicional de processamento do lado do GitHub.

### Validade externa
- Resultados dependem da API do GitHub.
- Experimentos em outras APIs podem ter comportamento diferente.

### Validade de construção
- O tempo total inclui latência da rede e overhead do cliente Python.

### Validade de conclusão
- O tamanho fixo dos payloads facilita a comparação.
- 30 repetições são adequadas para testes não paramétricos.

---

# 7. Conclusão

Com base nas 60 medições coletadas:

### **RQ1 — GraphQL é mais rápido que REST?**  
❌ **Não. REST foi mais rápido na média e a diferença foi significativa ao contrário (GraphQL mais lento).**

### **RQ2 — GraphQL retorna respostas menores que REST?**  
✅ **Sim. A diferença foi extremamente significativa, com redução de mais de 98% no tamanho.**

Portanto:

- **GraphQL perde em tempo**  
- **GraphQL vence em tamanho de resposta**

Cada abordagem apresenta vantagens diferentes, e a escolha deve considerar o contexto da aplicação.

---

# 8. Referências

- GitHub REST API  
- GitHub GraphQL API  
- Wohlin, C. *Experimentation in Software Engineering*  
- Python Documentation (`requests`, `time.perf_counter()`)  
