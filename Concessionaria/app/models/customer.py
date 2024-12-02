class Customer:
    def __init__(self, nome, cpf, rg, data_nascimento, sexo, telefone, email, endereco, cep, cidade, estado, pais):
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

    def save_to_db(self, cursor):
        query = """
            INSERT INTO tb_clientes (
                nome_cliente,
                cpf_cliente,
                rg_cliente,
                data_nascimento,
                sexo_cliente,
                telefone_cliente,
                email_cliente,
                endereco_cliente,
                cep_cliente,
                cidade_cliente,
                estado_cliente,
                pais_cliente
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (self.nome, self.cpf, self.rg, self.data_nascimento, self.sexo, self.telefone,
                  self.email, self.endereco, self.cep, self.cidade, self.estado, self.pais)
        cursor.execute(query, values)

    @staticmethod
    def find_by_cpf(cursor, cpf):
        query = "SELECT * FROM tb_clientes WHERE cpf_cliente = %s"
        cursor.execute(query, (cpf,))
        return cursor.fetchone()

    @staticmethod
    def delete_by_cpf(cursor, cpf):
        query = "DELETE FROM tb_clientes WHERE cpf_cliente = %s"
        cursor.execute(query, (cpf,))

    @staticmethod
    def update_by_cpf(cursor, cpf, nome, rg, data_nascimento, sexo, telefone, email, endereco, cep, cidade, estado, pais):
        query = """
            UPDATE tb_clientes
            SET nome_cliente = %s, rg_cliente = %s, data_nascimento = %s, sexo_cliente = %s, telefone_cliente = %s, email_cliente = %s, endereco_cliente = %s, cep_cliente = %s, cidade_cliente = %s, estado_cliente = %s, pais_cliente = %s
            WHERE cpf_cliente = %s
        """
        values = (nome, rg, data_nascimento, sexo, telefone, email, endereco, cep, cidade, estado, pais, cpf)
        cursor.execute(query, values)