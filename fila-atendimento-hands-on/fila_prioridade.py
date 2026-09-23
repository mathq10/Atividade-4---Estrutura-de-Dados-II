import heapq


class FilaPrioridade:
    def __init__(self):
        self.fila = []
        self.contador = 0

    def enqueue(self, cliente):
        item = (cliente["prioridade"], self.contador, cliente)
        heapq.heappush(self.fila, item)
        self.contador += 1

    def dequeue(self):
        if self.empty():
            return None

        prioridade, contador, cliente = heapq.heappop(self.fila)
        return cliente

    def head(self):
        if self.empty():
            return None

        return self.fila[0][2]

    def size(self):
        return len(self.fila)

    def empty(self):
        return len(self.fila) == 0