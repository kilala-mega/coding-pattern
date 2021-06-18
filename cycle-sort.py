def cycleSort(nums: List[int]) -> List[int]:
    index = 0
    while index < len(nums):
        j = nums[index]-1
        # it's better to use the condition nums[index] != nums[j]
        # rather than comparing j and i directly
        # o.w. the algo might infinite loop to detect duplicates
        if nums[index] != nums[j]:
            nums[index], nums[j] = nums[j], nums[index]
        else:
            index += 1
    return nums

print(cycleSort([4,1,2,5,3]))
