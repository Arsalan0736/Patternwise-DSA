class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        sort_freq=sorted(freq.items(), key=lambda item:item[1], reverse=True)
        return "".join([char*count for char,count in sort_freq])
        