from app.funcao import funcao_ola_pessoal

def test_funcao_ola_pessoal():
    saida = funcao_ola_pessoal()
    gabarito = "Olá pessoal!"   
    assert saida == gabarito