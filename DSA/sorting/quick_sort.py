def partition(arr,i,j):
    pivot_index=i
    pivot=arr[pivot_index]
    
    
    while i<j:
        while i<len(arr) and arr[i]<=pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[pivot_index],arr[j]=arr[j],arr[pivot_index]
    # print(arr)
   
    return j
def quick_sort(arr,l,h):
    if l<h:
        pi=partition(arr,l,h)
        quick_sort(arr,l,pi-1)
        quick_sort(arr,pi+1,h)
    
       
    
arr=[]
n=int(input('HOW MANY ENTRIES? '))
for i in range(n):
    ele=int(input('ENTER THE ELEMENT HERE: '))
    arr.append(ele)   
quick_sort(arr,0,len(arr)-1)
print(arr)
        
    
        