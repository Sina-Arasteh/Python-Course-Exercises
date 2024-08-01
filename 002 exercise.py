def titleize(a):
    c = [i.capitalize() for i in a.split(" ")]
    return " ".join(c)

def find_factors(a):
    return lambda i: i <= a; a % i == 0



#print(titleize('this is awesome'))
#print(titleize('oNLy cAPITALIZe fIRSt'))

print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
print(find_factors(321421))
print(find_factors(412146))