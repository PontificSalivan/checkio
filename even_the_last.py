def checkio(array: list) -> int:

    #Проверка на пустой лист
    if len(array) > 0:
        check = True
        answer = 0

        #Добавляем каждый второй элемент листа к ответу
        for number in array:
            if check:
                answer += number
                check = False
            else:
                check = True

        #Умножаем получившийся ответ на последний элемент массива
        return answer*array[len(array)-1]

    else:
        return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")