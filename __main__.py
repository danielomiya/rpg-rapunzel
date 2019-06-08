import os
from random import randint
from arts import print_princess, print_castle
from terminalutils import pause, clear

clear()

# Personagens

# Sorteio

sorteio_personagem = randint(1, 4)

if sorteio_personagem == 1:
    personagem = 'Cavalheiro'
    hp_personagem = 100
elif sorteio_personagem == 2:
    personagem = 'Principe'
    hp_personagem = 90
elif sorteio_personagem == 3:
    personagem = 'Lenhador'
    hp_personagem = 80
else:
    personagem = 'Escudeiro'
    hp_personagem = 70

# Aposentos

# Variaveis

adversario_portao = 'nenhum'  # 1
adversario_trono = 'nenhum'  # 2
adversario_festas = 'nenhum'  # 3
adversario_suite = 'nenhum'  # 4
adversario_calabouco = 'nenhum'  # 5
adversario_patio = 'nenhum'  # 6
adversario_masmorra = 'nenhum'  # 7
adversario_torre = 'nenhum'  # 8
nenhum_monstro = 'nenhum'

energia_perdida_portao = 0
energia_perdida_trono = 0
energia_perdida_festas = 0
energia_perdida_suite = 0
energia_perdida_calabouco = 0
energia_perdida_patio = 0
energia_perdida_masmorra = 0
energia_perdida_torre = 0

arma_portao = 'nenhum'
arma_trono = 'nenhum'
arma_festas = 'nenhum'
arma_suite = 'nenhum'
arma_calabouco = 'nenhum'
arma_patio = 'nenhum'
arma_masmorra = 'nenhum'
arma_torre = 'nenhum'

nenhuma_arma = 'nenhum'

energia_extra_portao = 0
energia_extra_trono = 0
energia_extra_festas = 0
energia_extra_suite = 0
energia_extra_calabouco = 0
energia_extra_patio = 0
energia_extra_masmorra = 0
energia_extra_torre = 0

a1 = 0
a2 = 0
a3 = 0
a4 = 0

# Sorteio Adversario

# Sorteio Dragao

sorteio_dragao = randint(1, 9)

if sorteio_dragao == 1:
    adversario_portao = 'Dragao'
    energia_perdida_portao = 60

elif sorteio_dragao == 2:
    adversario_trono = 'Dragao'
    energia_perdida_trono = 60

elif sorteio_dragao == 3:
    adversario_festas = 'Dragao'
    energia_perdida_festas = 60

elif sorteio_dragao == 4:
    adversario_suite = 'Dragao'
    energia_perdida_suite = 60

elif sorteio_dragao == 5:
    adversario_calabouco = 'Dragao'
    energia_perdida_calabouco = 60

elif sorteio_dragao == 6:
    adversario_patio = 'Dragao'
    energia_perdida_patio = 60

elif sorteio_dragao == 7:
    adversario_masmorra = 'Dragao'
    energia_perdida_masmorra = 60

elif sorteio_dragao == 8:
    adversario_torre = 'Dragao'
    energia_perdida_torre = 60

else:
    nenhum_monstro = 'nenhum'

# Sorteio Cavalheior Negro

sorteio_cavalheiro = randint(1, 9)

if sorteio_cavalheiro == 1 and adversario_portao == 'nenhum':
    adversario_portao = 'Cavalheiro Negro'
    energia_perdida_portao = 40

elif sorteio_cavalheiro == 2 and adversario_trono == 'nenhum':
    adversario_trono = 'Cavalheiro Negro'
    energia_perdida_trono = 40

elif sorteio_cavalheiro == 3 and adversario_festas == 'nenhum':
    adversario_festas = 'Cavalheiro Negro'
    energia_perdida_festas = 40

elif sorteio_cavalheiro == 4 and adversario_suite == 'nenhum':
    adversario_suite = 'Cavalheiro Negro'
    energia_perdida_suite = 40

elif sorteio_cavalheiro == 5 and adversario_calabouco == 'nenhum':
    adversario_calabouco = 'Cavalheiro Negro'
    energia_perdida_calabouco = 40

elif sorteio_cavalheiro == 6 and adversario_patio == 'nenhum':
    adversario_patio = 'Cavalheiro Negro'
    energia_perdida_patio = 40

