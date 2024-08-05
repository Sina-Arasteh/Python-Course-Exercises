def two_list_dictionary(list1, list2):
    """This function accepts two lists of varying lengths. The first list consists of keys and the second one consists of values. This function returns a dictionary created from the keys and values."""
    if len(list1) == len(list2):
        return {list1[i]: list2[i] for i in range(len(list1))}
    elif len(list1) > len(list2):
        dic = {list1[i]: list2[i] for i in range(len(list2))}
        for num in range(len(list2), len(list1)):
            dic.update({list1[num]: None})
        return dic
    else:
        return {list1[i]: list2[i] for i in range(len(list1))}

def range_in_list(lst, start=0, end=None):
    """This function accepts a list and start and end indices, and returns the sum of the values between (and including) the start and end index."""
    if end != None:
        return sum(lst[start:end+1])
    else:
        return sum(lst[start:])

def same_frequency(num1, num2):
    return len(str(num1)) == len(str(num2))


#The testing codes of the "two_list_dictionary" function:
#print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
#print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4])) # {'a': 1, 'b': 2, 'c': 3}
#print(two_list_dictionary(['x', 'y', 'z']  , [1,2])) # {'x': 1, 'y': 2, 'z': None}

#The testing codes of the "range_in_list" function:
#print(range_in_list([1,2,3,4],0,2)) #  6
#print(range_in_list([1,2,3,4],0,3)) # 10
#print(range_in_list([1,2,3,4],1)) #  9
#print(range_in_list([1,2,3,4])) # 10
#print(range_in_list([1,2,3,4],0,100)) # 10
#print(range_in_list([],0,1)) # 0