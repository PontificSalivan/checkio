def isometric_strings(str1: str, str2: str) -> bool:
    special_char_str1 = []
    special_char_str2 = []

    for char1, char2 in zip(str1, str2):
        if char1 not in special_char_str1:
            special_char_str1.append(char1)
        if char2 not in special_char_str2:
            special_char_str2.append(char2)
        if len(special_char_str1) != len(special_char_str2):
            return False

    return True


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings("hlll", "hooo"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
