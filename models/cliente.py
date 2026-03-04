class Cliente:
    def __init__(self, id: int, nome: str, email: str, telefone: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }
    
    @classmethod
    def from_dict(cls, dados: dict) -> "Cliente":
        return cls(
            id=dados["id"],
            nome=dados["nome"],
            email=dados["email"],
            telefone=dados["telefone"]
        )
    def __str__(self) -> str:
        return f"[{self.id}] {self.nome} | {self.email} | {self.telefone}"