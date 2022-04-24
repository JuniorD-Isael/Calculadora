import funcao_da_calculadora as fc
from dicionario import dic_de_funcao as df


while True:
    funcao = ''
    while funcao == '':
        print('-' * 10)
        funcao = str(input('Qual função você deseja usar?'
                           '\n(a) Adição'
                           '\n(s) Subtração'
                           '\n(d) Divisão'
                           '\n(m) Multiplicação'
                           '\n(t) Tabuada'
                           '\n(r) Raízes (Cúbica e Quadrada)'
                           '\n(p) Potenciação'
                           '\n> ')).lower().strip()[0]
        print('-' * 10)

        if not funcao.isalpha():
            print('-' * 10)
            print('Opção errada')
            funcao = ''

        elif funcao not in df.keys():
            print('-' * 10)
            print('Opção errada')
            funcao = ''

        else:
            print(df[funcao])
            print('-' * 10)

            # somar
            if funcao == 'a':
                valor1 = fc.coletando_valor()
                valor2 = fc.coletando_valor()
                print(f'{valor1} + {valor2} = {fc.adicao(valor1, valor2)}')

            # subtrair
            if funcao == 's':
                valor1 = fc.coletando_valor()
                valor2 = fc.coletando_valor()
                print(f'{valor1} - {valor2} = {fc.subitrair(valor1, valor2)}')

            # dividir
            if funcao == 'd':
                valor1 = fc.coletando_valor()
                valor2 = fc.coletando_valor()
                print(f'{valor1} / {valor2} = {fc.dividir(valor1, valor2) :.1f}')

            # multiplicar
            if funcao == 'm':
                valor1 = fc.coletando_valor()
                valor2 = fc.coletando_valor()
                print(f'{valor1} * {valor2} = {fc.multiplicacao(valor1, valor2)}')

            # taboada
            if funcao == 't':
                valor1 = fc.coletando_valor()
                for multiplicador in range(1, 11):
                    print(f'{valor1} x {multiplicador} = '
                          f'{fc.multiplicacao(valor1, multiplicador)}')

            # raiz
            if funcao == 'r':
                valor1 = fc.coletando_valor()
                fc.raizes(valor1)

            # potencia
            if funcao == 'p':
                valor1 = fc.coletando_valor()
                print('Elevado a')
                valor2 = fc.coletando_valor()
                print(f'{valor1} elevado a {valor2} é = {fc.potencia(valor1, valor2)}')

    continuar = ''
    while continuar not in ['s', 'n']:
        continuar = str(input('Deseja continuar? s:Sim, n:Não'
                        '> ')).lower().strip()[0]
    if continuar == 's':
        continue
    elif continuar == 'n':
        break
