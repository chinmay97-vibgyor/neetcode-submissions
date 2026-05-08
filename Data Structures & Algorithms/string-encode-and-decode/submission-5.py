class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s))+"~"+s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res_str = []
        i=0
        while i<len(s):
            j=i
            while i<=j and s[j]!="~":
                j=j+1
            length=int(s[i:j])
            wrd= s[j+1: j+1+length]
            res_str.append(wrd)
            i = j+1+length
        return res_str

                

