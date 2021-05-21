"""Projeto 3 da disciplina de algoritmo"""


import random


def valida_dados(info):
    """
    Retorna True se um determinado dado é numérico maior que zero e menor que 100.
    Imprime na tela caso seja um dado inválido.
    Argumento:
    info (str) - A informação que precisa ser validada.
    Retorna: bool - True se o dado for válido, False caso contrário
    """
    if info.isnumeric() is True:
        info = int(info)
        if info > 100:
            print("O número passado deve ser menor ou igual a 100!")
            return False
        if info < 1:
            print("O número passado deve ser maior ou igual a 1!")
            return False
        return True
    if info == "":
        return None
    print("A informação passada não é válida!")
    return False


def testa_chute(chute, resposta):
    """
    Compara o chute realizado com a resposta dada.
    Argumentos:
    chute (int) - O chute que o usuário passou.
    resposta (int) - O valor a ser comparado.
    Retorna: bool - True se o chute for igual à resposta, False caso contrário.
    """
    if chute == resposta:
        return True
    return False


def main():
    """Função principal, contém a lógica principal do programa."""
    resposta = random.randint(1, 100)
    info = input("Chute um número inteiro entre 1 e 100: ")
    while valida_dados(info) is False:
        info = input("Chute um número inteiro entre 1 e 100: ")
    chute = int(info)
    while testa_chute(chute, resposta) is False:
        if chute > resposta:
            print("O número chutado foi muito alto! ")
            chute = int(input("Chute um número inteiro entre 1 e 100: "))
        else:
            print("O número chutado foi muito baixo! ")
            chute = int(input("Chute um número inteiro entre 1 e 100: "))
    print("Parabéns! Você acertou a resposta!")


main()
