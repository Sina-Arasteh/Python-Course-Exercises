def valid_parentheses(paren_string):
    count = 0
    for char in paren_string:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

def reverse_vowels(string):
    vowels = "aAeEiIoOuU"
    a = list(string)
    i , j = 0, len(a)-1
    while i < j:
        if a[i] not in vowels:
            i += 1
        elif a[j] not in vowels:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
    return "".join(a)


#The testing codes of the "valid_parentheses" function:
#print(valid_parentheses("()")) # True 
#print(valid_parentheses(")(()))")) # False 
#print(valid_parentheses("(")) # False 
#print(valid_parentheses("(())((()())())")) # True 
#print(valid_parentheses('))((')) # False
#print(valid_parentheses('())(')) # False
#print(valid_parentheses('()()()()())()(')) # False

#The testing codes of the "reverse_vowels" function:
print(reverse_vowels("Hello!")) # "Holle!" 
print(reverse_vowels("Tomatoes")) # "Temotaos" 
print(reverse_vowels("Reverse Vowels In A String")) # "RivArsI Vewols en e Streng"
print(reverse_vowels("aeiou")) # "uoiea"
print(reverse_vowels("why try, shy fly?")) # "why try, shy fly?"