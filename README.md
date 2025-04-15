# Estudos em Python

Bem-vindo aos estudos em Python! Este material aborda desde conceitos fundamentais até aspectos mais avançados da linguagem. É ideal para iniciantes e também útil como referência rápida.

---

## ✅ Índice
1. [Sintaxe em Python](#1-sintaxe-em-python)
2. [Variáveis, Tipos de Dados e Operadores](#2-variáveis-tipos-de-dados-e-operadores)
3. [Estruturas Condicionais](#3-estruturas-condicionais-if-elif-else)
4. [Estruturas de Repetição](#4-estruturas-de-repetição-for-while)
5. [Funções e Sub-rotinas](#5-introdução-a-funções-e-sub-rotinas)
6. [Comentários e Documentação](#6-comentários-e-documentação-básica-de-código)
7. [POO: Classes e Objetos](#7-definição-de-classes-e-objetos)
8. [Encapsulamento](#8-encapsulamento)
9. [Getter e Setter](#9-métodos-getter-e-setter)
10. [Exemplo: Classe Calculadora](#10-criação-de-uma-classe-simples-e-manipulação-de-objetos)
11. [Extras](#11-extras)
    - [Listas, Tuplas e Dicionários](#listas-tuplas-e-dicionários)
    - [Importação de Módulos](#importação-de-módulos)
    - [Tratamento de Exceções](#tratamento-de-exceções)
    - [List Comprehensions](#list-comprehensions)
    - [Lambda e Funções Anônimas](#lambda-e-funções-anônimas)

---

## 1. Sintaxe em Python
Python é conhecido por sua sintaxe simples e legível. Vamos explorar alguns conceitos básicos:

### Exemplo: "Hello, World!"
```python
print("Hello, World!")
```

### Conceitos Importantes:
- **Indentação:** define blocos de código. É obrigatória!
- **Comentários:**
  - Linha única: `# Exemplo`
  - Multilinhas:
    ```python
    '''
    Comentário de múltiplas linhas
    '''
    ```

---

## 2. Variáveis, Tipos de Dados e Operadores
```python
x = 10             # int
pi = 3.14          # float
nome = "Alice"      # str
ativo = True       # bool
```

### Operadores:
- Aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Relacionais: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Lógicos: `and`, `or`, `not`

---

## 3. Estruturas Condicionais (if, elif, else)
```python
idade = 20

if idade >= 18:
    print("Maior de idade")
elif 13 <= idade < 18:
    print("Adolescente")
else:
    print("Criança")
```

---

## 4. Estruturas de Repetição (for, while)
### `for`
```python
for i in range(5):
    print(i)
```

### `while`
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

---

## 5. Introdução a Funções e Sub-rotinas
```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")
```

---

## 6. Comentários e Documentação Básica de Código
### Comentário de Linha Única
```python
# Função que soma dois valores
def soma(a, b):
    return a + b
```

### Docstrings
```python
def soma(a, b):
    """
    Retorna a soma de dois números.
    Argumentos:
    - a: int ou float
    - b: int ou float
    """
    return a + b
```

---

## 7. Definição de Classes e Objetos
```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f"O {self.modelo} está acelerando.")

    def frear(self):
        print(f"O {self.modelo} está freando.")

meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.acelerar()
```

### Conceitos:
- **Instância:** objeto criado a partir de uma classe.
- **Atributos:** propriedades (variáveis).
- **Métodos:** comportamentos (funções).

---

## 8. Encapsulamento
### Público
```python
self.marca = marca
```
### Protegido
```python
self._marca = marca
```
### Privado
```python
self.__marca = marca
```

---

## 9. Métodos Getter e Setter
```python
class Carro:
    def __init__(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

    def set_marca(self, nova_marca):
        self.__marca = nova_marca
```

---

## 10. Criação de uma Classe Simples e Manipulação de Objetos
```python
class Calculadora:
    def __init__(self):
        self._resultado = 0

    def somar(self, valor):
        self._resultado += valor

    def subtrair(self, valor):
        self._resultado -= valor

    def multiplicar(self, valor):
        self._resultado *= valor

    def dividir(self, valor):
        if valor != 0:
            self._resultado /= valor
        else:
            print("Erro: divisão por zero.")

    def get_resultado(self):
        return self._resultado

    def reset(self):
        self._resultado = 0
```

---

## 11. Extras

### Listas, Tuplas e Dicionários
```python
lista = [1, 2, 3]
tupla = (1, 2, 3)
dicionario = {"nome": "Alice", "idade": 30}
```

### Importação de Módulos
```python
import math
print(math.sqrt(25))
```

### Tratamento de Exceções
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero!")
```

### List Comprehensions
```python
quadrados = [x**2 for x in range(5)]
```

### Lambda e Funções Anônimas
```python
quadrado = lambda x: x * x
print(quadrado(5))
```

---

## 📌 Dicas Finais
- Use `help()` para consultar documentação no terminal.
- Utilize `type()` para verificar o tipo de uma variável.
- Organize o código em funções reutilizáveis.
- Comente seu código! Isso ajuda você e outras pessoas no futuro.

---

Se quiser aprofundar ainda mais, recomendo estudar:
- Manipulação de arquivos
- Módulos externos (como `requests`, `pandas`, `flask`)
- Testes unitários com `unittest` ou `pytest`
- Programação assíncrona com `asyncio`
- Estruturas avançadas de dados (filas, pilhas, árvores)

---

🚀 Continue praticando e explorando o mundo Python!

