def backward_string_by_word(text: str) -> str:
    answer = ''
    string = ''
 
    for char in text:
        if char.isspace():
            answer += ''.join(string[::-1] + ' ')
            string = ''
        else:
            string += ''.join(char)

    answer += ''.join(string[::-1] + ' ') 

    answer = answer[:len(answer)-1]
    return answer


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
