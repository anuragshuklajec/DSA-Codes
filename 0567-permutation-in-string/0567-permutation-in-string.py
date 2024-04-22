class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d = {}
        for i in s1:
            d[i] = d.get(i, 0) + 1
        for j in range(len(s2)-len(s1) + 1):
            if s2[j] in d:
                total = len(s1)
                temp_d = d.copy()
                l = j
                r = j
                while r < len(s2):
                    if temp_d.get(s2[r], 0) > 0:
                        temp_d[s2[r]] = temp_d.get(s2[r], 0) - 1
                        total -= 1
                        r += 1
                    else:
                        break
                    if total == 0:
                        return True
        return False
            


                