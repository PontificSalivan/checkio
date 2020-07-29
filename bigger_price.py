def bigger_price(limit: int, data: list) -> list:
    
    lst = list()
    sets = []
    answer = list()

    for name in data:
        sets = [name.get("price"),name.get("name")] # создаем пары значений price и name 
        lst.append(sets) # создаем массив массивов

    lst.sort() # сортируем его 

    for i in range(limit):
        # так как мы знаем, где стоят значения price и name, то загружаем их в словарь
        d = {"name": lst[len(lst)-1-i][1], "price": lst[len(lst)-1-i][0]} 
        answer.append(d)
    
    return answer


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')