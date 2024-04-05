class AnimalDatabase:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_racas_disponiveis(self):
        return set([animal.raca for animal in self.animais])

    def listar_personalidades_disponiveis(self):
        return set([animal.personalidade for animal in self.animais])

    def listar_aparencias_disponiveis(self):
        return set([animal.aparencia for animal in self.animais])

    def obter_nomes_por_raca(self, raca):
        return [animal.nome for animal in self.animais if animal.raca == raca]

    def obter_nomes_por_personalidade(self, personalidade):
        return [animal.nome for animal in self.animais if animal.personalidade == personalidade]

    def obter_nomes_por_aparencia(self, aparencia):
        return [animal.nome for animal in self.animais if animal.aparencia == aparencia]
