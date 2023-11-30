import time
from funçoes import linha
import random
from random import randint
import sys

print('\033[35m  \TerLam/  \033[m')
print('''\033[31m1.\033[m Iniciar
\033[31m2.\033[m Sair''')

while True:
    try:
        menu = int(input('escolha:'))
        if menu > 2:
            print('\033[31mERRO! valor invalido tente novamente\033[m')
        elif menu == 1:
            linha()
            print('faça suas escolhas com sabedoria')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            break
        elif menu == 2:
            print('Já vai? hora dessa :D')
            break
    except ValueError:
        print('\033[31mERRO! valor invalido tente novamente\033[m')
    except KeyboardInterrupt:
        print('')
        print('O jogador forçou saida :(')

print('"Você acorda em um local desconhecido, a primeira coisa que vẽ são arvores em sua volta."')
print('''              
                       *
   *        *         ***
  ***      ***   *   *****
 *****    ***** ***    |
*******     |  ***** 
   |          *******    
                 |
''')
print('''
\033[31m1\033[m. Explorar em volta.
\033[31m2\033[m. Ficar parado.''')
while True:
    try:
        escolha = int(input('escolha:'))
        if escolha == 1:
            print('"Explorando o local, você encontra uma velha cabana. Logo em frente, encontra uma senhora..."')
            print('''
              ________
             /       /
             |       |
             |   _   |
             |__|_|__|            
            ''')
            time.sleep(1)
            break
        elif escolha == 2:
            print('"você fica parado no mesmo lugar por muito tempo mas nada acontece"')
            time.sleep(1)
            print('"Já sem esperanças vocẽ reza para o Deus Lero até que uma luz aparece mostrando um caminho..."')
            time.sleep(1)
            print('"seguindo esse caminho você econtra uma velha cabana. Logo em frente, encontra uma senhora..."')
            print('''
              ________
             /       /
             |       |
             |   _   |
             |__|_|__|            
            ''')
            break
    except ValueError:
        print('\033[31mERRO! valor invalido tente novamente\033[m')
    except KeyboardInterrupt:
        print('')
        print('O jogador forçou saida :(')
print('<desconhecido(a)> - Quem é você? Por que está aqui?')
while True:
    try:
        nome = str(input('Digite seu nome:'))
        if nome.isnumeric() or ' ' in nome:
             print('\033[31mERRO! valor invalido tente novamente\033[m')
        else:
             break
    except ValueError:
        print('\033[31mERRO! valor invalido tente novamente\033[m')
    except KeyboardInterrupt:
        print('')
        print('O jogador forçou saida :(')
        break
