import random
import os
from time import sleep
print('\t GERADOR DE  DADOS DE TESTE')
print('Bem-vindo ao Gerador de Dados de Teste!')
print('-'*100)


# Criando listas
nomes = ['Carlos', 'Regina', 'Giovana', 'Cassia', 'Vander']
emails = ['carlos123@hotmail.com', 'regina344@gmail.com',
    'giovana@gmail.com', 'cassia2022@gmail.com']
cidades = ['São Paulo', 'Dourados', 'João Monlevade',
    'Rio de Janeiro', 'João Pessoa']
estados = ['São Paulo', 'Mato Grosso do Sul',
    'Minas Gerais', 'Rio de Janeiro', 'Paraiba']
telefones = ['(11)9854-85214', '(67)9988-94298',
               '(31)9885-27415', '(21)96541-85362', '(83)98524-2231']
parar_tudo = 1
while parar_tudo == 1:
    print('[1] - nome')
    print('[2] - emails')
    print('[3] - cidade')
    print('[4] - estado')
    print('[5] - telefone')
    item_aleatorio = ['']
    entrada = input('Escolha uma ou mais opções: ')
    for entradas in entrada:
        if entradas == '1':
            nome_aleatorio = random.choice(nomes)
            item_aleatorio.append(nome_aleatorio)
            print(f'O nome gerado foi: {(nome_aleatorio)}')
        elif entradas == '2':
            email_aleatorio = random.choice(emails)
            item_aleatorio.append(email_aleatorio)
            print(f'O email gerado foi: {(email_aleatorio)}')
        elif entradas == '3':
            cidade_aleatoria = random.choice(cidades)
            item_aleatorio.append(cidade_aleatoria)
            print(f' A cidade gerada foi: {cidade_aleatoria}')
        elif entradas == '4':
            estado_aleatorio = random.choice(estados)
            item_aleatorio.append(estado_aleatorio)
            print(f' O estado gerado foi : {estado_aleatorio}')
        elif entradas == '5':
            telefone_aleatorio = random.choice(telefones)
            item_aleatorio.append(telefone_aleatorio)
            print(f' O telefone Gerado foi: {telefone_aleatorio}')
        
    #SALVANDO ARQUIVO
    imprimir_dados = input('Deseja Gerar um arquivo? \n Digite "s" para gerar o aquivo ou "n" para não gerar o arquivo: ')
    if imprimir_dados == 's':
        print('gerando arquivo...')

        sleep(3)

        print('Arquivo gerado!')

        with open('Dados.txt', 'a') as arquivo:
            for dado in item_aleatorio:
                arquivo.write(dado + os.linesep)

    
    
    parar_programa = input(' Deseja parar o programa? Digite 0 para parar e 1 para continuar: ')
    if parar_programa == '0':


        print('Obrigado por usar o software! (^_^)/')
        break





         
       
        














