def count_rotations(nums: List[int]) -> int:
    if not nums:
        return 0
    start, end = 0, len(nums)-1
    if nums[start] <= nums[end]:
        return 0
    while start + 1 < end:
        mid = (start + end)//2
        if nums[mid] >= nums[start]:
            start = mid
        else:
            end = mid
    if nums[start] < nums[end]:
        return start
    else:
        return end
def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()
