def titleize(a):
    c = [i.capitalize() for i in a.split(" ")]
    return " ".join(c)

def find_factors(a):
    return lambda i: i <= a; a % i == 0

#print(titleize('this is awesome'))
#print(titleize('oNLy cAPITALIZe fIRSt'))