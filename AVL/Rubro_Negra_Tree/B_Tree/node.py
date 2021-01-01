class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf  # Nó Folha
        self.keys = []  # Valores
        self.child = []  # Nós Filhos