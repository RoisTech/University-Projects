from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def atualizar(self, titulo) -> None:
        pass

class ReservaAtiva(Observer):
    def __init__(self, email_leitor: str):
        self._email = email_leitor

    def atualizar(self, titulo) -> None:
        print(f"Notificação enviada para {self._email}: O livro '{titulo.nome}' já se encontra disponível.")

class Titulo:
    def __init__(self, nome: str):
        self.nome = nome
        self._observadores: List[Observer] = []

    def adicionar_observador(self, observador: Observer) -> None:
        self._observadores.append(observador)

    def exemplar_devolvido(self) -> None:
        # Quando um exemplar entra em stock, avisa automaticamente os interessados
        for observador in self._observadores:
            observador.atualizar(self)