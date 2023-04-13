test_cases = [
    "()",
    "((()))",
    "(()()()()()()",
    "(()(())"
]

def valid_parenthesis(parens):
    #return True if valid parenthesis
    #return False if unpaired parenthesis
    #count the opens
    #count the closes
    #for each character in the string
    open_paren_count = 0

    for paren in parens:
        if paren == "(":
            open_paren_count += 1
        if paren == ")":
            open_paren_count -= 1

        if open_paren_count <0:
            return False
        
    return open_paren_count == 0

print([valid_parenthesis(t) for t in test_cases])