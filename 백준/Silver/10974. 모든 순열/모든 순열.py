def permute(nums):
    res = []
    generate_permute(nums, [], res)
    return res

def generate_permute(remaining_nums, current_permutation, res):
    if not remaining_nums:
        res.append(current_permutation[:])
        return

    for i in range(len(remaining_nums)):
        current_permutation.append(remaining_nums[i])
        generate_permute(remaining_nums[:i] + remaining_nums[i+1:], current_permutation, res)
        current_permutation.pop()


n = int(input())

nums = []

for i in range(1, n+1):
    nums.append(i)

res = permute(nums)

for i in res:
    print(" ".join(map(str, i)))