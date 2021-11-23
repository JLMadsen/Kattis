import re
cards = re.findall('\w\d\d', input())
suits = [[],[],[],[]]
index = ['P','K','H','T']
for card in cards:
    for suit in suits:
        if card in suit:
            print("GRESKA")
            exit()
    suits[index.index(card[0])].append(card)
length = 13
result = ""
for suit in suits:
    result += str(length-len(suit)) +" "
print(result)