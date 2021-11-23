nums = sorted(list(map(int, input().split())))
order = input()
out = ""
for c in order:
    idx = ord(c) - 65
    out += str(nums[idx]) + " "
print(out)