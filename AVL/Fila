class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, element):
        # Insere um elemento na fila
        node = Node(element)

        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1


    def pop(self):

        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next

            if self.first is None:
                self.last = None

            self._size = self._size - 1
            return elem
        raise Exception("A fila está vazia !")


    def peek(self):
        # Retorna o inicio da fila, sem remover

        if self._size > 0:
            return print(self.first.data)
        raise IndexError("A fila está vazia !")

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:

            r = ""

            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " | "
                pointer = pointer.next

            return r
        raise IndexError("A fila está vazia !")

    def __str__(self):
        return self.__repr__()