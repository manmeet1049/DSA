class Node:
    def __init__(self,data):
        self.data =data
        self.next=None
        
class Stack:
    def __init__(self):
        self.head=None
        
    def push(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
            new_node.next=None
    
    def pop(self):
        temp=self.head
        if self.head==None:
            print('STACK IS EMPTY! ')
            
        elif self.head.next==None:
            print(self.head.data +' popped')
            self.head=None
            
        else:
            while temp.next.next!=None:
                temp=temp.next
            print(temp.next.data +' popped')
            temp2=temp.next
            temp2.next=None
            temp.next=None
            
    def print(self):
        if self.head==None:
            print('STACK IS EMPTY! ')
        else: 
             temp=self.head
             while temp.next!=None:
                print(temp.data)
                temp=temp.next
             print(temp.data)
        
if __name__ == '__main__':
    stck=Stack()
    while True:
        print('1=> PUSH\n2=> DISPLAY\n3=> POP\n100=> EXIT')
        ch=int(input('ENTER YOUR CHOICE HERE: '))
        if ch==1:
            data=input('ENTER THE DATA HERE: ')
            stck.push(data)
        if ch==2:
            stck.print()
        if ch==3:
            stck.pop()
        if ch==100:
            exit()
                
        
        