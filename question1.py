class Solution(object): 
    # This fucntion takes in a list and uses a for loop to find the indices that add up to the target number
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i!=j:
                    if nums[i]+nums[j] == target:
                        return [i,j]