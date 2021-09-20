from linked_list import node


class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node= Node(data)
        if self.head==None:
            self.head=new_node
            self.prev=None
        else:
            temp=self.head
            while temp.next!=None:    
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
            
    def ins_position(self,data,pos):
        new_node= Node(data)
        i=0
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while new_node.next!=None and i<=pos:
                temp=temp.next
                i+=1
            new_node.next=temp.next
            temp.next=new_node
            new_node.prev=temp
            
    def del_position(self,pos,num):
        if self.head==None:
            print('The List Is Empty')
        elif pos==num:
            num=num-1
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            prevv=temp.next
            temp.next=None
            prevv.next=None
            prevv.prev=None
        else:
            i=0
            temp=self.head
            while temp.next!=None and i<pos-2:
                temp=temp.next
                i+=1
            temp2=temp.next
            temp.next=temp2.next 
            noode=temp.next
            noode.prev=temp
            temp2.next=None
            temp2.prev=None
            num=num-1       
            
    def print(self):
        temp=self.head
        i=0
        while temp.next!=None:
            print(temp.data)
            temp=temp.next
            i+=1
        print(temp.data)
        
        
if __name__ == '__main__':
    dllist=DLL()
    # n=int(inpu)
    print('1=> CREATE LIST\n2=> PRINT LIST\n3=> INSERT\n4=> DELETE\n100=> EXIT')
    while True:
        n=int(input("ENTER YOUR CHOICE: "))
        if n==1:
            num=int(input("HOW MANY NODES? "))
            for i in range(num):
                data=input("ENTER THE DATA HERE: ")
                dllist.insert(data)
        elif n==2:
            dllist.print()
        elif n==100:
            exit()
        elif n==3:
            pos=int(input("ENTER THE POSITION: "))
            data=input("ENTER THE DATA: ")
            dllist.ins_position(data,pos)
        elif n==4:
           pos=int(input("ENTER THE POSITION: "))
           dllist.del_position(pos,num)    
           num-=1
            
                  
    