elif sorteio_cavalheiro == 7 and adversario_masmorra == 'nenhum':
    adversario_masmorra = 'Cavalheiro Negro'
    energia_perdida_masmorra = 40

elif sorteio_cavalheiro == 8 and adversario_torre == 'nenhum':
    adversario_torre = 'Cavalheiro Negro'
    energia_perdida_torre = 40

else:
    nenhum_monstro = 'nenhum'

# Sorteio Monstro

sorteio_monstro = randint(1, 9)

if sorteio_monstro == 1 and adversario_portao == 'nenhum':
    adversario_portao = 'Monstro'
    energia_perdida_portao = 40

elif sorteio_monstro == 2 and adversario_trono == 'nenhum':
    adversario_trono = 'Monstro'
    energia_perdida_trono = 40

elif sorteio_monstro == 3 and adversario_festas == 'nenhum':
    adversario_festas = 'Monstro'
    energia_perdida_festas = 40

elif sorteio_monstro == 4 and adversario_suite == 'nenhum':
    adversario_suite = 'Monstro'
    energia_perdida_suite = 40

elif sorteio_monstro == 5 and adversario_calabouco == 'nenhum':
    adversario_calabouco = 'Monstro'
    energia_perdida_calabouco = 40

elif sorteio_monstro == 6 and adversario_patio == 'nenhum':
    adversario_patio = 'Monstro'
    energia_perdida_patio = 40

elif sorteio_monstro == 7 and adversario_masmorra == 'nenhum':
    adversario_masmorra = 'Monstro'
    energia_perdida_masmorra = 40

elif sorteio_monstro == 8 and adversario_torre == 'nenhum':
    adversario_torre = 'Monstro'
    energia_perdida_torre = 40

else:
    nenhum_monstro = 'nenhum'

# Sorteio Feiticeira

sorteio_feiticeira = randint(1, 9)

if sorteio_feiticeira == 1 and adversario_portao == 'nenhum':
    adversario_portao = 'Feiticeira'
    energia_perdida_portao = 30

elif sorteio_feiticeira == 2 and adversario_trono == 'nenhum':
    adversario_trono = 'Feiticeira'
    energia_perdida_trono = 30

elif sorteio_feiticeira == 3 and adversario_festas == 'nenhum':
    adversario_festas = 'Feiticeira'
    energia_perdida_festas = 30

elif sorteio_feiticeira == 4 and adversario_suite == 'nenhum':
    adversario_suite = 'Feiticeira'
    energia_perdida_suite = 30

elif sorteio_feiticeira == 5 and adversario_calabouco == 'nenhum':
    adversario_calabouco = 'Feiticeira'
    energia_perdida_calabouco = 30

elif sorteio_feiticeira == 6 and adversario_patio == 'nenhum':
    adversario_patio = 'Feiticeira'
    energia_perdida_patio = 30

elif sorteio_feiticeira == 7 and adversario_masmorra == 'nenhum':
    adversario_masmorra = 'Feiticeira'
    energia_perdida_masmorra = 30

elif sorteio_feiticeira == 8 and adversario_torre == 'nenhum':
    adversario_torre = 'Feiticeira'
    energia_perdida_torre = 30

else:
    nenhum_monstro = 'nenhum'

# Sorteio Bruxo

sorteio_bruxo = randint(1, 9)

if sorteio_bruxo == 1 and adversario_portao == 'nenhum':
    adversario_portao = 'Bruxo'
    energia_perdida_portao = 20

elif sorteio_bruxo == 2 and adversario_trono == 'nenhum':
    adversario_trono = 'Bruxo'
    energia_perdida_trono = 20

elif sorteio_bruxo == 3 and adversario_festas == 'nenhum':
    adversario_festas = 'Bruxo'
    energia_perdida_festas = 20

elif sorteio_bruxo == 4 and adversario_suite == 'nenhum':
    adversario_suite = 'Bruxo'
    energia_perdida_suite = 20

elif sorteio_bruxo == 5 and adversario_calabouco == 'nenhum':
    adversario_calabouco = 'Bruxo'
    energia_perdida_calabouco = 20

elif sorteio_bruxo == 6 and adversario_patio == 'nenhum':
    adversario_patio = 'Bruxo'
    energia_perdida_patio = 20

