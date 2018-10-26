



def calculate(arg):
    tokens = ['+','-','*','/']
    stack = []
    arg = arg.split()
    for x in arg:
        try:
            stack.append(int(x))
        except ValueError:
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 + v2)
    return stack[0]
def main():
    while True :
        calculate(input('rpn calc> '))

if __name__ == '__main__':
    main()