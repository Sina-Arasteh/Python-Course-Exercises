def titleize(a):
    c = [i.capitalize() for i in a.split(" ")]
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
    elif n == 3:
        return "..."
    else:
        return a[:n-4] + "..."



#The testing codes of titleize function:
#print(titleize('this is awesome'))
#print(titleize('oNLy cAPITALIZe fIRSt'))

#The testing codes of find_factors function: 
#print(find_factors(10))
#print(find_factors(11))
#print(find_factors(111))
#print(find_factors(321421))
#print(find_factors(412146))

#The testing codes of includes function:
#print(includes([1, 2, 3], 1))
#print(includes([1, 2, 3], 1, 2))
#print(includes({ 'a': 1, 'b': 2 }, 1)) 
#print(includes({ 'a': 1, 'b': 2 }, 'a'))
#print(includes('abcd', 'b'))
#print(includes('abcd', 'e'))

#The testing codes of repeat function:
#print(repeat('*', 3))
#print(repeat('abc', 2))
#print(repeat('abc', 0))