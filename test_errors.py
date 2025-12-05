# Archivo de prueba para el linter
x = 1
y = 2


def bad_function(a, b, c):
    if x == 1:
        print("mal formateado")
    return a + b + c


class BadClass:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
