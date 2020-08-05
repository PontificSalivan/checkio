# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    gate_1= False
    gate_2= False
    for i in password:
        if i.isdigit() :
            gate_1= True
        if i.islower() or i.isupper() :
            gate_2= True

    
    return True if len(password) > 6 and gate_1 and gate_2 else False
    


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('muchlonger5'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")