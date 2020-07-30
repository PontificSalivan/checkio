def second_index(text: str, symbol: str) -> [int, None]:
    
    if symbol in text: # проверка на наличие символа в тексте

        first_index = text.index(symbol) # найдем первый индекс символа

        if first_index == text.rindex(symbol): # если индекс первый и последний одинаковы, то символ всего один
            return None

        return text.index(symbol,first_index+1) # иначе выведем следующий индекс символа

    return None



if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')