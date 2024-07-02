import keyboard
import math
from os import system

clear_terminal = system('cls')

# flags
pass_try = None
flag_raiz_quadrada = None


def close_program():
    close = True
    print('Pressione "F" para sair...')
    while close:
        if keyboard.is_pressed('f'):
            close = False
            break

try:
    clear_terminal
    valor_a = float(input('Digite valor de a: '))
    valor_b = float(input('Digite valor de b: '))
    valor_c = float(input('Digite valor de c: '))
    pass_try = True

except BaseException:
    print('Você não digitou um número válido.')
    close_program()
    

def resolver_delta(a, b, c):
    if a or c > 0:
        delta = (b**2) - (4 * a * c)
        return delta
    elif a or c < 0:
        delta = (b**2) + (4 * a * c)
        return delta
    elif a == 0 and b == 0 and c == 0:
        print('Você digitou apenas 0')
        close_program()

def calculo_corpo(delta, a, b, c):
    try:
        raiz_quadrada = math.sqrt(delta)
        if raiz_quadrada == 0:
            flag_raiz_quadrada = True
            return flag_raiz_quadrada
    except ValueError or TypeError:  
        print('Nenhum dos valores de x é um número real')
        close_program()

    x_adicao = (-(b) + raiz_quadrada) / (2 * a)
    x_subtracao = (-(b) - raiz_quadrada) / (2 * a)

    conjunto_solucao = (x_adicao, x_subtracao)
        
    return conjunto_solucao

if pass_try:
        valor_delta = resolver_delta(valor_a, valor_b, valor_c)
        resultado_final = calculo_corpo(valor_delta, valor_a, valor_b, valor_c)

if isinstance(resultado_final, str):
        print(resultado_final)

elif isinstance(resultado_final, bool):
        print('Resultado final não pode ser obtido!') 

elif flag_raiz_quadrada:
        print(f'A equação possui apenas a seguinte resposta:')
        print(f'\t x= {resultado_final[0]}')
else:
        print(f'O conjunto solução é:')
        for resultados in resultado_final:
            print(f'\tx= {resultados}')

close_program()
