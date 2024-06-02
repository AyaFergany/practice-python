if __name__ == '__main__':
    elements_a = set(map(int, input().split()))
    n_sets = int(input())
    is_strict_superset = True
    for _ in range(n_sets):
        other_set = set(map(int, input().split()))
        if not elements_a.issuperset(other_set):
           is_strict_superset = False
    print(is_strict_superset)
            
            
    