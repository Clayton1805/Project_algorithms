def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if not word:
        return False
    if high == 0:
        return True

    if word[low] != word[high]:
        # print(low)
        return False

    if low < high:
        return is_palindrome_recursive(word, low + 1, high - 1)
    # print(low)
    return True
