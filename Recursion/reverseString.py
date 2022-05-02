def reverseString(s,si,ei):
    if si > ei:
        return ''
    return reverseString(s,si+1,ei) + s[si]

s = input()
print(reverseString(s,0,len(s)-1))
