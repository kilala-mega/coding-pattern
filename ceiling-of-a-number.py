def ceiling_binary_search(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    start, end = 0, len(nums)-1
    while start + 1 < end:
        mid = (start + end)//2
        if nums[mid] >= target:
            end = mid
        else:
            start = mid
    
    if nums[start] >= target:
        return start
    elif nums[end] >= target:
        return end
    else:
        return -1

def test():
    print(ceiling_binary_search([1,4,8,9],5))
    print(ceiling_binary_search([1,4,8,9],4))
    print(ceiling_binary_search([1,4,8,9],10))
    print(ceiling_binary_search([],5))

test()
