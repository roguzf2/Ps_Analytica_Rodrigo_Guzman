# Função padrão para identificar se um número é um int
def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def questao4():

    # Criando dicionário das ocorrências
    ocorrencias = {}

    # While True para rodar o programa para sempre
    while True:

        num = input('Digite o valor: ')

        # Código que para o programa
        if num == 'f':
            break

        # Se for inteiro, ele deve rodar o programa
        if is_int(num):
            # Adicionando o dicionário e suas chaves para não gerar um erro
            ocorrencias[num] = ocorrencias.get(num, 0) + 1

            # Organizando o dicionário
            sorted_ocorrencias = sorted(ocorrencias.items(), key=lambda x: x[0])

    # Código que printa as ocorrências com o protuguês correto para singular e plural
    for var_num, vez_num in sorted_ocorrencias:
        if vez_num > 1:
            print('O número {} apareceu {} vezes'.format(var_num, vez_num))
        else:
            print('O número {} apareceu {} vez'.format(var_num, vez_num))

    print('Fim...')

def questao3():
    try:
        # Input coletando valor de float
        valor_monetario = float(input("Digite um valor com duas casas decimais: "))

        # Verificando se o número possui duas casas decimais!
        if round(valor_monetario, 2) != valor_monetario or float(valor_monetario) == int(valor_monetario) or round(valor_monetario, 1) == valor_monetario:
            print(('INVÁLIDO'))
            
        else:

            # Arrays de notas e moedas
            notas = [100, 50, 20, 10, 5, 2]
            moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

            # Criando Arrays para depositar a quantidade de notas e moedas respectivamente
            quantidade_notas = []
            quantidade_moedas = []

            print('\nNOTAS:\n')
            # Loop onde se realiza o código relacionado as notas

            for nota in notas:

                # Variável onde dividimos o valor do input pela nota
                troco_notas = int(valor_monetario / nota)

                # Pegando o resto do cálculo anterior e passando adiante
                valor_monetario = valor_monetario % nota

                # Adicionando o valor de troco_notas para o array quantidade_notas
                quantidade_notas.append(troco_notas)

                # Printando a quantidade de notas e seus valores correspondentes
                print('{} nota(s) de R$ {}.00'.format(troco_notas, nota))

            print('\nMOEDAS:\n')

            for moeda in moedas:

                # Variável onde dividimos o valor do input pela moeda 
                # %.2f para pegar duas casas e aproximar, já que o float eh apenas possui uma leve imprecisão
                valor_monetario = float('%.2f' % valor_monetario)

                # Variável onde dividimos o valor do input pela nota
                troco_moedas = int(valor_monetario / moeda)

                # Pegando o resto do cálculo anterior e passando adiante
                valor_monetario = valor_monetario % moeda

                # Adicionando o valor de troco_moedas para o array quantidade_moedas
                quantidade_moedas.append(troco_moedas)

                # Organizando o print das moedas
                if (moeda == 1.00) or (moeda == 0.50) or (moeda == 0.10):
                    print('{} moeda(s) de R$ {}0'.format(troco_moedas, moeda))
                else: 
                    print('{} moeda(s) de R$ {}'.format(troco_moedas, moeda))

            print('\n')

    # Se o resultado não for válido, retorna inválido
    except ValueError:
        print('INVALIDO')

def questao2():
    casas = input("Digite as casas inical e final: ")
    linhas = [1, 2, 3, 4, 5, 6, 7, 8]
    colunas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    while casas != 'f':
        valido = False
        try:
            # Input com split para separar os dois elementos do input (entrada e saida)
            list_input = list(casas.split(' '))

            # Para o usuário não poder colocar mais de 2 posições
            if len(list_input) != 2:
                raise IndexError

            # Separando os dois elementos da lista anterior em 2 listas
            cavalo_inicio = list_input[0]
            cavalo_final = list_input[1]

            # Separando os caracteres das duas listas 
            list_cavalo_inicio = list(cavalo_inicio)
            list_cavalo_final = list(cavalo_final)

            # Transformando o valor númerico da entrada e da saída do input em int
            list_cavalo_inicio[1] = int(list_cavalo_inicio[1])
            list_cavalo_final[1] = int(list_cavalo_final[1])
            
            # Analisando cada caractere do input para atender os requisitos do tabuleiro da imagem
            if list_cavalo_inicio[0] in colunas and list_cavalo_inicio[1] in linhas and list_cavalo_final[0] in colunas and list_cavalo_final[1] in linhas:

                # Condição para avaliar se o movimento do cavalo é válido, onde o número se movimenta em 2 casas e a letra em 1
                if (list_cavalo_inicio[1] - list_cavalo_final[1] == 2) or (list_cavalo_inicio[1] - list_cavalo_final[1] == -2):
                    if ( colunas.index(list_cavalo_inicio[0]) - colunas.index(list_cavalo_final[0]) == 1) or ( colunas.index(list_cavalo_inicio[0]) - colunas.index(list_cavalo_final[0]) == -1):
                        print('VÁLIDO')
                        valido = True

                #Condição para avaliar se o movimento do cavalo é válido, onde a letra se movimenta em 2 casas e o número em 1
                if (list_cavalo_inicio[1] - list_cavalo_final[1] == 1) or (list_cavalo_inicio[1] - list_cavalo_final[1] == -1):
                    if ( colunas.index(list_cavalo_inicio[0]) - colunas.index(list_cavalo_final[0]) == 2) or ( colunas.index(list_cavalo_inicio[0]) - colunas.index(list_cavalo_final[0]) == -2):
                        print('VÁLIDO')
                        valido = True

            # Se o resultado não for válido, retorna o erro
            if not valido:
                raise IndexError
        except: 
            print('INVÁLIDO')
        casas = input("Digite as casas inical e final: ")

def questao1():
    horario = input("Digite o horário desejado: ")

    while horario != 'f':
        try:
            
            # Input com split para separar os dois elementos do input (horas e minutos)
            listHorario = list(horario.split(':'))

            # Separando os dois elementos da lista anterior em 2 listas
            horas = listHorario[0]
            minutos = listHorario[1]

            # Condição onde embarreiramos o qualquer valor diferente de dois números em cada lista (horas e minutos)
            if len(horas) != 2 or len(minutos) != 2:
                raise IndexError

            # Transformando elementos das listas em int
            horas = int(horas)
            minutos = int(minutos)

            # Condição onde embarreiramos qualquer valor fora do intervaldo de 0 a 24 para horas e 0 a 60 para minutos
            if (horas < 0) or (horas > 24) or (minutos < 0) or (minutos > 60):
                raise IndexError

            # Código onde realizamos a lógica da angulação
            angulo = 360 - minutos*6 - horas*30

            # Condição para transformar a entrada de ângulos negativos para positivo
            if angulo < 0:
                angulo *= -1

            # Condição para transformar a entrada de ângulos maiores que 180 para menores que 180
            if angulo > 180:
                angulo = 360 - angulo

            print(f'{angulo=}°')
            horario = input("Digite o horário desejado: ")

        # Se o resultado não for válido, retorna inválido
        except:
            print('INVÁLIDO')

        horario = input("Digite o horário desejado: ")

def main():
    questao1()
    questao2()
    questao3()
    questao4()


if __name__ == '__main__': 
    main()