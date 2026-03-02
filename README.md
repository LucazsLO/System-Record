# 📋 Sistema de Cadastro de Clientes

Sistema simples de gerenciamento de clientes desenvolvido em Python rodando direto no terminal, sem banco de dados ou APIs externas. Os dados são persistidos localmente em um arquivo JSON.

---

## �️ Estrutura do Projeto

O projeto está organizado na seguinte estrutura:

```
system record py/
│
├── main.py                    ← Ponto de entrada da aplicação
├── menu.py                    ← Interface com o usuário (inputs e prints)
│
├── models/
│   ├── __init__.py
│   └── cliente.py             ← Estrutura/modelo do objeto Cliente e serialização
│
├── services/
│   ├── __init__.py
│   └── cliente_service.py     ← Regras de negócio (adicionar, buscar, editar, remover)
│
├── utils/
│   ├── __init__.py
│   └── arquivo.py             ← Leitura e escrita no arquivo JSON
│
└── data/
    └── clientes.json          ← Criado automaticamente na primeira execução
```

---

## ⚙️ Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

- ✅ **Adicionar Cliente**: Insere um novo cliente com Nome, Email e Telefone.
- ✅ **Listar Clientes**: Exibe todos os clientes cadastrados de forma tabular ordenada.
- ✅ **Buscar Cliente por Nome**: Localiza clientes com base em um trecho do nome fornecido.
- ✅ **Editar Cliente**: Permite a visualização prévia da lista para alterar os dados (Nome, Email ou Telefone) de um cliente existente através do seu ID.
- ✅ **Remover Cliente**: Deleta um cliente existente (exigindo confirmação) a partir do seu ID.
- ✅ **Persistência de dados em JSON**: Os dados são salvos em `data/clientes.json`.

---

## 🚀 Como executar

**Pré-requisito:** Ter o [Python](https://www.python.org/downloads/) (versão 3.10 ou superior) instalado em sua máquina.

```bash
# Acesse a pasta do projeto (caso ainda não esteja)
cd "system record py" # ou ajuste se necessário para o seu caminho

# Execute o sistema
python main.py
```

---

## 🏛️ Arquitetura em Camadas

O projeto segue o princípio de **separação de responsabilidades**, onde cada camada conhece apenas o necessário:

```
Usuário
   ↓
menu.py          → fala com o usuário (input/print)
   ↓
cliente_service  → aplica as regras de negócio
   ↓          ↓
arquivo.py   cliente.py
(JSON)       (estrutura dos dados)
```

| Camada | Responsabilidade |
|--------|-----------------|
| `models/` | Define **o que é** um Cliente e como ele se converte em dicionário (`to_dict`/`from_dict`) |
| `utils/` | Define **como** os dados são salvos (Lida com o JSON e sistema de arquivos) |
| `services/` | Define **o que o sistema faz** (CRUD e validações de negócio) |
| `menu.py` | Define **como o usuário interage** |
| `main.py` | Inicializa a aplicação |

---

## 👨‍💻 Contribuindo 

Este é um projeto simples feito para fins de estudo em Python, sendo de uso educacional livre. 