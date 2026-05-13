class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest_seq = 0

        for x in num_set:
            if (x-1) not in num_set:
                length = 1

                while (x+length) in num_set:
                    length= length+1
                longest_seq = max(length, longest_seq)
        
        return longest_seq
        