from typing import Any, Callable, List


# Cria uma nova lista juntando todos os elementos de list1 e depois todos de list2.
def append(list1: list[int], list2: list[int]) -> list[int]:
    result: list[int] = []
    for item in list1:
        result += [item]
    for item in list2:
        result += [item]
    return result


# Recebe várias listas e junta todos os seus itens numa única lista.
def concatenate(*lists: list[Any]) -> list[Any]:
    result: list[Any] = []
    for lst in lists:
        for item in lst:
            result += [item]
    return result


# Aplica uma função lógica (predicado) a cada item e mantém só os que forem True
def filter(predicate: Callable[[Any], bool], lst: list[Any]) -> list[Any]:
    result: list[Any] = []
    for item in lst:
        if predicate(item):
            result += [item]
    return result


# Conta quantos itens tem na lista
def length(lst: List[Any]) -> int:
    count: int = 0
    for _ in lst:
        count += 1
    return count


# Aplica uma função a cada item da lista e retorna uma nova lista com os resultados.
def map(function: Callable[[Any], Any], lst: List[Any]) -> List[Any]:
    result: List[Any] = []
    for item in lst:
        result += [function(item)]
    return result


# Reduz a lista para um único valor, combinando os itens da esquerda para a direita.
def foldl(function: Callable[[Any, Any], Any], lst: List[Any], accumulator: Any) -> Any:
    for item in lst:
        accumulator = function(accumulator, item)
    return accumulator

# Reduz a lista da direita para a esquerda — começa pelo final.
def foldr(function: Callable[[Any, Any], Any], lst: List[Any], accumulator: Any) -> Any:
    size = 0
    for _ in lst:
        size += 1

    index = size - 1
    while index >= 0:
        accumulator = function(lst[index], accumulator)
        index -= 1

    return accumulator


# Inverte a ordem dos itens da lista original.
def reverse(lst: List[Any]) -> List[Any]:
    result: List[Any] = []
    for item in lst:
        result = [item] + result
    return result
