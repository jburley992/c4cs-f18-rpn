



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
            if x == '-':
                stack.append(v1 - v2)
            if x == '*':
                stack.append(v1 * v2)
            if x == '/':
                stack.append(v1 / v2)
    if len(stack) == 1:
        return stack[0]
    return None
def main():
    while True :
        calculate(input('rpn calc> '))

if __name__ == '__main__':
    main()