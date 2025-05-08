# Importando bibliotecas necessárias
import requests  # Para fazer requisições HTTP
import pandas as pd  # Para manipulação de dados em DataFrame
import matplotlib.pyplot as plt  # Para visualização gráfica

# Requisitando dados da API de COVID-19 no Brasil
url = "https://covid19-brazil-api.now.sh/api/report/v1"
resposta = requests.get(url)  # Obtendo a resposta da API
dados = resposta.json()  # Convertendo a resposta para JSON

# Criando um DataFrame com os dados de COVID-19
tabela = pd.DataFrame(dados['data'])

# Selecionando as 5 primeiras linhas com informações dos estados, mortes e casos
tabela_areas = pd.DataFrame({
    'Estados': tabela['uf'].head(),
    'Mortes': tabela["deaths"].head(),
    'Casos': tabela["cases"].head()
})
print(tabela_areas)

# Realizando uma junção entre o DataFrame original e o tabela_areas com base nas mortes
tabela = tabela.merge(tabela_areas, how="left", left_on="deaths", right_on="Mortes")

# Configurando a janela do gráfico
fig = plt.figure()
fig.canvas.manager.set_window_title("Análise Casos de COVID por Estado (UF)")

# Agrupando e somando os casos e mortes por estado
resumo_uf = tabela.groupby("Estados")[["Casos", "Mortes"]].sum().sort_values("Casos", ascending=False)

# Criando gráfico de barras para mostrar o total de casos
cores = ['#007acc', '#33a02c', '#ff7f00', '#6a3d9a', '#e31a1c']
resumo_uf["Casos"].plot(kind="bar", color=cores, figsize=(10,6))

# Adicionando título, rótulos e texto ao gráfico
plt.title("Total de Casos por Estado (UF)")
plt.xlabel("UF")
plt.ylabel("Casos")
plt.text(x=tabela["Casos"][6], y=160000, s="Pico de casos", fontsize=10, color="red")
plt.grid(True)

# Exibindo o gráfico
plt.show()
