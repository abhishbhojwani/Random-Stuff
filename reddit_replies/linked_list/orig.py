class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, node):
        if type(node) is Node or node is None:
            self.__next = node
            return
        else:
            raise TypeError("can't set :next: to {}, must be Node.".format(type(node)))
           
class LinkedList:
    def __init__(self, root=None, data=None):
        if root is None:
            root = Node()
        root.data = data
        self.root = root
        self.current = self.root
   
    def __iter__(self):
        self.current = self.root
        return self
   
    def __next__(self):
        if self.current is not None:
            r = self.current
            self.current = self.current.next
            return r
        else:
            raise StopIteration
   
    def add(self, data=None):
        last = self.getlast()
        last.next = Node(data=data)
       
    def getlast(self):
        current = self.current
        while current.next is not None:
            current = current.next
        return current
   
    def find(self, value):
        for node in self:
            if value == node.data:
                return node
        return None
   
    def insert(self, node, nodes):
        if type(nodes) is LinkedList:
            if node in self:
                nodes.getlast().next = node.next
                node.next = nodes.root
            else:
                raise TypeError("can only insert into Nodes in this object")
        else:
            raise TypeError("can only insert LinkedList")
 
def main():
    #new list
    l = LinkedList()
    l.root.data = 13
    l.add(12)
    #add stuff
    for i in range(92,116):
        l.add(i)
    for node in l:
        print(node.data)
    print("root:{}  next:{}  root value:{}  next value:{}".format(
           l.root, l.root.next, l.root.data, l.root.next.data
           )
         )
         
    print("gets a Node: ", l.find(111))
    print("returns None: ", l.find(-1))
   
    #new list
    l2 = LinkedList(data=1000)
    for i in range(1000,1015):
        l2.add(i)
   
    #insert new list into first list
    l.insert(l.find(113), l2)
 
    for node in l:
        print(node.data)
 
 
main()
