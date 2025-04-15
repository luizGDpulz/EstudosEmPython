# Estudos em Python 🐍

Bem-vindo aos estudos em Python! Este material é um guia completo que aborda desde conceitos fundamentais até aspectos avançados da linguagem. É ideal para iniciantes e também serve como referência rápida para programadores experientes.

## 📚 Exemplos Práticos
Todos os exemplos de código mencionados neste guia podem ser encontrados na pasta [Exemplos](./Exemplos):
- [basicos.py](./Exemplos/basicos.py) - Demonstrações de conceitos fundamentais
- [biblioteca.py](./Exemplos/biblioteca.py) - Sistema completo de biblioteca demonstrando POO
- [avancado.py](./Exemplos/avancado.py) - Conceitos avançados como decoradores, async/await, etc.

## ✅ Índice Detalhado
1. [Sintaxe em Python](#1-sintaxe-em-python)  
2. [Variáveis e Tipos de Dados](#2-variáveis-tipos-de-dados-e-operadores)  
3. [Estruturas Condicionais](#3-estruturas-condicionais-if-elif-else)  
4. [Estruturas de Repetição](#4-estruturas-de-repetição-for-while)  
5. [Funções e Sub-rotinas](#5-introdução-a-funções-e-sub-rotinas)  
6. [Comentários e Documentação](#6-comentários-e-documentação-básica-de-código)  
7. [POO: Classes e Objetos](#7-definição-de-classes-e-objetos)  
8. [Encapsulamento](#8-encapsulamento)  
9. [Getter e Setter](#9-métodos-getter-e-setter)  
10. [Exemplo Prático: Biblioteca](#10-criação-de-uma-classe-simples-e-manipulação-de-objetos)
11. [Conceitos Avançados](#11-conceitos-avançados)

---

## 1. Sintaxe em Python
Python é famoso por sua sintaxe clara e legível. Vamos explorar suas características principais:

### 1.1 Indentação
Python usa indentação para definir blocos de código. Isso não é apenas uma convenção de estilo, é uma regra da linguagem:

```python
def funcao():
    if True:
        print("Indentado com 8 espaços")
        for i in range(3):
            print(f"Número {i}")
```

### 1.2 Comentários
```python
# Comentário de uma linha

"""
Comentário de
múltiplas linhas (docstring)
"""
```

### 1.3 Convenções de Nomeação
- Variáveis e funções: `snake_case` (nome_da_variavel)
- Classes: `PascalCase` (NomeDaClasse)
- Constantes: `SCREAMING_SNAKE_CASE` (NOME_DA_CONSTANTE)
- Módulos: nomes curtos, em minúsculas

---

## 2. Variáveis, Tipos de Dados e Operadores

### 2.1 Tipos Básicos
```python
# Números
inteiro = 42
flutuante = 3.14
complexo = 3 + 4j

# Strings
texto = "Python"
texto_multilinha = """
Múltiplas
linhas
"""

# Booleanos
verdadeiro = True
falso = False

# None (null/nil em outras linguagens)
nulo = None
```

### 2.2 Coleções
```python
# Listas (mutáveis)
lista = [1, 2, 3, "python"]

# Tuplas (imutáveis)
tupla = (1, 2, "python")

# Dicionários (chave-valor)
dicionario = {
    "nome": "Python",
    "versao": 3.11
}

# Sets (conjuntos únicos)
conjunto = {1, 2, 3}
```

### 2.3 Operadores
- Aritméticos: `+`, `-`, `*`, `/`, `//` (divisão inteira), `**` (potência), `%` (módulo)
- Comparação: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Lógicos: `and`, `or`, `not`
- Atribuição: `=`, `+=`, `-=`, `*=`, `/=`
- Identidade: `is`, `is not`
- Pertencimento: `in`, `not in`

---

## 3. Estruturas Condicionais

### 3.1 if/elif/else
```python
idade = 18
if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")
```

### 3.2 Operador Ternário
```python
status = "maior" if idade >= 18 else "menor"
```

---

## 4. Estruturas de Repetição

### 4.1 For Loop
```python
# Iterando sobre uma sequência
for i in range(5):
    print(i)

# Iterando sobre uma lista
for item in ["a", "b", "c"]:
    print(item)

# Enumerate para índice e valor
for indice, valor in enumerate(["a", "b", "c"]):
    print(f"{indice}: {valor}")
```

### 4.2 While Loop
```python
contador = 5
while contador > 0:
    print(contador)
    contador -= 1
```

### 4.3 Controle de Loop
- `break`: Sai do loop
- `continue`: Pula para a próxima iteração
- `else`: Executado quando o loop termina normalmente

---

## 5. Introdução a Funções e Sub-rotinas

### 5.1 Definição Básica
```python
def saudacao(nome):
    return f"Olá, {nome}!"
```

### 5.2 Parâmetros
```python
# Parâmetros default
def saudacao(nome="Visitante"):
    return f"Olá, {nome}!"

# Args e Kwargs
def funcao_flexivel(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
```

### 5.3 Type Hints (Python 3.5+)
```python
def soma(a: int, b: int) -> int:
    return a + b
```

---

## 6. Comentários e Documentação

### 6.1 Docstrings
```python
def calcular_media(numeros):
    """
    Calcula a média de uma sequência de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        float: Média dos números
    """
    return sum(numeros) / len(numeros)
```

---

## 7. Definição de Classes e Objetos

### 7.1 Classe Básica
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, sou {self.nome} e tenho {self.idade} anos"
```

### 7.2 Herança
```python
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo
```

---

## 8. Encapsulamento
Python usa convenções de nomeação para indicar encapsulamento:

```python
class Conta:
    def __init__(self):
        self.publico = "Acesso público"
        self._protegido = "Acesso protegido"
        self.__privado = "Acesso privado"
```

---

## 9. Métodos Getter e Setter

### 9.1 Usando @property
```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor
```

---

## 10. Exemplo Prático: Sistema de Biblioteca
Veja um exemplo completo de um sistema de biblioteca em [biblioteca.py](./Exemplos/biblioteca.py), que demonstra:
- Gerenciamento de livros e usuários
- Empréstimo e devolução
- Buscas e relatórios
- Interface de linha de comando

---

## 11. Conceitos Avançados

### 11.1 Decoradores
```python
def medir_tempo(func):
    def wrapper(*args, **kwargs):
        import time
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio}")
        return resultado
    return wrapper

@medir_tempo
def funcao_lenta():
    # código aqui
    pass
```

### 11.2 Context Managers
```python
class MeuContextManager:
    def __enter__(self):
        print("Entrando no contexto")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saindo do contexto")
```

### 11.3 Async/Await
```python
async def funcao_async():
    await asyncio.sleep(1)
    return "Resultado"
```

Para mais exemplos avançados, consulte [avancado.py](./Exemplos/avancado.py).

---

## 🚀 Próximos Passos
1. Pratique com os exemplos fornecidos
2. Explore a documentação oficial do Python
3. Desenvolva seus próprios projetos
4. Participe da comunidade Python

---

## 📚 Recursos Adicionais
- [Documentação Oficial do Python](https://docs.python.org)
- [PEP 8 - Guia de Estilo](https://pep8.org)
- [Python Package Index (PyPI)](https://pypi.org)

---

Lembre-se: A prática é a chave para o aprendizado. Use os exemplos fornecidos como base para seus próprios experimentos!


