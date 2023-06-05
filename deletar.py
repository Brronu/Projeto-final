"""import pymysql

conexao = pymysql.connect(
    host= "localhost",
    user= "root",
    password="",
    database= "cinema_db"
)

codigo = int(input("Qual codigo do filme deseja apagar? "))
comando = "delete from filmes where codigo = %s"

consulta = conexao.cursor()
consulta.execute(comando, codigo)
conexao.commit()
print(consulta.rowcount, "Linha foi excluida com sucesso\n")
conexao.close()
if comando and 0:
    print("filme deletado com sucesso! ")
else:
    print("Filme não encontrado.")"""
