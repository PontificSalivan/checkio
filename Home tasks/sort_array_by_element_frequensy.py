from typing import List, Tuple

def dis_of(circle1, circle2):
    distance = ((circle1[0]-circle2[0])2 + (circle1[1]-circle2[1])2)**0.5
    return distance > (circle1[2] + circle2[2]) and not (distance + circle1[2] < circle2[2] or distance + circle2[2] < circle1[2])

def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    chains = []
    for i in range(len(circles)):
        chain = []
        if circles[i] in chains:
            continue
        chain.append(circles[i])
        for j in range(i, len(circles)):
            for k in

    return 0


if name == 'main':
    print("Example:")
    print(count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")

