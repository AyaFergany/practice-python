if __name__ == '__main__':
    num_cases = int(input())
    for i in range(0, num_cases):
       num_cases_a = int(input())
       a = set(map(int, input().split()))
       num_cases_b = int(input())
       b = set(map(int, input().split()))
       if num_cases_a > num_cases_b:
           print('False')
       else:
           a.difference_update(b)
           if len(a) == 0:
               print('true')
           else:  
               print('False')  


