def date_time(time: str) -> str:
    months = {'01': 'January','02': 'February','03': 'March','04': 'April','05': 'May','06': 'June','07': 'July',
    '08': 'August','09': 'September','10': 'October','11': 'November','12': 'December'}

    month = months.get(time[3:5]) # получаем месяц по дате с помощью словаря 

    if time[0] == '0': # проверка на первый ноль в начале
        start = time[1] 
    else:
        start = time[:2]
    
    if time[12] == '1': # проверка на множественное число часов
        s_hours = ''
    else:
        s_hours = 's'
    
    if time[15] == '1': # проверка на множественное число минут
        s_minutes = '' 
    else:
        s_minutes = 's'
    

    # проверка на первый ноль во времени
    if time[11]=='0' and time[14]== '0': 
        return start + ' ' + month + ' ' + time[6:10] + ' year ' + time[12] + ' hour' + s_hours + ' ' + time[15] + ' minute' + s_minutes
    elif time[11]=='0':
        return start + ' ' + month + ' ' + time[6:10] + ' year ' + time[12] + ' hour' + s_hours + ' ' + time[14:16] + ' minute' + s_minutes
    elif time[14]=='0':
        return start + ' ' + month + ' ' + time[6:10] + ' year ' + time[11:13] + ' hour' + s_hours + ' ' + time[15] + ' minute' + s_minutes

    return start + ' ' + month + ' ' + time[6:10] + ' year ' + time[11:13] + ' hour' + s_hours + ' ' + time[14:16] + ' minute' + s_minutes
    
if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
