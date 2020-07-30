def between_markers(text: str, begin: str, end: str) -> str:

    begin_index=-1
    end_index=-1

    if begin in text: # проверка на наличие начальной строки 
        begin_index = text.index(begin)

    if end in text: # проверка на наличие конечной  строки 
        end_index = text.index(end)
    
    if begin_index != -1 and end_index != -1: # если есть обе выводим внутренности
        return text[ begin_index + len(begin) : end_index ]
       
    elif begin_index != -1: # если есть только начальная выводи от нее до конца
        return text[ begin_index + len(begin) : ]

    elif end_index != -1:   # если есть конечная выводим все до нее
        return text[ : end_index ]

    return text # если нет ограничений выводим все
        



if __name__ == '__main__':
    print('Example:')
    print(between_markers("Never send a human to do a machine's job.","Never","do"))



    