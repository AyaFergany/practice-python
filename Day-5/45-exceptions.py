T=int(input())
for i in range(T):
    try:
        a, b=map(int, input().split())
        result= int(a)//int(b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
    else:
        print(result)
 
