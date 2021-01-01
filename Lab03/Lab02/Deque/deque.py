from .node import Node

class DequeDinamico:

    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

        self.first = None
        self.last = None
        self.size = 0

    def inserir_esquerda(self, element):

        node = Node(element)

        if self.first is None:
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node

        self.size = self.size +1

    def inserir_direita(self, element):

        node = Node(element)

        if self.first is None:
            self.first = node

        else:
            node.prev = self.last
            self.last.next = node
        self.last = node

        self.size = self.size + 1

    def remover_esquerda(self):

        if self.first is not None:
            element = self.first
            data = element.data
            self.first =  self.first.next
            self.size = self.size - 1

            del element
            return print('Item {} removido, a fila andou !'.format(data))
        else:
            raise Exception('Lista Vazia!')

    def remover_direita(self):

        if self.last is not None:
            element = self.last
            data = element.data
            self.last = element.prev
            self.size = self.size - 1

            del element
            return print('Item {} removido, a fila andou !'.format(data))
        else:
            raise Exception('Lista Vazia!')

    def remover_indice(self, indice):
        if len(self.root) > 0:
            elemento_removido = self.root[indice]

            del self.root[indice]

            return elemento_removido
        
        return False

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def __len__(self):
        return self.size

    def __repr__(self):
        if self.size > 0:

            r = ""

            pointer = self.first
            while pointer:
                r = r + str(pointer.data) + " | "
                pointer = pointer.next

            return r
        raise Exception("A fila está vazia !")

    def __str__(self):
        return self.__repr__()