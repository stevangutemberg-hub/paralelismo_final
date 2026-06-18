# 🚇 Análise Paralela de Dados Metroviários

---

## 🎯 Tema do Projeto

**Análise e Predição Paralela de Congestionamento em Sistemas Metroviários**

---

## 📝 Descrição do Tema

O objetivo deste projeto é analisar grandes volumes de dados de mobilidade urbana utilizando técnicas de paralelização para identificar padrões de uso e prever situações de congestionamento.

---

## 📊 Visão Geral do Dataset

Dataset de fluxo de passageiros do metrô de Nova York (Kaggle).

📎 https://www.kaggle.com/datasets/yaminh/mta-subway-hourly-ridership-2022-to-2024/data

---

## ⚙️ Abordagem Técnica

* Paralelização por estação
* Paralelização por tempo
* Uso de múltiplos processos (melhoria aplicada)

---

# 📊 RESULTADOS

---

## ⏰ Horários Mais Movimentados

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

## 🏆 Estação Mais Movimentada

**Times Sq-42 St / 42 St**
**84.480.828 passageiros**

---

## ⏱️ Tempo Final

* **12 processos → 59.85 segundos** ✅

---

## 📊 Comparativo

| Processos | Tempo (s) | Speedup |
| --------- | --------- | ------- |
| 2         | 132.40    | 1.00x   |
| 4         | 70.04     | 1.89x   |
| 8         | 62.41     | 2.12x   |
| 12        | 59.85     | 2.21x   |

---

# 📊 Gráficos Atualizados

### ⏱️ Tempo

![Tempo](tempo.png)

### 🚀 Speedup

![Speedup](speedup.png)

### ⚡ Eficiência

![Eficiência](eficiencia.png)

---

## 📌 Conclusão

* O uso de **multiprocessamento** trouxe ganho real de desempenho
* Threads não foram eficientes nesse cenário
* O tipo de paralelismo impacta diretamente o resultado

---

## 🛠️ Tecnologias

* Python
* Processamento paralelo
* Multiprocessing

---

## 📌 Considerações Finais

Este projeto demonstra na prática que:

* Nem todo paralelismo é eficiente
* Processos podem ser superiores a threads
* Avaliar desempenho é essencial

---
