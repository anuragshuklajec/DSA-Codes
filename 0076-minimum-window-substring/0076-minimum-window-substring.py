class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t

        countT,window = {},{}
        for i in t: countT[i] = countT.get(i, 0) + 1
        l = 0
        have,need = 0,len(set(t))
        res,resLen = [-1,-1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in countT and window[c] == countT[c]:
                have+=1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l,r]

                # pop from left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
            
        