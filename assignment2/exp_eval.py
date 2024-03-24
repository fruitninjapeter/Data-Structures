from Stack_Revised import *

operators = {'+', '-', '*', '/', '(', ')', '^'}  # set of operators
priority = {"(": 1, "-": 2, "+": 2, "/": 3, "*": 3, "^": 4}  # dictionary of priorities (PEMDAS)

def infix_to_postfix(infixexpr):  # Converts string of infix expression to an equivalent postfix expression
    # Signature:  a string containing an infix expression where tokens are space separated is
    # the single input parameter and returns a string containing a postfix expression where tokens are space separated
    stack = Stack(30)   # initialize stack with capacity 30, stack holds all operands
    infix = infixexpr.split()  # splits infix expression string into list of characters
    postfix = []    # initialize empty.txt postfix list
    for ch in infix:    # for loop going through each character in the expression
        if ch not in operators:  # if we have an operand
            postfix.append(ch)  # put operands in postfix list
        elif ch in '(^':  # if we have parenthesis operator or if we have exponent, exponent evaluated starting
            # from the right side
            stack.push(ch)
        elif ch == ')':
            topchar = stack.pop()
            while topchar != '(':   # pop the stack until we get the other parenthesis
                postfix.append(topchar)
                topchar = stack.pop()
        else:   # if we have an operator
            while (stack.is_empty() is False) and (priority[ch] <= priority[stack.peek()]):
                postfix.append(stack.pop)
            stack.push(ch)
    while stack.is_empty() is False:  # pop all elements into postfix list
        postfix.append(stack.pop())
    return " ".join(postfix)    # make postfix list into string again

def postfix_eval(postfixExpr):  # Evaluates what the postfix expression is, uses doMath
    stack = Stack(30)   # this stack holds operands
    postfix = postfixExpr.split()  # splits string into a list of characters
    for ch in postfix:
        if ch not in operators:  # if character isn't an operator
            stack.push(float(ch))
        else:   # if character is an operator
            op2 = stack.pop()   # pop operand 2 first, because stack holds 2nd operand then 1st operand
            op1 = stack.pop()
            result = doMath(ch, op1, op2)
            stack.push(float(result))
    return stack.pop()

def doMath(op, op1, op2):  # evaluates the expression given two operands and one operator
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        if op2 == 0:
            raise ValueError
        else:
            return op1 / op2
    elif op == "^":
        return op1 ** op2
    else:
        raise("No operand here")

def postfix_valid(postfixexpr):  # given postfix string, determines if it is valid by counting operands and operators
    postfix = postfixexpr.split()   # splits string into a list of characters
    num_operands = 0
    num_operators = 0

    if len(postfix) == 0:   # if we have no postfix string
        return False
    if len(postfix) == 1:   # if we have one element
        if postfix[0] in operators:
            return False
        else:
            return True
    if postfix[0] in operators or postfix[1] in operators:  # first two elements have to be operands
        return False
    else:
        num_operands = 2
    for ch in postfix[2:len(postfix)]:  # consider the rest of the elements
        if ch in operators:
            num_operators += 1
        else:
            num_operands += 1
        if num_operands - num_operators < 1:
            return False
    if num_operands - num_operators != 1:
        return False
    return True