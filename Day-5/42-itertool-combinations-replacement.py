from itertools import combinations_with_replacement
s, n = input().split()
sw=sorted(s)
[print(''.join(combo)) for combo in list(combinations_with_replacement(sw, int(n)))]
 