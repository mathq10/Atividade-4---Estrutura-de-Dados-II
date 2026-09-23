class Fila:
    def __init__(self):
        self.clientes = []

    def enqueue(self, cliente):
        self.clientes.append(cliente)

    def dequeue(self):
        if self.empty():
            return None
        return self.clientes.pop(0)

    def head(self):
        if self.empty():
            return None
        return self.clientes[0]

    def size(self):
        return len(self.clientes)

    def empty(self):
        return len(self.clientes) == 0