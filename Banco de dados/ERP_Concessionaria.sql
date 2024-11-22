CREATE DATABASE IF NOT EXISTS erp_concessionaria;
USE erp_concessionaria;

CREATE TABLE IF NOT EXISTS tb_usuarios(
	id_usuario INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(40) NOT NULL,
	login VARCHAR(40) NOT NULL,
	CONSTRAINT pk_usuarios PRIMARY KEY(id_usuario)
);

CREATE TABLE IF NOT EXISTS tb_funcionarios(
	id_funcionario INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(40) NOT NULL,
	cpf_funcioario VARCHAR(11) NOT NULL,
	rg VARCHAR(10) NOT NULL,
	data_nascimento DATE NOT NULL,
	sexo CHAR(1) NOT NULL,
	telefone VARCHAR(11) NOT NULL,
	email VARCHAR(40) NOT NULL,
	foto BLOB NOT NULL,
	endereco VARCHAR(40) NOT NULL,
	cep VARCHAR(8) NOT NULL,
	cidade VARCHAR(40) NOT NULL,
	estado VARCHAR(2) NOT NULL,
	pais VARCHAR(40) NOT NULL,
	salario DECIMAL(10,2) NOT NULL,
	cargo VARCHAR(40) NOT NULL,
	id_usuario INT NOT NULL,
	CONSTRAINT pk_funcionarios PRIMARY KEY(id_funcionario),
	CONSTRAINT fk_funcionarios_usuarios FOREIGN KEY(id_usuario) REFERENCES tb_usuarios(id_usuario)
);

CREATE TABLE IF NOT EXISTS tb_clientes(
	id_cliente INT NOT NULL AUTO_INCREMENT,
	nome_cliente VARCHAR(40) NOT NULL,
	cpf_cliente VARCHAR(11) NOT NULL,
	rg_cliente VARCHAR(10) NOT NULL,
	data_nascimento DATE NOT NULL,
	sexo_cliente CHAR(1) NOT NULL,
	telefone_cliente VARCHAR(11) NOT NULL,
	email_cliente VARCHAR(40) NOT NULL,
	endereco_cliente VARCHAR(40) NOT NULL,
	cep_cliente VARCHAR(8) NOT NULL,
	cidade_cliente VARCHAR(40) NOT NULL,
	estado_cliente VARCHAR(2) NOT NULL,
	pais_cliente VARCHAR(40) NOT NULL,
	CONSTRAINT pk_clientes PRIMARY KEY(id_cliente)
);

CREATE TABLE IF NOT EXISTS tb_atendimento(
	id_atendimento INT NOT NULL AUTO_INCREMENT,
	hora_atendimento TIME NOT NULL,
	data_atendimento DATE NOT NULL,
	id_cliente INT NOT NULL,
	id_funcionario INT NOT NULL,
	CONSTRAINT pk_atendimento PRIMARY KEY(id_atendimento),
	CONSTRAINT fk_atendimento_funcionarios FOREIGN KEY(id_funcionario) REFERENCES tb_funcionarios(id_funcionario),
	CONSTRAINT fk_atendimento_clientes FOREIGN KEY(id_cliente) REFERENCES tb_clientes(id_cliente)
);

CREATE TABLE IF NOT EXISTS tb_categorias(
	id_categoria INT NOT NULL AUTO_INCREMENT,
	tipo_veiculo VARCHAR(40) NOT NULL,
	CONSTRAINT pk_categorias PRIMARY KEY(id_categoria)
);

CREATE TABLE IF NOT EXISTS tb_veiculos(
	id_veiculo INT NOT NULL AUTO_INCREMENT,
	marca VARCHAR(40) NOT NULL,
	modelo VARCHAR(40) NOT NULL,
	ano_fabricacao INT NOT NULL,
	ano_modelo INT NOT NULL,
	cor VARCHAR(40) NOT NULL,
	placa VARCHAR(8) NOT NULL,
	chassi VARCHAR(17) NOT NULL,
	renavam VARCHAR(11) NOT NULL,
	km_rodado INT NOT NULL,
	valor_compra DECIMAL(10,2) NOT NULL,
	valor_venda DECIMAL(10,2) NOT NULL,
	condicao VARCHAR(40) NOT NULL,
	foto_veiculo BLOB NOT NULL,
	id_categoria INT NOT NULL,
	CONSTRAINT pk_veiculos PRIMARY KEY(id_veiculo),
	CONSTRAINT fk_veiculos_categorias FOREIGN KEY(id_categoria) REFERENCES tb_categorias(id_categoria)
);

CREATE TABLE IF NOT EXISTS tb_compra(
	id_compra INT NOT NULL AUTO_INCREMENT,
	data_compra DATE NOT NULL,
	valor_compra DECIMAL(10,2) NOT NULL,
	id_cliente INT NOT NULL,
	id_funcionario INT NOT NULL,
	id_veiculo INT NOT NULL,
	CONSTRAINT pk_compra PRIMARY KEY(id_compra),
	CONSTRAINT fk_compra_funcionarios FOREIGN KEY(id_funcionario) REFERENCES tb_funcionarios(id_funcionario),
	CONSTRAINT fk_compra_clientes FOREIGN KEY(id_cliente) REFERENCES tb_clientes(id_cliente),
	CONSTRAINT fk_compra_veiculos FOREIGN KEY(id_veiculo) REFERENCES tb_veiculos(id_veiculo)	
);


CREATE TABLE IF NOT EXISTS tb_historico_vendas(
	id_historico INT NOT NULL AUTO_INCREMENT,
	data_venda DATE NOT NULL,
	valor_venda DECIMAL(10,2) NOT NULL,
	id_funcionario INT NOT NULL,
	CONSTRAINT pk_historico PRIMARY KEY(id_historico),
	CONSTRAINT fk_historico_funcionarios FOREIGN KEY(id_funcionario) REFERENCES tb_funcionarios(id_funcionario)
);

CREATE TABLE IF NOT EXISTS tb_historico_estoque(
	id_historico INT NOT NULL AUTO_INCREMENT,
	data_entrada DATE NOT NULL,
	data_saida DATE NOT NULL,
	id_veiculo INT NOT NULL,
	id_funcionario INT NOT NULL,
	quantidade INT NOT NULL,
	CONSTRAINT pk_historico_estoque PRIMARY KEY(id_historico),
	CONSTRAINT fk_historico_estoque_funcionarios FOREIGN KEY(id_funcionario) REFERENCES tb_funcionarios(id_funcionario),
	CONSTRAINT fk_historico_estoque_veiculos FOREIGN KEY(id_veiculo) REFERENCES tb_veiculos(id_veiculo)
);
