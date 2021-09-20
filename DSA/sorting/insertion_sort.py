
def ins_sort(arr,n):
    # key=arr[len(arr)//2]
    for i in range(n):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print(arr)
        

if __name__ == '__main__':
    n=int(input('HOW MANY ENTRIES? '))
    arr=[]
    
    for i in range(n):
        ele=input('ENTER THE ELEMENT: ')
        arr.append(ele)
ins_sort(arr,n)
print(arr)