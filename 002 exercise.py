def titleize(a):
    c = [i.capitalize() for i in a.split(" ")]
    return " ".join(c)

def find_factors(a):
    return list(filter(lambda i: a % i == 0, range(1, a+1)))

def includes():



#titleize's testing codes:
#print(titleize('this is awesome'))
#print(titleize('oNLy cAPITALIZe fIRSt'))

#find_factors' testing codes: 
#print(find_factors(10))
#print(find_factors(11))
#print(find_factors(111))
#print(find_factors(321421))
#print(find_factors(412146))