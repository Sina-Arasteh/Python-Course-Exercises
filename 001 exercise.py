def reverse_string(a):
    if type(a) != str:
        raise TypeError("Please insert a string.")
    return a[::-1]

print(reverse_string("Hello World!!!"))
print(reverse_string(54))