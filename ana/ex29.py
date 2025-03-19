def exibir_menu(): 
    print("Bem vindo ao menu de cadastro")
    print("1 - novo cadastro")
    print("2 - ver cadastro")
    print("3 -sair")
    print("-----------------------------")

def cadastrar_pessoa(cadastros):
    nome = input("Nome:")
    idade = input("Idade:")
    turma = input("Turma")
    curso = input("Curso")
    cadastros.append({"Nome":nome, "Idade": idade, "Turma":turma, "Curso": curso})
    print("Cadastro realizado com sucesso!")

def ver_cadastros(cadastros):
    if not cadastros:
        print("Nenhum cadastro no sistema")
    else:
        print("\n-------Lista de Cadastros------")
        for i, pessoa in enumerate(cadastros, 1):
            print(f"{i} . Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Turma: {pessoa['Turma']}, Curso: {pessoa['Curso']}")

def main():
    cadastros = []
    while True:
        exibir_menu()
        opção = input("escolha uma opcao:")
        if opção == "1":
            cadastrar_pessoa(cadastros)
        elif opção == "2":
            ver_cadastros(cadastros)
        elif opção == "3":
            print("Obrigado por o sistema de cadastro!")
            break
        else:
            print("Opcao invalida! Tente novamente")


if __name__ == "__main__":
    main()

            