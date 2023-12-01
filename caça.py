#Cainã,José,Gabriel,Erika,Bianca,Jaiane

import random

tabuleiro = {
    (0, 0): None, (0, 1): None, (0, 2): None,
    (1, 0): None, (1, 1): None, (1, 2): None,
    (2, 0): None, (2, 1): None, (2, 2): None
}

simbolos = ["☣", "☣", "☣", "7", "7", "7", "⚅", "⚅", "⚅", "☠︎", "☠︎", "☠︎", "1", "1", "1", "❤︎", "❤︎", "❤︎", "?", "?", "?", "!", "!", "!"]

random.shuffle(simbolos)

for i in range(3):
    for j in range(3):
        tabuleiro[(i, j)] = simbolos.pop()

dinheiro = int(input("Quanto dinheiro você deseja iniciar? (Deve ser maior que 0): "))
while dinheiro <= 0:
    print("Por favor, insira um valor maior que 0.")
    dinheiro = int(input("Quanto dinheiro você deseja iniciar? (Deve ser maior que 0): "))

def verificar_vitoria():
    for i in range(3):
        if tabuleiro[(i, 0)] == tabuleiro[(i, 1)] == tabuleiro[(i, 2)]:
            return True
        if tabuleiro[(0, i)] == tabuleiro[(1, i)] == tabuleiro[(2, i)]:
            return True

    if tabuleiro[(0, 0)] == tabuleiro[(1, 1)] == tabuleiro[(2, 2)]:
        return True
    if tabuleiro[(0, 2)] == tabuleiro[(1, 1)] == tabuleiro[(2, 0)]:
        return True

    return False

while dinheiro > 0:
    for i in range(3):
        for j in range(3):
            print(tabuleiro[(i, j)], end="  ")
        print()

    aposta = int(input(f"Quanto você quer apostar? (Se deseja sair, digite 0; Saldo atual: {dinheiro}): "))
    
    while aposta < 0 or aposta > dinheiro:
        if aposta < 0:
            print("Por favor, insira um valor maior ou igual a 0.")
        else:
            print("Você não tem dinheiro suficiente para essa aposta. Tente novamente.")
        aposta = int(input(f"Quanto você quer apostar? (Se deseja sair, digite 0; Saldo atual: {dinheiro}): "))
    
    if aposta == 0:
        print("Você saiu do jogo. Até a próxima!")
        break

    if verificar_vitoria():
        dinheiro += aposta * 2
        print(f"Parabéns! Você venceu! Seu saldo atual é: {dinheiro}")
    else:
        dinheiro -= 10 
        print(f"Você perdeu. Seu saldo atual é: {dinheiro}")

        if dinheiro <= 0:
            print("Você não tem dinheiro suficiente para continuar. Até a próxima!")
        else:
            dinheiro_adicional = int(input("Quanto dinheiro você gostaria de adicionar? (Deve ser maior que 0): "))
            while dinheiro_adicional <= 0:
                print("Por favor, insira um valor maior que 0.")
                dinheiro_adicional = int(input("Quanto dinheiro você gostaria de adicionar? (Deve ser maior que 0): "))
            
            dinheiro += dinheiro_adicional

