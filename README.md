# Estudos em Python

Bem-vindo aos estudos em Python! Este material aborda desde conceitos fundamentais até aspectos mais avançados da linguagem. É ideal para iniciantes e também útil como referência rápida.

---

## ✅ Índice
1. Sintaxe em Python  
2. Variáveis, Tipos de Dados e Operadores  
3. Estruturas Condicionais (if, elif, else)  
4. Estruturas de Repetição (for, while)  
5. Funções e Sub-rotinas  
6. Comentários e Documentação  
7. POO: Classes e Objetos  
8. Encapsulamento  
9. Getter e Setter  
10. Exemplo: Classe Calculadora  
11. Extras  

---

## 1. Sintaxe em Python
Python é conhecido por sua sintaxe simples e legível. Vamos explorar alguns conceitos básicos:

### Exemplo de "Hello, World!":
```python
print("Hello, World!")
```
Este é o programa mais simples em Python, que imprime a mensagem "Hello, World!" na tela.

- **Sem ponto e vírgula**: O Python não exige ponto e vírgula ao final das linhas.
- **Indentação**: É obrigatória para definir blocos de código (como dentro de `if`, `for`, funções, etc.).

### Indentação:
```python
if True:
    print("Indentado corretamente")
```

### Comentários:
- Linha única: `# comentário`
- Multilinha:
```python
'''
Comentário de múltiplas linhas
'''
```

---

## 2. Variáveis, Tipos de Dados e Operadores
```python
x = 10        # Inteiro
y = 3.14      # Float
nome = "Alice"  # String
ativo = True  # Booleano
```
Python detecta o tipo automaticamente. Você pode usar operadores matemáticos (+, -, *, /, %, //, **) e operadores lógicos (and, or, not).

### Operações Matemáticas
```python
soma = x + y
potencia = x ** 2
resto = x % 3
```

### Concatenação de strings
```python
mensagem = "Olá, " + nome
print(mensagem)
```

---

## 3. Estruturas Condicionais (if, elif, else)
```python
idade = 20
if idade >= 18:
    print("Você é maior de idade.")
elif idade > 12:
    print("Você é adolescente.")
else:
    print("Você é criança.")
```
Python usa `if`, `elif` e `else` sem parênteses, e os blocos são definidos por indentação.

---

## 4. Estruturas de Repetição (for, while)
### `for`
```python
for i in range(5):
    print(i)
```
`range(5)` gera números de 0 a 4.

### `while`
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```
O loop continua enquanto a condição for verdadeira.

---

## 5. Introdução a Funções e Sub-rotinas
```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")
```
Funções são definidas com `def`. `f"{nome}"` é uma f-string, usada para interpolar variáveis.

---

## 6. Comentários e Documentação Básica de Código
### 6.1 Comentários de Linha Única
```python
# Esta função calcula a soma de dois números
def soma(a, b):
    return a + b
```

### 6.2 Docstrings
```python
def soma(a, b):
    """
    Retorna a soma de dois números.

    Argumentos:
    a -- o primeiro número
    b -- o segundo número
    """
    return a + b
```
`Docstrings` são usados para documentar funções, classes e módulos.

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
print(vars(meu_carro))
meu_carro.acelerar()
```
- `__init__` é o construtor.
- `self` referencia o próprio objeto.

### 7.1 Instâncias, Atributos e Métodos
- **Instância**: `meu_carro` é uma instância da classe `Carro`.
- **Atributos**: `marca`, `modelo`, `ano`.
- **Métodos**: `acelerar`, `frear`.

---

## 8. Encapsulamento
### Público
```python
class Carro:
    def __init__(self, marca):
        self.marca = marca
```

### Protegido (convenção: _underscore)
```python
class Carro:
    def __init__(self, marca):
        self._marca = marca
```

### Privado (convenção: __duplo underscore)
```python
class Carro:
    def __init__(self, marca):
        self.__marca = marca
```

---

## 9. Métodos Getter e Setter
### Getter
```python
class Carro:
    def __init__(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca
```

### Setter
```python
class Carro:
    def __init__(self, marca):
        self.__marca = marca

    def set_marca(self, marca):
        self.__marca = marca
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
            print("Erro: Divisão por zero não é permitida.")

    def get_resultado(self):
        return self._resultado

    def reset(self):
        self._resultado = 0
```

---

## 11. Extras
### Conversão de tipos
```python
numero_str = "123"
numero_int = int(numero_str)
print(numero_int + 10)
```

### Listas
```python
frutas = ["maçã", "banana", "uva"]
print(frutas[0])  # maçã
```

### Dicionários
```python
pessoa = {"nome": "João", "idade": 30}
print(pessoa["nome"])
```

### Laços com enumerate()
```python
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
```

### List comprehension
```python
quadrados = [x**2 for x in range(5)]
print(quadrados)  # [0, 1, 4, 9, 16]
```

### Manipulação de arquivos
```python
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!")
```

---

Pronto! Agora você tem uma base sólida de Python. Explore mais e pratique bastante!

