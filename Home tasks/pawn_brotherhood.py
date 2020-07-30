def defence_pawns(char): # определение двух защитников 
    return (chr(ord(char[0])+1) + str(int(char[1])-1)),(chr(ord(char[0])-1) + str(int(char[1])-1))

def safe_pawns(pawns: set) -> int:
    answer = 0

    for pawn in pawns:
        if pawn[1] != '1': # проверка на всякий случай, так как пешку на 1 линии никто не может защитить 
            defence_pawns_lst = defence_pawns(pawn) # для текущей пешки загружаем ее возможных защитников
            if defence_pawns_lst[0] in pawns or defence_pawns_lst[1] in pawns : # если они есть в вводе увеличиваем ответ
                answer += 1
    
    return answer


if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
