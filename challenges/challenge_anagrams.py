def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    length = len(first_string) != len(second_string)

    if not first_string or not second_string or length:
        return False

    second_string = [letter for letter in second_string]

    for indice, letter in enumerate(first_string):
        if letter != second_string[indice]:
            if letter in second_string[indice:]:
                letter_previous = second_string.index(letter)
                second_string[letter_previous] = second_string[indice]
                second_string[indice] = letter
            else:
                return False
    return True

# if len(first_string) != len(second_string):
#     return False
# first_memory = {}
# second_memory = {}
# for index, first in enumerate(first_string):
#     try:
#         first_memory[first] += 1
#     except KeyError:
#         first_memory[first] = 1
#     try:
#         second_memory[second_string[index]] += 1
#     except KeyError:
#         second_memory[second_string[index]] = 1

# for i in first_memory.keys():
#     try:
#         if first_memory[i] != second_memory[i]:
#             return False
#     except KeyError:
#         return False
# return True
