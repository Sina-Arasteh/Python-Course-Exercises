def valid_parentheses(paren_string):
    count = 0
    for char in paren_string:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

def reverse_vowels(string):
    vowels = "aAeEiIoOuU"
    a = list(string)
    i , j = 0, len(a)-1
    while i < j:
        if a[i] not in vowels:
            i += 1
        elif a[j] not in vowels:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
    return "".join(a)

def three_odd_numbers(list_numbers):
    for num in range(len(list_numbers)-2):
        if (list_numbers[num]+list_numbers[num+1]+list_numbers[num+2]) % 2 != 0:
            return True
    return False

def mode(list_numbers):
    set_numers = set(list_numbers)
    b = 0
    most_frequent = 0
    for i in set_numers:
        a = list_numbers.count(i)
        if a > b:
            b = a
            most_frequent = i
    return most_frequent
    
def running_average():
    sum_nums = 0
    count = 0
    def average(num):
        nonlocal count
        count += 1
        nonlocal sum_nums
        sum_nums += num
        return round(sum_nums/count, 2)
    return average



#The testing codes of the "valid_parentheses" function:
#print(valid_parentheses("()")) # True 
#print(valid_parentheses(")(()))")) # False 
#print(valid_parentheses("(")) # False 
#print(valid_parentheses("(())((()())())")) # True 
#print(valid_parentheses('))((')) # False
#print(valid_parentheses('())(')) # False
#print(valid_parentheses('()()()()())()(')) # False

#The testing codes of the "reverse_vowels" function:
#print(reverse_vowels("Hello!")) # "Holle!" 
#print(reverse_vowels("Tomatoes")) # "Temotaos" 
#print(reverse_vowels("Reverse Vowels In A String")) # "RivArsI Vewols en e Streng"
#print(reverse_vowels("aeiou")) # "uoiea"
#print(reverse_vowels("why try, shy fly?")) # "why try, shy fly?"

#The testing codes of the "three_odd_numbers" function:
#print(three_odd_numbers([1,2,3,4,5])) # True
#print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
#print(three_odd_numbers([5,2,1])) # False
#print(three_odd_numbers([1,2,3,3,2])) # False

#The testing code of the "mode" function:
#print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4

#The testing codes of the "running_average" function:
#rAvg = running_average()
#print(rAvg(10)) # 10.0
#print(rAvg(11)) # 10.5
#print(rAvg(12)) # 11
#rAvg2 = running_average()
#print(rAvg2(1)) # 1
#print(rAvg2(3)) # 2