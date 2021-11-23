text = input()
per = "PER"
while(len(per)<len(text)):
    per+=per
collisions = 0
for t, p in zip(text, per):
    if(t == p):
        continue
    else:
        collisions += 1
        
print(collisions)