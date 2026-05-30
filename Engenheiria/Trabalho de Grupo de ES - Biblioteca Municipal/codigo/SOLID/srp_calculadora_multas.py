class CalculadoraMultas:
    TAXA_DIARIA = 0.50

    def calcular_total(self, dias_atraso: int) -> float:
        if dias_atraso <= 0:
            return 0.0
        return dias_atraso * self.TAXA_DIARIA