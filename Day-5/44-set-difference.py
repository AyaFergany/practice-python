if __name__ == '__main__':
    n = int(input())
    l = input().split()
    m = int(input())
    k = input().split()
    set1 = set(l)
    set2 = set(k)
    print(len(set1.difference(set2)))

    
