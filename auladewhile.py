boot_video_gamer = '0'
while boot_video_gamer != '1':
    print('1-Sair')
    print('2-Baixar o jogo')
    print('3-Desinstalar o jogo')
    print('4-Ligar o video gamer')
    boot_video_gamer = input('Digite um numero: ')
    if boot_video_gamer == '1':
        print('Saindo')
    elif boot_video_gamer == '2':
        print('Baixando o jogo')
    elif boot_video_gamer == '3':
        print('Densistalando o jogo')
    elif boot_video_gamer == '4':
        print('Ligando o video gamer')
    else:
        print('não tenho esse comando, repita')