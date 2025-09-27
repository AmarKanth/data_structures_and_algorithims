"""
Find the subsets of given list 
nums = [1,3]
"""
def find_subsets(nums):
    def backtrack(start, path):
        subsets.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    subsets = []
    backtrack(0, [])
    return subsets

nums = [1, 3]
print(find_subsets(nums))