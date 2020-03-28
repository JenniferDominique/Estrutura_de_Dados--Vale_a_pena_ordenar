# Estrutura de Dados - Vale a pena ordenar? - ED FATEC SJC - 2020

### 👨🏽‍🏫 Professor Orientador: [Fernando Masanori](https://github.com/fmasanori)

## Enunciado
---
O algoritmo de busca binária é muito mais rápido que o de busca sequencial, no entanto, para poder utilizá-lo precisamos antes ordenar os elementos do vetor, isto gasta certo tempo computacional. Quando vale a pena ordenar o vetor, para poder utilizar busca binária? Veremos na prática como medir isso verificando o número de buscas que são necessárias para que valha a pena ordenar o vetor. Isto é, fazer certo número de buscas sequenciais custa o mesmo tempo que fazer esse mesmo número de buscas binárias, mais uma ordenação anterior do vetor. Neste EP1 é programado os algoritmos de busca binária, busca sequencial e os algoritmos de ordenação por seleção, inserção, mergesort, quicksort e sort nativo do Python 3 e verificar esse número mínimo para cada método diferente de ordenação. Este EP1 deverá ser feito em Python 3.x e a saída deverá ser em formato texto (não utilizar interface GUI). 

1. Não precisa pedir opções ao usuário, basta mostrar todos os tempos na saída até passarem 30 segundos. 

2. Depois iniciará um loop onde irá testando diferentes vetores aleatórios, começando com 10000 inteiros e incrementando de mais 10000 elementos a cada passo. Deverá salvar uma cópia do vetor para auxiliar nos testes. Para cada algoritmo de ordenação  irá guardar o tempo consumido para a ordenação e depois rodar seguidamente busca sequencial e busca binária até que o tempo de ordenação mais o tempo das buscas binárias igualem o tempo das buscas sequenciais. 

3. No programa não será necessário ler parâmetros, poderá mostrar a saída abaixo no programa em Python, incluindo o sort nativo, que não está na saída abaixo, mas deve ser incluído no EP.

<img src= "https://drive.google.com/file/d/1gQmdhXQghTg_BQR74CdH-IjxtQ-IOBUn/view?usp=sharing">