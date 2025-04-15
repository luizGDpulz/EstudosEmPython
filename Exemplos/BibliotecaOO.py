class Livro:
    def __init__(self, id_livro, titulo, autor, isbn, disponibilidade=True):
        self.__id_livro = id_livro
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn 
        self.__disponibilidade = disponibilidade 
      
    def __str__(self):
        status = "Disponivel" if self.__disponibilidade == True else "Indisponivel"
        return f'ID: {self.__id_livro}\nTitulo: {self.__titulo}\nAutor: {self.__autor}\nISBN: {self.__isbn}\nStatus: {status}\n'
    
    @property
    def get_id_livro(self):
        return self.__id_livro
    
    @property
    def get_titulo(self):
        return self.__titulo
    
    @property
    def get_autor(self):
        return self.__autor
    
    @property
    def get_isbn(self):
        return self.__isbn
    
    @property
    def get_disponibilidade(self):
        return self.__disponibilidade
    
    def adicionar(self, biblioteca):
        biblioteca.livros.append(self)
    
    def emprestar(self):
        pass

    def devolver(self):
        pass
    
    @staticmethod
    def buscar(biblioteca, id_livro=None, titulo=None):
        livros_encontrados = [livro for livro in biblioteca.livros if (id_livro is not None and id_livro == livro.get_id_livro) or (titulo and titulo.lower() in livro.get_titulo.lower())]

        # for livro in biblioteca.livros:
        #     if (id_livro is not None and id_livro == livro.get_id_livro) or (titulo and titulo.lower() in livro.get_titulo.lower()):
        #         livros_encontrados.append(livro)

        return livros_encontrados

class Usuario:
    def __init__(self, id_usuario, nome):
        self.__id_usuario = id_usuario
        self.__nome = nome
        self.__livros_emprestados = []

    def __str__(self):
        return f'ID: {self.__id_usuario}\nNome: {self.__nome}\nLivros Emprestados: {self.__livros_emprestados}\n'
    
    def adicionar(self, biblioteca):
        biblioteca.usuarios.append(self)

class Autor:
    pass

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

# Função que administra e trata o input de livros no sistema
def adicionar_livro(biblioteca):
    print("\nAdicionar Livro")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    id_livro = len(biblioteca.livros)

    livro = Livro(id_livro, titulo, autor, isbn) # Objeto livro recebe uma instância da classe Livro inciada com o seu construtor
    livro.adicionar(biblioteca)                  # Usa-se o método adicionar da classe para inserir o novo livro na biblioteca

# Função para exibir todos os livros armazenados na biblioteca e seus atributos
def listar_livros(biblioteca):
    print("\n")
    for livro in biblioteca.livros:
        print(livro)

# Função para pesquisar por livros no sistema
def buscar_livros(biblioteca):
    while(True):
        print("\nBuscar Livro por:")
        print("(1) ID")
        print("(2) Titulo")
        print("(0) Cancelar")
        opcao = input("Opcao escolhida: ")

        if opcao == "0":
            print("\nBusca Cancelada")
            break
        elif opcao == "1":
            id_livro = int(input("\nInsira o ID do livro: "))
            livros_encontrados = Livro.buscar(biblioteca, id_livro=id_livro)
        elif opcao == "2":
            titulo = input("\nInsira o Titulo do livro: ")
            livros_encontrados = Livro.buscar(biblioteca, titulo=titulo)
        else:
            print("Opcao invalida. Tente novamente.")
            continue

        if livros_encontrados:
            print("Livros encontrados:\n")
            for livro in livros_encontrados:
                print(livro)
            break
        else: 
            print("Nenhum Livro Encontrado")
            break

# Função para adicionar novos usuarios ao sistema
def adicionar_usuario(biblioteca):
    print("\nAdicionar Usuario")
    nome = input("Nome: ") 
    id_usuario = len(biblioteca.usuarios)

    usuario = Usuario(id_usuario, nome)     # Objeto usuario recebe uma instância da classe Usuario inciada com o seu construtor
    usuario.adicionar(biblioteca)           # Usa-se o método adicionar da classe para inserir o novo usuario na biblioteca

def listar_usuarios(biblioteca):
    print("\n")
    for usuario in biblioteca.usuarios:
        print(usuario)

def main():
    biblioteca = Biblioteca() # Instância da classe Biblioteca
    
    while True:
        print("\n======= Menu =======")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        #print("4. Remover Livro")
        print("5. Emprestar Livro")
        print("6. Devolver Livro")
        print("7. Adicionar Usuario")
        print("8. Listar Usuarios")
        #print("9. Remover Usuario")
        print("0. Sair")
        print("====================")
        opcao = input("Digite o número da opcao: ")

        match opcao:
            case "0": 
                print("Saindo...") 
                break
            case "1": 
                adicionar_livro(biblioteca)
            case "2": 
                listar_livros(biblioteca)
            case "3": 
                buscar_livros(biblioteca)
            case "7":
                adicionar_usuario(biblioteca)
            case "8":
                listar_usuarios(biblioteca)
            case _:
                print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
	main()
