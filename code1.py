
def dfs(nums,k):
    if k==1:
        return max(nums[0],nums[-1])
    left = nums.pop(0)
    la =dfs(nums,k-1)
    la += left
    nums.insert(0,left)
    right = nums.pop()
    ra = dfs(nums,k-1)
    ra+=right
    nums.append(right)
    return max(ra,la)
print(dfs([2,2,2], k = 2))