from itertools import combinations
s, n = input().split()
sw=sorted(s)
[print(''.join(combo)) for i in range(1, int(n)+1) for combo in list(combinations(sw,i))]
 