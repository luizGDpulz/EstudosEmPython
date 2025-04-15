class Livro:
    _contador_id = 0
    
    def __init__(self, titulo, autor, isbn, disponibilidade=True):
        self.__id_livro = Livro._contador_id
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponibilidade = disponibilidade
        Livro._contador_id += 1
      
    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return (
            f'ID: {self.id}\n'
            f'Título: {self.titulo}\n'
            f'Autor: {self.autor.nome}\n'
            f'ISBN: {self.isbn}\n'
            f'Status: {status}\n'
        )
    
    @property
    def id(self):
        return self.__id_livro
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def isbn(self):
        return self.__isbn
    
    @property
    def disponivel(self):
        return self.__disponibilidade
    
    @disponivel.setter
    def disponivel(self, status):
        self.__disponibilidade = status

class Usuario:
    _contador_id = 0
    
    def __init__(self, nome):
        self.__id_usuario = Usuario._contador_id
        self.__nome = nome
        self.__livros_emprestados = []
        Usuario._contador_id += 1

    def __str__(self):
        livros = ', '.join([livro.titulo for livro in self.__livros_emprestados]) or "Nenhum"
        return (
            f'ID: {self.id}\n'
            f'Nome: {self.nome}\n'
            f'Livros Emprestados: {livros}\n'
        )
    
    @property
    def id(self):
        return self.__id_usuario
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def livros_emprestados(self):
        return self.__livros_emprestados
    
    def emprestar_livro(self, livro):
        if livro.disponivel:
            self.__livros_emprestados.append(livro)
            livro.disponivel = False
            return True
        return False
    
    def devolver_livro(self, livro):
        if livro in self.__livros_emprestados:
            self.__livros_emprestados.remove(livro)
            livro.disponivel = True
            return True
        return False

class Autor:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def livros(self):
        return self.__livros
    
    def adicionar_livro(self, livro):
        self.__livros.append(livro)

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__usuarios = []
        self.__autores = []

    @property
    def livros(self):
        return self.__livros
    
    @property
    def usuarios(self):
        return self.__usuarios
    
    @property
    def autores(self):
        return self.__autores
    
    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        # Verifica se o autor já existe
        for autor in self.__autores:
            if autor.nome == livro.autor.nome:
                autor.adicionar_livro(livro)
                return
        # Se não existe, cria novo autor
        novo_autor = Autor(livro.autor.nome)
        novo_autor.adicionar_livro(livro)
        self.__autores.append(novo_autor)
    
    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)
    
    def buscar_livros(self, **kwargs):
        resultados = []
        for livro in self.__livros:
            match = True
            for key, value in kwargs.items():
                if key == 'titulo':
                    if value.lower() not in livro.titulo.lower():
                        match = False
                elif key == 'autor':
                    if value.lower() != livro.autor.nome.lower():
                        match = False
                elif key == 'isbn':
                    if value != livro.isbn:
                        match = False
                elif key == 'disponivel':
                    if value != livro.disponivel:
                        match = False
            if match:
                resultados.append(livro)
        return resultados
    
    def buscar_usuario(self, usuario_id):
        for usuario in self.__usuarios:
            if usuario.id == usuario_id:
                return usuario
        return None

def mostrar_detalhes_livro(livro):
    print(livro)

def mostrar_detalhes_usuario(usuario):
    print(usuario)

def interface_adicionar_livro(biblioteca):
    print("\nAdicionar Livro")
    titulo = input("Título: ").strip()
    autor_nome = input("Autor: ").strip()
    isbn = input("ISBN: ").strip()
    
    if not titulo or not autor_nome or not isbn:
        print("Todos os campos são obrigatórios!")
        return
    
    autor = Autor(autor_nome)
    livro = Livro(titulo, autor, isbn)
    biblioteca.adicionar_livro(livro)
    print("Livro adicionado com sucesso!")

