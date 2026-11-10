class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        curr=s
        n=len(curr)
        if n!=len(goal):
            return False
        for i in range(n):
            if curr==goal:
                return True
            curr=curr[-1]+curr[:-1]
        return False