time.sleep(1)
print(f'<{nome}> - Ah, eu... meu nome é Bruno. eu acabei me perdendo, que lugar é esse?')
time.sleep(1)
print('<Amy, a veia> Amy, a veia, é como todos me chamam por aqui. Estamos em uma parte isolada, um tanto longe da cidade.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print(f'<{nome}> - bem... você pode me ajudar? ;D')
print(f'<Amy, a veia> - ta achando que a vida é um morango? se você me trouxer 5 presas de lobo eu te levo até a cidade.')
print('''
\033[31m1\033[m. Aceitar missão.
\033[31m2\033[m. Recusar missão.
\033[31m3\033[m. Irineu...
''')
while True:
    try:
        escolha = int(input('Escolha:'))
        if escolha > 3:
            print('\033[31mERRO! valor invalido tente novamente\033[m')
        if escolha == 1:
            print(f'<{nome}> - Como não tenho muita escolha... eu aceito.')
            break
        if escolha == 2:
            print(f'<{nome}> - Não, faz o L.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('"Após dizer isso, Amy, a veia entra dentro de casa e você fica do lado de fora."')
            time.sleep(1)
            print('"Você passa muito tempo do lado de fora sem comer e sem beber água"')
            time.sleep(1)
            print(f'{nome} is \033[31mdead!!\033[m')
            sys.exit()
        if escolha == 3:
            print(f'<Amy, a veia> - Irineu?')
            print(f'<{nome}> - Você não sabe nem eu')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            sys.exit()
    except ValueError:
        print('\033[31mERRO! valor invalido tente novamente\033[m')
    except KeyboardInterrupt:
        print('')
        print('O jogador forçou saida :(')
        break
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print(f'<{nome}> - Você pode ao menos me da arma?')
time.sleep(1)
print('''<Amy, a veia> - 

      ⡀⣐⣌⣍⣍⣍⣍⣍⣍⣍⣝⣀⡀
    ⡀⡠⠢⠊⠌⠂⠊⠝⠽⣿⣿⣿⣿⣿⡟⠏⠋⠑⠐⠀⡀⠀⠀⠀⠀ 
⢀⢄⠎⠌⣠⣴⣴⡶⡷⣦⣆⢀⠨⢿⣿⣿⣗⠁⢀⣶⣿⣽⣷⣮⡄⠀⠀
⠠⡪⡪⠀⢪⣿⣿⠝⠈⠈⢸⢟⠁⠀⣸⢿⣿⣯⠀⠀⠹⣻⣿⠨⠀⢛⠂⠀⠀
⡱⡱⠈⠠⠀⠙⠯⠳⠐⠀⠁⠀⠀⠠⣺⣿⣿⣿⣗⡀⠀⠀⠙⠹⠚⠐⠀⠕⣅ 
⡪⣊⢂⠈⠐⠀⡄⢄⢐⠨⠀⠀⡂⡱⣿⣿⣿⣿⣿⣧⢂⠀⠀⠀⢄⠢⠡⠁⣸ 
⡪⡪⡐⠀⠀⠁⠈⠀⠁⢀⠐⢈⢄⣶⣯⣭⣽⣏⣿⣿⣷⡨⡠⢀⠀⠁⡀⡰⣼ 
⡪⡪⠪⡪⢌⢢⢂⢨⢢⢱⢀⢇⣿⣿⣿⣿⣿⣿⣋⣿⣿⣿⣾⣷⣷⣷⣷⣿⣿
⡪⡊⠀⡪⡪⡪⡪⡪⡪⡪⣮⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿ 
⡪⠀⡜⡜⣌⢎⢎⣮⢾⠿⢟⠟⠻⠙⠁⠊⠑⠁⠑⠈⠈⠘⠈⠉⠋⠟⠯⢫⣿ 
⠘⠀⢳⠱⠹⠉⠃⠁⡀⢄⣠⡠⣤⣢⣦⣷⣶⣷⣾⣾⣾⣾⣾⣮⣦⣤⣤⠀⡟ 
⠀⠁⠹⣅⢤⣦⡷⣷⢿⢿⣻⢻⢿⢻⢿⡻⡿⣿⣿⣿⣿⣿⣿⡿⠻⠙⠉⡰⠀ 
⠀⠀⠁⠌⠪⢪⢪⢪⢪⢕⢜⢜⢜⢜⢔⢕⢭⣿⣿⣿⣿⣿⠯⢑⣴⣾⣿⠁⠀ 
⠀⠀⠀⠈⠢⢸⢸⢸⢸⢨⢪⢢⢣⢱⠱⠱⠱⠹⡻⠻⠫⠁⣠⣾⣿⠿ 
''')
time.sleep(0.5)
print(f'<{nome}> - Já entendi...')
time.sleep(2)
print('"após alguns minutos procurando por lobos, voçê escuta uma moita se mexendo..."')
print('''
    ***
   *****
  ******* 
 *********
  ******* 
   *****
    ***
''')
time.sleep(2)
print('"De dentro dessa moita surge um lobo pidão. \033[31mHORA DA BATLHA!!!\033[m')
print('''
      /^\      /^|
      |  \    /  |
      ||\ \../ /||
      )'        `(
     ,;`w,    ,w';,
     ;,  ) __ (  ,;
      ;  \(\/)/  ;;
     ;|  |vwwv|    ``-...
      ;  `lwwl'   ;      ```''-.
     ;| ; `""' ; ;              `.
      ;         ,   ,          , |
      '  ;      ;   l    .     | |
      ;    ,  ,    |,-,._|      \;
       ;  ; `' ;   '    \ `\     \;
       |  |    |  |     |   |    |;
       |  ;    ;  |      \   \   (;
       | |      | l       | | \  |
       | |      | |       | |  ) |
       | |      | ;       | |  | |
       ; ,      : ,      ,_.'  | |
      :__'      | |           ,_.'
               `--'
''')

lobo = 10
time.sleep(2)
vida = 10

def jogador():
    print(f'jogador:{nome} / vida:\033[31m️{vida}❤️\033[m')


print('"como funciona a batalha, você escolhera uma opção e caso o dado dé acima de 5 a ação é feita com sucesso. Mas senão...')
time.sleep(1)
linha()
print(f'''

                                  {jogador()} 
                                      O
    Lobo: \033[31m{lobo}❤\033[m️      /|\\
                /^._                 / \\
  ,___,--~~~~--' /'~
  `~--~\\ )___,)/'                   
      (/\\_  (/\\
  

''')
while True:
    try:
        print('''
\033[31m1.\033[m Dar uma piza. (2 de dano)
\033[31m2.\033[m "È o filinho de papai è?..." (?)
''')
        escolha = int(input('Escolha:'))

        if escolha > 2:
            print('\033[31mERRO! valor invalido tente novamente\033[m')

        if escolha == 2:
            print('<lobo> - huehuehue')
            vida = vida - 2
            linha()
            print(f'''

                                 {jogador()}
                                      O
    Lobo: \033[31m️{lobo}❤\033[m️      /|\\
                /^._                 / \\
  ,___,--~~~~--' /'~
  `~--~\ )___,)/'                   
      (/\\_  (/\\
  

''')

        if escolha == 1:
            for c in range(10):
                dado = random.randint(1, 10)
                print('\rDado: {}'.format(dado), end='', flush=True)
                time.sleep(0.2)
            if dado > 5:
                print('')
                print('Você acertou!')
                lobo = lobo - 2
                linha()
                print(f'''

                                 {jogador()}
                                      O
    Lobo: \033[31m️{lobo}❤\033[m️      /|\\
                /^._                 / \\
  ,___,--~~~~--' /'~
  `~--~\ )___,)/'                   
      (/\\_  (/\\
  

''')

            else:
                print('')
                print('Voce errou :(')
                linha()
                print(f'''

                                 {jogador()}
                                      O
    Lobo: \033[31m️{lobo}❤\033[m️      /|\\
                /^._                 / \\
  ,___,--~~~~--' /'~
  `~--~\ )___,)/'                   
      (/\\_  (/\\
  

''')

        for c in range(10):
            dado = random.randint(1, 10)
        if dado > 5:
            print('Lobo te acertou!')
            vida = vida - 2
            linha()
            print(f'''

                                 {jogador()}
                                      O
    Lobo: \033[31m️{lobo}❤\033[m️      /|\\
                /^._                 / \\
  ,___,--~~~~--' /'~
  `~--~\ )___,)/'                   
      (/\\_  (/\\
  

''')

        else:
           print('Lobo errou!')
        linha()
        print(f'''

                                 {jogador()}
                                      O
    Lobo: \033[31m️{lobo}❤\033[m️      /|\\
                /^._                 / \\
  ,___,--~~~~--' /'~
  `~--~\ )___,)/'                   
      (/\\_  (/\\
  

''')

        if lobo == 0:
            print('lobo is \033[31mdead!!\033[m')
            break
        elif vida == 0:
            print(f'{nome} is \033[31mdead!!!\033[m')
            sys.exit()
    except ValueError:
        print('\033[31mERRO! valor invalido tente novamente\033[m')
    except KeyboardInterrupt:
        print('')
        print('O jogador forçou saida :(')
        break

linha()
print('\033[35mParabéns!\033[m Você conseguiu derrotar o lobo e pegar as 5 presas!')
print('Voltando para a velha cabana, você entrega as presas de lobo a Amy, a velha. E vão direto para a cidade.')
time.sleep(1)
print('Durante a viagem, vocês conversam bastante, se divertem bastante, até que finalmente vocês chegam à cidade.')
time.sleep(1)
print('Amy, a velha, se dirige até um guarda e diz:')
print('<Amy, a veia> - Com licença guarda, pode ajudar meu amigo? ele acabou se perdendo.')
print('<Guarda> - Que amigo?')
print('''

   O            = O
  /|\           |/|\\
  / \           |/ \\                   

''')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
