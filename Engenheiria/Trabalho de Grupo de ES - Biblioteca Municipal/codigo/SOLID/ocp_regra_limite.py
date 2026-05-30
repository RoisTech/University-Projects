from abc import ABC, abstractmethod

class RegraLimite(ABC):
    @abstractmethod
    def obter_limite_maximo(self) -> int:
        pass

class RegraLeitorAdulto(RegraLimite):
    def obter_limite_maximo(self) -> int:
        return 5

class RegraLeitorJovem(RegraLimite):
    def obter_limite_maximo(self) -> int:
        return 3