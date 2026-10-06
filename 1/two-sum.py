class Solution1:
    '''
    暴力枚举
    遍历所有的数对，判断是否满足条件
    '''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i,a in enumerate(nums):
            for j in range(i+1,len(nums)):
                b=nums[j]
                if a+b == target:
                    return [i,j]

class Solution2:
    '''
    哈希表
    遍历数组，对于每个元素，检查目标值与该元素的差值是否在哈希表中
    '''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []


class Solution3:
    '''
    优化内存分布
    '''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            j = num_dict.get(complement)
            if j is not None:
                return [j, i]
            num_dict[num] = i
        return []