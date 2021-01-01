from .deque import DequeDinamico

def test():

    deque = DequeDinamico()

    deque.inserir_direita("Vanessa")
    deque.inserir_esquerda("Gonçalves")
    deque.inserir_esquerda("Vanessa")

    print('\n')
    print(deque)

    print('\n')
    print(len(deque))