# 🚇 Análise Paralela de Dados Metroviários

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

## 🎯 Tema do Projeto

**Análise e Predição Paralela de Congestionamento em Sistemas Metroviários**

---

## 📝 Descrição do Tema

O objetivo deste projeto é analisar grandes volumes de dados de mobilidade urbana utilizando técnicas de paralelização para identificar padrões de uso e prever situações de congestionamento no sistema metroviário.

### 🔎 A proposta consiste em:

* Processar dados massivos de fluxo de passageiros
* Detectar padrões de uso ao longo do tempo
* Identificar estações com maior risco de superlotação

---

## 💡 Justificativa

Sistemas de transporte urbano geram grandes volumes de dados continuamente. A análise eficiente dessas informações é essencial para:

* Melhorar a mobilidade urbana
* Reduzir congestionamentos
* Otimizar a operação do transporte público

Nesse contexto, o uso de processamento paralelo se torna fundamental para lidar com a alta quantidade de dados e reduzir o tempo de análise.

---

## ⚙️ Abordagem Técnica

O projeto utiliza técnicas de paralelização para dividir o processamento dos dados em múltiplas tarefas executadas simultaneamente.

### 🧠 Estratégias aplicadas:

* Paralelização por estação
* Paralelização por intervalos de tempo
* Processamento concorrente utilizando múltiplas threads

---

## 📈 Métricas e Análises

As principais análises realizadas incluem:

* Cálculo do fluxo de passageiros (**entradas - saídas**)
* Identificação de horários de pico
* Detecção de estações congestionadas
* Previsão de fluxo futuro
* Identificação de gargalos no sistema

---

## 📊 Resultados Obtidos

### 🚉 Top 10 Estações Mais Movimentadas

| Estação                    | Total de Passageiros |
| -------------------------- | -------------------- |
| Times Sq-42 St / 42 St     | 84.480.828           |
| Grand Central-42 St        | 59.456.033           |
| 34 St-Herald Sq            | 46.907.575           |
| 14 St-Union Sq             | 42.161.109           |
| Fulton St                  | 35.158.520           |
| 34 St-Penn Station (A,C,E) | 33.972.338           |
| 59 St-Columbus Circle      | 31.489.614           |
| 34 St-Penn Station (1,2,3) | 30.595.789           |
| 74-Broadway / Jackson Hts  | 27.966.198           |
| Flushing-Main St           | 27.446.956           |

---

### ⏰ Horários Mais Movimentados

| Hora | Fluxo de Passageiros |
| ---- | -------------------- |
| 17h  | 216.732.188          |
| 16h  | 188.419.876          |
| 08h  | 184.222.952          |
| 18h  | 169.894.629          |
| 15h  | 166.336.093          |
| 07h  | 152.379.532          |
| 14h  | 137.990.419          |
| 09h  | 127.616.202          |
| 13h  | 117.243.769          |
| 19h  | 114.133.640          |

---

### ⚠️ Possíveis Atrasos Detectados

Algumas estações apresentaram fluxo anormalmente baixo, o que pode indicar falhas operacionais ou atrasos:

* High St (A,C)
* 81 St - Museum of Natural History
* 135 St
* Hoyt St
* Canal St
* 57 St
* Broadway-Lafayette St / Bleecker St
* 14 St-Union Sq
* Times Sq-42 St

---

### 🚨 Possíveis Riscos de Superlotação

Foram identificadas estações com alto volume concentrado, indicando risco de superlotação:

* Canal St
* 57 St
* 86 St
* Sutphin Blvd (JFK Airport)
* 14 St-Union Sq
* Times Sq-42 St
* Atlantic Av-Barclays Center
* Broadway-Lafayette St

---

### 🏆 Estação Mais Movimentada

* **Estação:** Times Sq-42 St / 42 St
* **Total de Passageiros:** 84.480.828

---

### ⏱️ Desempenho

* **Tempo total de processamento:** 364,94 segundos

O uso de paralelização contribuiu significativamente para a redução do tempo de análise, mesmo com grande volume de dados.

---

## 🎯 Resultados Esperados

* Identificação das estações mais movimentadas
* Previsão de períodos de superlotação
* Mapeamento de gargalos operacionais
* Redução do tempo de processamento através da paralelização

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Java
* **Paradigma:** Programação concorrente
* **Estruturas:** Threads, ExecutorService
* **Manipulação de dados:** Arquivos CSV

---

## 📌 Considerações Finais

Este projeto demonstra como técnicas de paralelização podem ser aplicadas na análise de grandes volumes de dados reais, contribuindo para soluções eficientes em problemas de mobilidade urbana.

Além disso, evidencia a importância da computação concorrente no processamento de dados em larga escala.
