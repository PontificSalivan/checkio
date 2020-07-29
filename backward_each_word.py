def backward_string_by_word(text: str) -> str:
    answer = ''
    string = ''
 
    for char in text:
        if char.isspace(): # проверка на пробел
            answer += ''.join(string[::-1] + ' ') # реверсируем строку и добавляем пробел
            string = ''
        else:
            string += ''.join(char)

    answer += ''.join(string[::-1] + ' ') # добавляем последнюю строку

    return answer[:len(answer)-1] # выводим строку с удалением последнего символа - пробела

if __name__ == '__main__':

    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
