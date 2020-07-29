def defence_pawns(char):

    previous_line_pawn = str(int(char[1])-1) # пешку защищают пешки с линии ниже, ее мы и будем выводить
    
    # проходка по всем диагоналям для каждой буквы
    if char[0] == 'a':
        return ('b' + previous_line_pawn),('z' + previous_line_pawn)
    elif char[0] == 'b':
        return ('a' + previous_line_pawn),('c' + previous_line_pawn)
    elif char[0] == 'c':
        return ('b' + previous_line_pawn),('d' + previous_line_pawn)
    elif char[0] == 'd':
        return ('c' + previous_line_pawn),('e' + previous_line_pawn)
    elif char[0] == 'e':
        return ('d' + previous_line_pawn),('f' + previous_line_pawn)
    elif char[0] == 'f':
        return ('e' + previous_line_pawn),('g' + previous_line_pawn)
    elif char[0] == 'g':
        return ('f' + previous_line_pawn),('h' + previous_line_pawn)
    else:
        return ('g' + previous_line_pawn),('z' + previous_line_pawn)



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
