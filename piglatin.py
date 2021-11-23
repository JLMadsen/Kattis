sentances = []
while(True):
    try:
        sentances.append(input())
    except:
        break
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for sentance in sentances:
    words = sentance.split(" ")
    result = ""
    for word in words:
        if word[0] not in vowels:
            first_vowel = 0
            for j in range(len(word)):
                if word[j] in vowels:
                    first_vowel = j
                    break
            result += word[first_vowel:] + word[0:first_vowel] + "ay "
        else:
            result += word +"yay " 
    print(result)