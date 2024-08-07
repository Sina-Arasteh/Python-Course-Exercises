def letter_counter(string):
    def count(letter):
        return string.lower().count(letter)
    return count

def once(fn):
    count = 0
    def inner(a, b):
        nonlocal count
        if count == 0:
            count = 1
            return fn(a, b)
        else:
            return None
    return inner



#The testing codes of the "letter_counter" function:
#counter = letter_counter('Amazing')
#print(counter('a')) # 2
#print(counter('m')) # 1
#counter2 = letter_counter('This Is Really Fun!')
#print(counter2('i')) # 2
#print(counter2('t')) # 1

#The testing codes of the "once" function:
#def add(a,b):
#    return a+b
#oneAddition = once(add)
#print(oneAddition(2,2)) # 4
#print(oneAddition(2,2)) # None
#print(oneAddition(12,200)) # None