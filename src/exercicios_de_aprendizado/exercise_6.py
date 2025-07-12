# Cria uma nova lista juntando todos os elementos de list1 e depois todos de list2.
def append(list1, list2): #percorre cada lista e adiciona em result, na ordem
    result = []
    for item in list1:
        result += [item]
    for item in list2:
        result += [item]
    return result

# Recebe várias listas e junta todos os seus itens numa única lista.
def concatenate(*lists): #*pq aceita varias listas
    result = []
    for list in lists:
        for item in list:   # o primeiro for acessa as listas, o segundo os elementos, isso faz
            result += [item] #com que  a saida nao seja uma lista de listas e sim uma unica lista
    return result

# Aplica uma função lógica (predicado) a cada item e mantém só os que forem True
def filter(predicate, list):
    result = []
    for item in list:     #Vai pegar cada item na lista e ver se passa pelo predicado, se passar vai pro result
        if predicate(item):
            result += [item]
    return result

# Conta quantos itens tem na lista, sem usar len()
def length(list):
    count = 0
    for _ in list: # _ só verifica se tem algo, não importa o conteúdo
        count += 1
    return count

# Aplica uma função a cada item da lista e retorna uma nova lista com os resultados.
def map(function, list):
    result = []
    for item in list:
        result += [function(item)]
    return result

# Reduz a lista para um único valor, combinando os itens da esquerda para a direita.
def foldl(function, list, accumulator):
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator

# Reduz a lista da direita para a esquerda — começa pelo final!
def foldr(function, list, accumulator):
    for item in reverse(list):
        accumulator = function(item, accumulator)
    return accumulator

# Inverte a ordem dos itens da lista original.
def reverse(list):
    result = []
    for item in list:
        result = [item] + result
    return result
