from collections import Counter

def popular_words(text: str, words: list) -> dict:
     
    text = text.lower() # преобразуем весь текст в нижний регистр
    
    string = ''
    lst = []
    answer = []

    #Погружаем слова в массив
    for letter in text.split():
        lst.append(letter)
    
    # если элемент есть в данных по заданию словах, то загружаем его в массив ответов - answer 
    for elem in lst: 
        if elem in words:
            answer.append(elem)

    answer = Counter(answer)  # посчитаем количество повторений элемента с помощью Counter 

    keys = answer.keys() # создадим переменную, хранящую ключи ответов 

    for word in words: # если по заданию были даны слова, не встречающиеся в тексте, добавим их в ответ с повторением 0
        if word not in keys:
            answer.update({word:0})


    return answer


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
