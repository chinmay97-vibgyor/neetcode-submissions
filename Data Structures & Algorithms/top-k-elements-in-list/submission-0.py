class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1

        sorted_nums = sorted(freq, key= lambda x: freq[x], reverse=True)

        return sorted_nums[:k]
        