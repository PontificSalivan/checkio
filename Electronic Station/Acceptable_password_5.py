# Taken from mission Acceptable Password IV


def is_acceptable_password(password: str) -> bool:
    gate_1= False
    gate_2= False
    for i in password:
        if i.isdigit() :
            gate_1= True
        if i.isalpha():
            gate_2= True

    password = password.lower()
    if password.find('password') != -1:
        return False

    return True if (len(password) > 6 and gate_1 and gate_2) or len(password) > 9   else False
    


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('PASSWORD12345'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")