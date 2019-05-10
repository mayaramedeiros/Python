#Dupla Lucas Salvador e Mayara Brigida Turma 3B
def gerarRegioes(matriz):
    regioes = {}
    regiao = 0
    tamM = len(matriz)
    tamL = len(matriz[0])    
    for linha in range(0,tamM):
        for coluna in range(tamL):
            if matriz[linha][coluna]:
                if linha == 0 and coluna == 0:
                    regiao += 1
                    lista = []
                    t = (linha, coluna)
                    lista.append(t)                  
                    regioes[regiao] = lista 
                    
                elif linha == 0:
                    esquerda = verificaEsquerda(matriz, linha, coluna)
                    if esquerda:
                    	chave1 = achaChave(linha, coluna-1, regioes)
                    	regioes[chave1].append((linha, coluna))
                    else:
                    	regiao+=1
                    	lista = []
                    	t = (linha, coluna)
                    	lista.append(t)
                    	regioes[regiao] = lista                    
                elif coluna == 0:
                    cima = verificaCima(matriz, linha, coluna)
                    if cima:
                    	 chave2 = achaChave(linha-1, coluna, regioes)
                    	 regioes[chave2].append((linha, coluna))
                    else:
                    	regiao += 1
                    	lista = []
                    	t = (linha, coluna)
                    	lista.append(t)
                    	regioes[regiao] = lista
                else:
                    esquerda = verificaEsquerda(matriz, linha, coluna)
                    cima = verificaCima(matriz, linha, coluna)
                    if esquerda and cima:
                        chave1 = achaChave(linha-1, coluna, regioes)
                        chave2 = achaChave(linha, coluna-1, regioes)             
                        regioes[chave1].append((linha, coluna))

                        if (chave1 != chave2):                                            	
                        	listaR2 = regioes[chave2]
                        	regioes[chave1]+=listaR2
                        	regioes.pop(chave2)	
                        regiao = chave1     
                        
                    elif cima:
                    	chave2 = achaChave(linha-1, coluna, regioes)
                    	regioes[chave2].append((linha, coluna))
                        
                    elif esquerda:
                    	chave1 = achaChave(linha, coluna-1, regioes)
                    	regioes[chave1].append((linha, coluna))                       
                    else:
                        regiao += 1
                        lista = []
                        t = (linha, coluna)
                        lista.append(t)
                        regioes[regiao] = lista     
    return regioes

def printMatriz(matriz, linha, coluna):
	tamM = len(matriz)
	for l in range(linha):
		for c in range(coluna):
			print(matriz[l][c], end = " ")
		print()
		
def verificaEsquerda(matriz, linha, coluna):
    return matriz[linha][coluna -1]

def verificaCima(matriz, linha, coluna):
    return matriz[linha -1][coluna]

def achaChave(linha, coluna, regioes):
	for regiao in regioes:
		posicao = (linha, coluna) 
		valores = regioes[regiao]
		if posicao in valores:
			return regiao

def geraMatriz(regioes):
	cont = 1
	valores = []
	matriz = [[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0,0,0,0]]
	
	for regiao in regioes:
		valores = regioes[regiao]
		for valor in valores:
			matriz[valor[0]][valor[1]] = cont
		cont +=1
	return matriz


def main():
	M = [[0,1,0],[1,1,1],[0,0,0],[1,0,1]]

	M1 = [[1,0,1,0,1],[1,0,1,0,1],[1,1,1,1,1]]

	M2 = [[0,0,1,1,0,0,1,0,1,0],[0,1,1,0,0,0,1,0,1,0],[0,0,1,1,0,0,1,1,1,0],[0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,1,0],[0,0,1,0,0,1,1,1,1,1],[1,1,1,1,1,0,0,0,0,0],[0,0,1,0,0,0,1,1,1,0],[0,0,1,0,0,0,1,1,1,0]]


	regiao0 = gerarRegioes(M)
	regiao1 = gerarRegioes(M1)
	regiao2 = gerarRegioes(M2)
	matriz0 = geraMatriz(regiao0)
	matriz1 = geraMatriz(regiao1)
	matriz2 = geraMatriz(regiao2)

	print('Entrada:')
	printMatriz(M,4,3)
	print('Saida:')
	printMatriz(matriz0,4,3)
	print('Entrada:')
	printMatriz(M1, 3,5)
	print('Saida:')
	printMatriz(matriz1, 3,5)
	print('Entrada:')
	printMatriz(M2, 9,10)
	print('Saida:')
	printMatriz(matriz2, 9,10)

if __name__ == '__main__':
	main()
 
