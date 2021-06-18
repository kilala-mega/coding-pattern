def findFirstKMissingPositive(nums: List[int], k: int)-> List[int]:
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]-1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    missing_nums = []
    extra_nums = set()
    
    print(nums)
    for i in range(n):
        if len(missing_nums) < k:
            if nums[i] != i+1:
                missing_nums.append(i+1)
                extra_nums.add(nums[i])

    i = 1
    while len(missing_nums) < k:
        if n+i not in extra_nums:
            missing_nums.append(n+i)
        i += 1
    
    return missing_nums
    
print(findFirstKMissingPositive([4,5,-1,6,9],4)) # [1 2 3 7]
