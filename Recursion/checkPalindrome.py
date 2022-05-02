def checkPalindrome(s,si,ei):
    if si >= ei:
        return True
    if s[si] != s[ei]:
        return False
    else:
        return checkPalindrome(s,si+1,ei-1)

s =input()
print(checkPalindrome(s,0,len(s)-1))
