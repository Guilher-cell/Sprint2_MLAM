# Relatório Técnico — Estatística Descritiva e Visualização de Dados de Recarga de Veículos Elétricos
Integrantes do grupo:
André Fujinaga - RM569158
Arthur Machado - RM569919
Conrado Gracie - RM569157
Guilherme Belo - RM570079
Renato Sandreschi - RM569156
1- CCPJ
## Introdução

Este trabalho tem como objetivo aplicar conceitos de Estatística Descritiva utilizando uma base de dados real relacionada ao carregamento de veículos elétricos. A análise foi realizada utilizando Python e suas bibliotecas de análise de dados e visualização gráfica.

A base escolhida apresenta informações sobre usuários, veículos, consumo energético e características das sessões de carregamento, permitindo identificar padrões relevantes para a tomada de decisão em empresas do setor de mobilidade elétrica e infraestrutura de recarga.

---

## Metodologia

Foi utilizada uma amostra aleatória de 100 registros da base de dados, garantindo reprodutibilidade através do parâmetro `random_state = 100`.

As análises realizadas incluíram:

* Gráfico de Setores;
* Gráfico de Barras;
* Histograma;
* Boxplot;
* Medidas de Tendência Central;
* Medidas de Dispersão;
* Medidas Separatrizes.

---

## Gráfico de Setores — User Type

O gráfico de setores foi utilizado para analisar a distribuição dos tipos de usuários que utilizam os carregadores.

### Insight Principal

A distribuição dos perfis de usuários permite identificar quais segmentos utilizam com maior frequência a infraestrutura de recarga. Essas informações podem orientar estratégias de expansão, marketing e personalização de serviços.

### Valor para a Empresa

* Segmentação de clientes;
* Criação de planos específicos para cada perfil;
* Melhor direcionamento de investimentos.

---

## Gráfico de Barras — Time of Day

O gráfico de barras foi utilizado para analisar a quantidade de sessões de recarga ao longo dos diferentes períodos do dia.

### Insight Principal

A concentração de recargas em determinados períodos evidencia horários de pico, permitindo identificar momentos de maior demanda energética.

### Valor para a Empresa

* Balanceamento inteligente de carga;
* Planejamento da capacidade energética;
* Tarifação diferenciada por horário.

---

## Histograma — Energy Consumed (kWh)

O histograma permitiu visualizar a distribuição da energia consumida durante as sessões de carregamento.

### Insight Principal

A distribuição dos consumos evidencia diferentes perfis de utilização dos carregadores, mostrando que nem todos os usuários apresentam as mesmas necessidades energéticas.

### Valor para a Empresa

* Planejamento da infraestrutura elétrica;
* Previsão de demanda energética;
* Otimização da distribuição de energia.

---

## Boxplot — Charging Duration (hours)

O boxplot foi utilizado para analisar a duração das sessões de carregamento e identificar possíveis valores atípicos.

### Insight Principal

A presença de valores extremos indica que algumas sessões apresentam comportamento diferente da maioria dos usuários, podendo estar relacionadas a veículos específicos ou padrões distintos de utilização.

### Valor para a Empresa

* Identificação de comportamentos atípicos;
* Monitoramento operacional;
* Otimização dos recursos de carregamento.

---

## Medidas de Tendência Central

Foram calculadas:

* Média;
* Mediana;
* Moda.

### Insight Principal

Essas medidas permitiram identificar o comportamento central do consumo energético dos usuários, fornecendo uma visão geral do padrão de utilização da infraestrutura.

---

## Medidas de Dispersão

Foram calculadas:

* Amplitude;
* Variância;
* Desvio Padrão.

### Insight Principal

Os resultados demonstraram o nível de variabilidade existente entre as sessões de carregamento, evidenciando diferenças nos padrões de consumo energético.

---

## Medidas Separatrizes

Foram calculados:

* Primeiro Quartil (Q1);
* Segundo Quartil (Q2);
* Terceiro Quartil (Q3);
* Percentil 90.

### Insight Principal

As medidas separatrizes permitiram compreender como os consumos energéticos estão distribuídos entre os usuários, identificando faixas de consumo predominantes e grupos com maior demanda energética.

---

## Conclusão

As análises realizadas demonstraram que a estatística descritiva é uma ferramenta fundamental para compreender o comportamento dos usuários e o funcionamento da infraestrutura de carregamento de veículos elétricos.

Os resultados obtidos fornecem informações relevantes para tomada de decisão estratégica, permitindo otimizar recursos, melhorar a eficiência energética e desenvolver soluções inteligentes para o setor de mobilidade elétrica.

Além disso, os dados analisados apresentam potencial para aplicações futuras em modelos de aprendizado de máquina voltados para previsão de consumo energético, identificação de padrões de uso e gerenciamento inteligente da demanda elétrica.
