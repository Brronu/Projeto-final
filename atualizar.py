"""import pymysql

conexao = pymysql.connect(
    host= "localhost",
    user="root",
    password="",
    database="cinema_db"

)

nome = input("Informe um novo nome para o filme: ")
codigo = int(input("Qual o codigo: "))

comando = "update filmes set nome = %s where codigo = %s"

valores = (nome, codigo)

consulta = conexao.cursor()
consulta.execute(comando, valores)
conexao.commit()
print(consulta.rowcount,"A linha foi atualizada com sucesso\n ")
conexao.close()"""