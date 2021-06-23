def find_max_in_bitonic_array(nums: List[int]) -> int:
    if not nums:
        return -1
    start, end = 0, len(nums)-1
    while start + 1 < end:
        mid = (start + end)//2
        if mid == len(nums)-1 or nums[mid] > nums[mid+1]:
            end = mid
        else:
            start = mid
    if nums[start] > nums[end]:
        return nums[start]
    else:
        return nums[end]
def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()
