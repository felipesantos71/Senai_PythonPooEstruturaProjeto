from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa
class Pessoa:
    def __init__(self,id: int, nome: str, dataNascimento: str, telefone: str, email: str, idade: int, sexo: Sexo, endereco: Endereco, unidadeFederativa: UnidadeFederativa) -> None:
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco
        self.unidadeFederativa = unidadeFederativa

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