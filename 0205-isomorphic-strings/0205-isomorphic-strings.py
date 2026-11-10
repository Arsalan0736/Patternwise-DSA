class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if n!=m:
            return False
        mappingS={}
        mappingT={}
        for i in range(n):
            charS=s[i]
            charT=t[i]
            if charS in mappingS:
                if mappingS[charS]!=charT:
                    return False
            else:
                mappingS[charS]=charT
            if charT in mappingT:
                if mappingT[charT]!=charS:
                    return False
            else:
                mappingT[charT]=charS
        return True