CREATE TABLE IF NOT EXISTS Banco (
	codigo SERIAL PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	endereço VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Agencia (
	endereço VARCHAR(50) NOT NULL,
	num_agencia SERIAL PRIMARY KEY,
	codigo INTEGER
);

ALTER TABLE Agencia ADD CONSTRAINT Agencia_fk FOREIGN KEY(codigo) REFERENCES Banco(codigo);

CREATE TABLE IF NOT EXISTS Conta (
	numero_conta SERIAL PRIMARY KEY,
	saldo INTEGER NOT NULL,
	num_agencia INTEGER
);

ALTER TABLE Conta ADD CONSTRAINT Conta_fk FOREIGN KEY(num_agencia) REFERENCES Agencia(num_agencia);

CREATE TABLE IF NOT EXISTS Emprestimo (
	numero_emprestimo SERIAL PRIMARY KEY,
	valor INTEGER NOT NULL,
	tipo VARCHAR(10) NOT NULL,
	num_agencia INTEGER
);

ALTER TABLE Emprestimo ADD CONSTRAINT Emprestimo_fk FOREIGN KEY(num_agencia) REFERENCES Agencia(num_agencia);

CREATE TABLE IF NOT EXISTS Cliente (
	cpf CHAR(11) PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	telefone VARCHAR(15) NOT NULL,
	endereço VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS EmprestimoCliente (
	numero_emprestimo INTEGER,
	cpf CHAR(11)
);

ALTER TABLE EmprestimoCliente ADD CONSTRAINT EmprestimoCliente_fk FOREIGN KEY(numero_emprestimo) REFERENCES Emprestimo(numero_emprestimo);
ALTER TABLE EmprestimoCliente ADD CONSTRAINT EmprestimoCliente_fk FOREIGN KEY(cpf) REFERENCES Cliente(cpf);

CREATE TABLE IF NOT EXISTS ContaCliente (
	numero_conta INTEGER,
	cpf CHAR(11)
);

ALTER TABLE ContaCliente ADD CONSTRAINT ContaCliente_fk FOREIGN KEY(numero_conta) REFERENCES Conta(numero_conta);
ALTER TABLE ContaCliente ADD CONSTRAINT ContaCliente_fk FOREIGN KEY(cpf) REFERENCES Cliente(cpf);

