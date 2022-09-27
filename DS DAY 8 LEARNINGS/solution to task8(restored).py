"""
solution from trainer :
    
T = int(input())

for i in range(T):
    a,b = map(str,input().strip().split())

    try:
       divide = print(int(a)//int(b))
        
    except Exception as e:
        print("Error Code:",e)
        
    else :
        print ("Your solution is : ",divide )
    
    finally :
        print("Task Completed")
"""        

"""
solution from co-learners :
    
T = int(input())
for i in range(T):
    a,b = input().split()
    try:
        result = int(a)/int(b)
    except Exception as e:
        print('Error code: ', e)
    else:
        print(result)
"""        
T = int(input())
for i in range(T):
    a,b = input().split()
    try:
        result = int(a)/int(b)
    except Exception as e:
        print('Error code: ', e)
    else:
        print(result)
        