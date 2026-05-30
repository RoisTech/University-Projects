from abc import ABC, abstractmethod

class Leitor(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    @abstractmethod
    def pode_requisitar(self) -> bool:
        pass

class LeitorAdulto(Leitor):
    def pode_requisitar(self) -> bool:
        return True

class LeitorSuspenso(Leitor):
    def pode_requisitar(self) -> bool:
        return False