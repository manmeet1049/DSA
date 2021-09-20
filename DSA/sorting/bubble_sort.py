def b_sort(n,arr):
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            
        print(arr)


if __name__ == '__main__':
    
    
    arr=[]
    i=0

    n=int(input('HOW MANY ENTRIES? '))

    for i in range(n):
        ele=int(input('ENTE RTHE ELEMENT HERE: '))
        arr.append(ele)
        
    b_sort(n,arr)