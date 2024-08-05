def valid_parentheses(paren_string):
    if len(paren_string) % 2 != 0:
        return False
    else:
        for char in paren_string:
            if char == "(" and paren_string.index(char) % 2 != 0:
                return False
            if char == ")" and paren_string.index(char) % 2 == 0:
                return False
        return True



#The testing codes of the "valid_parentheses" function:
print(valid_parentheses("()")) # True 
print(valid_parentheses(")(()))")) # False 
print(valid_parentheses("(")) # False 
print(valid_parentheses("(())((()())())")) # True 
print(valid_parentheses('))((')) # False
print(valid_parentheses('())(')) # False
print(valid_parentheses('()()()()())()(')) # False