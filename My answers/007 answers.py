def letter_counter(string):
    def count(letter):
        return string.count(letter)
    return count



#The testing codes of the "letter_counter" function:
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1
counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1