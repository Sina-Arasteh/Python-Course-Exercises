def letter_counter(string):
    def count(letter):
        return string.lower().count(letter)
    return count



#The testing codes of the "letter_counter" function:
#counter = letter_counter('Amazing')
#print(counter('a')) # 2
#print(counter('m')) # 1
#counter2 = letter_counter('This Is Really Fun!')
#print(counter2('i')) # 2
#print(counter2('t')) # 1