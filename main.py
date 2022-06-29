import random
from unidecode import unidecode

x = 0
arquivo = open('dicionario.txt', "rt", encoding="utf-8")
dicionario1 = arquivo.read().split()
dicionario2 = [unidecode(palavra) for palavra in dicionario1]
arquivo.close()
contador = 0
aleatoria = random.randrange(1, 16716)
palavraFinalComAcento = dicionario1[aleatoria]
palavraFinalSemAcento = dicionario2[aleatoria]


while contador < 5:
    i = 0
    palavra = unidecode(input("").lower())
    while palavra not in dicionario2 or len(palavra) != 5:
        print(f"\033[1;41m PALAVRA INVÁLIDA \033[0;0m")
        palavra = unidecode(input("").lower())
    palavraCertaIndex = dicionario2.index(palavra)
    palavraCerta = dicionario2[palavraCertaIndex]
    palavraCertaComAcento = dicionario1[palavraCertaIndex]
    while i < len(palavra):
        letraPalavraFinalSemAcento = palavraFinalSemAcento[i]
        letraPalavraFinalComAcento = palavraFinalComAcento[i]
        letraPalavraCertaSemAcento = palavraCerta[i]
        letraPalavraCertaComAcento = palavraCertaComAcento[i]
        verificação = letraPalavraCertaSemAcento in palavraFinalSemAcento
        i += 1
        if letraPalavraCertaSemAcento == letraPalavraFinalSemAcento:
            print(f"\033[1;42m {letraPalavraCertaComAcento.upper()} \033[0;0m", end="")
        elif verificação == True:
            print(f"\033[1;43m {letraPalavraCertaComAcento.upper()} \033[0;0m", end="")
        elif letraPalavraCertaSemAcento != letraPalavraFinalSemAcento:
            print(f"\033[1;40m {letraPalavraCertaComAcento.upper()} \033[0;0m", end="")
    if palavra == palavraFinalSemAcento:
        print("\n\033[1;46m PARABÉNS A PALAVRA ESTÁ CORRETA \033[0;0m")
        x += 1
        break
    contador +=1
if x == 0:
    print(f"\n\033[1;41m ACABOU SUAS CHANCES, A PALAVRA CORRETA ERA {palavraFinalComAcento.upper()} \033[0;0m")