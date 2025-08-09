Input = [2, 2, 7, 11, 15]
Target = 4
Output = [0, 1]

def two_sum(nums, target):
    if nums is None:
        return []
    
    nums_dict = {}
    for i in range(len(nums)):
        nums_dict[nums[i]] = i

    for i in range(len(nums)):
        des = target - nums[i]
        if des in nums_dict and nums_dict[des] != i:
            return [i, nums_dict[des]]

    return []

print(two_sum(Input, Target))