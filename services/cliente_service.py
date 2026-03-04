from models.cliente import Cliente
from utils.arquivo import ler_dados, salvar_dados
from utils.validadores import validar_cliente
def _proximo_id(clientes: list) -> int:
    if not clientes:
        return 1
    return max(c.id for c in clientes) + 1

def _carregar() -> list:
    return [Cliente.from_dict(d) for d in ler_dados()]

def _persistir(clientes: list) -> None:
    salvar_dados([c.to_dict() for c in clientes])

def adicionar_cliente(nome: str, email: str, telefone: str) -> Cliente:
    valido, erro = validar_cliente(nome, email, telefone)
    if not valido:
        raise ValueError("Erro de validação: " + "; ".join(erro))

    clientes = _carregar()
    novo = Cliente(
        id=_proximo_id(clientes),
        nome=nome,
        email=email,
        telefone=telefone
    )
    clientes.append(novo)
    _persistir(clientes)
    return novo

def listar_clientes() -> list:
    return _carregar()

def buscar_por_nome(nome: str) -> list:
    clientes = _carregar()
    return [c for c in clientes if nome.lower() in c.nome.lower()]

def editar_cliente(id: int, nome: str, email: str, telefone: str) -> Cliente:
    valido, erro = validar_cliente(nome, email, telefone)
    if not valido:
        raise ValueError("Erro de validação: " + "; ".join(erro))


    clientes = _carregar()
    for c in clientes:
        if c.id == id:
            c.nome = nome
            c.email = email
            c.telefone = telefone
            _persistir(clientes)
            return c
    raise ValueError("Cliente não encontrado")

def remover_cliente(id: int) -> bool:
    clientes = _carregar()
    for c in clientes:
        if c.id == id:
            clientes.remove(c)
            _persistir(clientes)
            return True
    return False