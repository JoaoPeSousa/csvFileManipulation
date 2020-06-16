#--------QUESTÃO NÚMERO 3-----------

def controle_moradia(renda_mensal, moradia):
    porcentagem = moradia * (100 / renda_mensal)
    recomendado = 30
    gasto_max = renda_mensal * (recomendado / 100)
    tipo = 'moradia'
    if porcentagem < recomendado:
        return controle_mensagem_ok(tipo, porcentagem, recomendado)
    else:
        return controle_mensagem_nao_ok(tipo, porcentagem, recomendado, gasto_max)


def controle_educacao(renda_mensal, educacao):
    porcentagem = educacao * (100 / renda_mensal)
    recomendado = 20
    gasto_max = renda_mensal * (recomendado / 100)
    tipo = 'educação'
    if porcentagem < recomendado:
        return controle_mensagem_ok(tipo, porcentagem, recomendado)
    else:
        return controle_mensagem_nao_ok(tipo, porcentagem, recomendado, gasto_max)


def controle_transporte(renda_mensal, transporte):
    porcentagem = transporte * (100 / renda_mensal)
    recomendado = 15
    gasto_max = renda_mensal * (recomendado / 100)
    tipo = 'transporte'
    if porcentagem < recomendado:
        return controle_mensagem_ok(tipo, porcentagem, recomendado)
    else:
        return controle_mensagem_nao_ok(tipo, porcentagem, recomendado, gasto_max)


def controle_mensagem_ok(tipo, porcentagem, recomendado):
    return f'Seus gastos totais com {tipo} comprometem {porcentagem}% de sua renda total. O máximo\
recomendado é de {recomendado}%. Seus gastos estão dentro da margem recomendada.'


def controle_mensagem_nao_ok(tipo, porcentagem, recomendado, gasto_max):
    return f'Seus gastos totais com {tipo} comprometem {porcentagem}% de sua renda total. O máximo recomendado é de {recomendado}%. \
Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {str(gasto_max).replace(".", ",")}. '


renda_mensal = float(input('Insira sua renda mensal:'))
moradia = float(input('Digite o quanto gasta com moradia:'))
educacao = float(input('Digite o quanto gasta com educação:'))
transporte = float(input('Digite o quanto gasta com transporte:'))

print(f'Renda mensal {str(renda_mensal).replace(".", ",")} ')
print(f'Gastos totais com moradia: {str(moradia).replace(".", ",")}')
print(f'Gastos totais com educação: {str(educacao).replace(".", ",")}')
print(f'Gastos totais com transporte: {str(transporte).replace(".", ",")}')
print('  ')
print('Diagnóstico:')
print(controle_moradia(renda_mensal, moradia))
print(controle_educacao(renda_mensal, educacao))
print(controle_transporte(renda_mensal, transporte))
