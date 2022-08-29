import numpy as np

#Fução para crair uma matriz através da leitura de um arquivo que é passada como instancia seu retorno é a matriz
def criaMatriz(inst): 
    caminho = 'C:/Users/bryan/OneDrive/Área de Trabalho/sin110/ATV1/arquivos_matriz/' + inst + '.txt'
    with open(caminho, 'rb') as f:
        #ncols lê quantas colunas tem a matriz e a variavel data traz a primeira linha da matriz
        ncols = [int(field) for field in f.readline().split()] 
        data = np.genfromtxt(f, dtype='int32', max_rows=len(ncols))
    matrix = np.vstack((ncols,data))
    return matrix

#Função para salvar em arquivo de texto o nome do arquivo lido e a dimensão da matriz 
def salvaResultado(resultado,nome):
    arquivo = open('C:/Users/bryan/OneDrive/Área de Trabalho/sin110/ATV1/arquivos_matriz/Resultados/' + nome + '.txt', "w")
    arquivo.writelines(resultado + "\n")
    arquivo.close()

#Variavel arquivoEntrada modifica qual arquivo sera aberto
arquivoEntrada = "zachary"

#chama função criaMatriz e armazena em uma variavel
a = criaMatriz(arquivoEntrada)
print(a)

#shape é usado para obter as dimensões da matriz
print("Dimensão: ", a.shape)

#Variavel resultado é uma string que armazena o que sera inscrito no arquivo resultado
resultado = '\nNome: ' + arquivoEntrada + '\nNumeros de linhas: ' + str(a.shape[0]) + '\nNumeros de colunas: ' + str(a.shape[1])

#Variavel para dar nome ao arquivo resultante
nome = arquivoEntrada + 'Resultado'

#chama função para salvar
salvaResultado(resultado,nome)


