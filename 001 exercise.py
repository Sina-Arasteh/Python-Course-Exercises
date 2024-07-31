def reverse_string(a):
    if type(a) != str:
        raise TypeError("Please insert a string.")
    return a[::-1]

def list_check(a):
    for value in a:
        if type(value) != list:
            return False
        return True

print(reverse_string("Hello World!!!"))
print(reverse_string(54))