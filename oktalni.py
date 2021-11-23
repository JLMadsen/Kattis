import re
bin = input()
bins = ['000', '001','010', '011', '100', '101', '110', '111']
reals = ['0','1','2','3','4','5','6','7']
while len(bin) % 3 != 0:
    bin = '0' + bin
result = ""
for number in re.findall('...', bin):
    result += reals[bins.index(number)]
print(result)