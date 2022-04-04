from ClaseNodoArbol import Node
class BinarySearchTree:
    def __init__(self):
        self.root=None
#Metodod para crear nodos
    def insert(self,label):
        new_node=Node(label,None)
        #Si el arbol esta vacio
        if self.empty():
            self.root=new_node
        else:
            #Si no esta vacio
            curr_node=self.root
            while curr_node is not None:
                parent_node=self.root
                if new_node.getlabel()<curr_node.getlabel():
                    curr_node=curr_node.getLeft()
                else:
                    curr_node=curr_node.getRight()
            if new_node.getlabel()<parent_node.getlabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRigth(new_node)
            new_node.setParent(parent_node)
    #Metodo para saber si esta vacio el arbol
    def empty(self):
        if self.root is None:
            return True
        return False