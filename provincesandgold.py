g, s, c = input().split(" ")
buying_power = (int(g)*3)+(int(s)*2)+(int(c)*1)
#print(buying_power)
victory = {"Province": 8, "Duchy": 5, "Estate": 2}
treasure = {"Gold": 6, "Silver": 3, "Copper": 0}
buy = ""
for card, value in victory.items():
    if buying_power >= value:
        buy += card + " or "
        break
for coin, value in treasure.items():
    if buying_power >= value:
        buy += coin
        break
        
print(buy)