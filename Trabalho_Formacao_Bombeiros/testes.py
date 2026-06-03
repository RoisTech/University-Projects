from logica import inserir_materia, matricular_e_avaliar, remover_materia_e_vinculos

def executar_testes_sistema():
    print("A inicializar rotinas de integridade estrutural (assert)...")
    m_teste = []
    b_teste = []
    
    ok, msg = inserir_materia(m_teste, "MOD_UNIT", "Teste Unitário", 10, "Teórica")
    assert ok is True
    
    ok_duplicado, msg = inserir_materia(m_teste, "MOD_UNIT", "Outro Nome", 20, "Prática")
    assert ok_duplicado is False
    
    matricular_e_avaliar(b_teste, m_teste, "Recruta Teste", "MOD_UNIT", 15.0)
    assert len(b_teste) == 1
    
    remover_materia_e_vinculos(m_teste, b_teste, "MOD_UNIT")
    assert len(m_teste) == 0
    assert len(b_teste) == 0
    
    print("Todas as asserções de segurança passaram com distinção!")
