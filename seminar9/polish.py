#zalupa

def priority(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0

def normal_to_rpolish(str):
    stack = []
    output = ""
    for symbol in str:
        if symbol.isalnum():
            output += symbol
        elif symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            while stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and priority(symbol) <= priority(stack[-1]):
                output += stack.pop()
            stack.append(symbol)
    while stack:
        output += stack.pop()
    return output

def normal_to_dpolish(str):
    stack = []
    output = ''
    for symbol in str[::-1]:
        if symbol.isalnum():
            output += symbol
        elif symbol == ')':
            stack.append(symbol)
        elif symbol == '(':
            while stack and stack[-1] != ')':
                output += stack.pop()
            stack.pop()
        else:
            while stack and priority(symbol) <= priority(stack[-1]):
                output += stack.pop()
            stack.append(symbol)
    while stack:
        output += stack.pop()

    return output[::-1]

str='(3+4*(2-1))/5'
print(normal_to_rpolish(str))
print(normal_to_dpolish(str))
