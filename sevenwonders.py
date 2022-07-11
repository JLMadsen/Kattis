types = ['T', 'C', 'G']
n_types = []
points = 0
hand = input()

for t in types:
  count = hand.count(t)
  points += count**2
  n_types.append(count)

points += 7 * min(n_types)

print(points)