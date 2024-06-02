if __name__ == '__main__':
    n = int(input())
    l = list(input().split())
    m = int(input())
    k = list(input().split())
    set1 = set(l)
    set2 = set(k)
    print(len(set1.difference(set2))+len(set2.difference(set1)))


    