
def flat_list(array):
    # Если текущий элемент не является массивом, возвращаем его, если является то повторяем функцию
    # далее чтобы вывести результат складываем генератор с пустым массивом (чтобы получить iterable)
    return sum(([number] if not isinstance(number, list) else flat_list(number) for number in array), [])

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')