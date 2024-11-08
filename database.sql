CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE veiculos (
    id INT PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    ano INT,
    preco DECIMAL(10, 2)
);

CREATE TABLE vendas (
    id INT PRIMARY KEY,
    id_cliente INT,
    id_veiculo INT,
    data DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    FOREIGN KEY (id_veiculo) REFERENCES veiculos(id)
);