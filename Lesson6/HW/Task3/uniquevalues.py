def unique_values (list1: list, list2: list) -> list:
    set1 = set(list1)
    set2 = set(list2)

    unique_set = (set1 - set2) | (set2 - set1)
    unique_list = list(unique_set)
    return unique_list

if __name__ == '__main__':
    list1 = [1, 2, 2, 3, 4, 4, 5]
    list2 = [2, 2, 4, 3, 6, 4, 8]
    print(*unique_values(list1, list2))
    
