def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False
    first_memory = {}
    second_memory = {}
    for index, first in enumerate(first_string):
        try:
            first_memory[first] += 1
        except KeyError:
            first_memory[first] = 1
        
        try:
            second_memory[second_string[index]] += 1
        except KeyError:
            second_memory[second_string[index]] = 1
    for i in first_memory.keys():
        try:
            if first_memory[i] != second_memory[i]:
                return False
        except KeyError:
            return False
    return True

# var1 = 'coxinha'
# var2 = 'empada'
# print(is_anagram(var1, var2))
# m = {}
# m[1] = 1
# print(len(var1))
# for ola in enumerate(var1):
#     print(ola)
