import os
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa
os.system("cls ||clear")

#Instanciando classe.
pessoa_01 = Pessoa(36987, "Jose", "02/05/1992", "(71)99999-8888", "js236@outlook.com", 32, Sexo.MASCULINO, 
                   Endereco("Rua Marasol", 48, "Apartamento C", "40320-480", "Salvador"), UnidadeFederativa.BAHIA)

print(pessoa_01)