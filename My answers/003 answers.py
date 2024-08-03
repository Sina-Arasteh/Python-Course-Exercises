def two_list_dictionary(list1, list2):
    if len(list1) == len(list2):
        return {list1[i]: list2[i] for i in range(len(list1))}
    elif len(list1) > len(list2):
        dic = {list1[i]: list2[i] for i in range(len(list2))}
        for num in range(len(list2), len(list1)):
            dic.update({list1[num]: None})
        return dic
    else:
        return {list1[i]: list2[i] for i in range(len(list1))}



#The test codings of the "two_list_dictionary" function:
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4])) # {'a': 1, 'b': 2, 'c': 3}
print(two_list_dictionary(['x', 'y', 'z']  , [1,2])) # {'x': 1, 'y': 2, 'z': None}