



def calculate(arg):
    tokens = ['+','-','*','/']
    stack = []
    arg = arg.split()
    for x in arg:
        try:
            stack.append(int(x))
        except ValueError:
            v2 = stack.pop()
            v1 = stack.pop()
            if x == '+':
                stack.append(v1 + v2)
            elif x == '-':
                stack.append(v1 - v2)
            elif x == '*':
                stack.append(v1 * v2)
            elif x == '/':
                stack.append(v1 / v2)
    if len(stack) == 1:
        return stack[0]
    raise ValueError("Too many arguments on stack")
def main():
    while True :
        try:
            calculate(input('rpn calc> '))
        except ValueError:
            pass

if __name__ == '__main__':
    main()