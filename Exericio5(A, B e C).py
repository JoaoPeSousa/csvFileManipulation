#---------QUESTÃO 4 (A, B E C)-----------

import pandas as pd

import matplotlib.pyplot as plt

#EXERCICIO 5A
def mostra_pib_pais(pais, ano):
    ler = pd.read_csv('PIBs.csv', index_col='País', )
    try:
        return f'O {pais} no ano {ano} teve um PIB de {ler.loc[pais][ano]}'
    except KeyError:
        return f'O pais ou ano não foram encontrados.'

#EXERCICIO 5B
def variacao_pib():
    ler = pd.read_csv('PIBs.csv', index_col='País', )
    paises = ler.index.tolist()

    for pais in paises:
        variacao_formula = (ler.loc[pais][-1] / ler.loc[pais][0] - 1) * 100
        print(f'{pais}             variação de {variacao_formula:.2f}% entre 2013 e 2020.')

#EXERCICIO 5C
def exibir_grafico_pib(pais):
    ler = pd.read_csv('PIBs.csv', index_col='País', )
    try:
        eixo_x = ler.loc[pais].index
        eixo_y = ler.loc[pais].values
        plt.plot(eixo_x, eixo_y)
        plt.show()
    except KeyError:
        return f'O pais ou ano não foram encontrados.'

#Deixei tudo descomentado, dessa forma o programa vai gerar as saídas dos exercicios A, B e C

pais = str(input("Digite o nome do Pais que deseja consultar o PIB: ")).capitalize()
ano = str(input("Insira o ano do PIB que deseja consultar: "))

print(mostra_pib_pais(pais, ano))
print('')
variacao_pib()
print('')
print(exibir_grafico_pib(pais))

