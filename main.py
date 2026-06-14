import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

database = pd.read_csv("./.csv/ev_charging_patterns.csv")
amostra = database.sample(n=100, random_state=100)
amostra.head()

# qualitativas: 

# nominais -----> amostra["Vehicle Model"].value_counts() , amostra["Charging Station Location"].value_counts(), amostra["Charger Type"].value_counts() , amostra["User Type"].value_counts(), amostra["User Id"].value_counts(), amostra["Charging Station Id"].value_counts() 
# ordinais -----> amostra["Day of Week"].value_counts() , amostra["Time of Day"].value_counts()

# quantitativas:

# discretas -----> amostra["Vehicle Age (years)"].value_counts() , amostra["Charging Start Time"].value_counts() , amostra["Charging End Time"].value_counts()
# contínuas -----> amostra["Battery Capacity (kWh)"].value_counts() , amostra["Energy Consumed (kWh)"].value_counts() , amostra["Charging Duration (hours)"].value_counts() , amostra["Charging Rate (kW)"].value_counts() , amostra["Charging Cost (USD)"].value_counts() , amostra["State of Charge (Start %)"].value_counts() , amostra["Distance Driven (since last charge) (km)"].value_counts() , amostra["Temperature (°C)"].value_counts()

# Questão 2:
# a)quantitativa discreta

freq_hora = amostra["Vehicle Age (years)"].value_counts().sort_index()

freq_rel_hora = (freq_hora / freq_hora.sum()) * 100

freq_acum_hora = freq_hora.cumsum()

tabela_hora = pd.DataFrame({
    "Frequência": freq_hora,
    "Frequência Relativa (%)": freq_rel_hora.round(2),
    "Frequência Acumulada": freq_acum_hora
})

print(tabela_hora)

# b)quantitativa contínua
custos = amostra["Charging Cost (USD)"]
n = len(custos)
k = int(1 + 3.3 * np.log10(n))

print("Número de classes:", k)

classes = pd.cut(custos, bins=k)

freq = classes.value_counts().sort_index()

freq_rel = (freq / n) * 100

freq_acum = freq.cumsum()

tabela_continua = pd.DataFrame({
    "Frequência": freq,
    "Frequência Relativa (%)": freq_rel.round(2),
    "Frequência Acumulada": freq_acum
})

print(tabela_continua)


# Histogramas para uma melhor analíse grafica

# Histograma quantitativa discreta:
plt.figure(figsize=(10,6))
plt.hist(
    amostra["Vehicle Age (years)"],
    bins=10,
    edgecolor="black"
)
plt.title(
    "Distribuição da Idade dos Veículos Elétricos",
    fontsize=16
)
plt.xlabel(
    "Idade do veículo (anos)",
    fontsize=12
)
plt.ylabel(
    "Frequência",
    fontsize=12
)
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.7
)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

# Histograma quantitativa contínua:
plt.figure(figsize=(10,6))
plt.hist(
    amostra["Charging Cost (USD)"],
    bins=10,
    edgecolor="black"
)
plt.title(
    "Distribuição do Custo de Recarga",
    fontsize=16
)
plt.xlabel(
    "Custo da recarga (USD)",
    fontsize=12
)
plt.ylabel(
    "Frequência",
    fontsize=12
)
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.7
)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

# Sprint 2 ----------------------

# GRÁFICO DE SETORES
dados_setor = amostra["User Type"].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    dados_setor,
    labels=dados_setor.index,
    autopct="%1.1f%%"
)

plt.title("Distribuição dos Tipos de Usuários")

plt.legend(
    title="Tipos de Usuários",
    loc="best"
)

plt.show()

# GRÁFICO DE BARRAS
dados_barra = amostra["Time of Day"].value_counts()

plt.figure(figsize=(10, 6))

plt.bar(
    dados_barra.index,
    dados_barra.values,
    color="steelblue",
    label="Quantidade de Sessões"
)

plt.title("Sessões de Recarga por Período do Dia")

plt.xlabel("Período do Dia")
plt.ylabel("Quantidade de Sessões")

plt.legend()

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()

# HISTOGRAMA
plt.figure(figsize=(10, 6))

plt.hist(
    amostra["Energy Consumed (kWh)"],
    bins=10,
    color="orange",
    edgecolor="black"
)

plt.title("Distribuição da Energia Consumida")

plt.xlabel("Energia Consumida (kWh)")
plt.ylabel("Frequência")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()

# BOXPLOT
plt.figure(figsize=(10, 6))

plt.boxplot(
    amostra["Charging Duration (hours)"],
    patch_artist=True
)

plt.title("Boxplot da Duração das Recargas")

plt.ylabel("Duração da Recarga (horas)")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()


# ESTATÍSTICA DESCRITIVA
energia = amostra["Energy Consumed (kWh)"]

print("MEDIDAS DE TENDÊNCIA CENTRAL")

print("Média:", round(energia.mean(), 2))
print("Mediana:", round(energia.median(), 2))
print("Moda:")
print(energia.mode())

print("MEDIDAS DE DISPERSÃO")

print("Amplitude:", round(energia.max() - energia.min(), 2))
print("Variância:", round(energia.var(), 2))
print("Desvio Padrão:", round(energia.std(), 2))

print("MEDIDAS SEPARATRIZES")

print("Q1 (25%):", round(energia.quantile(0.25), 2))
print("Q2 (50%):", round(energia.quantile(0.50), 2))
print("Q3 (75%):", round(energia.quantile(0.75), 2))
print("Percentil 90:", round(energia.quantile(0.90), 2))

