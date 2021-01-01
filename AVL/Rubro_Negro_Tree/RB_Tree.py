import sys
from .node import Node
from .Fila import Queue


class RB_Tree:

    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def insert(self, key):

        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        pai = None
        aux = self.root

        while aux != self.TNULL:
            pai = aux
            if node.item < aux.item:
                aux = aux.left
            else:
                aux = aux.right

        node.parent = pai
        if pai is None:
            self.root = node
        elif node.item < pai.item:
            pai.left = node
        else:
            pai.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.balancear_pos_insercao(node)

    # Balanceia a arvore depois da inserção
    def balancear_pos_insercao(self, node):

        while node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                aux = node.parent.parent.left
                if aux.color == 1:
                    aux.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rightRotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.leftRotate(node.parent.parent)
            else:
                aux = node.parent.parent.right

                if aux.color == 1:
                    aux.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.leftRotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.rightRotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0

    def remove(self, node, key):

        aux = self.TNULL

        while node != self.TNULL:
            if node.item == key:
                aux = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if aux == self.TNULL:
            print("O numero inserido não foi encontrado.")
            return

        aux2 = aux
        aux2_cor_original = aux2.color
        if aux.left == self.TNULL:
            aux3 = aux.right
            self.__swap(aux, aux.right)
        elif aux.right == self.TNULL:
            aux3 = aux.left
            self.__swap(aux, aux.left)
        else:
            aux2 = self.getMenorNum(aux.right)
            aux2_cor_original = aux2.color
            aux3 = aux2.right
            if aux2.parent == aux:
                aux3.parent = aux2
            else:
                self.__swap(aux2, aux2.right)
                aux2.right = aux.right
                aux2.right.parent = aux2

            self.__swap(aux, aux2)
            aux2.left = aux.left
            aux2.left.parent = aux2
            aux2.color = aux.color
        if aux2_cor_original == 0:
            self.balancear_pos_remocao(aux3)

    # Balanceia a árvore depois da remoção de um nó
    def balancear_pos_remocao(self, data):

        while data != self.root and data.color == 0:
            if data == data.parent.left:
                aux = data.parent.right
                if aux.color == 1:
                    aux.color = 0
                    data.parent.color = 1
                    self.leftRotate(data.parent)
                    aux = data.parent.right

                if aux.left.color == 0 and aux.right.color == 0:
                    aux.color = 1
                    data = data.parent
                else:
                    if aux.right.color == 0:
                        aux.left.color = 0
                        aux.color = 1
                        self.rightRotate(aux)
                        aux = data.parent.right

                    aux.color = data.parent.color
                    data.parent.color = 0
                    aux.right.color = 0
                    self.leftRotate(data.parent)
                    data = self.root
            else:
                aux = data.parent.left
                if aux.color == 1:
                    aux.color = 0
                    data.parent.color = 1
                    self.rightRotate(data.parent)
                    aux = data.parent.left

                if aux.right.color == 0 and aux.right.color == 0:
                    aux.color = 1
                    data = data.parent
                else:
                    if aux.left.color == 0:
                        aux.right.color = 0
                        aux.color = 1
                        self.leftRotate(aux)
                        aux = data.parent.left

                    aux.color = data.parent.color
                    data.parent.color = 0
                    aux.left.color = 0
                    self.rightRotate(data.parent)
                    data = self.root
        data.color = 0

    def delete_node(self, item):
        self.remove(self.root, item)

    def leftRotate(self, x):

        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, x):

        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __swap(self, node, aux):
        if node.parent is None:
            self.root = aux
        elif node == node.parent.left:
            node.parent.left = aux
        else:
            node.parent.right = aux
        aux.parent = node.parent

    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def percurso_nivel(self, node):

        if node is self.TNULL:
            node = self.root

        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            if node.item != 0:
                print(node.item, end=" ")

    def getMenorNum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def getMaiorNum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.TNULL:
            return self.getMenorNum(x.right)

        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    def antecessor(self, x):
        if x.left != self.TNULL:
            return self.getMaiorNum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    def get_root(self):
        return self.root

    def print_tree(self):
        self.percurso_nivel(self.root)


bst = RB_Tree()

# Não inserir o numero 0 !

bst.insert(55)
bst.insert(40)
bst.insert(65)
bst.insert(60)
bst.insert(75)
bst.insert(57)

bst.print_tree()

print("\nDepois de remover um item da árvore:\n")
bst.delete_node(40)
bst.print_tree()