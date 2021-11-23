import math
height, angle = input().split(" ")
height, angle = int(height), math.radians(int(angle))
minimum_length = height / math.sin(angle) + 0.99999999
minimum_length = int(minimum_length)
print(minimum_length)