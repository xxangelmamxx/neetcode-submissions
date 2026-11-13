class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i in range(len(nums)):
            if nums[i] in temp:
                fin = [temp[nums[i]],i]
                return fin
            else:
                temp[target - nums[i]] = i
       
        