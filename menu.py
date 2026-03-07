from services.cliente_service import (
    adicionar_cliente,
    listar_clientes,
    buscar_por_nome,
    editar_cliente,
    remover_cliente
)

from utils.exceptions import ValidacaoClienteError, ClienteNaoEncontradoError

def _input_campo(label: str, valor_atual: str = None) -> str:
    if valor_atual:
        entrada = input(f"  > {label} [{valor_atual}]: ").strip()
        return entrada if entrada else valor_atual
    return input(f"  > {label}: ").strip()

def tela_adicionar() -> None:
    print("=== Adicionar Cliente ===")
    nome = _input_campo("Nome")
    email = _input_campo("Email")
    telefone = _input_campo("Telefone") 
    try:
        cliente = adicionar_cliente(nome, email, telefone)
        print(f"Cliente {cliente.nome} adicionado com ID {cliente.id}.")
    except ValidacaoClienteError as e:
        print(f"Erro ao cadastrar cliente: {e}")

def tela_listar() -> None:
    clientes = listar_clientes()
    if not clientes:
        print("Nenhum cliente encontrado.")
        return
    
    print("=== Lista de Clientes ===")
    print(f"\n{'ID':<5} {'Nome':<25} {'Email':<30} {'Telefone'}")
    print("-" * 70)
    for c in clientes:
        print(f"{c.id:<5} {c.nome:<25} {c.email:<30} {c.telefone}")

def tela_buscar() -> None:
    termo = input("\n  > Digite o nome para buscar: ").strip()
    resultados = buscar_por_nome(termo)
    if not resultados:
        print("Nenhum cliente encontrado com esse nome.")
        return
    for c in resultados:
        print(c)

def tela_editar() -> None:
    tela_listar()
    try:
        id_busca = int(input("\n  > Digite o ID do cliente a editar: "))
    except ValidacaoClienteError as e:
        print(f"Erro de validação: {e}")
    except ClienteNaoEncontradoError:
        print("Erro: Nenhum cliente com esse ID foi encontrado no banco de dados.")
        return

    clientes = listar_clientes()
    atual = next((c for c in clientes if c.id == id_busca), None)
    if not atual:
        print("Cliente não encontrado.")
        return

    print(f"\nEditando cliente: {atual.nome}")
    nome = _input_campo("Novo Nome", atual.nome)
    email = _input_campo("Novo Email", atual.email)
    telefone = _input_campo("Novo Telefone", atual.telefone)

    try:
        editar_cliente(id_busca, nome, email, telefone)
        print("Cliente atualizado com sucesso!")
    except ValidacaoClienteError as e:
        print(f"Erro ao atualizar cliente: {e}")
    except ClienteNaoEncontradoError as e:
        print(f"Erro ao atualizar cliente: {e}")


def tela_remover() -> None:
    tela_listar()
    try:
        id_busca = int(input("\n  > Digite o ID do cliente a remover: "))
    except ValueError: 
        print("ID inválido.")
        return
    clientes = listar_clientes()
    atual = next ((c for c in clientes if c.id == id_busca), None)
    if not atual:
        print("Cliente não encontrado.")
        return
    confirma = input(f"\n  > Tem certeza que deseja remover {atual.nome}? (s/n): ")
    if confirma.lower() == "s":
        remover_cliente(id_busca)
        print("Cliente removido.")
    else:        
        print("Operação cancelada.")

def exibir_menu() -> None:
    opcoes = {
        "1": ("Adicionar Cliente", tela_adicionar),
        "2": ("Listar Clientes", tela_listar),
        "3": ("Buscar Cliente por Nome", tela_buscar),
        "4": ("Editar Cliente", tela_editar),
        "5": ("Remover Cliente", tela_remover),
        "0": ("Sair", lambda: None)
    }
    while True:
        print("\n=== Menu de Clientes ===")
        for chave, (descricao, _) in opcoes.items():
            print(f"{chave}. {descricao}")
        print("===========================")

        escolha: str = input("\n  > Escolha uma opção: ").strip()

        if escolha == "0":
            print("Até logo!")
            break
        elif escolha in opcoes:
            opcoes[escolha][1]()
        else:
            print("Opção inválida.")
