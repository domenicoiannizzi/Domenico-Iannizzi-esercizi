import mysql.connector
# try:
#     miodb= mysql.connector.connect(
#         host= "localhost",
#         user="root",
#         password= "root"
#         )
    
#     c=miodb.cursor()
#     try:
#      c.execute("CREATE DATABASE IF NOT EXISTS scuola_db")
#      print("Database 'scuola_db' creato con successo.")
#     except mysql.connector.Error as err:
#      print(f"Errore durante l'esecuzione di CREATE DATABASE: {err}")
#     except :
#      print("Errore non riconosciuto")  

# except mysql.connector.Error as conn_err:
#  print(f"Errore di connessione al server MySQL: {conn_err}")
# except :
#  print("Errore non riconosciuto")
# miodb.database= "scuola_db"
miodb= mysql.connector.connect(
        host= "localhost",
        user="root",
        password= "root",
        database= "scuola_db"
        )
    
c=miodb.cursor()
c.execute("create table studenti ( name VARCHAR(255))")
                  
'''
c.execute("""
    CREATE TABLE IF NOT EXISTS materie (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255)  UNIQUE NOT NULL 
    )
""")

c.execute (""""
    id INT AUTO_INCREMENT PRIMARY KEY,
    studente_id INT,
    materia_id INT,
    voto INT,
    FOREIGN KEY (studente_id) REFERENCES studenti(id),
    FOREIGN KEY (materia_id) REFERENCES materie(id)
    )
""")
'''


#class Studente:
#   def __init__(self,name,voto_Ita,voto_Mate):
#     self.name=name
#     self.voto_Ita=voto_Ita
#     self.voto_Mate=voto_Mate




def aggiungi_studente(name,voto_Ita,voto_Mate):
  c.execute("insert into studenti (name,voto_Ita,voto_Mate) values (%s,%s,%s)", (name,voto_Ita,voto_Mate))
  miodb.commit()
  print(f"studente : {name}, voto di italiano : {voto_Ita}, voto di matematica : {voto_Mate}")

def rimuovi_studente(name):
  c.execute("delete from studenti where name = %s", (name,))
  miodb.commit()
  print(f"studente : {name} eliminato con successo")
  
def aggiorna_studente(new_name,old_name,n_voto_Ita,n_voto_Mate, ):
  c.execute("UPDATE studenti SET name = %s, voto_Ita= %s ,voto_Mate = %s where name = %s",(new_name,n_voto_Ita,n_voto_Mate,old_name))
  miodb.commit()
  print(f"Aggiornamento da studente {old_name} a studente {new_name}")

def modifica_voti(name,materia,nuovo_voto):
  if materia == "italiano":
    c.execute("UPDATE studenti SET voto_Ita = %s where name = %s",(nuovo_voto,name))
  elif materia == "matematica":
    c.execute("UPDATE studenti SET voto_Mate = %s where name = %s",(nuovo_voto,name))
  else:
    print("Voto non valido, scegliere italiano o matematica")
  miodb.commit()
  print(f"Voto di {name} in materia {materia} aggiornato a {nuovo_voto}")




