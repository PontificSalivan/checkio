def checkio(data: str) -> bool:

    gate1 = False 
    gate2 = False 
    gate3 = False 

    for char in data:
        if char.isdigit() and gate1 == False: # Проверка на цифры
            gate1 = True

        if char.isupper() and gate2 == False: # Проверка на заглавные
            gate2 = True

        if char.islower() and gate3 == False: # Проверка на прописные
            gate3 = True

    if gate1 and gate2 and gate3 and len(data) >= 10:
        return True 

    return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")