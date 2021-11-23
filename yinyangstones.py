import re
stones = input()
if (len(re.findall('B', stones))) == (len(re.findall('W', stones))):
    print(1)
else:
    print(0)