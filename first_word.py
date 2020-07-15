def first_word(text: str) -> str:

    string = ''
    
    
    for char in text:
        
        if char.isupper() or char.isdigit() or char.islower() or char == "'":
            string += ''.join(char)
      
        elif len(string) > 0:
            answer = ''
            gate = True


            for char in string:

                if char.islower() or char.isupper() or char == "'":
                    answer += char

                else:
                    answer = ''
                    string = ''
                    gate = False
                    break

            if gate:
                return answer

    return text
 
if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
    