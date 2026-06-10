# 🚇 Análise Paralela de Dados Metroviários

---

## 🎯 Tema do Projeto

**Análise e Predição Paralela de Congestionamento em Sistemas Metroviários**

---

## 📝 Descrição do Tema

O objetivo deste projeto é analisar grandes volumes de dados de mobilidade urbana utilizando técnicas de paralelização para identificar padrões de uso e prever situações de congestionamento no sistema metroviário.

---

## 📊 Visão Geral do Dataset

Este projeto utiliza o dataset de fluxo de passageiros do sistema metroviário de Nova York, disponibilizado através da plataforma Kaggle.

O conjunto de dados contém informações detalhadas sobre o uso do metrô em intervalos de tempo (horários), permitindo análises temporais, espaciais e comportamentais do fluxo de passageiros.

---

## 🗂️ Estrutura do Banco de Dados

O dataset é composto por registros contendo:

* **station** → nome da estação
* **line** → linha do metrô
* **datetime** → data e hora da medição
* **entries** → número de entradas de passageiros
* **exits** → número de saídas de passageiros
* **latitude / longitude** → localização geográfica
* **payment_method** → método de pagamento

📎 Dataset:
https://www.kaggle.com/datasets/yaminh/mta-subway-hourly-ridership-2022-to-2024/data

---

## ⚙️ Abordagem Técnica

* Paralelização por estação
* Paralelização por tempo
* Uso de múltiplas threads

---

## 📊 Resultados Obtidos (Atualizado com Paralelização)

### 🚉 Top 10 Estações Mais Movimentadas

| Estação                    | Total      |
| -------------------------- | ---------- |
| Times Sq-42 St / 42 St     | 84.480.828 |
| Grand Central-42 St        | 59.456.033 |
| 34 St-Herald Sq            | 46.907.575 |
| 14 St-Union Sq             | 42.161.109 |
| Fulton St                  | 35.158.520 |
| 34 St-Penn Station (A,C,E) | 33.972.338 |
| 59 St-Columbus Circle      | 31.489.614 |
| 34 St-Penn Station (1,2,3) | 30.595.789 |
| 74-Broadway / Jackson Hts  | 27.966.198 |
| Flushing-Main St           | 27.446.956 |

---

### ⏰ Horários Mais Movimentados

| Hora | Fluxo       |
| ---- | ----------- |
| 17h  | 216.732.188 |
| 16h  | 188.419.876 |
| 08h  | 184.222.952 |
| 18h  | 169.894.629 |
| 15h  | 166.336.093 |
| 07h  | 152.379.532 |
| 14h  | 137.990.419 |
| 09h  | 127.616.202 |
| 13h  | 117.243.769 |
| 19h  | 114.133.640 |

---

### ⚠️ Possíveis Atrasos Detectados

Foram identificadas estações com fluxo anormalmente baixo, indicando possíveis falhas operacionais:

* 23 St (R,W)
* Halsey St (L)
* 57 St (F)
* Canal St (A,C,E)
* 63 Dr-Rego Park (M,R)
* 2 Av (F)
* W 4 St-Wash Sq
* Lexington Av/63 St
* 103 St
* Grand Av-Newtown

---

### 🚨 Riscos de Superlotação

* Canal St
* 57 St
* 2 Av
* Lexington Av/63 St
* Chambers St
* 1 Av
* 103 St

---

### 🏆 Estação Mais Movimentada

* **Times Sq-42 St / 42 St**
* **Total:** 84.480.828 passageiros

---

## ⏱️ Desempenho com Paralelização

* **Tempo com 12 threads:** 259.42 segundos

---

## 📊 Comparativo de Desempenho

| Threads | Tempo (s) | Speedup |
| ------- | --------- | ------- |
| 2       | 257.92    | 1.00x   |
| 4       | 257.40    | 1.00x   |
| 8       | 257.43    | 1.00x   |
| 12      | 259.42    | 0.99x   |

---

## 📌 Análise

Apesar do uso de múltiplas threads, não houve ganho significativo de desempenho.

Isso indica:

* Overhead de threads elevado
* Possível gargalo de I/O
* Limitação pelo hardware

---

# 🧮 Relatório de Paralelismo — Soma de Dados

---

## 📌 Descrição do Problema

Desenvolver um programa para somar milhões de números utilizando paralelismo com múltiplas threads.

---

## 💻 Ambiente Experimental

| Item        | Descrição          |
| ----------- | ------------------ |
| Processador | Intel i5 / Ryzen 5 |
| Núcleos     | 12                 |
| RAM         | 8 GB               |
| SO          | Windows            |
| Linguagem   | Python             |
| Biblioteca  | concurrent.futures |

---

## ⚙️ Metodologia

Execução com:

* 1 thread (serial)
* 2, 4, 8 e 12 threads

---

## 📊 Resultados

| Threads | Tempo (s) |
| ------- | --------- |
| 1       | 0.081     |
| 2       | 0.081     |
| 4       | 0.086     |
| 8       | 0.084     |
| 12      | 0.165     |

---

## 📈 Speedup e Eficiência

| Threads | Tempo | Speedup | Eficiência |
| ------- | ----- | ------- | ---------- |
| 1       | 0.081 | 1.0     | 1.0        |
| 2       | 0.081 | 0.99    | 0.50       |
| 4       | 0.086 | 0.94    | 0.24       |
| 8       | 0.084 | 0.96    | 0.12       |
| 12      | 0.165 | 0.49    | 0.04       |

---

## 📊 Gráficos

### ⏱️ Tempo de Execução

![Tempo](graficorafa/tempo.png)

### 🚀 Speedup

![Speedup](graficorafa/speedup.png)

### ⚡ Eficiência

![Eficiência](graficorafa/eficiência.png)

---

## 📌 Análise dos Resultados

Os testes mostraram que o paralelismo não trouxe ganho significativo de desempenho.

Principais motivos:

* Overhead de criação de threads
* Limitações de memória
* Gargalos de leitura de dados
* Escalonamento ineficient

---

## 🛠️ Tecnologias Utilizadas

* Python
* Java
* Programação concorrente
* Processamento paralelo
  
---

## 🏁 Conclusão

O projeto demonstrou na prática que:

* Paralelismo nem sempre melhora desempenho
* O tipo de tarefa influencia diretamente o ganho
* Threads em excesso podem prejudicar performance

Mesmo assim, o experimento foi essencial para consolidar conceitos como:

* Concorrência
* Speedup
* Eficiência

---

## 📌 Considerações Finais

Este projeto reforça a importância de avaliar cuidadosamente o uso de paralelismo, considerando não apenas a quantidade de threads, mas também o tipo de processamento e os gargalos envolvidos.


Este projeto demonstra como técnicas de paralelização podem ser aplicadas na análise de grandes volumes de dados reais, contribuindo para soluções eficientes em problemas de mobilidade urbana.

Além disso, evidencia a importância da computação concorrente no processamento de dados em larga escala.
