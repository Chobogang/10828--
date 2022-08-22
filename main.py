import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n) :
    case = sys.stdin.readline().split()
    if case[0] == "push" :
        stack.append(int(case[1]))
    elif case[0] == "pop" :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    elif case[0] == "size" :
        print(len(stack))
    elif case[0] == "empty" :
        if len(stack) == 0 :
            print(1)
        else : print(0)
    elif case[0] == "top" :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])