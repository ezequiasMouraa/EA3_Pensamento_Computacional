# app.py

from view import exibir_apresentacao, limpar_tela, exibir_opcoes_filtros, exibir_lista_nomes
from model import Animal
from database import AnimalDatabase

def listar_opcoes_numericamente(opcoes):
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    num_opcao = int(input("Escolha o número correspondente à opção: "))
    return list(opcoes)[num_opcao - 1]

def filtrar_por_raca(banco_de_dados):
    racas_disponiveis = banco_de_dados.listar_racas_disponiveis()
    raca = listar_opcoes_numericamente(racas_disponiveis)
    return banco_de_dados.obter_nomes_por_raca(raca)

def filtrar_por_personalidade(banco_de_dados):
    personalidades_disponiveis = banco_de_dados.listar_personalidades_disponiveis()
    print("\nPersonalidades disponíveis:")
    personalidade = listar_opcoes_numericamente(personalidades_disponiveis)
    return banco_de_dados.obter_nomes_por_personalidade(personalidade)

def filtrar_por_aparencia(banco_de_dados):
    aparencias_disponiveis = banco_de_dados.listar_aparencias_disponiveis()
    print("\nAparências disponíveis:")
    aparencia = listar_opcoes_numericamente(aparencias_disponiveis)
    return banco_de_dados.obter_nomes_por_aparencia(aparencia)

def main():
    limpar_tela()
    exibir_apresentacao()

    banco_de_dados = AnimalDatabase()

    # Adição de animais ao banco de dados
    banco_de_dados.adicionar_animal(Animal("Fido", "Cachorro", "Vira-lata", "Brincalhão", "Marrom"))
    banco_de_dados.adicionar_animal(Animal("Rex", "Cachorro", "Labrador", "Ativo", "Preto"))
    banco_de_dados.adicionar_animal(Animal("Luna", "Cachorro", "Poodle", "Carinhosa", "Branca"))
    banco_de_dados.adicionar_animal(Animal("Bolinha", "Cachorro", "Pinscher", "Guarda", "Marrom"))
    banco_de_dados.adicionar_animal(Animal("Mel", "Cachorro", "Golden Retriever", "Calma", "Dourada"))
    banco_de_dados.adicionar_animal(Animal("Zeca", "Cachorro", "Schnauzer", "Inteligente", "Cinza"))
    banco_de_dados.adicionar_animal(Animal("Mimi", "Gato", "Siamês", "Brincalhão", "Branco"))
    banco_de_dados.adicionar_animal(Animal("Nina", "Gato", "Persa", "Carinhosa", "Cinza"))
    banco_de_dados.adicionar_animal(Animal("Milo", "Gato", "Maine Coon", "Curioso", "Amarelo"))
    banco_de_dados.adicionar_animal(Animal("Billy", "Pássaro", "Canário", "Cantor", "Amarelo"))
    banco_de_dados.adicionar_animal(Animal("Polly", "Pássaro", "Papagaio", "Falante", "Verde"))

    opcoes = {
        '1': filtrar_por_raca,
        '2': filtrar_por_personalidade,
        '3': filtrar_por_aparencia,
        '4': exit
    }

    while True:
        exibir_opcoes_filtros()
        opcao = input("Escolha uma opção: ")

        if opcao not in opcoes:
            print("Opção inválida. Por favor, escolha novamente.")
            continue

        if opcao == '4':
            opcoes[opcao]()
        else:
            nomes_filtrados = opcoes[opcao](banco_de_dados)
            exibir_lista_nomes(nomes_filtrados)
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
