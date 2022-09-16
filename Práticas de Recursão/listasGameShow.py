'''
Nome: Lila Maria Salvador Frazão
Turma: 2021.1
Matrícula: 510809
'''
import os #Para aguardar pressionar uma tecla.
clear = lambda: os.system("cls") #Para limpar o terminal.

'''Parte fixa'''
# Retorna verdadeiro ou falso indicando se a lista está vazia.
def vazio(lista):
 return lista == []
# Retorna o primeiro elemento da lista.
def cabeca(lista):
 return lista[0]
# Retorna a lista sem seu primeiro elemento.
def cauda(lista):
 return lista[1:]
# Retorna a lista com o elemento x inserido no final.
def insere(lista, x):
 lista.append(x)
 return lista

'''Minha parte de manipulação de listas'''
# Retorna a União das Listas A e B
def concatenacao(lista1, lista2):
    # Se a lista1 estiver vazia, retornará a lista2, supostamente cheia
    # Se ambas estiverem vazias, retornará vazio de um jeito ou de outro, então retorna a lista2 mesmo
    if(vazio(lista1)):
        return lista2
    # Se a lista2 estiver vazia, retornará a lista1, supostamente cheia
    elif(vazio(lista2)):
        return lista1
    # Só cairá aqui se ambas estiverem cheias
    else:
        insere(lista1, cabeca(lista2))
        concatenacao(lista1, cauda(lista2))
        return lista1

# Retorna o Comprimento da Lista A
def comprimento(lista):
    if (vazio(lista)):
        return 0
    else:
        lista = cauda(lista) # Diminui o tamanho da lista enquanto acrescenta ao contador.
        contador = 1 # Já que não caiu em vazio, a lista tem pelo menos um elemento.
        return contador + comprimento(lista) # Soma os contadores até a lista esvaziar.

# Retorna o n-ésimo elemento da Lista A
def elemento(lista, n):
    contador = n
    
    if (vazio(lista)):
        return lista
    elif (comprimento(lista) - 1 < n): # O -1 é para a diferença da forma de acessar índices
        print("ERRO: O elemento escolhido não existe na lista.")
        return "ERRO"
    elif (contador == 0):
        return cabeca(lista) # Retornará o primeiro elemento da lista, que é o n-ésimo elemento
    else:
        lista = cauda(lista) # Já que não caiu no if anterior, é seguro descartar o primeiro elemento
        return elemento(lista, contador - 1) # Certificará que o contador chegará a zero no n desejado

# Retorna se o elemento x pertence à lista A
def pertence(lista, x):
    # Se x for vazio, dará True, pois o vazio está em todos os conjuntos.
    if (x == ""):
        return True 
    # Se a Lista tiver esvaziado e não ter encontrado equivalente, ou se ela for vazia, x não pertence
    elif (vazio(lista) and x != ""):
        return False
    # Se for igual ao elemento x, então x pertence à lista
    elif(cabeca(lista) == x):
        return True
    else: # Passará por todos os elementos até que esvazie ou caia no if anterior
        lista = cauda(lista)
        return pertence(lista, x)

# Retorna o último elemento da lista A
def ultimo(lista):
    if (vazio(lista)): # O último elemento da lista vazia é o vazio, então retorna como si mesma
        return lista
    else:
        return elemento(lista, comprimento(lista) - 1) # O índice do elemento final é o comprimento - 1

def primeiros(lista, n):
    # Se a lista for vazia, qualquer n primeiros elementos = []
    if (vazio(lista)):
        return lista
    # Se pedir os 0 primeiros elementos, não estaria pedindo elemento nenhum, portanto []
    if (n == 0):
        return []
    # Se pedir o 1º elementos, retorna a cabeça da lista atual.
    elif (n == 1):
        return [cabeca(lista)]
    # Caso geral:
    else:
        # Chama a função recursiva até chegar no caso acima, guardando a cabeça da lista em união.
        # Depois, ele faz de novo, com o penúltimo elemento, e concatena a cabeça da lista atual,
        # com o(s) elemento(s) guardado(s)
        união = primeiros(cauda(lista), n-1)
        return concatenacao([cabeca(lista)], união)

def inverte(lista):
    #O inverso de uma lista vazia é o vazio
    if (vazio(lista)):
        return lista
    #Se o comprimento da lista for 1, então, retorna a cabeça.
    elif (comprimento(lista) == 1):
        return [cabeca(lista)]
    # Caso geral:
    else:
        # Chama a função recursiva até chegar no caso acima, guardando a cabeça da lista em invertendo.
        # Retorna para onde chamou, com a cabeça da anterior guardada, depois, repete e faz a concatenação
        # da cabeça anterior, com a cabeça atual. Repete até chegar chegar com o primeiro elemento.
        invertendo = inverte(cauda(lista))
        return concatenacao(invertendo, [cabeca(lista)])

