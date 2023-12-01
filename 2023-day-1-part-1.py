sam = 0
for i in range(1000):
    w = input()
    nums = []
    for c in w:
        if c.isdigit():
            nums.append(c)
    sam += int(nums[0] + nums[-1])
print(sam)

