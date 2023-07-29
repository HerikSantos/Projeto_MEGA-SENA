import random, time, sys, os

os.system("cls")
print("-----------------------BEM-VINDO A MEGA-SENA-----------------------\n\n\n")
decisao = input("Você deseja jogar agora ou primeiro ler as regras? Digite 'JOGAR' ou 'REGRAS'\n")
regra_da_MEGA = '''
Para uma única aposta na Mega Sena, escolha seis números de 1 a 60.\nVocê pode escolher os seus próprios números ou escolher uma Surpresinha,\nonde o sistema informático gera um conjunto ao acaso para você.
Você também pode escolher mais de seis números, até no máximo 15.
'''

#recenbendo os daods dos usuários
if decisao.upper() == "JOGAR":
    quantidade_de_numeros = int(input('Deseja jogar quantos números? O mínimo é 6 e o máximo é 15.'))
    if quantidade_de_numeros < 6:
        print("Você seleciounou uma quantidade número inferior ao mínimo permitido, por favor jogue novamente")
        sys.exit()
    numeros_escolhidos = (input("Digite o numero escolhido separado por espaço"))
    # convertendo os dados de numeros_escolhidos para inteiros para poderem serem contados pela função len
    quantidade_de_inteiros = []
    #usei a função split pra divir a string inteira em sub strings, então antes tava assim numeros escolhidos = '11 12 13 14 15' e passou a ficar assim numeros escolhidos = [11,12,13,14,15]
    numeros_escolhidos = numeros_escolhidos.split()
    # o for foi pra interar todos os números e transformá-los como inteiros
    for i in numeros_escolhidos:
        quantidade_de_inteiros.append(int(i))
    quantidade_de_inteiros_final = len(quantidade_de_inteiros)
    # fiz uma comparação pra identificar se a pessoa não escolheu uma quantidade x de números e jogou y
    if quantidade_de_numeros != (quantidade_de_inteiros_final):
        print("Você selecionou uma quantidade número e jogou outra, o joga será encerrado")
    else:
        print("Então o grande número sorteado dessa vez é... ")
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        sorteador_dos_numeros = []
        for i in range(6):
            sorteador_dos_numeros.append(random.randint(1,60)) 
        print(f"Esses foram os números sorteados de hoje -> -> -> -> {sorteador_dos_numeros}")
        quantidade_de_acertos = []
        for i in quantidade_de_inteiros:
           if i in sorteador_dos_numeros:
               quantidade_de_acertos.append(i)
        quantidade_de_acertos = len(quantidade_de_acertos)
        print(f"Voce acertou um total de {quantidade_de_acertos} números")
        
        


elif decisao.upper() == "REGRAS":
    print(f"Escolha os seus números\n {regra_da_MEGA} ")
else:
    print('Não sei o que vc fez, mas algo deu errado!!! Jogue novamente')