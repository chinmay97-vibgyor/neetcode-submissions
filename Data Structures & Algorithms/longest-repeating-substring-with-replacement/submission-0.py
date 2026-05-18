class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        charSet = set(s)

        for x in charSet:
            count = 0
            l=0

            for r in range(len(s)):
                if s[r] == x:
                    count=count+1
                
                while (r-l+1) - count >k:
                    if s[l] == x:
                        count = count-1
                    l=l+1
                
                res = max(res, r-l+1)
        return res