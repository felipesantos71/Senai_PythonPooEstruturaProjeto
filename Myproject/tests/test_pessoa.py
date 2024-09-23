import pytest
from Myproject.models.pessoa  import Pessoa #Caminho absoluto
from Myproject.models.endereco import Endereco #Caminho absoluto
from Myproject.models.enums.sexo import Sexo #Caminho absoluto
from Myproject.models.enums.unidade_federativa import UnidadeFederativa #Caminho absoluto

# Modelo.
@pytest.fixture
def criar_pessoa():
    pessoa_01 = Pessoa(36987, "Jose", "02/05/1992", "(71)99999-8888", "js236@outlook.com", 32, Sexo.MASCULINO, 
                   Endereco("Rua Marasol", 48, "Apartamento C", "40320-480", "Salvador"), UnidadeFederativa.BAHIA)
    return pessoa_01

def test_id_valida(criar_pessoa):
    assert criar_pessoa.id == 36987

def test_pessoa_valida_nome(criar_pessoa):
    assert criar_pessoa.nome == "Jose"

def test_pessoa_valida_nome_alteracao(criar_pessoa):
    criar_pessoa.nome = "Adelaide"
    assert criar_pessoa.nome == "Adelaide"

def test_idade_valida(criar_pessoa):
    assert criar_pessoa.idade == 32

def test_idade_negativa_retorna_mensagem_excessao(criar_pessoa):
    with pytest.raises(ValueError, match="Idade não pode ser negativa."):
        Pessoa(36987, "Jose", "02/05/1992", "(71)99999-8888", "js236@outlook.com", -4, Sexo.MASCULINO, 
                   Endereco("Rua Marasol", 48, "Apartamento C", "40320-480", "Salvador"), UnidadeFederativa.BAHIA)

def test_pessoa_valida_sexo(criar_pessoa):
    assert criar_pessoa.sexo == Sexo.MASCULINO