def titleize(a):
    g = a.split(" ")
    c = [i[0].upper()+i[1:] for i in g]
    return " ".join(c)

def find_factors(a):
    return list(filter(lambda i: a % i == 0, range(1, a+1)))

def includes(a, b, c=0):
    if type(a) != dict:
        d = a[c:]
        return b in d
    else:
        return b in a.values()

def repeat(a, b):
    return a * b

def truncate(a, n):
    if n < 3:
        raise ValueError("Truncation must be at least 3 characters.")
    else:
        if n > len(a):
            return a[:n-3]
        else:
            return a[:n-3] + "..."



#The testing codes of the "titleize" function:
#print(titleize('this is awesome')) # "This Is Awesome"
#print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"

#The testing codes of the "find_factors" function:
#print(find_factors(10)) # [1, 2, 5, 10]
#print(find_factors(11)) # [1, 11]
#print(find_factors(111)) # [1, 3, 37 ,111]
#print(find_factors(321421)) # [1, 293, 1097, 321421]
#print(find_factors(412146)) # [1, 2, 3, 6, 7, 9, 14, 18, 21, 42, 63, 126, 3271, 6542, 9813, 19626, 22897, 29439, 45794, 58878, 68691, 137382, 206073, 412146]

#The testing codes of the "includes" function:
#print(includes([1, 2, 3], 1)) # True
#print(includes([1, 2, 3], 1, 2)) # False
#print(includes({'a': 1, 'b': 2}, 1)) # True
#print(includes({'a': 1, 'b': 2}, 'a')) # False
#print(includes('abcd', 'b')) # True
#print(includes('abcd', 'e')) # False

#The testing codes of the "repeat" function:
#print(repeat('*', 3)) # '***'
#print(repeat('abc', 2)) # 'abcabc'
#print(repeat('abc', 0)) # ''

#The testing codes of the "truncate" function:
#print(truncate("Super cool", 2)) # "Truncation must be at least 3 characters."
#print(truncate("Super cool", 1)) # "Truncation must be at least 3 characters."
#print(truncate("Super cool", 0)) # "Truncation must be at least 3 characters."
#print(truncate("Hello World", 6)) # "Hel..."
#print(truncate("Problem solving is the best!", 10)) # "Problem..."
#print(truncate("Another test", 12)) # "Another t..."
#print(truncate("Woah", 4)) # "W..."
#print(truncate("Woah", 3)) # "..."
#print(truncate("Yo", 100)) # "Yo"
#print(truncate("Holy guacamole!", 152)) # "Holy guacamole!"