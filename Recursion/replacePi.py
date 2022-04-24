def replacePi(s,a,b):
    l =len(s)
    if l == 0 or l == 1 :
        return s
    if s[0] + s[1] == a:
        return b + replacePi(s[2:],a,b)
    else:
        return s[0] + replacePi(s[1:],a,b)


s = input()
a = 'pi'
b = '3.14'
print(replacePi(s,a,b))
