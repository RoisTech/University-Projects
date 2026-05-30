from abc import ABC, abstractmethod

class Leitor(ABC):
    def __init__(self, nome: str):
        self.nome = nome

class LeitorJovem(Leitor):
    def __init__(self, nome: str):
        super().__init__(nome)

class LeitorFactory(ABC):
    @abstractmethod
    def criar_leitor(self, nome: str) -> Leitor:
        pass

class FabricaLeitorJovem(LeitorFactory):
    def criar_leitor(self, nome: str) -> Leitor:
        # Centraliza a criação do objeto com as suas restrições nativas
        return LeitorJovem(nome)

# Código do Cliente (Usa a abstração da fábrica)
fabrica: LeitorFactory = FabricaLeitorJovem()
novo_leitor = fabrica.criar_leitor("João Alves")