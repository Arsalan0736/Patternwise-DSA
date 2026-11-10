class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        curr=s+s
        if len(s)!=len(goal):
            return False
        if goal in curr:
            return True
        return False