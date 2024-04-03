import  os

print("""sabor express
        """)

print('1. cadastrar restaurante')
print('2. listar restaurante')
print('3. ativar restaurante')
print('4. sair')


opcao_escolhida = int(input('escolha uma opçao: '))



def finaliza_app():
    os.system('cls')
    print('encerrando oprograma\n')

    if opcao_escolhida == 1:
        print('cadastrar restaurante ')
    elif opcao_escolhida == 2:
        print('listar_restaurante')
    elif opcao_escolhida == 3:
        print('ativar restaurantes') 
    else:
        finaliza_app()