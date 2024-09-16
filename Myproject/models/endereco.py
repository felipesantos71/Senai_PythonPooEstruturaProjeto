class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNumero: {self.numero}"
                f"\nComplemento: {self.complemento}"
                f"\nCEP: {self.cep}"
                f"\nCidade: {self.cidade}")