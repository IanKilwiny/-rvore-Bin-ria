class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data



class binaryTree:

    def __init__(self):
        self.root = None


    def addItem(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        
        current =  self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    
    #visita a raiz primeiro -> pai - esquerda - direita
    def pre_ordem(self,  node):
        if node is None:
            return
        print(node.data, end=",")
        self.pre_ordem(node.left)
        self.pre_ordem(node.right)
    
    #visita a sub-árvore da esquerda primeiro -> esquerda - direita - pai
    def pos_ordem(self, node):
        if node is None:
            return
        self.pos_ordem(node.left)
        self.pos_ordem(node.right)

        print(node.data, end=",")
    
    #ordena a arvore em ordem crescente -> esquerda - pai - direita
    def em_ordem(self, node):
        if node is None:
            return
        
        self.em_ordem(node.left)
        print(node.data, end=",")
        self.em_ordem(node.right)
    
    
    
    def busca(self, data):
        current = self.root
        if current is None:
            return None
        
        while current.data != data:
            if current.data > data:
                current = current.left
            else:
                current  = current.right
            
            if current is None:
                return False
            
        return True

    def remover(self, root, data):
        # -> 3 possibilidades 
        #     - é um nó folha: o nó é simplismente removido
        #     - nó com um filho: o nó filho assume o lugar do pai
        #     - nó com dois filhos: substituir o nó a ser removido pelo menor valor da subárvore direita (sucessor inorder)
        #       ou pelo maior valor da subárvore esquerda (predecessor inorder).
        if root is None:
            return None

        if data < root.data:
            root.left = self.remover(root.left, data)
        elif data > root.data:
            root.right = self.remover(root.right,data)
        else:
        # Nó encontrado
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # Nó com dois filhos
                temp = self.minValueNode(root.right)
                root.data = temp.data
                root.right = self.remover(root.right, temp.data)

        return root
    
    def minValueNode(node):
        current = node
        while(current.left is not None):
            current = current.left
        
        return current 




tree =  binaryTree()
tree.addItem(5)
tree.addItem(3)
tree.addItem(7)
tree.addItem(10)

tree.pre_ordem(tree.root) 
print("\n")
tree.em_ordem(tree.root)
print("\n")
tree.pos_ordem(tree.root)
print("\n")
removido = tree.remover(tree.root, 5)
tree.pre_ordem(tree.root)
print("\n")

# print(tree.busca(10)) # True
# print(tree.busca(8))  # False
# print(tree.busca(7))  # True    
# print(tree.busca(2))  # False
# print(tree.busca(5))  # True