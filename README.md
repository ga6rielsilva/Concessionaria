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

- Python (versão 3.10 ou superior)
- Flask
- mysql-connector
- Banco de dados MySQL

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/ga6rielsilva/Concessionaria.git
   cd nome-do-repositorio
   ```

2. Instale as dependências:
   
   Crie um ambiente virtual para proteger seu sistema (Windows):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
   ```bash
   pip install flask
   ```
   ```bash
   pip install mysql-connector-python
   ```

4. Configure as variáveis de ambiente no arquivo `.env` (exemplo abaixo):
   ```env
   DATABASE_URL=postgres://usuario:senha@localhost:5432/nome-do-banco
   PORT=3000
   ```

5. Execute as migrações do banco de dados:
   ```bash
   npx sequelize-cli db:migrate
   ```

6. Inicie o servidor:
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
Abaixo está a [**modelagem**](https://github.com/ga6rielsilva/Concessionaria/tree/main/banco_de_dados/modelagem) do sistema.

**Diagrama de caso de uso**
---
![Diagrama de caso de uso](https://github.com/ga6rielsilva/Concessionaria/blob/main/banco_de_dados/modelagem/diagrama_de_caso_de_uso.png?raw=true)

**Diagrama de sequencia**
---
![Diagrama de sequencia](https://github.com/ga6rielsilva/Concessionaria/blob/main/banco_de_dados/modelagem/diagrama_de_sequencia.png?raw=true)


### Descrição das Entidades

- **Usuário**: Representa um usuário no sistema, com informações como `nome`, `email` e `senha`.
- **Tarefa**: Entidade que representa uma tarefa, incluindo `titulo`, `descricao`, `status`, `prioridade` e `prazo`.
- **Equipe**: Grupos de usuários que podem trabalhar em conjunto, permitindo visualização e gerenciamento das tarefas de todos os membros.

### Modelagem do Banco de Dados

Abaixo está o [**diagrama ER**](https://github.com/ga6rielsilva/Concessionaria/tree/main/banco_de_dados/modelo_er) do banco de dados.

**Modelo conceitual**
---
![Modelo conceitual](https://github.com/ga6rielsilva/Concessionaria/blob/main/banco_de_dados/modelo_er/modelo_conceitual.png?raw=true)

**Modelo lógico**
---
![Modelo lógico](https://github.com/ga6rielsilva/Concessionaria/blob/main/banco_de_dados/modelo_er/modelo_fisico.png?raw=true)

**Modelo físico**
---
![Modelo físico](https://github.com/ga6rielsilva/Concessionaria/blob/main/banco_de_dados/modelo_er/modelo_logico.png?raw=true)

#### Estrutura das Tabelas

1. **Tabela `tb_usuarios`**
   - **id_usuario** (PK): Identificador único do usuário.
   - **nome**: Nome do usuário.
   - **login**: Login único do usuário.

2. **Tabela `tb_funcionarios`**
   - **id_funcionario** (PK): Identificador único do funcionário.
   - **nome**: Nome do funcionário.
   - **cpf_funcionario**: CPF do funcionário.
   - **rg**: RG do funcionário.
   - **data_nascimento**: Data de nascimento do funcionário.
   - **sexo**: Sexo do funcionário (M/F).
   - **telefone**: Telefone de contato.
   - **email**: Email do funcionário.
   - **foto**: Foto do funcionário (armazenada como BLOB).
   - **endereco**: Endereço residencial do funcionário.
   - **cep**: CEP do endereço.
   - **cidade**: Cidade do funcionário.
   - **estado**: Estado do funcionário (sigla).
   - **pais**: País do funcionário.
   - **salario**: Salário do funcionário.
   - **cargo**: Cargo do funcionário.
   - **id_usuario** (FK): Referência ao usuário associado.

3. **Tabela `tb_clientes`**
   - **id_cliente** (PK): Identificador único do cliente.
   - **nome_cliente**: Nome do cliente.
   - **cpf_cliente**: CPF do cliente.
   - **rg_cliente**: RG do cliente.
   - **data_nascimento**: Data de nascimento do cliente.
   - **sexo_cliente**: Sexo do cliente (M/F).
   - **telefone_cliente**: Telefone de contato.
   - **email_cliente**: Email do cliente.
   - **endereco_cliente**: Endereço residencial do cliente.
   - **cep_cliente**: CEP do endereço.
   - **cidade_cliente**: Cidade do cliente.
   - **estado_cliente**: Estado do cliente (sigla).
   - **pais_cliente**: País do cliente.

4. **Tabela `tb_atendimento`**
   - **id_atendimento** (PK): Identificador único do atendimento.
   - **hora_atendimento**: Hora do atendimento.
   - **data_atendimento**: Data do atendimento.
   - **id_cliente** (FK): Referência ao cliente atendido.
   - **id_funcionario** (FK): Referência ao funcionário responsável pelo atendimento.

5. **Tabela `tb_categorias`**
   - **id_categoria** (PK): Identificador único da categoria.
   - **tipo_veiculo**: Tipo de veículo (ex.: Carro, Moto).

6. **Tabela `tb_veiculos`**
   - **id_veiculo** (PK): Identificador único do veículo.
   - **marca**: Marca do veículo.
   - **modelo**: Modelo do veículo.
   - **ano_fabricacao**: Ano de fabricação.
   - **ano_modelo**: Ano do modelo.
   - **cor**: Cor do veículo.
   - **placa**: Placa do veículo.
   - **chassi**: Número do chassi.
   - **renavam**: Código RENAVAM.
   - **km_rodado**: Quilometragem rodada.
   - **valor_compra**: Valor de compra do veículo.
   - **valor_venda**: Valor de venda do veículo.
   - **condicao**: Condição do veículo (ex.: Novo, Usado).
   - **foto_veiculo**: Foto do veículo (armazenada como BLOB).
   - **id_categoria** (FK): Referência à categoria do veículo.

7. **Tabela `tb_compra`**
   - **id_compra** (PK): Identificador único da compra.
   - **data_compra**: Data da compra.
   - **valor_compra**: Valor pago na compra.
   - **id_cliente** (FK): Referência ao cliente comprador.
   - **id_funcionario** (FK): Referência ao funcionário responsável pela venda.
   - **id_veiculo** (FK): Referência ao veículo adquirido.

8. **Tabela `tb_historico_vendas`**
   - **id_historico** (PK): Identificador único do histórico de vendas.
   - **data_venda**: Data da venda.
   - **valor_venda**: Valor recebido na venda.
   - **id_funcionario** (FK): Referência ao funcionário responsável pela venda.

9. **Tabela `tb_historico_estoque`**
   - **id_historico** (PK): Identificador único do histórico de estoque.
   - **data_entrada**: Data de entrada no estoque.
   - **data_saida**: Data de saída do estoque.
   - **id_veiculo** (FK): Referência ao veículo armazenado.
   - **id_funcionario** (FK): Referência ao funcionário responsável.
   - **quantidade**: Quantidade de veículos movimentados.

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
