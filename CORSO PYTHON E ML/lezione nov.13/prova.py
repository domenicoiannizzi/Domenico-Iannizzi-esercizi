import mysql.connector
try:
    miodb= mysql.connector.connect(
        host= "localhost",
        user="root",
        password= "root"
        )
    
    c=miodb.cursor()
    try:
     c.execute("CREATE DATABASE IF NOT EXISTS scuola_db")
     print("Database 'scuola_db' creato con successo.")
    except mysql.connector.Error as err:
     print(f"Errore durante l'esecuzione di CREATE DATABASE: {err}")
    except :
     print("Errore non riconosciuto")  

except mysql.connector.Error as conn_err:
 print(f"Errore di connessione al server MySQL: {conn_err}")
except :
 print("Errore non riconosciuto")
miodb.database= "scuola_db"

c=miodb.cursor()
c.execute("create table studenti (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
# c.execute("""
#     CREATE TABLE IF NOT EXISTS materie (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         nome VARCHAR(255)  UNIQUE NOT NULL 
#     )
# """) 
c.execute("""
    CREATE TABLE IF NOT EXISTS voti (
        id INT AUTO_INCREMENT PRIMARY KEY,
        studente_id INT,
        materia_id INT,
        voto INT,
        FOREIGN KEY (studente_id) REFERENCES studenti(id),
        FOREIGN KEY (materia_id) REFERENCES materie(id)
    )
""")