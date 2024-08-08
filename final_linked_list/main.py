class Node:
    def init(self,x,b):
        self.fio=x
        self.bal=b
        self.next=self.prev=None
class DLL:
    def init(self):
        self.head=self.tail=None
    def add(self,x,b):
        p=Node(x,b)
        if self.head==None:
            self.head=p
            self.tail=p
        else:
            self.tail.next=p
            p.prev=self.tail
            self.tail=p
    def pop(self):
        if self.head==None:
            print('empty DLL')
        elif self.head==self.tail:
            del(self.head)
            self.head=self.tail=None
        else:
            temp=self.tail.prev
            temp.next=None
            del(self.tail)
            self.tail=temp
    def print(self):
        if self.head:
            current=self.head
            while current!=None:
                print(current.fio,':',current.bal,'->')
                current=current.next
            print()
        else:
            return None
    def merit(self):
        if self.head:
            current=self.head
            while current!=None:
                if current.bal>=60 and current.bal<=80:
                    print(current.fio,':',current.bal,'->')
                current=current.next
            print()
        else:
            return None
llist=DLL()
llist.add('Ali',45)
llist.add('Vali',57)
llist.add('Gani',67)
llist.add('Qani',77)
llist.add('mana',87)
llist.print()
llist.merit()



from stack import *





class Node:
    def init(self, x):
        self.info = x
        self.next = None

class LL:
    def init(self):
        self.lst = None
        self.last = None

    def add_first(self, x):
        p = Node(x)
        p.next = self.lst
        self.lst = p

    def add_last(self, data):
        new_node = Node(data)
        if not self.lst:
            self.lst = new_node
        else:
            self.last.next = new_node
        self.last = new_node
    def print_list(self):
        p = self.lst
        while p is not None:
            print(p.info.title())
            p = p.next
    def find_same_products(self, other_list):
        c_list = LL()
        c_self = self.lst
        while c_self:
            c_other = other_list.lst
            while c_other:
                if c_self.info.lower() == c_other.info.lower():
                    c_list.add_last(c_self.info)
                    break
                c_other = c_other.next
            c_self = c_self.next
        return c_list

def show_products(company_name, products_list):
    print(f"Products for {company_name}:")
    products_list.print_list()

bosch_products = LL()
philips_products = LL()
bosch_product_names = ["hurmo", "apple", "lemon", "apelsin", "meat", "OIL"]
philips_product_names = ["banana", "apple", "lemon", "apelsin", "oil"]
for product in bosch_product_names:
    bosch_products.add_last(product)
for product in philips_product_names:
    philips_products.add_last(product)

# bosch_products.add_last("milk")
# philips_products.add_first("milk")

show_products("BOSCH", bosch_products)
show_products("PHILIPS", philips_products)
same_products = (bosch_products.find_same_products(philips_products))
show_products("Same Products", same_products)





class Node:
    def init(self,x):
        self.info=x
        self.next=None
class LinkedList:
    def init(self):
        self.lst=None
        self.last=None
    def append(self,x):
        p=Node(x)
        if(self.lst==None):
            self.lst=p
            self.last=p
        else:
            self.last.next=p
            self.last=p
    def addfirst(self,x):
        p=Node(x)
        if (self.lst == None):
            self.lst = p
            self.last = p
        else:
            q=self.lst
            self.lst=p
            p.next=q
    def addmiddle(self,c,x):
        p=Node(x)
        q=self.lst
        while q!=None:
            if q.info==c:
                break
            q=q.next
        if(q==None):
            print(c,'not found')
            return
        t=q.next
        q.next=p
        p.next=t
    def print(self):
        p=self.lst
        while p!=None:
            print(p.info,end='->',sep='')
            p=p.next
        print()
l1=LinkedList()
n=int(input('n='))
for i in range(n):x4
    k=int(input('son='))
    l1.append(k)
l1.print()
x=int(input('nimani='))
c=int(input('nimadan kn='))
l1.addmiddle(c,x)
l1.print()




import gc

# node creation

