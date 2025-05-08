import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://covid19-brazil-api.now.sh/api/report/v1"
resposta = requests.get(url)
dados = resposta.json()
tabela = pd.DataFrame(dados['data'])

tabela_areas = pd.DataFrame({
    'Estados': tabela['uf'].head(),
    'Mortes': tabela["deaths"].head(),
    'Casos': tabela["cases"].head()
})
print(tabela_areas)

tabela = tabela.merge(tabela_areas, how="left", left_on="deaths", right_on="Mortes")
#tabela = tabela.drop(columns="Nome Funcionário")

fig = plt.figure()
fig.canvas.manager.set_window_title("Análise Casos de COVID por Estado (UF)")

resumo_uf = tabela.groupby("Estados")[["Casos", "Mortes"]].sum().sort_values("Casos", ascending=False)
cores = ['#007acc', '#33a02c', '#ff7f00', '#6a3d9a', '#e31a1c']
resumo_uf["Casos"].plot(kind="bar", color=cores, figsize=(10,6))
#plt.plot(tabela["Casos"], tabela["Mortes"], color='blue', linestyle='--', marker='o')

plt.title("Total de Casos por Estado (UF)")
plt.xlabel("UF")
plt.ylabel("Casos")
plt.text(x=tabela["Casos"][6], y=160000, s="Pico de casos", fontsize=10, color="red")
plt.grid(True)

plt.show()

#ver_estado = input("Digite qual Estado você deseja ver o gráfico: ")
#if ver_estado == "São Paulo":
# Criando gráfico de barras com os dados totais por UF
    #sp = tabela["Estados"][0]
    #resumo_uf = tabela.groupby(sp)[["Casos", "Mortes"]].sum().sort_values("Casos", ascending=False)
    #resumo_uf["Casos"].plot(kind="bar", figsize=(12,6), color="skyblue")
    #plt.title("Total de Casos por Estado (UF)")
    #plt.xlabel("UF")
    #plt.ylabel("Total de Casos")
    #plt.grid(True)
    #plt.show()

