class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Partes del producto:", self.parts)

class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_result(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Parte A")

    def build_part_b(self):
        self.product.add("Parte B")

    def get_result(self):
        return self.product

class Orquestador:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()

# Ejemplo de Uso
builder = ConcreteBuilder()
director = Orquestador(builder)
director.construct()
product = builder.get_result()
product.show()


# Patron que construye un producto paso a paso
# Utilizando un director para guiar el proceso de construcción