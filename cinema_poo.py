import pymysql

class Filme:

    def conexao(self):
        conn = pymysql.connect(
            host= "localhost",
            user= "root",
            password="",
            database= "cinema_db"
        )
        return conn
    
    def cadastraFilme(self, codigo, titulo, genero, duracao, classificacao_indicativa):
        conexao = self.conexao()
        
        comando = "insert into filmes values(%s, %s, %s, %s, %s)"
        valores = (codigo, titulo, genero, duracao, classificacao_indicativa)
        consulta = conexao.cursor()
        consulta.execute(comando, valores)
        conexao.commit()
        print(consulta.rowcount,"Informação inserida com sucesso\n")
        conexao.close()


    def consultarFilmes(self):
        conexao = self.conexao()
        
        comando = "select * from filmes"
        consulta = conexao.cursor()
        consulta.execute(comando)
        resultado = consulta.fetchall()
        print(resultado, "\n")
        conexao.close()
            
        for filme in resultado:
            print("Título:", filme[1])
            print("Gênero:", filme[2])
            print("Duração:", filme[3])
            print("Classificação Indicativa:", filme[4])
            print("--------------------")

     
    def deletarFilme(self):
        conexao = self.conexao()
        codigo = int(input("Qual codigo do filme deseja apagar? "))
        comando = "delete from filmes where cinema_db = %s"
        consulta = conexao.cursor()
        consulta.execute(comando, codigo)
        conexao.commit()
        #print(consulta.rowcount,"filme deletado com sucesso")
       
        
        if comando > 0:
            print("filme deletado com sucesso! ")
        else:
            print("Filme não encontrado.")
        conexao.close()


    def atualizarFilme(self):
        conexao = self.conexao()
        titulo = input("Informe um novo titulo para o filme: ")
        codigo = int(input("Informe o codigo do filme: "))
        comando = "update filmes set titulo = %s where codigo = %s"
        valores = (titulo, codigo)
        consulta = conexao.cursor()
        consulta.execute(comando, valores)
        conexao.commit()
        #print(consulta.rowcount, "A linha foi atualizada com sucesso\n")
        if comando > "0":
            print("Filme atualizado com sucesso!")
        else:
            print("Filme não encontrado.")

        conexao.close()
        