class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            while d.get(s[r],0) > 0:
                d[s[l]] = d.get(s[l],0) - 1
                l+=1
            d[s[r]] = 1
            ans = max(ans,r-l + 1)
        return ans

            
        # for i in range(len(s)):
        #     d[s[i]] = 1
        #     count = 1
        #     for j in range(i + 1, len(s)):
        #         if s[j] in d:
        #             ans = max(ans, count)
        #             d = {}
        #             break
        #         else:
        #             count += 1
        #             ans = max(ans, count)
        #             d[s[j]] = 1
        #     ans = max(count, ans)
        # return ans

                
        