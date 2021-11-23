nums = [int(input()) for _ in range(10)]
mods = set()
for idx in range(len(nums)):
    mod = nums[idx] % 42
    mods.add(mod)
print(len(mods))