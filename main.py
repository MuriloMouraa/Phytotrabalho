'''
* Autor: Murilo Alessandro da Silva Moura
* Linguagem: Python
* Data: 11/12/2024
* Descrição: Uma calculadora para contas básicas em phyton
* Funcionalidades: Contas de adição, subtração, multiplicação, divisão, porcentagem e potenciação.
* Versão: Phyton3
'''

# Mostra uma imagem na tela para digitar o input

print("Digite o calculo que deseja fazer: (+, -, x, :, %)")

# Cria 3 variáveis, duas float e uma string

# Define as variaveis conta, A e B como input

conta = str(input())

# Pede um valor para fazer o cálculo

print("Digite o primeiro número desejado para fazer a conta")

A = float(input())

print("Digite o segundo número desejado para fazer a conta")

B = float(input())

# Estrutura de condição que se conta for igual a alguma das operações "+, -, x, :, %, ^", e caso for algum dos caracteres, faz a conta respectiva.

if conta == "+":
  print("%.2f" % (A + B))
elif conta == "-":
  print("%.2f" % (A - B))
elif conta == "x":
  print("%.2f" % (A * B))
elif conta == ":":
  print("%.2f" % (A / B))
elif conta == "%":
  print("%.2f" % ((B / 100) * A))

# Se não for alguma das condições anteriores mostra "Operação Invalida"

else:
  print("Conta Invalida")