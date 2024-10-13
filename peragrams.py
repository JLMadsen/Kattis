from collections import Counter
count = Counter([*(word := input())])
removed = sum([1 for c in count.values() if c%2!=0])
print(removed-(((len(word)-removed)%2==0)*1))