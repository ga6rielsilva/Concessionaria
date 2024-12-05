class Employee:
    def __init__(self, nome, cpf, rg, data_nascimento, sexo, telefone, email,
                 endereco, cep, cidade, estado, pais):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    # Método para salvar os dados do funcionário no banco de dados
    def save_to_db(self, cursor):
        query = """
            INSERT INTO tb_funcionarios (
                nome_funcionario,
                cpf_funcionario,
                rg_funcionario,
                data_nascimento,
                sexo_funcionario,
                telefone_funcionario,
                email_funcionario,
                endereco_funcionario,
                cep_funcionario,
                cidade_funcionario,
                estado_funcionario,
                pais_funcionario
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        # Valores a serem inseridos no banco de dados
        values = (self.nome, self.cpf, self.rg, self.data_nascimento, self.sexo, self.telefone,
                  self.email, self.endereco, self.cep, self.cidade, self.estado, self.pais)
        # Executa a query com os valores fornecidos
        cursor.execute(query, values)

    # Método para encontrar um funcionário pelo CPF
    @staticmethod
    def find_by_cpf(cursor, cpf):
        query = "SELECT * FROM tb_funcionarios WHERE cpf_funcionario = %s"
        cursor.execute(query, (cpf,))
        return cursor.fetchone()

    # Método para deletar um funcionário pelo CPF
    @staticmethod
    def delete_by_cpf(cursor, cpf):
        query = "DELETE FROM tb_funcionarios WHERE cpf_funcionario = %s"
        cursor.execute(query, (cpf,))

    # Método para atualizar os dados de um funcionário pelo CPF
    @staticmethod
    def update_by_cpf(cursor, cpf, nome, rg, data_nascimento, sexo, telefone,
                      email, endereco, cep, cidade, estado, pais):
        query = """
            UPDATE tb_funcionarios SET
                nome_funcionario = %s,
                rg_funcionario = %s,
                data_nascimento = %s,
                sexo_funcionario = %s,
                telefone_funcionario = %s,
                email_funcionario = %s,
                endereco_funcionario = %s,
                cidade_funcionario = %s,
                estado_funcionario = %s,
                cep_funcionario = %s,
                pais_funcionario = %s
            WHERE cpf_funcionario = %s
        """
        # Valores a serem atualizados no banco de dados
        values = (nome, rg, data_nascimento, sexo, telefone, email, endereco,
                  cep, cidade, estado, pais, cpf)
        # Executa a query com os valores fornecidos
        cursor.execute(query, values)