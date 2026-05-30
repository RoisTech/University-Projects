from abc import ABC, abstractmethod

class Pesquisavel(ABC):
    @abstractmethod
    def pesquisar_por_titulo(self, titulo: str) -> None:
        pass

class Reservavel(ABC):
    @abstractmethod
    def adicionar_reserva(self, leitor) -> None:
        pass

# Classe que implementa ambas as interfaces abstratas
class TituloFisico(Pesquisavel, Reservavel):
    def pesquisar_por_titulo(self, titulo: str) -> None:
        # Lógica de busca no catálogo
        pass

    def adicionar_reserva(self, leitor) -> None:
        # Lógica de inserção na fila de espera
        pass