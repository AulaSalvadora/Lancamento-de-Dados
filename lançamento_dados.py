"""Programa para lançar quaisquer quantidades de dados de qualquer face."""

import random


def user_input():
    """Função usada para receber valores do usuário."""
    breaker = True
    while breaker:
        dice_value = input("Forneça o tamanho do dado que será rolado: ")
        while dice_value_check(dice_value) is False:
            dice_value = input("Forneça o tamanho do dado que será rolado: ")
        dice_number = input("Forneça o número de dados que serão rolados: ")
        while dice_numbers_check(dice_number) is None:
            dice_number = input("Forneça o número de dados que serão rolados: ")
        if dice_value_check(dice_value) and dice_numbers_check(dice_number):
            breaker = False
            dice_number = dice_numbers_check(dice_number)
    return int(dice_value), int(dice_number)


def dice_value_check(dice_value):
    """Função usada para testar o valor do dado."""
    if dice_value.isnumeric():
        dice_value = int(dice_value)
        if dice_value > 0:
            return True
        print("O número passado deve ser maior que zero!")
        return False
    if dice_value == "":
        raise SystemExit
    print("A informação passada não é válida!")
    return False


def dice_numbers_check(dice_number):
    """Função usada para testar o valor relativo ao número de dados."""
    if len(dice_number) == 0:
        return 1
    if dice_number.isdigit():
        dice_number = int(dice_number)
        if dice_number == 0:
            print("O número passado deve ser maior que zero!")
            return None
        return dice_number
    print("A informação passada não é válida!")
    return None


def generator(max_value):
    """Função usada para gerar números aleatórios."""
    return random.randint(1, max_value)


dice_max_num, number_of_dices = user_input()

for i in range(number_of_dices):
    print(generator(dice_max_num), end=' ')
