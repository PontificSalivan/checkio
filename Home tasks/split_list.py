def split_list(items: list) -> list:

    len_items = len(items)

    if len_items == 0: # проверка на пустой массив 
        items_2 = items.copy()
        lst = [items,items_2]
        return lst
        
    elif len_items == 1: # проверка на единичный массив
        items_2 = []
        lst = [items,items_2]
        return lst

    elif len_items % 2 == 0: # если четный массив
        parts = int(len_items / 2) # находим разделитель середины
        items_2 = items[parts:] # вырезка от разделителя и до конца 
        lst = [items[:parts],items_2] # создание двойного массива, вырезка всего до разделителя в первом массиве
        return lst

    parts = int(len_items / 2) # находим разделитель середины в сторону меньших значений (3/2 = 1)
    items_2 = items[parts+1:] # вырезка от разделителя и до конца 
    lst = [items[:parts+1],items_2] # создание двойного массива, вырезка всего до разделителя в первом массиве
    return lst

if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")