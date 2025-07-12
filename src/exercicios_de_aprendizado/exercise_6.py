def append(list1, list2):
    result = []
    for item in list1:
        result += [item]
    for item in list2:
        result += [item]
    return result


def concatenate(*lists):
    result = []
    for lst in lists:
        for item in lst:
            result += [item]
    return result


def filter(predicate, lst):
    result = []
    for item in lst:
        if predicate(item):
            result += [item]
    return result


def length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def map(function, lst):
    result = []
    for item in lst:
        result += [function(item)]
    return result


def foldl(function, lst, accumulator):
    for item in lst:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, lst, accumulator):
    for item in reverse(lst):
        accumulator = function(item, accumulator)
    return accumulator


def reverse(lst):
    result = []
    for item in lst:
        result = [item] + result
    return result
