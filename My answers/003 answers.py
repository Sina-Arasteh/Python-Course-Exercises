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
    """This function accepts two numbers and returns True if they contain the same frequency of digits. Otherwise, it returns False."""
    return len(str(num1)) == len(str(num2))

def nth(list, num):
    """This function accepts a list and a number and returns the element at whatever index is the in the list."""
    return list[num]

def find_the_duplicate(list):
    """This function accepts a list of numbers containing a single duplicate. The function returns the number which is a duplicate or None if there are no duplicates."""
    for i in list:
        a = list.count(i)
        if a > 1:
            return i
    return None



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

#The testing codes of the "same_frequency" function:
#print(same_frequency(551122,221515)) # True
#print(same_frequency(321142,3212215)) # False
#print(same_frequency(1212, 2211)) # True

#The testing codes of the "nth" function:
#print(nth(['a', 'b', 'c', 'd'], 1))  # 'b' 
#print(nth(['a', 'b', 'c', 'd'], -2)) #  'c'
#print(nth(['a', 'b', 'c', 'd'], 0))  # 'a'
#print(nth(['a', 'b', 'c', 'd'], -4)) #  'a'
#print(nth(['a', 'b', 'c', 'd'], -1)) #  'd'
#print(nth(['a', 'b', 'c', 'd'], 3))  # 'd'