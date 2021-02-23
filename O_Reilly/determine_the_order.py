import os


def checkio(data):
    fake_alphabet = data[0]
    alphabet = ''
    # проверка на одинаковые символы
    for char in fake_alphabet:
        if char not in alphabet:
            alphabet += ''.join(char)

    data.pop(0)

    for word in data:
        for i in range(len(word)):
            paste = ''
            if word[i] not in alphabet:  # новая буква в алфавите
                paste += ''.join(word[i])
                if i == 0:
                    left_side_paste = 0  # левой границы склейки нет
                else:
                    left_side_paste = i

                right_side_paste = 0
                for j in range(1, len(word[i:])):
                    if word[i+j] not in alphabet:
                        paste += ''.join(word[i+j])  # добавляем новые буквы в склейку пока не найдем левую границу
                    else:
                        right_side_paste = i+j
                        break

                left_side_alphabet = alphabet.find(word[left_side_paste-1])
                right_side_alphabet = alphabet.find(word[right_side_paste])

                print(right_side_paste, left_side_paste, paste, alphabet)
                if right_side_paste == 0:
                    if left_side_paste == 0:  # несвязанные с алфавитом буквы
                        pass
                    else:
                        alphabet = alphabet[:left_side_alphabet+1] + paste
                        print(alphabet)

                else:
                    if left_side_paste == 0:
                        alphabet = paste + alphabet
                        print(alphabet)
                    else:
                        print(left_side_alphabet, right_side_alphabet)
                        # создаем конфликт алфавита, который должны решить
                        if left_side_alphabet == 0:
                            alphabet = alphabet[left_side_alphabet+1] + paste + alphabet[right_side_alphabet:]
                        else:
                            alphabet = alphabet[:left_side_alphabet+1] + paste + alphabet[right_side_alphabet:]

                print(alphabet)
                os.sys.exit(0)


                    

    return alphabet


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    print(checkio(["hfelcba", "hgxedba", "hgxfldca"]))
    # print(checkio(["acb", "bd", "zwa"]))

    # assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
    #     "Just concatenate it"
    # assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
    #     "Paste in"
    # assert checkio(["a", "b", "c"]) == "abc", \
    #     "Cant determine the order - use english alphabet"
    # assert checkio(["aazzss"]) == "azs", \
    #     "Each symbol only once"
    # assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
    #     "Concatenate and paste in"


