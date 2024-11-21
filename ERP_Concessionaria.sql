create database if not exists erp_concessionaria;
use erp_concessionaria;

create table if not exists usuarios(
	ID int not null auto_increment,
    Nome varchar(40) not null,
    login varchar (40) not null,
    constraint pk_usuarios primary key(ID)
);

create table if not exists empresa(
	ID int not null auto_increment,
	razaosocial varchar(40) not null,
	nmfantasia varchar(40) not null,
	dsemail varchar(40) not null,
	constraint pk_empresa primary key(ID)
);

create table if not exists departamento(
	ID int not null auto_increment,
	dsdepartamento varchar(40) not null,
	IDEmpresa int not null,
	constraint pk_empresa primary key(ID),
    constraint fk_departamento_empresa foreign key(IDEmpresa) references empresa(ID)
);
