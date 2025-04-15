#!/usr/bin/env python3

def demonstrar_tipos_basicos():
    # Números
    inteiro = 42
    decimal = 3.14
    complexo = 3 + 4j
    
    print(f"Inteiro: {inteiro}, tipo: {type(inteiro)}")
    print(f"Decimal: {decimal}, tipo: {type(decimal)}")
    print(f"Complexo: {complexo}, tipo: {type(complexo)}")
    
    # Strings
    texto = "Python é incrível!"
    print(f"\nString: {texto}")
    print(f"Maiúsculo: {texto.upper()}")
    print(f"Minúsculo: {texto.lower()}")
    print(f"Quantidade de caracteres: {len(texto)}")
    
    # Listas
    lista = [1, 2, 3, "python", True]
    print(f"\nLista: {lista}")
    lista.append(4)
    print(f"Lista após append(4): {lista}")
    print(f"Primeiro elemento: {lista[0]}")
    print(f"Último elemento: {lista[-1]}")
    
    # Tuplas (imutáveis)
    tupla = (1, 2, "python")
    print(f"\nTupla: {tupla}")
    
    # Dicionários
    dicionario = {
        "nome": "Alice",
        "idade": 30,
        "linguagens": ["Python", "JavaScript"]
    }
    print(f"\nDicionário: {dicionario}")
    print(f"Nome: {dicionario['nome']}")
    print(f"Linguagens: {dicionario['linguagens']}")

def demonstrar_controle_fluxo():
    # if/elif/else
    idade = 18
    if idade < 13:
        print("Criança")
    elif idade < 20:
        print("Adolescente")
    else:
        print("Adulto")
    
    # for loop
    print("\nContagem:")
    for i in range(1, 6):
        print(i, end=" ")
    
    # while loop
    print("\n\nContagem regressiva:")
    contador = 5
    while contador > 0:
        print(contador, end=" ")
        contador -= 1

def calcular_media(*args):
    """
    Calcula a média de uma sequência de números.
    
    Args:
        *args: Números para calcular a média
        
    Returns:
        float: Média dos números fornecidos
    """
    if not args:
        return 0
    return sum(args) / len(args)

def manipular_arquivos():
    # Escrevendo em um arquivo
    with open("exemplo.txt", "w") as arquivo:
        arquivo.write("Olá, Python!\n")
        arquivo.write("Esta é uma demonstração de manipulação de arquivos.")
    
    # Lendo o arquivo
    print("\nConteúdo do arquivo:")
    with open("exemplo.txt", "r") as arquivo:
        print(arquivo.read())

if __name__ == "__main__":
    print("=== Demonstração de Tipos Básicos ===")
    demonstrar_tipos_basicos()
    
    print("\n=== Demonstração de Controle de Fluxo ===")
    demonstrar_controle_fluxo()
    
    print("\n=== Demonstração de Funções ===")
    notas = [7.5, 8.0, 6.5, 9.0]
    media = calcular_media(*notas)
    print(f"Média das notas {notas}: {media:.2f}")
    
    print("\n=== Demonstração de Manipulação de Arquivos ===")
    manipular_arquivos()