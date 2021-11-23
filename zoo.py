lists = 1
while(True):
    n = int(input())
    if n == 0:
        exit()
    print("List "+ str(lists)+":")
    lists += 1
    animals = []
    count = []
    for g in range(n):
        #print(animals, count)
        animal = input().split(" ")
        animal = animal[len(animal)-1].lower()
        if animal in animals:
            count[animals.index(animal)] += 1
        else:
            animals.append(animal)
            count.append(1)
    for i in range(len(animals)):
        highest = i
        for j in range(i, len(animals)):
            if animals[highest] > animals[j]:
                highest = j
        animals[highest], animals[i] = animals[i], animals[highest]
        count[highest], count[i] = count[i], count[highest]
    for animal, cou in zip(animals, count):
        print(animal, "|", cou)