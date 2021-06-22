def getPermutation(input_string: str) -> List[str]:
    permutations = []
    permutations.append(input_string)
    for i in range(len(input_string)):
        if input_string[i].isalpha():
            n = len(permutations)
            for j in range(n):
                new_permutation = list(permutations[j])
                new_permutation[i] = new_permutation[i].swapcase()
                permutations.append(''.join(new_permutation))
    return permutations
def test():
    print(getPermutation('aD54i3er'))

test()
