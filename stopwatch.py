timestamps = [int(input()) for _ in range(int(input()))]
seconds = 0
running = False
prev = 0
for elapsed in timestamps:
    if running:
        seconds += int(elapsed) - int(prev)
    running = not running
    prev = elapsed
if running:
    print('still running')
else:
    print(seconds)