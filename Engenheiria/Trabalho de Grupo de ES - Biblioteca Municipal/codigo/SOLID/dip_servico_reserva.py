from abc import ABC, abstractmethod

class SistemaNotificacoes(ABC):
    @abstractmethod
    def enviar_confirmacao(self, email: str) -> None:
        pass

class ServicoReserva:
    def __init__(self, notificador: SistemaNotificacoes):
        self._notificador = notificador  # Injeção da dependência por construtor

    def confirmar(self, email: str) -> None:
        # Depende da interface abstrata, não de um serviço web concreto
        self._notificador.enviar_confirmacao(email)