'''
Your job is to create a calculator which evaluates expressions in
Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent
to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

Note that for simplicity you may assume that there are always spaces between
numbers and operations, e.g. 1 3 + expression is valid, but 1 3+ isn't.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack
underflow or division by zero).
'''


def calc(expr):
    operators = ['+', '-', '*', '/']
    stack = list()
    for item in expr.split(' '):
        if item in operators:
            #right, left = map(str, (stack.pop(), stack.pop()))
            right, left = [str(i) for i in (stack.pop(), stack.pop())]
            stack.append(eval(left + item + right))
        else:
            stack.append(eval(item + '+ 0'))

    return stack[-1]


print calc(""), 0, "Should work with empty string"
print calc("1 2 3"), 3, "Should parse numbers"
print calc("1 2 3.5"), 3.5, "Should parse float numbers"
print calc("1 3 +"), 4, "Should support addition"
print calc("1 3 *"), 3, "Should support multiplication"
print calc("1 3 -"), -2, "Should support subtraction"
print calc("4 2 /"), 2, "Should support division"
