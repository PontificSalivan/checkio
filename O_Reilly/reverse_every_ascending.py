def reverse_ascending(items):

    if len(items) < 2:
        return items
    answer_list = []
    sort_list = [items[0]]

    for i in range(1,len(items)):

        if items[i] > items[i-1]:
            sort_list.append(items[i])

        else:
            sort_list.sort(reverse=True)

            for number in sort_list:
                answer_list.append(number)
            
            sort_list.clear()
            sort_list.append(items[i])

    sort_list.sort(reverse=True)
    for number in sort_list:
        answer_list.append(number)  

    return answer_list


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

