def push(stack,data):
    stack.append(data)
def prints(stack):
    for i in range(len(stack)):
        print(stack[i])
def pop(stack):
    if len(stack)==0:
        print('EMPTY')
    else:
        stack.pop(0)





if __name__ == '__main__':
    stack =[]
    while True:
        print('1.PUSH\n2.POP\n3.DISPLAY\n')
        ch=int(input('ENTER YOUR CHOICE: '))
        if ch ==1:
            
            data=input('ENTER THE DATA HERE: ')
            push(stack,data)
        if ch==3:
            prints(stack)    
    
        if ch==2:
            pop(stack)    
            print(f'THE LENGTH OF THE STACK IS {len(stack)}')