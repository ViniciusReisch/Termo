# Importando bibliotecas
import random
from unidecode import unidecode

x = 0

# Abrindo o dicionario e alterando o dicionario para remover os acentos 
arquivo = open('dicionario.txt', "rt", encoding="utf-8")
dicionario1 = arquivo.read().split()
dicionario2 = [unidecode(palavra) for palavra in dicionario1]
arquivo.close()

# Definindo a palavra aleatória com e sem acento
contador = 0
aleatoria = random.randrange(1, 16716)
palavraFinalComAcento = dicionario1[aleatoria]
palavraFinalSemAcento = dicionario2[aleatoria]

# Contador para o número de chances
while contador < 5:
    i = 0

    # Recebendo a palavra chute
    palavra = unidecode(input("").lower())

    # Conferindo se a palavra chute consta no dicionário 
    while palavra not in dicionario2 or len(palavra) != 5:
        print(f"\033[1;41m PALAVRA INVÁLIDA \033[0;0m")
        palavra = unidecode(input("").lower())
    
    # Organizando o termo correto com acento e sem acento
    palavraCertaIndex = dicionario2.index(palavra)
    palavraCerta = dicionario2[palavraCertaIndex]
    palavraCertaComAcento = dicionario1[palavraCertaIndex]

    # Contador realizara até que a palavra acabe
    while i < len(palavra):

        # Recebendo as letras por ordem alfanúmerica
        letraPalavraFinalSemAcento = palavraFinalSemAcento[i]
        letraPalavraFinalComAcento = palavraFinalComAcento[i]
        letraPalavraCertaSemAcento = palavraCerta[i]
        letraPalavraCertaComAcento = palavraCertaComAcento[i]

        # Verificando se a letra existe no termo correto (letra amarela)
        verificação = letraPalavraCertaSemAcento in palavraFinalSemAcento
        i += 1

        # Printa na tela a letra em verde caso ela esteja na posição correta e contenha no termo correto 
        if letraPalavraCertaSemAcento == letraPalavraFinalSemAcento:
            print(f"\033[1;42m {letraPalavraCertaComAcento.upper()} \033[0;0m", end="")
        
        # Printa na tela a letra em amarelo caso ela esteja na posição errada mas contenha no termo correto
        elif verificação == True:
            print(f"\033[1;43m {letraPalavraCertaComAcento.upper()} \033[0;0m", end="")

        # Printa na tela a letra em preto caso ela não contenha no termo correto
        elif letraPalavraCertaSemAcento != letraPalavraFinalSemAcento:
            print(f"\033[1;40m {letraPalavraCertaComAcento.upper()} \033[0;0m", end="")
    
    # Se você acertou a palavra vai printar na tela, "PARABÉNS A PALAVRA ESTÁ CORRETA"
    if palavra == palavraFinalSemAcento:
        print("\n\033[1;46m PARABÉNS A PALAVRA ESTÁ CORRETA \033[0;0m")
        x += 1
        break
    contador +=1

# Se acabou suas chances vai printar na tela, "ACABOU SUAS CHANCES, A PALAVRA CORRETA ERA palavraCorreta"
if x == 0:
    print(f"\n\033[1;41m ACABOU SUAS CHANCES, A PALAVRA CORRETA ERA {palavraFinalComAcento.upper()} \033[0;0m")