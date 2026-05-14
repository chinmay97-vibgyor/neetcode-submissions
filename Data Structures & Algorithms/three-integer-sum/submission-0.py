class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, fixed_val in enumerate(nums):
            if fixed_val > 0:
                break
            
            if i>0 and fixed_val == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while l<r:
                if (fixed_val+nums[l]+nums[r])>0:
                    r=r-1
                elif (fixed_val+nums[l]+nums[r])<0:
                        l=l+1
                else:
                    res.append([fixed_val,nums[l],nums[r]])
                    l=l+1
                    r=r-1

                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
        
        return res
        