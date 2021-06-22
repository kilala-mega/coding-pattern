def search_next_letter(letters: List[str], target: str) -> str:
    if not letters:
        return ""
    start, end = 0, len(letters)-1
    while start + 1 < end:
        mid = (start + end)//2
        if letters[mid] <= target:
            start = mid
        else:
            end = mid
    if letters[start] > target:
        return letters[start]
    elif letters[end] > target:
        return letters[end]
    else:
        return letters[0]
def test():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


test()
