class Solution0:
    '''
    第一题思路：哈希表（字典）
    '''
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(numbers):
            complement = target - num
            j = num_dict.get(complement)
            if j is not None:
                return [j+1, i+1]
            num_dict[num] = i
        return []        

class Solution1:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum > target:
                right -= 1  
            elif sum < target:
                left += 1
            
        