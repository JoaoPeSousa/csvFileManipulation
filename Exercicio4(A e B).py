# EXERCIO 2 (A E B)

import matplotlib.pyplot as plt

valor_final = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
investimento_periodo = float(input("Depósito mensal:"))
tempo = int(input('Por quanto tempo irá render o dinheiro?:'))


# PLOTAGEM DO GRÁFICO DENTRO DA DEF JUROS_COMPOSTOS.
#EXERCICIO 4 A
def juros_compostos(valor_final, taxa, investimento_periodo, tempo):
    n = 0
    dicionario = {}
    print(f'Valor inicial investido: {valor_final}')
    print(f'Investimento mensal: {investimento_periodo}')
    print(f'Quantos meses ira render: {tempo}')
    print(f'Taxa de juros por periodo: {taxa}')
    for valor in range(tempo + 1):
        valor_final = valor_final + (valor_final * (taxa / 100)) + investimento_periodo
        n = n + 1
        dicionario.update({n: format(valor_final, '.2f')})
        print(f'Após {n} períodos(s), o montante será de R${valor_final:.2f}')
    # PLOTAGEM DE GRÁFICO (EXERCICIO 4B)
    periodo_meses = list(dicionario.keys())
    periodo_montante = list(dicionario.values())
    plt.plot(periodo_meses, periodo_montante)
    plt.show()


juros_compostos(valor_final, taxa, investimento_periodo, tempo)
