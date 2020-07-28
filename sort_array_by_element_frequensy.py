from collections import Counter

def frequency_sort(items):
    lst = []
    # считаем повторяющиеся элементы и вводим пары: элемент - повторения элемента, одновременно проводя сортировку по кол-ву повторений
    couples = sorted(Counter(items).items(),reverse=True, key=lambda kv: kv[1]) 
    
    for couple in couples: 
        for _ in range (couple[1]): # запускаем цикл 'количество повторений элемента' раз
            lst.append(couple[0]) # каждый раз добавляем в ответ элемент

    return lst


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")



