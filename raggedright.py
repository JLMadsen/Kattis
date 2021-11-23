lines = []
while(True):
    try:
        lines.append(len(input()))
    except:
        break
penalty = 0
longest = 0
for line in lines:
    if line > longest:
        longest = line
for a in range(len(lines)-1):
    penalty += (longest-lines[a])*(longest-lines[a])
print(penalty)