from typing import Iterable

def median_three(els: Iterable[int]) -> Iterable[int]:
    
    if len(els)<3:
        return els

    lst=[]
    lst.append(els[0])
    lst.append(els[1])

    for i in range (2,len(els)):
        median_list = []
        for j in range(3):
            median_list.append(els[i-j])

        median_list.sort()
        lst.append(median_list[1])
    return lst


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
