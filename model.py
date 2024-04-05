# model.py

class Animal:
    def __init__(self, nome, tipo, raca, personalidade, aparencia):
        self.nome = nome
        self.tipo = tipo
        self.raca = raca
        self.personalidade = personalidade
        self.aparencia = aparencia

    def __str__(self):
        return f"Nome: {self.nome}, Tipo: {self.tipo}, Raça: {self.raca}, Personalidade: {self.personalidade}, Aparência: {self.aparencia}"
