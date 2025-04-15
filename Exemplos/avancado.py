#!/usr/bin/env python3
from typing import List, Dict, Optional, Generator
from dataclasses import dataclass
from abc import ABC, abstractmethod
import threading
import asyncio
from time import time as get_time

# Decoradores
def medir_tempo(func):
    """Decorator para medir o tempo de execução de uma função"""
    from time import time
    
    def wrapper(*args, **kwargs):
        inicio = time()
        resultado = func(*args, **kwargs)
        fim = time()
        print(f"Função {func.__name__} levou {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

# Type Hints e Dataclasses
@dataclass
class Produto:
    nome: str
    preco: float
    quantidade: int = 0
    
    def valor_total(self) -> float:
        return self.preco * self.quantidade

# Classes Abstratas
class Animal(ABC):
    @abstractmethod
    def fazer_som(self) -> str:
        pass

class Cachorro(Animal):
    def fazer_som(self) -> str:
        return "Au au!"

class Gato(Animal):
    def fazer_som(self) -> str:
        return "Miau!"

# Generators
def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Context Managers
class Timer:
    def __enter__(self):
        self.start = get_time()
        return self
    
    def __exit__(self, *args):
        self.end = get_time()
        self.interval = self.end - self.start

# Programação Assíncrona
async def tarefa_demorada(nome: str, segundos: int) -> None:
    print(f"Iniciando {nome}")
    await asyncio.sleep(segundos)
    print(f"Finalizando {nome}")

async def executar_tarefas():
    tarefas = [
        tarefa_demorada("Tarefa 1", 2),
        tarefa_demorada("Tarefa 2", 1),
        tarefa_demorada("Tarefa 3", 3)
    ]
    await asyncio.gather(*tarefas)

# Threads
def thread_function(name: str):
    print(f"Thread {name}: iniciando")
    import time
    time.sleep(2)
    print(f"Thread {name}: finalizando")

@medir_tempo
def demonstrar_threads():
    threads = []
    for i in range(3):
        t = threading.Thread(target=thread_function, args=(f"Thread-{i}",))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    # Demonstração de Type Hints e Dataclasses
    produto = Produto("Notebook", 3500.00, 2)
    print(f"Valor total: R${produto.valor_total():.2f}")
    
    # Demonstração de Classes Abstratas
    animais = [Cachorro(), Gato()]
    for animal in animais:
        print(f"O animal faz: {animal.fazer_som()}")
    
    # Demonstração de Generators
    print("\nSequência Fibonacci:")
    for num in fibonacci(10):
        print(num, end=" ")
    print()
    
    # Demonstração de Context Managers
    with Timer() as timer:
        import time
        time.sleep(1)
    print(f"\nTempo decorrido: {timer.interval:.2f} segundos")
    
    # Demonstração de Threads
    print("\nDemonstrando Threads:")
    demonstrar_threads()
    
    # Demonstração de Async/Await
    print("\nDemonstrando Async/Await:")
    asyncio.run(executar_tarefas())