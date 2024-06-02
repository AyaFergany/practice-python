students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

a = [[student[0], student[1]] for student in students]
s = sorted(set([x[1] for x in a]))
for name in sorted(x[0] for x in a if x[1]==s[1]):
    print(name)
