t, n = map(int, input().split(' '))
songs = sorted(map(int, input().split(' ')))

counter = 0

for time in songs:
    if (counter + time) / 60 < t: 
        counter += time

print(counter)