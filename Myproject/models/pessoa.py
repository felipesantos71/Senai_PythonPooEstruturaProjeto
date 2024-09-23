from Myproject.models.enums.sexo import Sexo
from Myproject.models.endereco import Endereco
from Myproject.models.enums.unidade_federativa import UnidadeFederativa

class Pessoa:
    def __init__(self,id: int, nome: str, dataNascimento: str, telefone: str, email: str, idade: int, sexo: Sexo, endereco: Endereco, unidadeFederativa: UnidadeFederativa) -> None:
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.idade = self._verificar_idade(idade)
        self.sexo = sexo
        self.endereco = endereco
        self.unidadeFederativa = unidadeFederativa
        
    def _verificar_idade(self, idade):
        if idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        if not isinstance(idade, int):
            raise TypeError("A idade dece conter apenas números")

        return idade 

    def __str__(self) -> str:
        return (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nData Nascimento: {self.dataNascimento}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.texto}"
                f"\nSexo: {self.sexo.caracter}"
                f"\nEndereco {self.endereco}"
                f"\nUF: {self.unidadeFederativa.estado}"
                f"\nSigla: {self.unidadeFederativa.sigla}")