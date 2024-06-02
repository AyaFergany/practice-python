if __name__=='__main__':
    N_customers=int(input())
    lst=list(map(int, input().strip().split()))
    total_price=0
    for i in range(int(input())):
        size, price=input().strip().split()
        if int(size) in lst:
            total_price += int(price)
            lst.remove(int(size))
print(total_price)            
    
