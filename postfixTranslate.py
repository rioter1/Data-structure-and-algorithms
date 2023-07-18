from simpleStack import Stack
from queue import Queue
# Define operators and their precedence
# We group single character operators of equal precedence in strings
# Lowest precedence is on the left; highest on the right
# Parentheses are treated as high precedence operators
operators = ["|", "&", "+-", "*/%", "^", "()"]
def precedence(operator): # Get the precedence of an operator
    for p, ops in enumerate(operators): # Loop through operators
        if operator in ops:
        # If found,
            return p + 1
        # return precedence (low = 1)
        # else not an operator, return None
def delimiter(character): # Determine if character is delimiter
    return precedence(character) == len(operators)

def nextToken(s):
    # Parse next token from input string
    token = ""
    # Token is operator or operand
    s = s.strip()
    # Remove any leading & trailing space
    if len(s) > 0:
        # If not end of input
        if precedence(s[0]): # Check if first char. is operator
            token = s[0]
            # Token is a single char. operator
            s = s[1:]
        else:
            # its an operand, so take characters up
            while len(s) > 0 and not (
                # to next operator or space
                    precedence(s[0]) or s[0].isspace()):
                token += s[0]
                s = s[1:]
    return token, s # Return the token, and remaining input string