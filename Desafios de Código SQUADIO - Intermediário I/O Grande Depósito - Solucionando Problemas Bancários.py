"""
Desafio
Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a realizar depósitos em suas contas.
O programa deve solicitar ao cliente o valor do depósito e verificar se o valor é válido.
Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta.
Caso contrário, o programa deve exibir uma mensagem de erro. O programa deve solicitar apenas uma vez o valor de depósito.

Entrada
O programa deve receber o valor de depósito digitado pelo cliente.
Os valores podem ser decimais, representando valor em reais.

Saída
O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado e o saldo da conta for atualizado.
Se o valor for "0", deverá imprimir uma mensagem encerrando o programa.
Caso um valor inválido seja digitado, o programa deve exibir uma mensagem de erro solicitando um novo valor.
"""

valor = float(input())

if valor > 0:
  #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
    print(f"Deposito realizado com sucesso!\n Saldo atual: R$ {valor:.2f}")
elif valor < 0:
  #TODO: Imprimir a mensagem de valor inválido.
    print("Valor invalido! Digite um valor maior que zero.")
else:
    print("Encerrando o programa...")
