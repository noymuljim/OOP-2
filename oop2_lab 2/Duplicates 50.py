def remove_duplicates(lst):
    return list(set(lst))


lst = [1, 2, 3, 1, 2, 4, 4, 3, 5,5,5,5, 2, 1, 4]
print(remove_duplicates(lst))