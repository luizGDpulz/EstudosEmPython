# Estudos em Python

## 1. Sintaxe em Python
Python é conhecido por sua sintaxe simples e legível. Vamos explorar alguns conceitos básicos:

### Exemplo de "Hello, World!":
```python
print("Hello, World!")
```
Este é o programa mais simples em Python, que imprime a mensagem "Hello, World!" na tela.

### Conceitos Importantes:
- **Indentacão:**
  A indentacão define a estrutura do código. Blocos como loops e condicionais devem ser consistentemente indentados.

- **Comentários:**
  - Linha única: `# Comentário`
  - Múltiplas linhas:
    ```python
    '''
    Comentário de
    várias linhas
    '''
    ```

## 2. Variáveis, Tipos de Dados e Operadores
```python
x = 10           # Inteiro
y = 3.14         # Float
nome = "Alice"    # String
ativo = True     # Booleano
```

## 3. Estruturas Condicionais (if, elif, else)
```python
idade = 20  # int(input("Insira a sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
elif 12 < idade < 18:
    print("Você é adolescente.")
else:
    print("Você é criança.")
```

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

## 5. Introdução a Funções e Sub-rotinas
```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")
```

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

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)
print(vars(meu_carro))
meu_carro.acelerar()
```

### 7.1 Instâncias, Atributos e Métodos
- **Instância:** Objeto criado a partir de uma classe. Ex: `meu_carro`
- **Atributos:** Variáveis da classe. Ex: `marca`, `modelo`, `ano`
- **Métodos:** Funções dentro da classe. Ex: `acelerar`, `frear`

## 8. Encapsulamento

### Atributo Público
```python
class Carro:
    def __init__(self, marca):
        self.marca = marca
```

### Atributo Protegido
```python
class Carro:
    def __init__(self, marca):
        self._marca = marca
```

### Atributo Privado
```python
class Carro:
    def __init__(self, marca):
        self.__marca = marca
```

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

## 10. Criação de uma Classe Simples e Manipulação de Objetos
### Exemplo: Classe Calculadora
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