'''Funções suplementares'''
# Para converter input de string em listas
def InputEmLista(inputUser):
    lista = inputUser
    # Recebe inputs do Usuário
    lista = lista.split(",")
    # Remove os espaços em branco dos elementos.
    lista = [i.strip(" ") for i in lista]
    # Se for input "", retorna uma lista vazia.
    if(cabeca(lista) == ""):
        return []

    return lista

# Para tratamento de erros de inputs numéricos
def ConverterInputInt(inputUser):
    while (not inputUser.isnumeric()):
        inputUser = input("Por favor, certifique-se que digitou um número natural.\nTente novamente: ").strip()
    inputUser = (int(inputUser))
    return inputUser

'''Main'''
# Algo para deixar mais lúdico. Pode ignorar.
# Tenta abrir o arquivo PularTutorial e logo em seguida fechá-lo, se não conseguir, cria um.
try:
    pularTutorial = open("PularTutorial.txt", "r")
    pularTutorial.close()
except:
    print("""
Bem Vindo ao nosso Listas GameShow!
Onde nós colocamos nossas Listas a prova com a infâme Recursividade
e o adorado Sistema de Arquivamento!!!

Antes de tudo, um breve tutorial sobre criação de listas.
Para enviar as listas que irão participar deste **Game Show**, escreva
os elementos que quiser (números, nomes, letras, símbolos), separando-os
por vírgulas(,).

Exemplo 1: a, b, 3, 4, Itália, Macedônia
Exemplo 2: a,b,c,3,4,Itália, Macedônia

Qualquer forma que colocares a vírgula, está okay.

Esta mensagem só será mostrada na primeira execução do código.
Se deseja vê-la novamente, exclua o arquivo "PularTutorial.txt" da pasta do código.

Divirta-se :D
""")
    pularTutorial = open("PularTutorial.txt", "w")
    pularTutorial.write("Este arquivo não tem nenhuma utilidade além de me dizer se esse programa já rodou.")
    pularTutorial.close()
    os.system("pause")
    print("\n")

listasLog = open("listas.txt", "a")

# O conteúdo que realmente importa.
while (True):
    print("""Funções Disponíveis:
    1 - Concatenação
    2 - Comprimento
    3 - Elemento
    4 - Pertence
    5 - Último
    6 - Primeiros
    7 - Inverte
    0 - Sair do Programa
    """)
    escolha = input("Digite o número relacionado a função deseja experimentar: ").strip()
    escolha = ConverterInputInt(escolha) # Chama a função com o Tratamento de Erros

    # Sai do Programa
    if(escolha == 0):
        break

    # Vai pra Concatenação
    elif (escolha == 1):
        lista1 = InputEmLista(str(input("Digite a primeira lista que seja do seu agrado: ")))
        lista2 = InputEmLista(str(input("Digite a segunda lista que seja do seu agrado: ")))
        
        listasLog.write(f"concatenacao({lista1}, {lista2}")

        saída = concatenacao(lista1, lista2)
    
    # Vai para Comprimento
    elif (escolha == 2):
        lista = InputEmLista(str(input("Digite a lista que seja do seu agrado: ")))

        listasLog.write(f"comprimento({lista}")

        saída = comprimento(lista)

    # Vai para Elemento
    elif (escolha == 3):
        lista = InputEmLista(str(input("Digite a lista que seja do seu agrado: ")))
        n = str(input("Digite qual o índice do elemento que deseja ver: "))
        
        n = ConverterInputInt(n)

        listasLog.write(f"elemento({lista}, {n})")

        saída = elemento(lista, n)

    # Vai para Pertence
    elif (escolha == 4):
        lista = InputEmLista(str(input("Digite a lista que seja do seu agrado: ")))
        x = str(input("Digite o elemento que deseja ver se está na sua lista: ")).strip()
        
        listasLog.write(f"elemento({lista}, {x})")

        saída = pertence(lista, x)

    # Vai para Último
    elif (escolha == 5):
        lista = InputEmLista(str(input("Digite a lista que seja do seu agrado: ")))

        listasLog.write(f"ultimo({lista}")

        saída = ultimo(lista)

    # Vai para Primeiros
    elif (escolha == 6):
        lista = InputEmLista(str(input("Digite a lista que seja do seu agrado: ")))
        n = str(input("Digite quantos elementos da sua lista deseja ver: "))
        
        n = ConverterInputInt(n)

        listasLog.write(f"elemento({lista}, {n})")

        saída = primeiros(lista, n)

    # Vai para Inverte
    elif (escolha == 7):
        lista = InputEmLista(str(input("Digite a lista que seja do seu agrado: ")))

        listasLog.write(f"inverte({lista}")

        saída = inverte(lista)

    else:
        print("Número não encontrado, tente novamente.")

    print(saída)
    listasLog.write(f" --> {saída}\n") # Escreve a saída da operação atual em listas.txt

    os.system("pause")
    clear()

listasLog.close()

print("Byee")