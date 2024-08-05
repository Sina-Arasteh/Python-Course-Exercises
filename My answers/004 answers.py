def sum_up_diagonals(list):
    a = sum([list[i][i] for i in range(len(list))])
    b = sum([list[i][-i-1] for i in range(len(list))])
    return a + b

def min_max_key_in_dictionary(dic):
    a = []
    a.append(min(dic))
    a.append(max(dic))
    return a

def find_greater_numbers(list):
    a = 0
    for i in list:
        for g in list[list.index(i):]:
            if i < g :
                a += 1
    return a

def two_oldest_ages(list):
    oldest = max(list)
    list.remove(oldest)
    return [max(list), oldest]

def is_odd_string(string):
    alphabet = " abcdefghijklmnopqrstubwxyz"
    string.lower()
    a = 0
    for char in string:
        a += alphabet.index(char)
    return a % 2 != 0



#The testing codes of the "sum_up_diagonals" function:
#list1 = [
#  [ 1, 2 ],
#  [ 3, 4 ]
#]
#print(sum_up_diagonals(list1)) # 10
#
#list2 = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
#]
#print(sum_up_diagonals(list2)) # 30
# 
#list3 = [
#  [ 4, 1, 0 ],
#  [ -1, -1, 0],
#  [ 0, 0, 9]#
#]
#print(sum_up_diagonals(list3)) # 11
#
#list4 = [
#  [ 1, 2, 3, 4 ],
#  [ 5, 6, 7, 8 ],
#  [ 9, 10, 11, 12 ],
#  [ 13, 14, 15, 16 ]
#]
#print(sum_up_diagonals(list4)) # 68

#The testing codes of the "min_max_key_in_dictionary" function:
#print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'})) # [1,10]
#print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"})) # [1,4]

#The testing codes of the "find_greater_numbers" function:
#print(find_greater_numbers([1,2,3])) # 3 
#print(find_greater_numbers([6,1,2,7])) # 4
#print(find_greater_numbers([5,4,3,2,1])) # 0
#print(find_greater_numbers([])) # 0

#The testing codes of the "two_oldest_ages" function:
#print(two_oldest_ages( [1, 2, 10, 8] )) # [8, 10]
#print(two_oldest_ages( [6,1,9,10,4] )) # [9,10]
#print(two_oldest_ages( [4,25,3,20,19,5] )) # [20,25]

#The testing codes of the "is_odd_string" function:
print(is_odd_string('a')) # True
print(is_odd_string('aaaa')) # False
print(is_odd_string('amazing')) # True
print(is_odd_string('veryfun')) # True
print(is_odd_string('veryfunny')) # False