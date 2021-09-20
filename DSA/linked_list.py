class node:
    def __init__(self,data):
        self.data = data
        self.next=None
        
class linked_list:
    
    def __init__(self):
        self.head=None
        
    def print(self):
        temp=self.head
        i=0
        while temp.next!=None:
            print(temp.data)
            temp=temp.next
            i+=1
        print(temp.data)
            
            
    def ins_last(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
            
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
            
    def ins_pos(self,pos,data):
        new_node=node(data)
        i=0
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next!=None and i<pos-1:
                temp=temp.next 
                i=+1
            new_node.next=temp.next
            temp.next=new_node
    def del_end(self):
        # prev=node(None)
        if self.head==None:
            print('LINK IS EMPTY')
        else:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            prev=temp.next
            temp.next=None
            prev.next=None 
    def del_pos(self,pos):
        if self.head==None:
            print('LINK IS EMPTY')
        elif pos==1:
            self.head=self.head.next
            # self.head.next=
        else:
            i=0
            temp=self.head
            while temp.next!=None and i<pos-2:
                temp=temp.next
            prev=temp.next
            temp.next=prev.next
            prev.next=None
            # prev.next=None
                       
        
if __name__ == '__main__':
    llist=linked_list()
    while True:
        ch=int(input('1. CREATE LIST\n2. INSERT AT SPECIFIC POSITION\n3. PRINT\n4. EXIT\n5. DELETE AT END\n6. DELETE AT SPECIFIC POSITION\n'))
        if ch==1:
            n=int(input('HOW MANY ENTRIES? '))
            
            for i in range(n):
                data=input('INSERT THE DATA HERE ')
                llist.ins_last(data)
        elif ch==2:
            # llist=linked_list()
            pos=int(input("ENTER THE POSITION: "))
            data=input("ENTER THE NAME")
            llist.ins_pos(pos,data)
            # if pos!=0:
            #     n+=1
        elif ch==3:
            llist.print()
        elif ch==4:
            exit()
        elif ch==5:
            llist.del_end()
        elif ch==6:
            pos=int(input("ENTER THE POSITION: "))
            llist.del_pos(pos)
    
    