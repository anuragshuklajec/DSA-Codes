class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            ans = [0]*26
            for c in s:
                ans[ord(c) - ord('a')] += 1
            res[tuple(ans)].append(s)
        
        return res.values()
    
