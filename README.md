# 📝 Gerenciador de Tarefas em Python com uso de arquivo JSON

Este é um simples gerenciador de tarefas feito em Python, que permite adicionar, listar e remover tarefas, com persistência de dados usando um arquivo JSON.

## 🚀 Funcionalidades

- Adicionar novas tarefas
- Listar todas as tarefas salvas
- Remover tarefas específicas
- Salvamento automático em arquivo `tarefas.json`

## 📁 Estrutura do Projeto

```bash
.
├── tarefas.json       # Arquivo onde as tarefas são salvas
└── tarefas.py         # Script principal
```

## 💻 Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciador-tarefas-python.git
   cd gerenciador-tarefas-python
   ```

2. Execute o script:
   ```bash
   python tarefas.py
   ```

3. Escolha uma das opções do menu:
   ```
   1. Adicionar Tarefa
   2. Listar tarefas
   3. Remover tarefa
   4. Sair
   ```

## 🧠 Como Funciona

- As tarefas são armazenadas em uma lista.
- Ao adicionar ou remover uma tarefa, o arquivo `tarefas.json` é atualizado automaticamente.
- O script utiliza `match-case` para lidar com as opções do menu (disponível a partir do Python 3.10).

## 📌 Requisitos

- Python 3.10 ou superior

## 📷 Exemplo de Uso

```bash
Escolha uma opção: 1
Digite a tarefa: Estudar Python
Tarefa adicionada!

Escolha uma opção: 2
Lista de tarefas:
1. Estudar Python
```
