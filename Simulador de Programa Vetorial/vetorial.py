'''
Nome: Lila Maria Salvador Frazão
Turma: 2021.1
Matrícula: 510809
'''
import turtle
from math import sqrt

#Recebe os dados do desenho em específico
def Dados(caneta, janela):
    #Recebe os inputs para os dados
    x = janela.numinput("Valor Horizontal", "Digite o nº X em que você quer desenhar:")
    y = janela.numinput("Valor Vertical", "Digite o nº Y em que você quer desenhar:")
    grau = janela.numinput("Grau", "Digite o ângulo que você quer desenhar:")
    
    #Definindo as cores:
    cores = {
    "vermelho": "red",
    "rosa": "hotpink",
    "roxo": "darkorchid",
    "azul" : "blue",
    "ciano" : "darkturquoise",
    "verde" : "limegreen",
    "amarelo" : "yellow",
    "laranja" : "darkorange",
    "preto" : "black"
    }

    cor = janela.textinput("Cor", "Digite o nome da cor em que você quer desenhar:")
    cor = cor.lower()
    while(cor not in cores):
        cor = janela.textinput("Cor", "Cor não encontrada no banco de dados, tente novamente: ")
        cor = cor.lower() 

    cor = cores[cor] #Traduz a cor em português para inglês

    #Junta todos numa única tupla
    dados = (caneta, x, y, grau, cor) 
    return dados

def Retângulo(dados, largura, altura):
    caneta, x, y, grau, cor = dados
    caneta.goto(x, y)
    caneta.setheading(grau)
    caneta.pencolor(cor)
    caneta.fillcolor(cor)
    
    caneta.begin_fill()
    for i in range(2):
        caneta.pendown()
        caneta.forward(largura)
        caneta.right(90)
        caneta.forward(altura)
        caneta.right(90)
    caneta.end_fill()

def PolígonoReg(dados, lados, nLados):
    caneta, x, y, grau, cor = dados
    caneta.goto(x, y)
    caneta.setheading(grau)
    caneta.pencolor(cor)
    caneta.fillcolor(cor)
    
    caneta.pendown()
    caneta.begin_fill()
    caneta.circle(lados, 360, int(nLados))
    caneta.end_fill()

def Círculo(dados, raio):
    caneta, x, y, grau, cor = dados
    caneta.goto(x, y)
    caneta.setheading(grau)
    caneta.pencolor(cor)
    caneta.fillcolor(cor)

    caneta.pendown()
    caneta.begin_fill()
    caneta.circle(raio)
    caneta.end_fill()

def TriânguloRet(dados, catetoA, catetoO):
    caneta, x, y, grau, cor = dados
    caneta.goto(x, y)
    caneta.setheading(grau)
    caneta.pencolor(cor)
    caneta.fillcolor(cor)

    hipotenusa = catetoA**2 + catetoO**2
    hipotenusa = sqrt(hipotenusa)

    caneta.pendown()
    caneta.begin_fill()
    caneta.forward(catetoA)
    posAdjacente = caneta.pos()
    caneta.goto(x,y)
    caneta.left(90)
    caneta.forward(catetoO)
    angAdjacente = caneta.towards(posAdjacente)
    caneta.setheading(angAdjacente)
    caneta.forward(hipotenusa)
    caneta.end_fill()

'''Main:'''
#Criação da Janela
janela = turtle.Screen()
janela.title("Desenhos Vetoriais Simples")

janela.setup(width=.75, height=0.75, startx=None, starty=None)

#Criação da Caneta
caneta = turtle.Turtle()
caneta.pensize(2)
caneta.speed(10)
caneta.setheading(0)
caneta.penup()

#Armazena os desenhos feitos
histórico = []
dados = ()

'''Main Loop'''
while (True):
    escolha = janela.numinput("Escolha", """
    Digite o número correspondente ao que quer desenhar:
    1 = Retângulo
    2 = Polígono Regular
    3 = Círculo
    4 = Triângulo Retângulo
    5 = Sair
    """)

    #Criará um Retângulo
    if (escolha == 1):
        dados = Dados(caneta, janela)
        largura = janela.numinput("Largura", "Digite a largura do retângulo:")
        altura = janela.numinput("Altura", "Digite a altura do retângulo:")
        
        #Tratamento de Erros
        while (largura < 1):
            largura = janela.numinput("Largura", "Digite um número positivo: ")
        while(altura < 1):
            altura = janela.numinput("Altura", "Digite um número positivo: ")

        Retângulo(dados, largura, altura)
        histórico.append(("Retângulo", largura, altura))

    #Criará um Polígono Regular
    elif (escolha == 2):
        dados = Dados(caneta, janela)
        lados = janela.numinput("Tamanho dos Lados", "Digite o tamanho dos lados do polígono:")
        nLados = janela.numinput("Quantidade de Lados", "Digite quantos lados o polígono deve ter:")
        
        #Tratamento de Erros
        while (nLados < 3):
            nLados = janela.numinput("Quantidade de Lados", "Digite um número maior que 2:")
        
        PolígonoReg(dados, lados, nLados)
        histórico.append(("Polígono Regular", lados, nLados))

    #Criará um Círculo
    elif (escolha == 3):
        dados = Dados(caneta, janela)
        raio = janela.numinput("Tamanho do Raio", "Digite o tamanho do raio do círculo: ")

        #Tratamento de Erros
        while (raio < 1):
            raio = janela.numinput("Tamanho do Raio", "O número não deve ser neutro nem negativo: ")

        Círculo(dados, raio)
        histórico.append(("Círculo", raio))

    #Criará um Triâgulo Retângulo
    elif (escolha == 4):
        dados = Dados(caneta, janela)
        catetoA = janela.numinput("Tamanho do Cateto Adjacente", "Digite o tamanho do cateto adjacente: ")
        catetoO = janela.numinput("Tamanho do Cateto Oposto", "Digite o tamanho do cateto oposto: ")

        #Tratamento de Erros
        while (catetoA < 1):
            catetoA = janela.numinput("Tamanho do Cateto Adjacente", "Digite um valor positivo: ")
        while (catetoO < 1):
            catetoO = janela.numinput("Tamanho do Cateto Oposto", "Digite um valor positivo: ")

        TriânguloRet(dados, catetoA, catetoO)
        histórico.append(("Triângulo Retângulo", catetoA, catetoO))
    
    #Sairá da Janela
    elif (escolha == 5):
        break
    
    caneta.penup()
    histórico.append(dados)

    #Remover tuplas em branco da lista do histórico
    for i in histórico:
        if (i == ()):
            histórico.remove(i)

print(histórico)
janela.bye()