import numpy as np

#Fução para abrir o ar
def criaMatrizPeca(inst): 
    caminho = 'C:/Users/bryan/OneDrive/Documentos/SIN110/ATV1/arquivos_matriz/' + inst + '.txt'
    with open(caminho, 'rb') as f:
        ncols = [int(field) for field in f.readline().split()] 
        data = np.genfromtxt(f, dtype='int32', max_rows=len(ncols))
    matrix = np.vstack((ncols,data))
    return matrix

def salvaResultado(resultado,nome):
    arquivo = open('C:/Users/bryan/OneDrive/Documentos/SIN110/ATV1/arquivos_matriz/Resultados/' + nome + '.txt', "w")
    arquivo.writelines(resultado + "\n")
    arquivo.close()

arquivoEntrada = "ponte"
a = criaMatrizPeca(arquivoEntrada)
print(a)
print(a.shape)

resultado = '\nNome: ' + arquivoEntrada + '\nNumeros de linhas: ' + str(a.shape[0]) + '\nNumeros de colunas: ' + str(a.shape[1])
nome = arquivoEntrada + 'Resultado'
salvaResultado(resultado,nome)


