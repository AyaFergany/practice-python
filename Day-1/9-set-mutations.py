num_elem_a = int(input())
set_a = set(map(int, input().split()))
num_oper = int(input())
for i in range(0, num_oper):
    entry = input().split()
    if entry[0] == 'intersection_update':
        set_a.intersection_update(set(map(int, input().split())))
    elif entry[0] == 'update':
        set_a.update(set(map(int, input().split())))
    elif entry[0] == 'difference_update':
        set_a.difference_update(set(map(int, input().split())))
    elif entry[0] == 'symmetric_difference_update':
        set_a.symmetric_difference_update(set(map(int, input().split())))
           
print(sum(set_a))

