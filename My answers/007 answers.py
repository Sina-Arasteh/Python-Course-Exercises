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

def next_prime():
    num = 2
    value = 2
    while True:
        while value < num:
            if num % value == 0:
                num += 1
                value = 2
                continue
            value +=1
        yield num
        num += 1
        value = 2



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

#The testing codes of the "next_prime" function:
primes = next_prime()
print([next(primes) for i in range(25)]) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]