nums1 = [1, 3]
nums2 = [2]


def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2) #Tim sort because nums1 and nums2 already sort
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        return nums[n // 2]
    
print(find_median_sorted_arrays(nums1, nums2))