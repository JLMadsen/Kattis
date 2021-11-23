while 1:
    n = int(input())
    if n == 0:
        break
    list1 = [int(input()) for _ in range(n)]
    list2 = [int(input()) for _ in range(n)]
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)
    for item in list1:
        print(list2_sorted[ list1_sorted.index(item) ] )