def interface_emprestar_livro(biblioteca):
    print("\nEmprestar Livro")
    usuario_id = input("ID do usuário: ")
    livro_id = input("ID do livro: ")
    
    try:
        usuario_id = int(usuario_id)
        livro_id = int(livro_id)
    except ValueError:
        print("IDs devem ser números inteiros!")
        return
    
    usuario = biblioteca.buscar_usuario(usuario_id)
    livro = next((livro for livro in biblioteca.livros if livro.id == livro_id), None)
    
    if not usuario or not livro:
        print("Usuário ou livro não encontrado!")
        return
    
    if usuario.emprestar_livro(livro):
        print("Livro emprestado com sucesso!")
    else:
        print("Livro não está disponível para empréstimo!")

def interface_devolver_livro(biblioteca):
    print("\nDevolver Livro")
    usuario_id = input("ID do usuário: ")
    livro_id = input("ID do livro: ")
    
    try:
        usuario_id = int(usuario_id)
        livro_id = int(livro_id)
    except ValueError:
        print("IDs devem ser números inteiros!")
        return
    
    usuario = biblioteca.buscar_usuario(usuario_id)
    livro = next((livro for livro in biblioteca.livros if livro.id == livro_id), None)
    
    if not usuario or not livro:
        print("Usuário ou livro não encontrado!")
        return
    
    if usuario.devolver_livro(livro):
        print("Livro devolvido com sucesso!")
    else:
        print("Este usuário não tinha este livro emprestado!")

def interface_buscar_livros(biblioteca):
    print("\nBuscar Livros")
    print("Preencha os campos que desejar para filtrar:")
    
    criterios = {}
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    isbn = input("ISBN: ").strip()
    disponivel = input("Disponível (S/N): ").strip().upper()
    
    if titulo: criterios['titulo'] = titulo
    if autor: criterios['autor'] = autor
    if isbn: criterios['isbn'] = isbn
    if disponivel in ['S', 'N']:
        criterios['disponivel'] = True if disponivel == 'S' else False
    
    resultados = biblioteca.buscar_livros(**criterios)
    
    if resultados:
        print("\nResultados da busca:")
        for livro in resultados:
            mostrar_detalhes_livro(livro)
    else:
        print("Nenhum livro encontrado!")

def main():
    biblioteca = Biblioteca()
    
    while True:
        print("\n======= Sistema Biblioteca =======")
        print("1. Adicionar Livro")
        print("2. Listar Todos os Livros")
        print("3. Buscar Livros")
        print("4. Emprestar Livro")
        print("5. Devolver Livro")
        print("6. Cadastrar Usuário")
        print("7. Listar Usuários")
        print("0. Sair")
        
        opcao = input("\nOpção: ").strip()
        
        if opcao == "0":
            print("Saindo do sistema...")
            break
            
        elif opcao == "1":
            interface_adicionar_livro(biblioteca)
            
        elif opcao == "2":
            if biblioteca.livros:
                print("\nTodos os Livros:")
                for livro in biblioteca.livros:
                    mostrar_detalhes_livro(livro)
            else:
                print("\nNenhum livro cadastrado!")
                
        elif opcao == "3":
            interface_buscar_livros(biblioteca)
            
        elif opcao == "4":
            interface_emprestar_livro(biblioteca)
            
        elif opcao == "5":
            interface_devolver_livro(biblioteca)
            
        elif opcao == "6":
            nome = input("\nNome do usuário: ").strip()
            if nome:
                usuario = Usuario(nome)
                biblioteca.adicionar_usuario(usuario)
                print("Usuário cadastrado com sucesso!")
            else:
                print("Nome inválido!")
                
        elif opcao == "7":
            if biblioteca.usuarios:
                print("\nUsuários Cadastrados:")
                for usuario in biblioteca.usuarios:
                    mostrar_detalhes_usuario(usuario)
            else:
                print("\nNenhum usuário cadastrado!")
                
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
