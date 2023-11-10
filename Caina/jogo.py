import random
def jogo (jogo1,jogo2,jogo3):
    jogo1 = ["1", "2", "3"]
    jogo2 = ["1","2","3"]
    jogo3 = ["1","2","3"]
    resultado = random.shuffle(jogo1,jogo2,jogo3)
    if resultado:
        jogo1==jogo2==jogo3
        return "você ganhou puta"
    else:
        return "Você perdeu otario!"

print(jogo())
