import random
from time import time

# Função Principal
def main():
    # Variáveis inteiros globais
    global vetor 
    global num  
    global inicio_algoritmo
    global fim_algoritmo

    # Inicializando variáveis globais
    inicio_algoritmo = time()
    fim_algoritmo = time()
    quant_elementos = 0
    tempo_ordenacao = [5]
    buscas = [0,0,0,0,0] # Número de buscas


    # Cabeçalho do programa
    print("|------------------------------------[EP1 - Vale a pena ordenar?]--------------------------------------|\n"
        "|                      Estrutura de Dados - Analise e Desenvolvimento de Sistemas                      |\n"
        "|                      Aluno: Jennifer Dominique - FATEC - SJC 2020                                    |\n"
        "|                                                                                                      |\n"
        "|                   Algoritmo escolhido: Todos       Duração dos testes: 30.00                         |\n"
        "|                     Tempos de Ordenacao                                Numero de Buscas              |\n"          
        "|------------------------------------------------------------------------------------------------------|\n"
        "|    n   | SortNat.  Quick. Merge. Insercao  Selecao    |    SortNat. Quick. Merge. Insercao  Selecao  |\n"
        "|------------------------------------------------------------------------------------------------------|")
    
    while(fim_algoritmo - inicio_algoritmo < 30):
        quant_elementos = quant_elementos + 10000
        vetor = gerarVetor(quant_elementos) # Variável que armazenará os vetores     
        num = random.randint(0, len(vetor)) 
        tempo_ordenacao = [cronometra_sortNativo(), cronometra_quicksort(), cronometra_mergesort(), cronometra_insercao(), 
                        cronometra_selecao()]  
        
        i = 0
        while(i < 5):
            buscas[i] += Tempo(tempo_ordenacao[i], vetor, num) # Armazena o número de buscas feitas de um vetor em um tempo determinado
            i += 1
       
        print("  %d      %.2f    %.2f    %.2f    %.2f      %.2f             %d     %d     %d     %d     %d" 
                 %(quant_elementos, (tempo_ordenacao[0]), (tempo_ordenacao[1]), (tempo_ordenacao[2]), (tempo_ordenacao[3]), 
                 (tempo_ordenacao[4]), buscas[0], buscas[1], buscas[2], buscas[3], buscas[4]))

        print("|------------------------------------------------------------------------------------------------------|")        


        fim_algoritmo = time()



#__________________________________Declaração das Funções___________________________________#



#Função do Vetor
def gerarVetor(n): 
    vetor =[]
    vetor = list(range(0,n)) # Gera uma lista com uma sequência de 0 a N
    random.shuffle(vetor) # Embaralha a lista
    return vetor



# _____________Inicio das Funções de Algoritmos de Ordenação_______________ #



# Algoritmo de Ordenação por Inserção
def insercao(v):
    for j in range(1, len(v)):
        x = v[j]
        i = j - 1
        while (i >= 0) and (v[i] > x):
            v[i+1] = v[i]
            i = i - 1
        v[i+1] = x


# Algoritmo de Ordenação por Seleção
def selecao(v):
    n = len(v)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if(v[j] < v[mini]):
                mini = j
        v[i], v[mini] = v[mini], v[i]


# Algoritmo de Ordenação por MergeSort
def mergesort(v):
    if len(v) <= 1: # Melhor caso -> se o vetor já estiver ordenado
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

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



# Algoritmo de Ordenação por Quicksort
def quicksort(v):
    if len(v) <= 1: # Melhor caso -> se o vetor já estiver ordenado
        return v
    pivô = v[0] 
    iguais  = [x for x in v if x == pivô]
    menores = [x for x in v if x <  pivô]
    maiores = [x for x in v if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)



# Algoritmo de Ordenação por Sort Nativo
def sortNativo(v):
    sorted(v)




# _________Funções que cronometram os tempos das Funções de Ordenações__________ #



def cronometra_quicksort():
     tempo_quicksort = time()
     quicksort(vetor)
     return time() - tempo_quicksort
    
def cronometra_insercao():
    tempo_insercao = time()
    insercao(vetor)
    return time() - tempo_insercao

def cronometra_selecao():
    tempo_selecao  = time()
    selecao(vetor)
    return  time() - tempo_selecao

def cronometra_mergesort():
    tempo_megersort = time()
    mergesort(vetor)
    return  time() - tempo_megersort

def cronometra_sortNativo():
    tempo_sortNativo = time ()
    sortNativo(vetor)    
    return time() - tempo_sortNativo



# ___________Métodos de Algoritmos de Busca Binária & Busca Sequêncial____________ #



def BuscaSequencial(v, x):
    j = 0
    while j < len(v) and v[j] < x:
        j += 1
    return j

def BuscaBinaria(v, x):
    e = -1
    d = len(v)
    while e < d - 1: 
          m = (e + d) // 2
          if (v[m] < x):
              e = m
          else:
              d = m
    return d


# ________Funções de obtenção dos tempos das buscas________ #



def cronometra_BuscaSequencial(v,x):
    inicio = time()
    BuscaSequencial(v,x)
    return time() - inicio

def cronometra_BuscaBinaria(v,x):
    inicio = time()
    BuscaBinaria(v,x)
    return time() - inicio


# Função conta o tempo das ordenações
def Tempo(tempo_Ordenacao,vetor,num):
    total_Binaria = 0
    total_Sequencial = 0
    numeroBuscas = 0
    i = 0
    
    while (total_Sequencial < tempo_Ordenacao + total_Binaria): 
        # O tempo de Busca Sequencial tem que ser igualar ao tempo de Orsenação e Busca Binária
        tempo_Sequencial = cronometra_BuscaSequencial(vetor,num)
        tempo_Binaria = cronometra_BuscaBinaria(vetor,num)
            
        total_Binaria += tempo_Binaria
        total_Sequencial += tempo_Sequencial

        numeroBuscas += 1
            
    return numeroBuscas
        


# Chamada da função principal
main()