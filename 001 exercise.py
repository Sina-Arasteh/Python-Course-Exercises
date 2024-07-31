def reverse_string(a):
    if type(a) != str:
        raise TypeError("Please insert a string.")
    return a[::-1]

def list_check(a):
    for value in a:
        if type(value) != list:
            return False
        return True



#print(reverse_string("Hello World!!!"))
#print(reverse_string(54))

print(list_check([[],[1],[2,3], (1,2)]))
print(list_check([1, True, [],[1],[2,3]]))
print(list_check([[],[1],[2,3]]))