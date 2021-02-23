def checkio(text, word):
    text = text.lower().replace(' ', '').splitlines()
    len_word = len(word)
    len_text = len(text)
    for my_str in range(len_text):
        index = text[my_str].rfind(word)
        if index != -1:
            return [my_str+1, index+1, my_str+1, index+len(word)]

    for my_str in range(len_text):
        for char in range(len(text[my_str])):
            for i in range(len_word):
                try:
                    if text[my_str+i][char] == word[i]:
                        pass
                    else:
                        break
                except:
                    break
                if i == len_word-1:
                    return [my_str+1, char + 1, my_str+len_word, char + 1]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('''Hiall!
Andallgoodbye!
Ofcoursegoodbye.
ornot''', "haoo") == [1,1,4,1]
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
