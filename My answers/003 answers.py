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

