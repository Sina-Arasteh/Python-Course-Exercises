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
    return [i for i in a if a.index(i) % 2 == 0]

#print(reverse_string("Hello World!!!"))
#print(reverse_string(54))

#print(list_check([[], [1], [2, 3], (1, 2)]))
#print(list_check([1, True, [], [1], [2, 3]]))
#print(list_check([[], [1], [2, 3]]))

print(remove_every_other([1,2,3,4,5]))
print(remove_every_other([5,1,2,4,1]))
print(remove_every_other([1]))
