class Vehicle:
    def __init__(self, marca, modelo, motor_veiculo, placa, cor, ano_fabricacao,
                 ano_modelo, km_rodado, categoria, condicao, chassi, renavam, valor_compra, valor_venda, disponibilidade):
        self.marca = marca
        self.modelo = modelo
        self.motor_veiculo = motor_veiculo
        self.placa = placa
        self.cor = cor
        self.ano_fabricacao = ano_fabricacao
        self.ano_modelo = ano_modelo
        self.km_rodado = km_rodado
        self.categoria = categoria
        self.condicao = condicao
        self.chassi = chassi
        self.renavam = renavam
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.disponibilidade = disponibilidade

    # Método para salvar o veículo no banco de dados
    def save_to_db(self, cursor):
        query = """
            INSERT INTO tb_veiculos (
                marca, 
                modelo, 
                motor_veiculo, 
                placa, 
                cor, 
                ano_fabricacao, 
                ano_modelo, 
                km_rodado, 
                categoria, 
                condicao, 
                chassi, 
                renavam, 
                valor_compra, 
                valor_venda, 
                disponibilidade
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        # Valores a serem inseridos no banco de dados
        values = (self.marca, self.modelo, self.motor_veiculo, self.placa, self.cor, self.ano_fabricacao, self.ano_modelo, self.km_rodado,
                       self.categoria, self.condicao, self.chassi, self.renavam, self.valor_compra, self.valor_venda, self.disponibilidade)
        # Executa a query de inserção com os valores do veículo
        cursor.execute(query, values)

    # Método para encontrar um veículo pelo número da placa
    @staticmethod
    def find_by_plate(cursor, plate):
        query = "SELECT * FROM tb_veiculos WHERE placa = %s"
        cursor.execute(query, (plate,))
        return cursor.fetchone()

    # Método para deletar um veículo pelo número da placa
    @staticmethod
    def delete_by_plate(cursor, plate):
        query = "DELETE FROM tb_veiculos WHERE placa = %s"
        cursor.execute(query, (plate,))

    # Método para atualizar os dados de um veículo pelo número da placa
    @staticmethod
    def update_by_plate(cursor, plate, marca, modelo, motor_veiculo, cor, ano_fabricacao,
                        ano_modelo, km_rodado, categoria, condicao, chassi, renavam, valor_compra, valor_venda):
        query = """
            UPDATE tb_veiculos
            SET marca = %s, modelo = %s, motor_veiculo = %s, cor = %s, ano_fabricacao = %s, ano_modelo = %s, km_rodado = %s, categoria = %s, condicao = %s, chassi = %s, renavam = %s, valor_compra = %s, valor_venda = %s
            WHERE placa = %s
        """
        # Valores a serem atualizados no banco de dados
        values = (marca, modelo, motor_veiculo, cor, ano_fabricacao, ano_modelo, km_rodado, 
                  categoria, condicao, chassi, renavam, valor_compra, valor_venda, plate)
        # Executa a query com os valores fornecidos
        cursor.execute(query, values)