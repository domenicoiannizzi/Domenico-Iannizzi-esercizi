class Utente():
    def __init__(self, username, password):  # Corretto il costruttore
        self.username = username
        self.password = password
        self.punteggio = 0


# Questa è la lista che contiene tutti gli utenti
lista_utenti = []

# Esempio di creazione utente
lista_utenti.append(Utente('alessio', 'alessione123'))  # Rimosso il terzo argomento

# Aggiungo alcuni utenti per testare
lista_utenti.append(Utente('mario', 'mario123'))
lista_utenti.append(Utente('luigi', 'luigi123'))

# Aggiungo punteggi per testare
lista_utenti[0].punteggio = 100
lista_utenti[1].punteggio = 200
lista_utenti[2].punteggio = 150

def stampa_classifica(lista_utenti):
    # Ordina la lista di utenti in base al punteggio
    for i in range(len(lista_utenti)):
        for j in range(0, len(lista_utenti) - i - 1):  # Evita l'uscita dall'intervallo
            if lista_utenti[j].punteggio < lista_utenti[j + 1].punteggio:
                lista_utenti[j], lista_utenti[j + 1] = lista_utenti[j + 1], lista_utenti[j]

    print("Classifica : \n")
    for x in range(len(lista_utenti)):  # Inizia da 0
        print(f"{x + 1}. Nome: {lista_utenti[x].username} - Punteggio: {lista_utenti[x].punteggio}")  # Accesso corretto agli attributi

# Chiamata alla funzione
stampa_classifica(lista_utenti)
