import mysql.connector
import conexaoBD #Classe que faz a conexão com o banco de dados

db_connection = conexaoBD.conectar()
con = db_connection.cursor()

def inserir(nome, telefone, endereco, dataDeNascimento):
    try:
        sql = "insert into pessoa(codigo, nome, telefone, endereco, dataDeNascimento) values('', '{}', '{}','{}', '{}')".format(nome, telefone, endereco, tratarData(dataDeNascimento))
        con.execute(sql)
        db_connection.commit()#Inserção de dados no BD
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro

def tratarData(texto):
    separado = texto.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]
    return '{}-{}-{}'.format(ano, mes, dia)

def consultar():
    try:
        sql = 'select * from pessoa'
        con.execute(sql)
        for(codigo, nome, telefone, endereco, dataDeNascimento) in con:
            print('Código: {}, Nome: {}, Telefone: {}, Endereço: {}, Data de Nascimento: {}'.format(codigo, nome, telefone, endereco, dataDeNascimento))
        print('\n')
    except Exception as erro:
        print(erro)

def atualizar(cod, campo, novoDado):
    try:
        sql = "update pessoa set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluir(cod):
    try:
        sql = "delete from pessoa where codigo = '{}'".format(cod)
        con.execute(sql)
        db_connection.commit()
        print('{}excluido!'.format(con.rowcount))
    except Exception as erro:
        print(erro)