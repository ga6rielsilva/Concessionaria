# **Concessionária**
> Sistema ERP para gerenciamento de uma Concessionária de veículos.

---

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Modelagem do Sistema e Banco de Dados](#modelagem-do-sistema-e-banco-de-dados)
- [Contribuição](#contribuição)
- [Licença](#licença)


---

## Descrição do Projeto

Este é um sistema de gerenciamento ERP para uma Concessionaria de veículos, onde funcionários podem criar, editar e excluir veículos, além de definir prioridades e prazos. O objetivo é melhorar a organização e a produtividade, facilitando o acompanhamento de tarefas da empresa.

---

## Instalação

### Pré-requisitos

- Node.js (versão 14 ou superior)
- Banco de dados PostgreSQL (ou outro banco de dados relacional)

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/ga6rielsilva/Concessionaria.git
   cd nome-do-repositorio
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Configure as variáveis de ambiente no arquivo `.env` (exemplo abaixo):
   ```env
   DATABASE_URL=postgres://usuario:senha@localhost:5432/nome-do-banco
   PORT=3000
   ```

4. Execute as migrações do banco de dados:
   ```bash
   npx sequelize-cli db:migrate
   ```

5. Inicie o servidor:
   ```bash
   npm start
   ```

---

## Uso

1. **Acessar a interface**: Acesse `http://localhost:3000` em seu navegador.
2. **Criar uma tarefa**: Clique em "Nova Tarefa" e preencha os detalhes.
3. **Gerenciar tarefas**: Edite, exclua ou marque tarefas como concluídas para organizar suas atividades.

---

## Estrutura do Projeto

- `/src` - Código-fonte principal do sistema.
- `/src/models` - Modelos para as entidades do banco de dados.
- `/src/controllers` - Controladores que gerenciam a lógica de cada rota.
- `/src/routes` - Definições de rotas para a API.
- `/migrations` - Arquivos de migração para criar e modificar tabelas.
- `/config` - Arquivo de configuração de conexão com o banco de dados.

---

## Modelagem do Sistema e Banco de Dados

### Modelagem do Sistema

![Diagrama de Classes](https://github.com/ga6rielsilva/Concessionaria/imagens/diagrama_classes.png)
_(Substitua com a URL de uma imagem hospedada ou local do diagrama de classes do sistema)_

### Descrição das Entidades

- **Usuário**: Representa um usuário no sistema, com informações como `nome`, `email` e `senha`.
- **Tarefa**: Entidade que representa uma tarefa, incluindo `titulo`, `descricao`, `status`, `prioridade` e `prazo`.
- **Equipe**: Grupos de usuários que podem trabalhar em conjunto, permitindo visualização e gerenciamento das tarefas de todos os membros.

### Modelagem do Banco de Dados

Abaixo está o [**diagrama ER**](https://github.com/ga6rielsilva/Concessionaria/tree/main/Banco%20de%20dados/Modelo%20ER) do banco de dados.

**Modelo conceitual**
---
![Modelo conceitual](https://github.com/ga6rielsilva/Concessionaria/blob/main/Banco%20de%20dados/Modelo%20ER/Modelo%20conceitual.png?raw=true)

**Modelo lógico**
---
![Modelo lógico](https://github.com/ga6rielsilva/Concessionaria/blob/main/Banco%20de%20dados/Modelo%20ER/Modelo%20logico.png)

**Modelo físico**
---
![Modelo físico](https://github.com/ga6rielsilva/Concessionaria/blob/main/Banco%20de%20dados/Modelo%20ER/Modelo%20fisico.png)

#### Estrutura das Tabelas

1. **Tabela `usuarios`**
   - **id** (PK): Identificador único do usuário.
   - **nome**: Nome completo do usuário.
   - **email**: Email do usuário.
   - **senha**: Senha criptografada para login.

2. **Tabela `tarefas`**
   - **id** (PK): Identificador único da tarefa.
   - **titulo**: Título da tarefa.
   - **descricao**: Descrição detalhada da tarefa.
   - **status**: Status atual (e.g., 'Pendente', 'Em andamento', 'Concluída').
   - **prioridade**: Nível de prioridade (e.g., 'Baixa', 'Média', 'Alta').
   - **prazo**: Data de entrega ou prazo final para conclusão.
   - **usuario_id** (FK): Referência ao usuário que criou a tarefa.

3. **Tabela `equipes`**
   - **id** (PK): Identificador único da equipe.
   - **nome**: Nome da equipe.
   - **descricao**: Descrição da equipe.

4. **Tabela `usuario_equipe`** (Tabela de ligação entre `usuarios` e `equipes`)
   - **id** (PK): Identificador único.
   - **usuario_id** (FK): Referência ao usuário.
   - **equipe_id** (FK): Referência à equipe.

---

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Crie um fork do projeto.
2. Crie um branch para sua feature (`git checkout -b feature/NomeDaFeature`).
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Envie para o branch (`git push origin feature/NomeDaFeature`).
5. Abra um Pull Request.

---

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).

---

## Contato

Desenvolvido por **Gabriel Silva, Wellyson Rudnick, Lucas Calixto**.
