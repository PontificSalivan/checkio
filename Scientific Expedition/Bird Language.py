VOWELS = "aeiouy"

def translate(phrase):
    new_phrase = []
    for word in phrase.split():
        cursor = 0
        new_word = []
        while cursor < len(word):
            new_word.append(word[cursor])
            if word[cursor] in VOWELS:
                cursor += 3
            else:
                cursor += 2
        new_phrase.append(''.join(new_word))
    return ' '.join(new_phrase)

if __name__ == '__main__':
    print("Example:")
    print(translate("hoooowe yyyooouuu duoooiiine"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