elif sorteio_bruxo == 7 and adversario_masmorra == 'nenhum':
    adversario_masmorra = 'Bruxo'
    energia_perdida_masmorra = 20

elif sorteio_bruxo == 8 and adversario_torre == 'nenhum':
    adversario_torre = 'Bruxo'
    energia_perdida_torre = 20

else:
    nenhum_monstro = 'nenhum'

# Armas

# Armadura

sorteio_armadura = randint(1, 9)

if sorteio_armadura == 1:
    arma_portao = 'Armadura'
    energia_extra_portao = 20

elif sorteio_armadura == 2:
    arma_trono = 'Armadura'
    energia_extra_trono = 20

elif sorteio_armadura == 3:
    arma_festas = 'Armadura'
    energia_extra_festas = 20

elif sorteio_armadura == 4:
    arma_suite = 'Armadura'
    energia_extra_suite = 20

elif sorteio_armadura == 5:
    arma_calabouco = 'Armadura'
    energia_extra_calabouco = 20

elif sorteio_armadura == 6:
    arma_patio = 'Armadura'
    energia_extra_portao = 20

elif sorteio_armadura == 7:
    arma_masmorra = 'Armadura'
    energia_extra_masmorra = 20

elif sorteio_armadura == 8:
    arma_torre = 'Armadura'
    energia_extra_torre = 20

else:
    nenhuma_arma = 'nenhum'

# Lança

sorteio_lanca = randint(1, 9)

if sorteio_lanca == 1 and arma_portao == 'nenhum':
    arma_portao = 'Lança'
    energia_extra_portao = 15

elif sorteio_lanca == 2 and arma_trono == 'nenhum':
    arma_trono = 'Lança'
    energia_extra_trono = 15

elif sorteio_lanca == 3 and arma_festas == 'nenhum':
    arma_festas = 'Lança'
    energia_extra_festas = 15

elif sorteio_lanca == 4 and arma_suite == 'nenhum':
    arma_suite = 'Lança'
    energia_extra_suite = 15

elif sorteio_lanca == 5 and arma_calabouco == 'nenhum':
    arma_calabouco = 'Lança'
    energia_extra_calabouco = 15

elif sorteio_lanca == 6 and arma_patio == 'nenhum':
    arma_patio = 'Lança'
    energia_extra_portao = 15

elif sorteio_lanca == 7 and arma_masmorra == 'nenhum':
    arma_masmorra = 'Lança'
    energia_extra_masmorra = 15

elif sorteio_lanca == 8 and arma_torre == 'nenhum':
    arma_torre = 'Lança'
    energia_extra_torre = 15

else:
    nenhuma_arma = 'nenhum'

# Espada

sorteio_espada = randint(1, 9)

if sorteio_espada == 1 and arma_portao == 'nenhum':
    arma_portao = 'Espada'
    energia_extra_portao = 10

elif sorteio_espada == 2 and arma_trono == 'nenhum':
    arma_trono = 'Espada'
    energia_extra_trono = 10

elif sorteio_espada == 3 and arma_festas == 'nenhum':
    arma_festas = 'Espada'
    energia_extra_festas = 10

elif sorteio_espada == 4 and arma_suite == 'nenhum':
    arma_suite = 'Espada'
    energia_extra_suite = 10

elif sorteio_espada == 5 and arma_calabouco == 'nenhum':
    arma_calabouco = 'Espada'
    energia_extra_calabouco = 10

elif sorteio_espada == 6 and arma_patio == 'nenhum':
    arma_patio = 'Espada'
    energia_extra_portao = 10

elif sorteio_espada == 7 and arma_masmorra == 'nenhum':
    arma_masmorra = 'Espada'
    energia_extra_masmorra = 10

elif sorteio_espada == 8 and arma_torre == 'nenhum':
    arma_torre = 'Espada'
    energia_extra_torre = 10

else:
    nenhuma_arma = 'nenhum'

# Escudo

sorteio_escudo = randint(1, 9)

if sorteio_escudo == 1 and arma_portao == 'nenhum':
    arma_portao = 'Escudo'
    energia_extra_portao = 5

elif sorteio_escudo == 2 and arma_trono == 'nenhum':
    arma_trono = 'Escudo'
    energia_extra_trono = 5

