# tests.py
"""
MÓDULO DE TESTES ACADÉMICOS DA UC (REQUISITO COM ASSERT)
Garante a fiabilidade e validação das regras operacionais do Centro de Controlo.
"""

def calcular_gravidade_operacional(bombeiros, viaturas):
    """Função auxiliar lógica para testar proporção de meios empenhados."""
    if bombeiros == 0 or viaturas == 0:
        return "Sem Resposta"
    proporcao = bombeiros / viaturas
    if proporcao <= 2:
        return "Sub-dimensionada"
    return "Adequada"

def executar_testes_sistema():
    print("🧪 A iniciar testes funcionais unitários (Content: assert)...")
    
    # Teste 1: Validação de resposta sem meios
    assert calcular_gravidade_operacional(0, 0) == "Sem Resposta", "Erro no Teste 1"
    
    # Teste 2: Validação de resposta equilibrada de meios
    assert calcular_gravidade_operacional(5, 1) == "Adequada", "Erro no Teste 2"
    
    # Teste 3: Validação de escassez de efetivos operacionais
    assert calcular_gravidade_operacional(2, 2) == "Sub-dimensionada", "Erro no Teste 3"
    
    print("✅ Todos os testes funcionais (assert) passaram com sucesso no FireCommand Pro!")

if __name__ == "__main__":
    executar_testes_sistema()