# Classe Livro
class Livro():
    def __init__(self, id, titulo, autor, isbn, disponibilidade):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponibilidade = disponibilidade

    def __str__(self):
        return f'ID: {self._id}\nTitulo: {self._titulo}\nAutor: {self._autor}\nISBN: {self._isbn}\nDisponibilidade: {self._disponibilidade}\n'
        # ou
        # return "Titulo: " + str(self._titulo) + "\nAutor: " + str(self._autor) + "\nISBN: " + str(self._isbn) + "\nDisponibilidade: " + str(self._disponibilidade) 

    def get_livro(self):
        pass

    def set_livro(self):
        pass

# Classe Autor
class Autor:
    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    def __str__(self):
        return f'Nome: {self._nome}\nNacionalidade: {self._nacionalidade}'

    def get_autor(self):
        return self._nome, self._nacionalidade

    def set_autor(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

# Classe Usuario
class Usuario():
    def __init__(self, id, nome, livros_emprestados):
        self._id = id
        self._nome = nome
        self._livros_emprestados = livros_emprestados

    def get_usuario(self):
        pass

    def set_usuario(self):
        pass  

# Função para adicionar novo livro à biblioteca
def adicionar_livro(livros):
    print("\nAdicionar Livro")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    id = len(livros)
    livros.append(Livro(id, titulo, autor, isbn, True))            

def listar_livros(livros):
    while True:
        print("\nListar Livros:")
        print("(1) Todos")
        print("(2) Disoniveis")
        print("(3) Emprestados")
        print("(0) Cancelar")
        choice = int(input("Opcao escolhida: "))  

        if choice == 1:
            for livro in livros:
                print(f'ID: {livro._id}\nTitulo: {livro._titulo}\nAutor: {livro._autor}\nISBN: {livro._isbn}\nDisponibilidade: {livro._disponibilidade}\n')
            break
        elif choice == 2:
            for livro in livros:
                if livro._disponibilidade == True:
                    print(f'ID: {livro._id}\nTitulo: {livro._titulo}\nAutor: {livro._autor}\nISBN: {livro._isbn}\nDisponibilidade: {livro._disponibilidade}\n')
            break
        elif choice == 3:
            for livro in livros:
                if livro._disponibilidade == False:
                    print(f'ID: {livro._id}\nTitulo: {livro._titulo}\nAutor: {livro._autor}\nISBN: {livro._isbn}\nDisponibilidade: {livro._disponibilidade}\n')
            break
        elif choice == 0:
            break
        else:
            print("Opcao invalida")

def remover_livro(livros):
    print("\nRemover Livro")
    id = int(input("Insira o ID do livro: "))
    if id >= 0 and id <= len(livros):
        livros.pop(id)
        print("\nRemovido com Sucesso")
    else:
        print("\nID Inválido\n")

def buscar_livro(livros):
    while True:
        print("\nBuscar Livro por:")
        print("(1) ID")
        print("(2) Titulo")
        print("(0) Cancelar")
        choice = int(input("Opcao escolhida: ")) 

        if choice == 1:
            id = int(input("Insira o ID do livro: "))
            if id >= 0 and id <= len(livros):
                print(f'ID: {livros[id]._id}\nTitulo: {livros[id]._titulo}\nAutor: {livros[id]._autor}\nISBN: {livros[id]._isbn}\nDisponibilidade: {livros[id]._disponibilidade}\n')
            else:
                print("\nID Nao Encontrado\n")
            break
        elif choice == 2:
            titulo = input("Insira o Titulo do livro: ")
            for livro in livros:
                if livro._titulo == titulo:
                    print(f'ID: {livros[livro]._id}\nTitulo: {livros[livro]._titulo}\nAutor: {livros[livro]._autor}\nISBN: {livros[livro]._isbn}\nDisponibilidade: {livros[livro]._disponibilidade}\n')
                    break                
            print("\nTitulo Nao Encontrado\n")
        elif choice == 0:
            break
        else:
            print("Opcao invalida")
        
def emprestar_livro(self):
    pass

def devolver(self):
    pass

# Função Principal
def main():
    # Listas para armazenar os dados
    livros = []
    usuarios = []
    autores = []

    while True:
        print("\nMenu de Operações:")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        print("4. Remover Livro")
        print("5. Emprestar Livro")
        print("6. Devolver Livro")
        print("7. Adicionar Usuario")
        print("8. Remover Usuario")
        print("0. Sair")
        choice = input("Escolha uma Opcao: ")

        match choice:
            case '0':
                print("\nFinalizando Programa\n")
                break
            case '1':
                adicionar_livro(livros)
            case '2':
                listar_livros(livros)
            case '3':
                buscar_livro(livros)
            case '4':
                remover_livro(livros)
            case '5':
                print("Op 5")
            case '6':
                print("Op 6")
            case _:
                print("Op Invalida")

if __name__ == "__main__":
	main()