class Person:

    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def hola(self):
        print(f"hola {self.nombre}")