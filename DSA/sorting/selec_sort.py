arr=[]
n=int(input("HOW MANY ELEMENTS? "))

for i in range(n):
    el=int(input("Enter the element here:"))
    arr.append(el)
    
# print(arr[0])
# for i in range(n):
#     print(arr[i])

for i in range(0,n):
    min=i
    for j in range(i,n):
           if arr[min]>arr[j]:
            min=j 
       
    # arr[i],arr[min]=arr[min],arr[i]
    temp=arr[i]
    arr[i]=arr[min]
    arr[min]=temp    
    
    print(arr)