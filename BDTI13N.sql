create database bdti13n;
use bdti13n;

create table pessoa(
	codigo int not null primary key auto_increment,
    nome varchar(100) not null,
    telefone varchar(100) not null,
    endereco varchar(100) not null,
    dataDeNascimento date not null
)Engine = InnoDB;

select * from pessoa;