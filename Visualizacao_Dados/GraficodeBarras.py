import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#OS ARQUIVOS UTILIZADOS FORAM RETIRADOS DO PORTAL BRASILEIRO DE DADOS ABERTOS (https://dados.gov.br/dataset/investidores-do-tesouro-direto)
#ABRINDO ARQUIVOS EM DATAFRAME
investidores = pd.read_csv("InvestidoresTesouroDireto.csv", sep=";", encoding="ISO-8859-1")
investidores.head()

habitantes = pd.read_csv("habitantesporestado.csv", sep=";", encoding="ISO-8859-1")
print(habitantes.head())

#FILTRANDO COLUNAS DO CONJUNTO DE DADOS DE INVESTIDORES
investidores2 = investidores.filter(items=['UF do Investidor', 'Codigo do Investidor']).groupby('UF do Investidor').count().sort_values(by='Codigo do Investidor', ascending=True)

print(investidores2.head())

#UNINDO CONJUNTOS DE DADOS (INVESTIDORES E HABITANTES POR ESTADO)

dados = pd.merge(investidores2, habitantes, how='left', left_on=['UF do Investidor'], right_on=['UF'])
dados

#TROCANDO NOMES DAS COLUNAS
dados.columns = ['Investidores por Estado', 'UF', 'População total em 2019']
print(dados)

#CONVERTENDO COLUNA DE STR PARA INT
dados['População total em 2019'] = dados['População total em 2019'].apply(lambda x: float(str(x).replace(".", "")))

#GERANDO GRÁFICOS DE BARRAS

fig, ax = plt.subplots(1,2, figsize=(15, 6), sharey=True) #estudar mais sobre o comando subplots()
UFs = len(dados['UF']) #o resultado disso é 27. grupos, UFs = 27
investidores_por_estado = dados['Investidores por Estado'] #1o numero a ser ilustrado
populaçao_total = dados['População total em 2019'] #2o numero a ser ilustrado
indice = np.arange(UFs) #estudar mais sobre o comando arange
bar_larg = 0.4
bar_larg2 = 0.6
transp = 1
ax[0].barh(indice, investidores_por_estado, color='purple', label='Investidores por Estado')
ax[0].legend(bbox_to_anchor=(0.99, 0.08), loc=0)
ax[1].barh(indice, investidores_por_estado, bar_larg2, alpha=transp, color='purple', label='Investidores por Estado')
ax[1].barh(indice + bar_larg, populaçao_total, bar_larg, alpha=transp, color='black', label='População total por Estado')
plt.xlabel('População de 0 a 12.000.000')
plt.yticks(indice + bar_larg, dados['UF'])
plt.legend() 
fig.suptitle('Distribuição de Investidores do Tesouro Direto por Estado', size=15)
plt.subplots_adjust(wspace=0.01) #hspace=0
plt.show()