elif sorteio_escudo == 3 and arma_festas == 'nenhum':
    arma_festas = 'Escudo'
    energia_extra_festas = 5

elif sorteio_escudo == 4 and arma_suite == 'nenhum':
    arma_suite = 'Escudo'
    energia_extra_suite = 5

elif sorteio_escudo == 5 and arma_calabouco == 'nenhum':
    arma_calabouco = 'Escudo'
    energia_extra_calabouco = 5

elif sorteio_escudo == 6 and arma_patio == 'nenhum':
    arma_patio = 'Escudo'
    energia_extra_portao = 5

elif sorteio_escudo == 7 and arma_masmorra == 'nenhum':
    arma_masmorra = 'Escudo'
    energia_extra_masmorra = 5

elif sorteio_escudo == 8 and arma_torre == 'nenhum':
    arma_torre = 'Escudo'
    energia_extra_torre = 5

else:
    nenhuma_arma = 'nenhum'

# Capacete

sorteio_capacete = randint(1, 9)

if sorteio_capacete == 1 and arma_portao == 'nenhum':
    arma_portao = 'Capacete'
    energia_extra_portao = 5

elif sorteio_capacete == 2 and arma_trono == 'nenhum':
    arma_trono = 'Capacete'
    energia_extra_trono = 5

elif sorteio_capacete == 3 and arma_festas == 'nenhum':
    arma_festas = 'Capacete'
    energia_extra_festas = 5

elif sorteio_capacete == 4 and arma_suite == 'nenhum':
    arma_suite = 'Capacete'
    energia_extra_suite = 5

elif sorteio_capacete == 5 and arma_calabouco == 'nenhum':
    arma_calabouco = 'Capacete'
    energia_extra_calabouco = 5

elif sorteio_capacete == 6 and arma_patio == 'nenhum':
    arma_patio = 'Capacete'
    energia_extra_portao = 5

elif sorteio_capacete == 7 and arma_masmorra == 'nenhum':
    arma_masmorra = 'Capacete'
    energia_extra_masmorra = 5

elif sorteio_capacete == 8 and arma_torre == 'nenhum':
    arma_torre = 'Capacete'
    energia_extra_torre = 5

else:
    nenhuma_arma = 'nenhum'

(columns, _) = os.get_terminal_size() # tamanho do terminal

# PRINTS E INICIO DO PROGRAMA

clear()
print()
print('DOS MESMOS CRIADORES DE DUNGEONS & DRAGONS...'.center(columns))
print()
print('SALVE A RAPUNZEL'.center(columns))
print()


print_castle()

print()
pause() # espera o usuário interagir
clear()

# Regras

print()
print('REGRAS'.center(columns))
print()
print('1. Seja corajoso                   '.center(columns))
print('2. Não fuja dos desafios           '.center(columns))
print('3. Divirta-se, e use sua imaginação'.center(columns))
print()
print()
print('Público-alvo: todos que buscam diversão.')
print()
pause()
clear()

# Intro

print()
print('A princesa foi feita prisioneira no Castelo por um vilão assustador e precisa da sua ajuda, digno herói!')
print('Caberá a você adentrar no castelo cheio de armadilhas para salvá-la ou ela morrerá!')
print('Dentro do castelo, existe múltiplos obstáculos e cada um mais sombrio e forte que o outro, eles estão esperando pelo grande herói!')
print()
print('Você é um {}, e possui {} pontos.'.format(personagem, hp_personagem))

# Primeira decisão

print()
print('O que você prentende fazer? HAHAHA!')
print()
print('1. Invadir o portão do Castelo')
print('2. Não invadir o portão do Castelo')
print()

escolha = int(input('Escolha a opção: '))

clear()
# Entrada no Portao

