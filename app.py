# app.py

from view import exibir_apresentacao, limpar_tela, exibir_opcoes_filtros, exibir_lista_nomes
from model import Animal
from database import AnimalDatabase

def listar_opcoes_numericamente(opcoes):
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    num_opcao = int(input("Escolha o número correspondente à opção: "))
    return list(opcoes)[num_opcao - 1]

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

    while True:
        exibir_opcoes_filtros()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            racas_disponiveis = banco_de_dados.listar_racas_disponiveis()
            raca = listar_opcoes_numericamente(racas_disponiveis)
            nomes_filtrados = banco_de_dados.obter_nomes_por_raca(raca)
        elif opcao == '2':
            personalidades_disponiveis = banco_de_dados.listar_personalidades_disponiveis()
            print("\nPersonalidades disponíveis:")
            personalidade = listar_opcoes_numericamente(personalidades_disponiveis)
            nomes_filtrados = banco_de_dados.obter_nomes_por_personalidade(personalidade)
        elif opcao == '3':
            aparencias_disponiveis = banco_de_dados.listar_aparencias_disponiveis()
            print("\nAparências disponíveis:")
            aparencia = listar_opcoes_numericamente(aparencias_disponiveis)
            nomes_filtrados = banco_de_dados.obter_nomes_por_aparencia(aparencia)
        elif opcao == '4':
            exit()
        else:
            print("Opção inválida. Por favor, escolha novamente.")
            continue

        exibir_lista_nomes(nomes_filtrados)
        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
