Análise Paralela de Dados Metroviários

-Visão Geral do Dataset

Este projeto utiliza o dataset de fluxo de passageiros do sistema metroviário de Nova York, disponibilizado através da plataforma Kaggle.

O conjunto de dados contém informações detalhadas sobre o uso do metrô em intervalos de tempo (horários), permitindo análises temporais, espaciais e comportamentais do fluxo de passageiros.

- Estrutura do Banco de Dados

O dataset é composto por registros contendo:

station → nome da estação
line → linha do metrô
datetime → data e hora da medição
entries → número de entradas de passageiros
exits → número de saídas de passageiros
latitude / longitude → localização geográfica
payment_method → método de pagamento

Esses dados possibilitam a construção de análises complexas envolvendo fluxo de passageiros, padrões de mobilidade e comportamento do sistema de transporte.

- Tema do Projeto

Análise e Predição Paralela de Congestionamento em Sistemas Metroviários

- Descrição do Tema

O objetivo deste projeto é analisar grandes volumes de dados de mobilidade urbana utilizando técnicas de paralelização para identificar padrões de uso e prever situações de congestionamento no sistema metroviário.

A proposta consiste em:

Processar dados massivos de fluxo de passageiros
Detectar padrões de uso ao longo do tempo
Identificar estações com maior risco de superlotação
Prever congestionamentos futuros com base em dados históricos
Detectar gargalos operacionais na rede metroviária
- Justificativa

Sistemas de transporte urbano geram grandes volumes de dados continuamente. A análise eficiente dessas informações é essencial para:

melhorar a mobilidade urbana
reduzir congestionamentos
otimizar a operação do transporte público

Nesse contexto, o uso de processamento paralelo se torna fundamental para lidar com a alta quantidade de dados e reduzir o tempo de análise.

 - Abordagem Técnica

O projeto utiliza técnicas de paralelização para dividir o processamento dos dados em múltiplas tarefas executadas simultaneamente.

Estratégias aplicadas:
Paralelização por estação
Paralelização por intervalos de tempo
Processamento concorrente utilizando múltiplas threads
- Métricas e Análises

-As principais análises realizadas incluem:

Cálculo do fluxo de passageiros (entradas - saídas)
Identificação de horários de pico
Detecção de estações congestionadas
Previsão de fluxo futuro
Identificação de gargalos no sistema

- Resultados Esperados
Identificação das estações mais movimentadas
Previsão de períodos de superlotação
Mapeamento de gargalos operacionais
Redução do tempo de processamento através da paralelização

 -Tecnologias Utilizadas
Linguagem: Java
Paradigma: Programação concorrente
Estruturas: Threads, ExecutorService
Manipulação de dados: Arquivos CSV


- Considerações Finais

Este projeto demonstra como técnicas de paralelização podem ser aplicadas na análise de grandes volumes de dados reais, contribuindo para soluções eficientes em problemas de mobilidade urbana.

Além disso, evidencia a importância da computação concorrente no processamento de dados em larga escala.