if escolha == 1:
    print()
    print('Você destruiu o portao do castelo e adentrou a procura da princesa.')

    # Existe Arma no Portão

    print()
    if arma_portao == 'nenhum':
        print('Você olha ao redor procurando e não encontra nenhuma arma.')

    else:
        print('Você olha ao redor, encontra uma {} e tem um aumento de {} de energia.'.format(
            arma_portao, energia_extra_portao))

        hp_personagem += energia_extra_portao

        print('Sua nova energia é: {}'.format(hp_personagem))

    # Existe Adversário no Portão e combate

    if adversario_portao == 'nenhum':
        print('Você olha para os lados e não se depara com nenhum inimigo.')

    else:

        print('Poutis grila! Você foi emboscado por um {}, que é um adversário de {} de energia!'.format(adversario_portao, energia_perdida_portao))

        hp_personagem -= energia_perdida_portao

        print()
        print('Que comece a batalha!')

    # Verifica se continua vivo e segue

    print()

    if hp_personagem > 0:

        print('Congratulations! Você venceu a partida, contudo a sua energia sofreu uma modificação. A sua nova energia é de: {}'.format(hp_personagem))
        print()
        print('Olhando em volta você se depara com duas portas, uma para a Sala do Trono e outra para o Salão de Festas')
        print('Para onde o nobre herói gostaria de ir?')
        print()
        print('1. Sala do Trono')
        print('2. Salão de Festas')
        print()

        a1 = int(input('Digite uma opção: '))

    else:
        print('Você foi derrotado porque sua energia não superou o adversário.')

        a1 = 0


# Entrada na Sala do Trono

    if a1 == 1:
        clear()
        print()
        print('Você entrou na Sala do Trono!')
        print('O local é amplo, com um trono de pedra e caminhos de fogo demarcado no chão.')

        # Existe Arma na Sala do Trono

        if arma_trono == 'nenhum':
            print()
            print('Você olha em volta e não encontra nenhuma arma.')

        else:
            print()
            print('Você olha em volta e encontra uma {} que te dá um aumento de {} de energia.'.format(
                arma_trono, energia_extra_trono))

            hp_personagem += energia_extra_trono

            print()
            print('Sua nova energia é: {}'.format(hp_personagem))

        # Existe Adversário na Sala do Trono e combate

        if adversario_trono == 'nenhum':
            print()
            print('Você olha para os lados e não se depara com nenhum inimigo.')

        else:
            print()
            print('Nossa! Você se deparou com um {} que é um adversário de {} de energia!'.format(adversario_trono, energia_perdida_trono))

            hp_personagem -= energia_perdida_trono

            print()
            print('Um duelo é iniciado!')

        # Verifica se continua vivo e segue

        if hp_personagem > 0:
            clear()
            print()
            print('Congratulations! você venceu a partida, porém a sua energia sofreu uma alteração. A nova energia é: {}'.format(hp_personagem))

            print()
            print('Seguindo em diante ja ferido olha em volta e se depara com duas portas, uma para a Suíte Real e outra para o Calabouço')
            print('Para onde você gostaria de ir?')
            print()
            print('1. Suíte Real')
            print('2. Calabouço')
            print()

            a2 = int(input('Digite uma opção: '))

        else:
            print('Você foi derrotado porque sua energia não superou o adversário.')

            a2 = 0


# Entrada Salão de Festas

    if a1 == 2:
        clear()
        print()
        print('Você entrou no Salão de Festas!')

        # Existe Arma no Salão de Festas

        if arma_festas == 'nenhum':
            print()
            print('Você olha em volta e não encontra nenhuma arma.')

        else:
            print()
            print('Você olha em volta e encontra uma {} que te dá um aumento de {} de energia.'.format(
                arma_festas, energia_extra_festas))

            hp_personagem += energia_extra_festas

            print()
            print('Sua nova energia é: {}'.format(hp_personagem))

        # Existe Adversário no Salão de Festas e combate

        if adversario_festas == 'nenhum':
            print()
            print('Você olha para os lados e não se depara com nenhum inimigo.')

        else:
            print()
            print('Ohhh, não! Você se deparou com um {} que é um adversário de {} de energia!'.format(adversario_festas, energia_perdida_festas))

            hp_personagem -= energia_perdida_festas

            print()
            print('Um combate é iniciado!')

        # Verifica se continua vivo e segue

        print()
        
        if hp_personagem > 0:
            print('Congratulations! você venceu a partida, porém a sua energia sofreu uma alteração assim segue o herói ferido em sua jornada. A nova energia é: {}'.format(hp_personagem))
            print()
            print('Olhando em volta você se depara com duas portas, uma para a Suíte Real e outra para o Calabouço')
            print('Para onde você gostaria de ir?')
            print()
            print('1. Suíte Real')
            print('2. Calabouço')
            print()
            a2 = int(input('Digite uma opção: '))

        else:
            print('Você foi derrotado porque sua energia não superou o adversário.')

            a2 = 0


