from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    dot_one_dot = []
    one_dot = []
    two_dots = []
    two_one_dot = []

    for f in files:

        if f[0] == '.' and f.count('.') == 1:
            dot_one_dot.append(f)

        elif f[0] == '.' and f.count('.') == 2:
            two_one_dot.append(f)

        elif f.count('.') == 1:
            one_dot.append(f)

        elif f.count('.') == 2:
            two_dots.append(f)

    dot_one_dot.sort()
    one_dot.sort()
    two_one_dot.sort()
    two_dots.sort()
    
    print(dot_one_dot,one_dot,two_one_dot,two_dots)
    return dot_one_dot + one_dot + two_one_dot.append + two_dots


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")