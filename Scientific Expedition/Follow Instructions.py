def follow(instructions):
    number1 = 0
    number2 = 0
    for i in instructions:
        if i == 'f':
            number2 += 1
        if i == 'r':
            number1 += 1
        if i == 'b':
            number2 += -1
        if i == 'l':
            number1 += -1
    return (number1, number2)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