class Node:

    def init(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def init(self):
        self.head = None

    # insert node at the front
    def insert_front(self, data):

        # allocate memory for newNode and assign data to newNode
        new_node = Node(data)

        # make newNode as a head
        new_node.next = self.head

        # assign null to prev (prev is already none in the constructore)

        # previous of head (now head is the second node) is newNode
        if self.head is not None:
            self.head.prev = new_node

        # head points to newNode
        self.head = new_node

    # insert a node after a specific node
    def insert_after(self, prev_node, data):

        # check if previous node is null
        if prev_node is None:
            print("previous node cannot be null")
            return

        # allocate memory for newNode and assign data to newNode
        new_node = Node(data)

        # set next of newNode to next of prev node
        new_node.next = prev_node.next

        # set next of prev node to newNode
        prev_node.next = new_node

        # set prev of newNode to the previous node
        new_node.prev = prev_node

        # set prev of newNode's next to newNode
        if new_node.next:
            new_node.next.prev = new_node

    # insert a newNode at the end of the list
    def insert_end(self, data):

        # allocate memory for newNode and assign data to newNode
        new_node = Node(data)

        # assign null to next of newNode (already done in constructor)

        # if the linked list is empty, make the newNode as head node
        if self.head is None:
            self.head = new_node
            return

        # store the head node temporarily (for later use)
        temp = self.head

        # if the linked list is not empty, traverse to the end of the linked list
        while temp.next:
            temp = temp.next

        # now, the last node of the linked list is temp

        # assign next of the last node (temp) to newNode
        temp.next = new_node

        # assign prev of newNode to temp
        new_node.prev = temp

        return

    # delete a node from the doubly linked list
    def deleteNode(self, dele):

        # if head or del is null, deletion is not possible
        if self.head is None or dele is None:
            return

        # if del_node is the head node, point the head pointer to the next of del_node
        if self.head == dele:
            self.head = dele.next

        # if del_node is not at the last node, point the prev of node next to del_node to the previous of del_node
        if dele.next is not None:
            dele.next.prev = dele.prev

        # if del_node is not the first node, point the next of the previous node to the next node of del_node
        if dele.prev is not None:
            dele.prev.next = dele.next

        # free the memory of del_node
        gc.collect()

    # print the doubly linked list
    def display_list(self, node):

        while node:
            print(node.data, end="->")
            last = node
            node = node.next


# initialize an empty node
d_linked_list = DoublyLinkedList()

d_linked_list.insert_end(5)
d_linked_list.insert_front(1)
d_linked_list.insert_front(6)
d_linked_list.insert_end(9)

# insert 11 after head
d_linked_list.insert_after(d_linked_list.head, 11)

# insert 15 after the seond node
d_linked_list.insert_after(d_linked_list.head.next, 15)

d_linked_list.display_list(d_linked_list.head)

# delete the last node
d_linked_list.deleteNode(d_linked_list.head.next.next.next.next.next)

print()
d_linked_list.display_list(d_linked_list.head)




import gc

# node creation

class Node:

    def init(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def init(self):
        self.head = None

    # insert node at the front
    def insert_front(self, data):

        # allocate memory for newNode and assign data to newNode
        new_node = Node(data)

        # make newNode as a head
        new_node.next = self.head

        # assign null to prev (prev is already none in the constructore)

        # previous of head (now head is the second node) is newNode
        if self.head is not None:
            self.head.prev = new_node

        # head points to newNode
        self.head = new_node

    # insert a node after a specific node
    def insert_after(self, prev_node, data):

        # check if previous node is null
        if prev_node is None:
            print("previous node cannot be null")
            return

        # allocate memory for newNode and assign data to newNode
        new_node = Node(data)

        # set next of newNode to next of prev node
        new_node.next = prev_node.next

        # set next of prev node to newNode
        prev_node.next = new_node

        # set prev of newNode to the previous node
        new_node.prev = prev_node

        # set prev of newNode's next to newNode
        if new_node.next:
            new_node.next.prev = new_node

    # insert a newNode at the end of the list
    def insert_end(self, data):

        # allocate memory for newNode and assign data to newNode
        new_node = Node(data)

        # assign null to next of newNode (already done in constructor)

        # if the linked list is empty, make the newNode as head node
        if self.head is None:
            self.head = new_node
            return

        # store the head node temporarily (for later use)
        temp = self.head

        # if the linked list is not empty, traverse to the end of the linked list
        while temp.next:
            temp = temp.next

        # now, the last node of the linked list is temp

        # assign next of the last node (temp) to newNode
        temp.next = new_node

        # assign prev of newNode to temp
        new_node.prev = temp

        return

    # delete a node from the doubly linked list
    def deleteNode(self, dele):

        # if head or del is null, deletion is not possible
        if self.head is None or dele is None:
            return

        # if del_node is the head node, point the head pointer to the next of del_node
        if self.head == dele:
            self.head = dele.next

        # if del_node is not at the last node, point the prev of node next to del_node to the previous of del_node
        if dele.next is not None:
            dele.next.prev = dele.prev

        # if del_node is not the first node, point the next of the previous node to the next node of del_node
        if dele.prev is not None:
            dele.prev.next = dele.next

        # free the memory of del_node
        gc.collect()

    # print the doubly linked list
    def display_list(self, node):

        while node:
            print(node.data, end="->")
            last = node
            node = node.next


# initialize an empty node
d_linked_list = DoublyLinkedList()

d_linked_list.insert_end(5)
d_linked_list.insert_front(1)
d_linked_list.insert_front(6)
d_linked_list.insert_end(9)

# insert 11 after head
d_linked_list.insert_after(d_linked_list.head, 11)

# insert 15 after the seond node
d_linked_list.insert_after(d_linked_list.head.next, 15)

d_linked_list.display_list(d_linked_list.head)

# delete the last node
d_linked_list.deleteNode(d_linked_list.head.next.next.next.next.next)

print()
d_linked_list.display_list(d_linked_list.head)





























