def reorganize_string(original_string: str, k: int) -> str:
    if k <= 1:
        return original_string
    freq_map = Counter(list(original_string))
    
    maxheap = []
    for char, freq in freq_map.items():
        heappush(maxheap, (-freq, char))
    
    result_string = ""
    queue = deque()
    while maxheap:
        neg_freq, char = heappop(maxheap)
        result_string += char
        queue.append((char, neg_freq+1))
        if len(queue) >= k:
            char_to_push, neg_freq_to_push = queue.popleft()
            if -neg_freq_to_push > 0:
                heappush(maxheap, (neg_freq_to_push, char_to_push))
    return result_string if len(result_string) == len(original_string) else ""
        
def main():
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()
