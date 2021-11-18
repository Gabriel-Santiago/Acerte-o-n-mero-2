from random import *


def num_easy():
    num = randint(0, 10)
    return num


def num_medium():
    num = randint(0, 25)
    return num


def num_hard():
    num = randint(0, 50)
    return num


def num_insane():
    num = randint(0, 150)
    return num


def choose_nivel():
    nivel: int = int(input('''Escolha o nível!
    1 - Easy
    2- Medium
    3 - Hard
    4 - Insane
    :'''))

    return nivel


def easy_medium_tentative():
    tentative = 5
    return tentative


def hard_insane_tentative():
    tentative = 3
    return tentative


def loop():
    a = input('''Deseja Jogar de novo?
    Y - Yes
    N - No
    :\n''')

    if a == 'Y' or a == 'y':
        right_or_wrong()
    elif a == 'N' or a == 'n':
        print('Bye!')
    else:
        print('Tecla inválida')


def right_or_wrong():
    rw = choose_nivel()

    if rw == 1:

        r = num_easy()
        tentative = easy_medium_tentative()
        rodada = 1

        while rodada <= tentative:

            print('São 5 tentativas')
            print('Escolha um número entre 0 e 10')
            print('Tentativa {} de {}'.format(rodada, tentative))
            chute = int(input('\nDigite	o seu número: '))
            print('\nVocê digitou: ', chute)

            if r == chute:
                print('Você acertou!')
                break
            elif chute > r:
                print('\nVocê errou! O seu chute foi maior que o número secreto')
            elif chute < r:
                print('\nVocê errou! O seu chute foi menor que o número secreto')
            rodada += 1
        print('Fim do Jogo!')
        loop()

    elif rw == 2:
        r = num_medium()
        tentative = easy_medium_tentative()
        rodada = 1

        while rodada <= tentative:

            print('São 5 tentativas')
            print('Escolha um número entre 0 e 25')
            print('Tentativa {} de {}'.format(rodada, tentative))
            chute = int(input('\nDigite	o seu número: '))
            print('\nVocê digitou: ', chute)

            if r == chute:
                print('Você acertou!')
                break
            elif chute > r:
                print('\nVocê errou! O seu chute foi maior que o número secreto')
            elif chute < r:
                print('\nVocê errou! O	seu	chute foi menor que o número secreto')
            rodada += 1
        print('Fim do Jogo!')
        loop()

    elif rw == 3:
        r = num_hard()
        tentative = hard_insane_tentative()
        rodada = 1

        while rodada <= tentative:

            print('São 3 tentativas')
            print('Escolha um número entre 0 e 50')
            print('Tentativa {} de {}'.format(rodada, tentative))
            chute = int(input('\nDigite	o seu número: '))
            print('\nVocê	digitou: ', chute)

            if r == chute:
                print('Você acertou!')
                break
            elif chute > r:
                print('\nVocê errou! O seu chute foi maior que o número	secreto')
            elif chute < r:
                print('\nVocê errou! O seu chute foi menor que o número secreto')
            rodada += 1
        print('Fim do Jogo!')
        loop()

    elif rw == 4:
        r = num_insane()
        tentative = hard_insane_tentative()
        rodada = 1

        while rodada <= tentative:

            print('São 3 tentativas')
            print('Escolha um número entre 0 e 150')
            print('Tentativa {} de {}'.format(rodada, tentative))
            chute = int(input('\nDigite	o seu número: '))
            print('\nVocê	digitou: ', chute)

            if r == chute:
                print('Você acertou!')
                break
            elif chute > r:
                print('\nVocê errou! O seu chute foi maior que o número	secreto')
            elif chute < r:
                print('\nVocê errou! O seu chute foi menor que o número secreto')
            rodada += 1
        print('Fim do Jogo!')
        loop()


def main():
    right_or_wrong()


main()
