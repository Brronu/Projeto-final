import pymysql


conexao = pymysql.connect(
    host= "localhost",
    user= "root",
    password="",
    database="cinema_db" 
)

codigo = int(input("Informe o codigo do filme: "))
titulo = input("Informe o titulo do filme: ")
genero = input("Informe o genero do filme: ")
duracao = int(input("Informe a duração do filme: "))
classificacao_indicativa = int(input("Informe a classificação indicativa: "))

comando = "insert into filmes values(%s, %s, %s, %s, %s)"
campos = (codigo, titulo, genero, duracao, classificacao_indicativa)
consulta = conexao.cursor()
conexao.commit()
print(consulta.rowcount, "Informação inserida com sucesso\n")