## Dupla Lucas Salvador e Mayara Brígida
from random import shuffle
import datetime

def main():
    total=2000

    print('{:-<70}'.format('-'))
    print('{:<}{:<10}{:>}{:^57}{:>}'.format('|',' ', '|','Time(s)','|'))
    print('{:-<70}'.format('-'))
    print('{:<}{:<10}{:>}{:^11}{:^11}{:^11}{:^11}{:^11}{:>3}'.format('|',' ', '|','Mergesort','Quicksort', 'Selection','Insertion','Native','|'))
    
    dt_incial = datetime.datetime.now()  #inicial

    while(True):
        lista = list(range(total)) #Gerando lista
        shuffle(lista)
        
        lista1 = lista
        inicio_quick = datetime.datetime.now() #Quicksort
        quicksort(lista1)
        fim_quick = datetime.datetime.now()
        tempo_quick = fim_quick - inicio_quick

        lista2 = lista              
        inicio_insercao = datetime.datetime.now() #Insercao
        insercao(lista2)
        fim_insercao = datetime.datetime.now()
        tempo_insercao = fim_insercao - inicio_insercao

        lista3 = lista
        inicio_selecao = datetime.datetime.now() # selecao
        selecao(lista3)
        fim_selecao = datetime.datetime.now()
        tempo_selecao = fim_selecao - inicio_selecao

        lista4 = lista
        inicio_mergesort = datetime.datetime.now() #mergeShort
        mergesort(lista4)
        fim_mergesort = datetime.datetime.now()
        tempo_mergersort = fim_mergesort - inicio_mergesort

        lista5 = lista
        inicio_sort = datetime.datetime.now() #Sort nativo
        lista5.sort()
        fim_sort = datetime.datetime.now()
        tempo_sort = fim_sort - inicio_sort
        
        tempo_mergersort = str(tempo_mergersort.seconds)+':'+str(tempo_mergersort.microseconds)
        tempo_quick = str(tempo_quick.seconds)+':'+str(tempo_quick.microseconds)
        tempo_selecao = str(tempo_selecao.seconds)+':'+str(tempo_selecao.microseconds)
        tempo_insercao =  str(tempo_insercao.seconds)+':'+str(tempo_insercao.microseconds)
        tempo_sort = str(tempo_sort.seconds)+':'+str(tempo_sort.microseconds)


        print('{:<}{:^10}{:>}{:^11}{:^11}{:^11}{:^11}{:^11}{:>3}'.format('|',total, '|',tempo_mergersort, tempo_quick, tempo_selecao,tempo_insercao, tempo_sort,'|'))
        

        dt_final = datetime.datetime.now()  #final
        tempo = dt_final- dt_incial

        if int(tempo.seconds) >= 30:
            break
        else:
            total+=2000

    print('{:-<70}'.format('-'))

    
def quicksort(lista):
    if len(lista) <= 1: 
        return lista
    
    pivo = lista[0]
    iguais  = [x for x in lista if x == pivo]
    menores = [x for x in lista if x <  pivo]
    maiores = [x for x in lista if x >  pivo]
    return quicksort(menores) + \
           iguais + quicksort(maiores)

    
def insercao(v):
 for j in range(1, len(v)):
   x = v[j]
   i = j - 1
   while i >= 0 and v[i] > x:
     v[i + 1] = v[i]
     i = i - 1
   v[i + 1] = x
 return v

def selecao(v):
  resp = []
  while v:
    m = min(v)
    resp.append(m)
    v.remove(m)
  return resp


def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

main()
    