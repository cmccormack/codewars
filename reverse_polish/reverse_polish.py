def calc(expr):
    operators = ['+', '-', '*', '/']
    stack = list()
    for item in expr.split(' '):
        if item in operators:
            right, left = [str(i) for i in (stack.pop(), stack.pop())]
            stack.append(eval(left + item + right))
        else:
            stack.append(eval(item + '+ 0'))

    return stack[-1]


# Test Cases
print calc(""), 0, "Should work with empty string"
print calc("1 2 3"), 3, "Should parse numbers"
print calc("1 2 3.5"), 3.5, "Should parse float numbers"
print calc("1 3 +"), 4, "Should support addition"
print calc("1 3 *"), 3, "Should support multiplication"
print calc("1 3 -"), -2, "Should support subtraction"
print calc("4 2 /"), 2, "Should support division"
