import requests
import json
import random

# funzione per caricare il Pokédex 
def carica_pokedex():
    try:
        with open("pokedex.json", "r") as file:
            pokedex = json.load(file)
    except :
        pokedex = {}  
    return pokedex

# funzione per salvare il Pokédex nel file JSON
def salva_pokedex(pokedex):
    with open("pokedex.json", "w") as file:
        json.dump(pokedex, file, indent=4)

# funzione per ottenere un Pokémon dall'API
def ottieni_pokemon_da_api(numero):
    url = f"https://pokeapi.co/api/v2/pokemon/{numero}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # estrazione dati dal file json
        pokemon = {
            "numero": numero,
            "nome": data["name"],
            "abilita": data["abilities"][0]["ability"]["name"],
            "xp": data["base_experience"],
            "peso": data["weight"] / 10,  
            "altezza": data["height"] / 10  
        }
        return pokemon
    else:
        print(f"Errore nel recupero del Pokémon con ID {numero}")
        return None

# funzione per aggiungere un Pokémon al Pokédex
def aggiungi_al_pokedex(pokedex, pokemon):
    pokedex[str(pokemon["numero"])] = pokemon
    salva_pokedex(pokedex)

# funzione per mostrare i Pokémon nel Pokédex
def mostra_pokedex(pokedex):
    if not pokedex:
        print("Il Pokédex è vuoto")
    else:
        for numero, pokemon in pokedex.items():
            print(f"ID: {numero}, Nome: {pokemon['nome']}, Abilità: {pokemon['abilita']}, XP: {pokemon['xp']}, Peso: {pokemon['peso']}kg, Altezza: {pokemon['altezza']}m")

# funzione per catturare un pokemon
def cattura_pokemon():
    pokedex = carica_pokedex()

    while True:
        print("\n--- Menu ---")
        print("1. Cerca un Pokémon")
        print("2. Mostra il Pokédex")
        print("3. Esci dal gioco")
        scelta = input("Scegli un'opzione: ").strip()
        
        if scelta == "1":
            numero = random.randint(1, 1010)  
            print(f"Hai trovato un Pokémon con ID: {numero}!")

            # Verifica se il Pokémon è già nel Pokédex
            if str(numero) in pokedex:
                print(f"{pokedex[str(numero)]['nome']} è già nel tuo Pokédex. Non hai bisogno di catturarlo!")
            else:
                pokemon = ottieni_pokemon_da_api(numero)
                if pokemon:
                    print(f"Hai incontrato {pokemon['nome']}!")
                    cattura = input("Vuoi catturarlo? (s/n): ").strip().lower()
                    if cattura == "s":
                        aggiungi_al_pokedex(pokedex, pokemon)
                        print(f"Hai catturato {pokemon['nome']}! È stato aggiunto al tuo Pokédex.")
                    else:
                        print(f"Hai deciso di lasciare andare {pokemon['nome']}.")
        elif scelta == "2":
            mostra_pokedex(pokedex)
        elif scelta == "3":
            print("Esci dal gioco.")
            break
        else:
            print("Opzione non valida. Riprova.")

# Avvio del programma

cattura_pokemon()
