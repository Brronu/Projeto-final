"""import pymysql

conexao = pymysql.connect(
    host= "localhost",
    user= "root",
    password="",
    database= "cinema_db"
)
        
comando = "select * from funcionario"
consulta = conexao.cursor()
consulta.execute(comando)

resultado = consulta.fetchall()
print(resultado,"\n")

for itens in resultado:
    print(f"Codigo:{itens[1]}, Titulo{itens[2]}, Genero{itens[3]}, Duração{itens[4]},Classificação idicativa{itens[5]}")

print("\n")

conexao.close()"""