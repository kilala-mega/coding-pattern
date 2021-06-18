def cycleSort(nums: List[int]) -> List[int]:
    index = 0
    while index < len(nums):
        j = nums[index]-1
        if j != index:
            nums[index], nums[j] = nums[j], nums[index]
        else:
            index += 1
    return nums

print(cycleSort([4,1,2,5,3]))
