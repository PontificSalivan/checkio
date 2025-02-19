def checkio(line1: str, line2: str) -> str:
    return ",".join(sorted(set(line1.split(",")) & set(line2.split(","))))

if __name__ == '__main__':
    print("Example:")
    print(checkio('one,two,three', 'four,five,one,two,six,three'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three', 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
