class FilaCircular:
    def __init__(self, capacidade=5):
        self.capacidade = capacidade
        self.clientes = [None] * capacidade
        self.front = 0
        self.rear = 0
        self.tamanho = 0

    def enqueue(self, cliente):
        if self.tamanho == self.capacidade:
            print("Fila circular cheia!")
            return False

        self.clientes[self.rear] = cliente
        self.rear = (self.rear + 1) % self.capacidade
        self.tamanho += 1

        return True

    def dequeue(self):
        if self.empty():
            print("Fila circular vazia!")
            return None

        cliente = self.clientes[self.front]
        self.clientes[self.front] = None
        self.front = (self.front + 1) % self.capacidade
        self.tamanho -= 1

        return cliente

    def head(self):
        if self.empty():
            return None

        return self.clientes[self.front]

    def size(self):
        return self.tamanho

    def empty(self):
        return self.tamanho == 0

    def mostrar_estado(self):
        print(f"Front: {self.front}")
        print(f"Rear: {self.rear}")
        print(f"Fila: {self.clientes}")