def list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}


lst = ["a", "b", "c"]
print(list_to_dict(lst))