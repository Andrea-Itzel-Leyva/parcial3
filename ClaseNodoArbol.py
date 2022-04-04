#Declarar clase Nodo
class Node:
    def __init__(self,label,parent):
        self.label=label
        self.left=None
        self.right=None
        self.parent=parent
    #Declarar metodos para asignar nodos
    def getlabel(self):
        return self.label

    def setLabel(self,label):
        self.label=label
    #Metodos que trabajan con los punteros
    def getLeft(self):
        return self.left
    def setLeft(self, left):
        self.left=left

    def getRight(self):
        return self.right
    def setRigth(self, right):
        self.right=right
    
    def getParent(self):
        return self.parent
    def setParent(self, parent):
        self.parent=parent