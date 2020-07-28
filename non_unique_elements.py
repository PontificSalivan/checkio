from collections import Counter

def checkio(data: list) -> list:

    delete_lst = [] # список удаляемых элементов массива 
    dictionary = Counter(data) # посчитаем количество повторений элемента с помощью Counter 
    couples = dictionary.items() # создадим пары элемент - повторение элемента

    for couple in couples: # пройдемся по каждой из них
        if couple[1] == 1:  # если элемент уникальный то...
            delete_lst.append(couple[0]) # ... добавим его в массив элементов удаления 
    
    for elem in delete_lst: # удаляем все элементы из списка
        data.remove(elem)

    return data


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")