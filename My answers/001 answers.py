def reverse_string(a):
    if type(a) != str:
        raise TypeError("Please insert a string.")
    return a[::-1]

def list_check(a):
    return all([type(value) == list for value in a])
#    for value in a:
#        if type(value) != list:
#            return False
#        return True

def remove_every_other(a):
    result = []
    for i in range(len(a)):
        if i % 2 == 0:
            result.append(a[i])
    return result

def sum_pairs(a, b):
    result = []
    g = 0
    for i in a:
        result.append(i)
        g += i
        if g == b:
            return result
    return []

def vowel_count(a):
    b = a.lower()
    dic = {}
    for i in b:
        if i in "aeiou":
            dic[i] = b.count(i)
    return dic



#The testing codes of the "reverse_string" function:
#print(reverse_string('awesome')) # 'emosewa'
#print(reverse_string('Colt')) # 'tloC'
#print(reverse_string('Elie')) # 'eilE'

#The testing codes of the "list_check" function:
#print(list_check([[], [1], [2,3], (1,2)])) # False
#print(list_check([1, True, [], [1], [2,3]])) # False
#print(list_check([[], [1], [2,3]])) # True

#The testing codes of the "remove_every_other" function:
#print(remove_every_other([1, 2, 3, 4, 5])) # [1, 3, 5] 
#print(remove_every_other([5, 1, 2, 4, 1])) # [5, 2, 1]
#print(remove_every_other([1])) # [1] 

#The testing codes of the "sum_pairs" function:
#print(sum_pairs([4,2,10,5,1], 6)) # [4,2]
#print(sum_pairs([11,20,4,2,1,5], 100)) # []

#The testing codes of the "vowel_count" function:
#print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1}
#print(vowel_count('Elie')) # {'e': 2, 'i': 1}
#print(vowel_count('Colt')) # {'o': 1}