# Entrada Suite Real

    if a2 == 1:
        clear()
        print()
        print('Você entrou na Suite Real!')
        print()
        # Existe Arma na Suite Real

        if arma_suite == 'nenhum':
            print('Você olha em volta e não encontra nenhuma arma.')

        else:
            print('Você olha em volta e encontra uma {} que te dá um aumento de {} de energia.'.format(arma_suite, energia_extra_suite))

            hp_personagem += energia_extra_suite
            
            print()
            print('Sua nova energia é: {}'.format(hp_personagem))

        # Existe Adversário na Suite Real e combate

        if adversario_suite == 'nenhum':
            print()
            print('Você olha para os lados e não se depara com nenhum inimigo.')

        else:
            print()
            print('Céus! Você se deparou com um {} que é um adversário de {} de energia!'.format(
                adversario_suite, energia_perdida_suite))

            hp_personagem -= energia_perdida_suite

            print()
            print('Um combate é iniciado!')

        # Verifica se continua vivo e segue

        if hp_personagem > 0:

            print()
            print('Congratulations! você venceu a partida, porém a sua energia sofreu uma alteração. A nova energia é assim segue o herói ferido em sua jornada: {}'.format(hp_personagem))

            print('Olhando em volta você se depara com duas portas, uma para o Pátio e outra para a Masmorra.')
            print('Para onde você gostaria de ir?')
            print()
            print('1. Pátio')
            print('2. Masmorra')
            print()
            a3 = int(input('Digite uma opção: '))

        else:
            print('Você foi derrotado porque sua energia não superou o adversário.')

            a3 = 0


# Entrada Calabouço

    if a2 == 2:
        print()
        print('Você entrou no Calabouço!')

        # Existe Arma no Calabouço

        if arma_calabouco == 'nenhum':
            print()
            print('Você olha em volta e não encontra nenhuma arma.')

        else:
            print()
            print('Você olha em volta e encontra uma {} que te dá um aumento de {} de energia.'.format(
                arma_calabouco, energia_extra_calabouco))

            hp_personagem += energia_extra_calabouco

            print()
            print('Sua nova energia é: {}'.format(hp_personagem))

        # Existe Adversário na Suite Real e combate

        if adversario_calabouco == 'nenhum':
            print()
            print('Você olha para os lados e não se depara com nenhum inimigo.')

        else:
            print()
            print('Oh, não! Você se deparou com um {} que é um adversário de {} de energia!'.format(
                adversario_calabouco, energia_perdida_calabouco))

            hp_personagem -= energia_perdida_calabouco

            print()
            print('Um combate é iniciado!')

        # Verifica se continua vivo e segue

        if hp_personagem > 0:
            clear()
            print()
            print('Congratulations! Você venceu a partida, porém a sua energia sofreu uma alteração assim segue o herói ferido em sua jornada. A nova energia é: {}'.format(hp_personagem))
            print()
            print('Observando ao redor você se depara com duas portas, uma para o Pátio e outra para a Masmorra')
            print('Aonde você gostaria de ir?')
            print()
            print('1. Pátio')
            print('2. Masmorra')
            print()
            a3 = int(input('Digite uma opção: '))

        else:
            print('Você foi derrotado porque sua energia não superou o adversário.')

            a3 = 0


