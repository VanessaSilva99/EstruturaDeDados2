from .node import BTreeNode

class BTree:
    def __init__(self, d):
        self.root = BTreeNode(True)
        self.d = d

    def print_tree(self

        print("Level ", nivel, " ", len(tree

        for i in tree.keys:
            print(i, end=" ")
        print()

        nivel  

        if  
            for   
                self.print_tree

    def search(self, key, 

        if    
            i = 0
            while i < len(node.keys) and key > 
                i += 1
            if i < len(node.keys) and key == 
                return node, i
            elif node.leaf:
                return None
            else:
                return self.search(key, node.
        else:
            return self.search(key, self.root)

    def insert(self, key):

        root = self.root

        if len(root.keys) == (2 * self.d) - 1: # Chaves estão cheias, então é preciso dividir
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root) # Root original/inicial agora é o filho 0 do novo root
            self.split(temp, 0)
            self.insert_nao_cheia(temp, key)
        else:
            self.insert_nao_cheia(root, key)

    def insert_nao_cheia(self, tree, key):

        i = len(tree.keys) - 1

        if tree.leaf:
            tree.keys.append((None, None))
            while i >= 0 and key[0] < tree.keys[i][0]:
                tree.keys[i + 1] = tree.keys[i]
                i -= 1
            tree.keys[i + 1] = key
        else:
            while i >= 0 and key[0] < tree.keys[i][0]:
                i -= 1
            i += 1
            if len(tree.child[i].keys) == (2 * self.d) - 1:
                self.split(tree, i)
                if key[0] > tree.keys[i][0]:
                    i += 1
            self.insert_nao_cheia(tree.child[i], key)

    def split(self, tree, i):

        d = self.d
        y = tree.child[i]

        z = BTreeNode(y.leaf)

        # Passa todos os filhos de 'tree' para a direita e insere 'z' na posição i+1
        tree.child.insert(i + 1, z)
        tree.keys.insert(i, y.keys[d - 1])

        # Chaves de z tem de d a 2d - 1
        # Chaves de y tem de 0 a d-2
        z.keys = y.keys[d: (2 * d) - 1]
        y.keys = y.keys[0: d - 1]

        # Chaves de z tem de d a 2d
        # Chaevs de y tem de 0 a d
        if not y.
            z.child = y.child[d: 2 * 
            y.child = y.child[0: d]