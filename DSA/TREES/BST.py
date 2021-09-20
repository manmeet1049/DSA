class BST():
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None
        # self.root=None
    def Insert(self,data):
        if data==self.data:
            #as bst doesnt allow duplicate values
            return
        elif data<self.data:
            # add the data into left sub tree
            if self.left:
                #not an empty left node
                self.left.Insert(data)
            else:
                #left sub-tree is empty
                self.left=BST(data)
        else:
            if self.right:
                self.right.Insert(data)
            else:
                self.right=BST(data)
                
        
    def printt(self):
        #inorder traversal
        element=[]
        
        if self.left:
            # traversing through the right sub-tree
            element+=self.left.printt()
        element.append(self.data) #appending the base note
        if self.right:
            element+=self.right.printt()
            # print(len(element))
        return element         
if __name__ == '__main__':
    
    # tree=BST()
    
    while True:
        print("1=> CREATE A BST\n2=> DISPLAY\n3=> EXIT")
        ch=int(input("ENTER YOUR CHOICE: "))
        
        if ch==1:
            n=int(input('HOW MANY ENTRIES? '))
            r_data=int(input("enter the root data here:"))
            tree=BST(r_data)
            for i in range(n-1):
                data=int(input('ENTER THE DATA HERE: '))
                tree.Insert(data)
        if ch==2:
            print(tree.printt())
        if ch==100:
            exit()
                
    