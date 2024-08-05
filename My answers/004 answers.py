def sum_up_diagonals(list):
    a = sum([list[i][i] for i in range(len(list))])
    b = sum([list[i][-i-1] for i in range(len(list))])
    return a + b

def min_max_key_in_dictionary(dic):
    a = []
    a.append(min(dic))
    a.append(max(dic))
    return a




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