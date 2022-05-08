def parenthesis(s):
    d = {']':'[', ')':'(','}':'{'}
    stack = []
    for i in s:
        if i in '{[(':
            stack.append(i)
        if i in '}])':

            if not stack or stack.pop() != d[i]:
                return False
    return len(stack) == 0

s = input()

print(parenthesis(s))
