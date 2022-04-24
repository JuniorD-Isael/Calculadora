from math import sqrt
from numpy import cbrt

# Coleta e valida valor numérico


def coletando_valor(valor='*'):
    while not valor.isnumeric():
        valor = input('Digite o valor: ')
    print('-' * 10)
    return int(valor)


def adicao(a, b):
    soma = a + b
    return soma


def subitrair(a, b):
    diferenca = a - b
    return diferenca


def dividir(a, b):
    quociente = a / b
    return quociente


def multiplicacao(a, b):
    produto = a * b
    return produto


def raizes(a):
    tipo = ''
    while tipo not in ['q', 'c']:
        tipo = str(input('q:Quadrada, c:Cúbica '))
        print('-' * 10)
    if tipo == 'q':
        print(f'A raiz quadrada de {a} é = {sqrt(a) :.4f}')
        print('-' * 10)
    elif tipo == 'c':
        print(f'A raiz cúbica de {a} é = {cbrt(a) :.4f}')
        print('-' * 10)


def potencia(a, b):
    potenciacao = a ** b
    return potenciacao


if __name__ == '__main__':
    print(adicao(5, 2))
    print(subitrair(5, 2))
    print(dividir(5, 2))
    print(multiplicacao(5, 2))
    raizes(5)
    print(potencia(5, 2))
