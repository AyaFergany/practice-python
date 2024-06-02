from itertools import permutations
inputt=input().split()
string,length=inputt[0],int(inputt[1])
[print("".join(i)) for i in sorted(list(permutations(string,length)))]


