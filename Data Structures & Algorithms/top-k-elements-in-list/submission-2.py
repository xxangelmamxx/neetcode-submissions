class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        TempDict = {}
        arr =[0 for i in range(k)]

        for x in range(len(nums)):
            TempDict[nums[x]] = 1 + TempDict.get(nums[x],0)

        for i in range(k):
            largest_num = max(TempDict, key=TempDict.get)
            arr[i] = largest_num
            del TempDict[largest_num]

        return arr
        