class SistemaClienteError(Exception):
    """Classe base para todas as exceções do nosso sistema."""
    pass

class ValidacaoClienteError(SistemaClienteError):
    """Lançada quando os dados do cliente (nome, email, telefone) são inválidos."""
    pass

class ClienteNaoEncontradoError(SistemaClienteError):
    """Lançada quando tenta buscar, editar ou remover um ID que não existe."""
    pass
