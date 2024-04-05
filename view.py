# view.py

def exibir_apresentacao():
    print("Bem-vindo ao sistema de escolha de nomes para animais!")
    print("Vamos começar personalizando sua busca.")
    print("Por favor, preencha as informações sobre seu animal.")

def formatar_texto(texto):
    return texto.upper()

def limpar_tela():
    print("\n" * 100)

def exibir_opcoes_filtros():
    print("\nSelecione os filtros desejados para personalizar sua busca:")
    print("1. Raça")
    print("2. Personalidade")
    print("3. Aparência")
    print("4. Sair")

def exibir_lista_nomes(nomes):
    print("\nSugestões de nomes:")
    for nome in nomes:
        print("-", nome)
