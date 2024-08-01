def titleize(a):
    b = a.split()
    c = [i.capitalize() for i in b]
    return " ".join(c)