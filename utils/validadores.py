import re

def validador_nome (nome: str) -> tuple [bool, str]:
    if not nome or not nome.strip():
        return False, "O nome é obrigatório."
    if len(nome.strip()) < 3:
        return False, "O nome deve conter pelo menos 3 caracteres."
    return True, ""

def validador_email (email: str) -> tuple [bool, str]:
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    if not email or not email.strip():
        return False, "O email é obrigatório."
    if not re.match(padrao, email.strip()):
        return False, " Email inválido. Use o formato nome@dominio.com"
    return True, ""

def validador_telefone (telefone: str) -> tuple [bool, str]:
    if not telefone or not telefone.strip():
        return False, "O telefone é obrigatório."
    apenas_digitos = re.sub(r"[\s\-\(\)]", "", telefone) 
    if not apenas_digitos.isdigit():
        return False, "O telefone deve conter apenas números, espaços ou hífens."
    if len(apenas_digitos) < 8:
        return False, "O telefone deve conter pelo menos 8 dígitos."
    return True, ""

def validar_cliente (nome: str,email: str, telefone: str) -> tuple [bool, list[str]]:
    erros = []

    ok, msg = validador_nome(nome)
    if not ok:
        erros.append(msg)

    ok, msg = validador_email(email)
    if not ok:
        erros.append(msg)

    ok, msg = validador_telefone(telefone)
    if not ok:
        erros.append(msg)

    return len(erros) == 0, erros
    