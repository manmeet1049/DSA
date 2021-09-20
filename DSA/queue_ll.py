class Node:
    def __init__(self,data):
        self.data = data
        self.next=None 
        
class Queue:
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
        if self.head==None:
            print("EMPTY QUEUE! ")
        else:
             print(self.head.data+ " POPPED")
             temp=self.head
             self.head=self.head.next
             temp.next=None
    
    def print(self):
        if self.head==None:
            print('QUEUE IS EMPTY! ')
        else: 
             temp=self.head
             while temp.next!=None:
                print(temp.data)
                temp=temp.next
             print(temp.data)
        
if __name__ == '__main__':
    qu=Queue()
    while True:
        print('1=> PUSH\n2=> DISPLAY\n3=> POP\n100=> EXIT')
        ch=int(input('ENTER YOUR CHOICE HERE: '))
        if ch==1:
            data=input('ENTER THE DATA HERE: ')
            qu.push(data)
        if ch==2:
            qu.print()
        if ch==3:
            qu.pop()
        if ch==100:
            exit()