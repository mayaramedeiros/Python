def enumeracoes(items):
    n = len(items)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0: break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(items[s[j]-1])
            yield lista
 
def combinacoes(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinacoes(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc
 
def permutacoes(items):
    return combinacoes(items, len(items))

def vericaAmizade(listaMesa, listaAmigos):
    for posicao in range(1, len(listaMesa)):
        if not listaMesa[posicao-1] in listaAmigos[listaMesa[posicao]]:

            return 0
    if not listaMesa[0] in listaAmigos[listaMesa[-1]]:
       return 0
    
    return 1

def main():
    
    arq = open('casamento.txt','r')
    arq = arq.readlines()
    damas = {}
    for linha in arq:
        linha = linha.split()
        damas[linha[0]] = linha[1::]

    queridos = []

    for dama in damas:
        if not damas[dama] in queridos:
            queridos.append(damas[dama])
    
    flag = 0
    for p in enumeracoes(queridos):
        if len(damas) <= len(p):
            flag = 1

    if flag:
        print('Havera casamento')
    else:
        print('Nao Havera casamento')

    flag = 0
    arq = open('cavaleiros.txt','r')
    arqcavaleiros = arq.readlines()
    cavaleiro = {}
    cavaleiros = []

    for linha in arqcavaleiros:
        linha = linha.split()
        cavaleiro[linha[0]] = linha[1::]
        cavaleiros.append(linha[0])

    for permutacao in permutacoes(cavaleiros):
        retorno = vericaAmizade(permutacao, cavaleiro)
        if retorno:
            flag = 1
            break

    if flag:
        print(permutacao)
    else:
        print('Impossível gerar mesa')
        


main()
