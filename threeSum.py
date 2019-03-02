#给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#注意：答案中不可以包含重复的三元组。

def threeSum(nums):
    L = len(nums)
    res = []
    if L > 2:
        nums.sort()
        for i in range(L - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lx = i + 1
            rx = L - 1
            for j in range(L - 2):
                ss = nums[i] + nums[lx] + nums[rx]
                if ss == 0:
                    res.append([nums[i], nums[lx], nums[rx]])
                    lx += 1
                    rx -= 1
                    while lx < rx and nums[lx] == nums[lx - 1]:
                        lx += 1
                    while lx < rx and nums[rx] == nums[rx - 1]:
                        rx -= 1
                elif ss < 0:
                    lx += 1
                    while lx < rx and nums[lx] == nums[lx - 1]:
                        lx += 1
                else:
                    rx -= 1
                    while lx < rx and nums[rx] == nums[rx - 1]:
                        rx -= 1
                if lx >= rx:
                    break
    return res
