"""
Desafio
Você está trabalhando para uma empresa que utiliza extensivamente os serviços da AWS,
e após algumas análises a equipe de segurança identificou que algumas senhas dos usuários no IAM são fracas e podem representar um risco à segurança dos dados da empresa.
Para resolver esse problema,
foi solicitado que você desenvolva um programa capaz de analisar as senhas dos usuários e fornecer uma validação de força com base em critérios predefinidos.

Requisitos de segurança para a senha:

A senha deve ter no mínimo 8 caracteres.
A senha deve conter pelo menos uma letra maiúscula (A-Z).
A senha deve conter pelo menos uma letra minúscula (a-z).
A senha deve conter pelo menos um número (0-9).
A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.
Saiba mais sobre o Regex em: Java Regular Expressions

Entrada
A entrada será uma única string representando a senha que precisa ser validada.

Saída
Seu programa deve retornar uma mensagem indicando se a senha fornecida pelo usuário atende aos requisitos de segurança ou não,
juntamente com um feedback explicativo sobre os critérios considerados.
"""

import re

def verificar_forca_senha(senha):

    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False

    # Verificando se a senha contém sequências comuns
    sequencias_comuns = ["123456", "abcdef"]
    for sequencia in sequencias_comuns:
        if sequencia in senha:
            return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

    # Verificando se a senha contém palavras comuns
    palavras_comuns = ["password", "123456", "qwerty"]
    if senha in palavras_comuns:
        return "Sua senha e muito comum. Tente uma senha mais complexa."

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

    # Verificando se a senha contém letra minuscula
    if re.findall("[a-z]", senha):
        tem_letra_minuscula = True

    # Verificando a senha contém letra maiúscula
    if re.findall("[A-Z]", senha):
        tem_letra_maiuscula = True

    # Verificando se a senha contém caractere especial (se existe um caractere que não é letra ou número)
    if re.findall(r"[^a-zA-Z0-9]", senha):
        tem_caractere_especial = True

    #for caractere in senha:
      #if tem_caractere_especial == True:
        #break
      #if caractere.isdigit() == False and caractere.isupper() == False and caractere.islower() == False:
        #tem_caractere_especial = True

    # Checando se possui um numero
    if re.findall("[0-9]", senha):
        tem_numero = True

    if tem_letra_maiuscula and tem_caractere_especial and tem_letra_minuscula and tem_numero:
        return "Sua senha atende aos requisitos de seguranca. Parabens!"
    # Retorna saída informando que a senha atende aos requisitos de segurança
    return "Sua senha nao atende aos requisitos de seguranca."


# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)
