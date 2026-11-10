class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        letter = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        res=0
        for i in range(n):
            if i < n-1 and letter[s[i]] < letter[s[i+1]]:
                res -= letter[s[i]]
            else:
                res += letter[s[i]]
        return res
