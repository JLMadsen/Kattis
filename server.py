N, T = map(int, input().split())
tasks = [int(x) for x in input().split()]
done = 0
time = 0
for t in tasks:
  time += t
  if time > T:
    break
  done += 1
# print(sum(tasks[:done]))
print(done)