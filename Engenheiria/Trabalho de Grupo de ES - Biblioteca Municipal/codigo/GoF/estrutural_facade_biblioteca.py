class BibliotecaFacade:
    def __init__(self, stock_service, emprestimo_service):
        self._stock = stock_service
        self._gestor = emprestimo_service

    def efetuar_emprestimo(self, leitor, exemplar) -> bool:
        if leitor.tem_multas_actives():
            return False
        
        self._stock.atualizar_disponibilidade(exemplar, False)
        self._gestor.registrar_saida(leitor, exemplar)
        return True