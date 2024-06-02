n, list1 = int(input()), list(map(int, input().split()))
print(all([(x>0) for x in list1]) and any([str(x)==str(x)[::-1] for x in list1]))


