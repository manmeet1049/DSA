def merge_sort(arr):
    
    if len(arr)==1:
        return
    
    left=arr[0:len(arr)//2]
    print(left)
    right=arr[len(arr)//2:len(arr)]
    print(right)
        
    merge_sort(left)
    merge_sort(right)
    
    merge(left, right,arr)
    

def merge(a,b,arr):
    # sorted=[]
    i=j=0
    k=0
    
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            arr[k]=a[i]
            # sorted.append(a[i])
            i+=1
            k+=1
        else:
            arr[k]=b[j]
            j+=1
            k=+1
    while i<len(a)-1:
        arr[k]=a[i]
        i=+1
        k+=1
    while j<len(b):
        arr[k]=b[j]
        j+=1 
        k+=1      
            

if __name__ == '__main__':
    arr=[]
    i=0

    n=int(input('HOW MANY ENTRIES? '))

    for i in range(n):
        ele=int(input('ENTER THE ELEMENT HERE: '))
        arr.append(ele)
        
    
    merge_sort(arr)
    print(arr)
    