import mysql.connector

miodb= mysql.connector.connect(
    host= "localhost",
    user="root",
    password= "root",
    database= "domenicosql"
)

#CREAZIONE DI DATABASE
mycursor = miodb.cursor()

#query= "create database domenicosql" 

#MOSTRARE I DATABASES NEL SERVER
#query = "show databases"

#mycursor.execute(query)

#for x in mycursor:
    #print(x)

#UNA VOLTA FATTO CIò AGGIUNGO SOPRA IN MIO DB: database= "domenicosql"

#CREO tabella
#query= "create table utenti(nome varchar(50), indirizzo varchar(50))"
#mycursor.execute(query)


#MOSTRO TABELLA IN DATABASE
#query1="show table"
#for x in mycursor:
  #print(x)

#CANCELLO TABELLA
#query= "drop table utenti"
#mycursor.execute(query)

#RICREO TABELLA CON AUTO INCREMENT E PRIMARY KEY
#query ="CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
#mycursor.execute(query)


#INSERISCO VALORI NELLA TABELLA
#query= "INSERT INTO customers (name, address) VALUES (%s, %s)"
#valori=("tommaso", "corso citta") oppure una lista di tuple per inserire più valori
#valori=[("mimmo", "corso1"), 
        #("sergio","via via"),
        #("rocco","via 19")
#]
#mycursor.execute(query,valori)
#mycursor.executemany(query,valori) #per inserire più valori

#miodb.commit()
#print(mycursor.rowcount, "record inserted.")

#SELECT
# query="SELECT * FROM customers "
# mycursor.execute(query)

#risultati=mycursor.fetchall() #salvo tutti i risultati della query in risultati
#for x in risultati:
   # print(x)

#risultati=mycursor.fetchone() #stampa la prima riga
#rint(risultati) 

#SELECT E WHERE
# query="SELECT * FROM customers where name= %s"
# valore=("sergio",)
# mycursor.execute(query,valore)
# risultati=mycursor.fetchall() #salvo tutti i risultati della query in risultati
# for x in risultati:
#    print(x)

#DELETE
# sql = "DELETE FROM customers WHERE name = %s "
# valore= ("rocco",)
# mycursor.execute(sql,valore)
# miodb.commit()
# print(mycursor.rowcount, "record(s) deleted")