
class BST:
    def __init__(self, x):
        self.info=x
        self.left=None
        self.right=None
    def add(self,x):
        if x<self.info:
            if self.left==None:
                self.left=BST(x)
            else:
                self.left.add(x)
        else:
            if self.right == None:
                self.right = BST(x)
            else:
                self.right.add(x)
    def preorder(self):
        if self and (self.left!=None or self.right!=None):
            print(self.info, end=' ')
            if self.left:
                print('chapida',self.left.info, end=' ')
            if self.right:
                print('ungida',self.right.info)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def search(self,x):
        if self.info==x:
            return self
        elif x<self.info and self.left:
            return self.left.search(x)
        elif x>self.info and self.right:
            return self.right.search(x)
    def delet(self,x):
        if self==None:
            return None
        if x<self.info and self.left:
            self.left=self.left.delet(x)
            return self
        elif x>self.info and self.right:
            self.right=self.right.delet(x)
            return self
        else:
            if self.left==None and self.right==None:
                del(self)
                return None
            elif self.left==None or self.right==None:
                temp=None
                if self.left:
                    temp=self.left
                else:
                    temp=self.right
                del(self)
                return temp
            else:
                voris_otasi=self
                voris=self.right
                while voris.left:
                    voris_otasi=voris
                    voris=voris.left
                if voris_otasi!=self:
                    voris_otasi.left=voris.right
                else:
                    self.right=voris.right
                self.info=voris.info
                del(voris)
                return self
def node_internal(a, root= True):
    sum = 0
    if a == None:
        return 0
    if not root and  (a.left != None or a.right != None):
        sum += a.info
    sum += node_internal(a.left, False)
    sum += node_internal(a.right, False)
    return sum

b=BST(15)
b.add(12)
b.add(18)
b.add(13)
b.add(7)
b.add(9)
b.add(11)
b.add(14)
b.preorder()
k=int(input('enter el-t to be removed='))
b.delet(k)
b.preorder()
print("sum int nodes:", node_internal(b))







