# Entrada Patio

    if a3 == 1:
        clear()
        print()
        print('Você entrou no Pátio!')

        # Existe Arma no Pátio

        print()
        if arma_patio == 'nenhum':
            print('Você olha em volta e não encontra nenhuma arma.')

        else:
            print('Você olha em volta e encontra uma {} que te dá um aumento de {} de energia.'.format(arma_patio, energia_extra_patio))

            hp_personagem += energia_extra_patio

            print()
            print('Sua nova energia é: {}'.format(hp_personagem))

        # Existe Adversário na Suite Real e combate

        if adversario_patio == 'nenhum':
            clear()
            print()
            print('Você olha para os lados e não se depara com nenhum inimigo.')

        else:
            print()
            print('Oh, não! Você se deparou com um {} que é um adversário de {} de energia!'.format(adversario_patio, energia_perdida_patio))

            hp_personagem -= energia_perdida_patio

            print()
            print('Um combate é iniciado!')

        # Verifica se continua vivo e segue

        if hp_personagem > 0:
            clear()
            print()
            print('Congratulations! Você venceu a partida, porém a sua energia sofreu uma alteração assim segue o herói ferido em sua jornada. A nova energia é: {}'.format(hp_personagem))
            print()
            print('Olhando em volta, você se depara com uma porta diferente, para entrada da Torre, o grande herói tem certeza que deseja entrar nessa porta?')
            print('Para onde você gostaria de ir?')
            print()
            print('1. Torre')
            print()
            a4 = int(input('Digite uma opção: '))

        else:

            print('Você foi derrotado porque sua energia não superou o adversário.')

            a4 = 0


# Entrada Masmorra

    if a3 == 2:
        clear()
        print()
        print('Você entrou na Masmorra!')

        # Existe Arma na Masmorra

        if arma_masmorra == 'nenhum':
            print()
            print('Você olha em volta e não encontra nenhuma arma.')

        else:
            print()
            print('Você olha em volta e encontra uma {} que te dá um aumento de {} de energia.'.format(arma_masmorra, energia_extra_masmorra))

            hp_personagem += energia_extra_masmorra

            print()
            print('Sua nova energia é: {}'.format(hp_personagem))

        # Existe Adversário na Suite Real e combate

        if adversario_masmorra == 'nenhum':
            print()
            print('Você olha para os lados e não se depara com nenhum inimigo.')

        else:
            print()
            print('Ahhhh não! Você se deparou com um {} que é um adversário de {} de energia!'.format(adversario_masmorra, energia_perdida_masmorra))

            hp_personagem -= energia_perdida_masmorra

            print()
            print('Um combate é iniciado!')

        # Verifica se continua vivo e segue

        if hp_personagem > 0:
            clear()
            print()
            print('Congratulations!')
            print('Você venceu a partida, porém a sua energia sofreu uma alteração assim segue o herói ferido em sua jornada.')
            print()
            print('A nova energia é: {}'.format(hp_personagem))
            print()
            print('Seguindo em uma passagem estreita e humida, você se depara com uma porta enorme, para entrada da Torre')
            print('Para onde você gostaria de ir?')
            print()
            print('1. Torre')
            print()

            a4 = int(input('Digite uma opção: '))

        else:
            print('Você foi derrotado porque sua energia não superou o adversário.')
            a4 = 0


# Entrada Torre

    if a4 == 1:
        clear()
        print()
        print('Você entrou na Torre!')
        print()
        # Existe Arma na Torre

        if arma_torre == 'nenhum':

            print('Você olha em volta e não encontra nenhuma arma.')

        else:

            print('Você olha em volta e encontra uma {} que te dá um aumento de {} de energia.'.format(
                arma_torre, energia_extra_torre))

            hp_personagem += energia_extra_torre
            
            print()
            print('Sua nova energia é: {}'.format(hp_personagem))
            print()
        # Existe Adversário na Suite Real e combate

        if adversario_torre == 'nenhum':

            print('Você olha para os lados e não se depara com nenhum inimigo.')

        else:

            print('Oh não! você se deparou com um {} que é um adversário de {} de energia!'.format(adversario_torre, energia_perdida_torre))

            hp_personagem -= energia_perdida_torre

            print()
            print('Um combate é iniciado!')

        # Verifica se continua vivo e segue

        if hp_personagem > 0:
            print()
            print('Congratulations!')
            print('Você venceu a partida, porém a sua energia sofreu uma alteração. A nova energia é: {}'.format(hp_personagem))

            print()
            
            pause()
            clear()
            print()
            print('Parabéns! Você resgatou a princesa do assustador vilão!'.center(columns, ' '))
            print()
            print_princess()

        else:

            print('Você foi derrotado porque sua energia não superou o adversário.')


else:

    print()
    print('Você escolheu não entrar no castelo e não salvar a princesa.')
    print('Seja corajoso, tente novamente e enfrente essa jornada e seus grandes desafios')
