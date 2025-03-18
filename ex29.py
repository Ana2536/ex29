def exibir_menu(): 
    print("Bem vindo ao menu de cadastro")
    print("1 - novo cadastro")
    print("2 - ver cadastro")
    print("3 -sair")
    print("-----------------------------")

def cadastrar_pessoa():
        nome = input("Nome:")
        idade = input("Idade:")
        tuema = input("Turma")
        curso = input("Curso")
        cadastros.append({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
        print("Cadastro realizado com sucesso!")