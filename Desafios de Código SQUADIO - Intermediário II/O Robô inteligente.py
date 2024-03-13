"""
Desafio
Você foi contratado pela empresa DIO Robots para programar um robô capaz de classificar números em uma das seguintes categorias: negativo, positivo ou zero.
Para isso, você deve criar uma função de classificação que receba um número como parâmetro e retorne a mensagem "negativo!" ou " positivo!", de acordo com sua categoria.

O programa deve ser executado continuamente, permitindo que o usuário insira vários números.
Quando ele quiser encerrar a execução, deverá digitar um número igual a zero.
A cada novo número inserido, o robô deve classificá-lo e exibir a mensagem correspondente.
Ao final da execução, o programa deverá exibir a quantidade de números positivos, negativos e zeros que foram inseridos.

Entrada:
A entrada deve receber valores inteiros.

numero: valor inteiro que pode ser positivo, negativo ou zero. Lembrando que a entrada zero deve encerrar o programa.
Saída:
O código deverá retornar uma mensagem (string) informando se o número é positivo ou não.
Ao receber o valor 0, ele deverá encerrar o e informar quantos números foram positivos e negativos.
"""

# Função para classificar um número como positivo ou negativo
def classificar_numero(numero):
    if numero > 0:
        return "positivo!"
    return "negativo!"

def main():
    positivos = 0
    negativos = 0

    while True:
        numero = int(input())

        if numero == 0:
            break  # Encerra o loop se o usuário digitar 0.

        # Chama a função classificar_numero para imprimir a classificação do número
        print(classificar_numero(numero))

        # Verificação para saber quantos números positivos e negativos foram inseridos
        if classificar_numero(numero) == "positivo!":
            positivos += 1
        else:
            negativos += 1

    # Imprime a quantidade de números positivos e negativos inseridos
    print(f"{positivos} números positivos, {negativos} números negativos")

if __name__ == "__main__":
    main()
