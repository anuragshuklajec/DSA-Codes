def replaceChar(s,a,b):
    if len(s) == 0:
        return s
    smallOutput = replaceChar(s[1:],a,b)
    if s[0] == a:
        return b + smallOutput
    else:
        return s[0] + smallOutput 

s = input()
a =input()
b =input()
print(replaceChar(s,a,b))
