class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr={}
        first_index={}
        i=0
        for ele in s:
            if ele not in arr:
                arr[ele]=1
                first_index[ele]=i
            else:
                arr[ele]+=1
            i+=1
        for key,val in arr.items():
            if val==1:
                return first_index[key]
        return -1