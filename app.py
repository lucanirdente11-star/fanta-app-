import random

def genera_rosa_fantacalcio():
    # Listone completo con 25+ giocatori (Titolari e Panchinari)
    listone = [
        # PORTIERI (3)
        {"nome": "Sommer", "ruolo": "P", "crediti": 120, "fantamedia": 5.8},
        {"nome": "Di Gregorio", "ruolo": "P", "crediti": 100, "fantamedia": 5.5},
        {"nome": "Svilar", "ruolo": "P", "crediti": 90, "fantamedia": 5.4},
        {"nome": "Skorupski", "ruolo": "P", "crediti": 30, "fantamedia": 4.8},
        {"nome": "Falcone", "ruolo": "P", "crediti": 25, "fantamedia": 4.7},
        {"nome": "Turati", "ruolo": "P", "crediti": 15, "fantamedia": 4.5},
        
        # DIFENSORI (8)
        {"nome": "Dimarco", "ruolo": "D", "crediti": 140, "fantamedia": 6.8},
        {"nome": "Theo Hernandez", "ruolo": "D", "crediti": 150, "fantamedia": 6.7},
        {"nome": "Bastoni", "ruolo": "D", "crediti": 95, "fantamedia": 6.4},
        {"nome": "Bremer", "ruolo": "D", "crediti": 90, "fantamedia": 6.3},
        {"nome": "Buongiorno", "ruolo": "D", "crediti": 85, "fantamedia": 6.3},
        {"nome": "Cambiaso", "ruolo": "D", "crediti": 70, "fantamedia": 6.2},
        {"nome": "Bellanova", "ruolo": "D", "crediti": 65, "fantamedia": 6.1},
        {"nome": "Zappacosta", "ruolo": "D", "crediti": 45, "fantamedia": 5.9},
        {"nome": "Baschirotto", "ruolo": "D", "crediti": 20, "fantamedia": 5.6},
        {"nome": "Gila", "ruolo": "D", "crediti": 15, "fantamedia": 5.5},
        {"nome": "Beukema", "ruolo": "D", "crediti": 15, "fantamedia": 5.5},
        {"nome": "Ismajli", "ruolo": "D", "crediti": 10, "fantamedia": 5.4},
        
        # CENTROCAMPISTI (8)
        {"nome": "Calhanoglu", "ruolo": "C", "crediti": 230, "fantamedia": 8.0},
        {"nome": "Koopmeiners", "ruolo": "C", "crediti": 220, "fantamedia": 7.9},
        {"nome": "Pulisic", "ruolo": "C", "crediti": 210, "fantamedia": 7.8},
        {"nome": "Zaccagni", "ruolo": "C", "crediti": 130, "fantamedia": 6.9},
        {"nome": "Colpani", "ruolo": "C", "crediti": 90, "fantamedia": 6.6},
        {"nome": "Ferguson", "ruolo": "C", "crediti": 75, "fantamedia": 6.5},
        {"nome": "Vlasic", "ruolo": "C", "crediti": 65, "fantamedia": 6.3},
        {"nome": "Brescianini", "ruolo": "C", "crediti": 30, "fantamedia": 6.0},
        {"nome": "Suslov", "ruolo": "C", "crediti": 25, "fantamedia": 5.9},
        {"nome": "Frendrup", "ruolo": "C", "crediti": 20, "fantamedia": 5.8},
        
        # ATTACCANTI (6)
        {"nome": "Lautaro Martinez", "ruolo": "A", "crediti": 380, "fantamedia": 9.5},
        {"nome": "Retegui", "ruolo": "A", "crediti": 300, "fantamedia": 8.8},
        {"nome": "Thuram", "ruolo": "A", "crediti": 280, "fantamedia": 8.5},
        {"nome": "Dovbyk", "ruolo": "A", "crediti": 250, "fantamedia": 8.1},
        {"nome": "Gudmundsson", "ruolo": "A", "crediti": 190, "fantamedia": 7.7},
        {"nome": "Castellanos", "ruolo": "A", "crediti": 140, "fantamedia": 7.3},
        {"nome": "Krstovic", "ruolo": "A", "crediti": 70, "fantamedia": 6.6},
        {"nome": "Lucca", "ruolo": "A", "crediti": 60, "fantamedia": 6.5}
    ]

    budget_totale = 1500
    requisiti = {"P": 3, "D": 8, "C": 8, "A": 6}

    # Separiamo i giocatori per ruolo per gestirli meglio
    giocatori_per_ruolo = {
        "P": [g for g in listone if g["ruolo"] == "P"],
        "D": [g for g in listone if g["ruolo"] == "D"],
        "C": [g for g in listone if g["ruolo"] == "C"],
        "A": [g for g in listone if g["ruolo"] == "A"]
    }

    rosa = []
    spesa_totale = 0

    # Peschiamo i giocatori necessari per ogni reparto mescolandoli casualmente
    for ruolo, quantita in requisiti.items():
        disponibili = giocatori_per_ruolo[ruolo]
        random.shuffle(disponibili)
        
        scelti = 0
        for g in disponibili:
            if scelti < quantita:
                # Controlliamo di non sforare i 1500 crediti totali
                if spesa_totale + g["crediti"] <= budget_totale:
                    rosa.append(g)
                    spesa_totale += g["crediti"]
                    scelti += 1

    return rosa, spesa_totale

# Esecuzione
rosa_ideale, spesa = genera_rosa_fantacalcio()

print(f"=== ROSA IDEALE DEL FANTACALCIO (Spesa totale: {spesa}/1500 crediti) ===\n")

for ruolo_chiave, titolo in [("P", "PORTIERI (3)"), ("D", "DIFENSORI (8)"), ("C", "CENTROCAMPISTI (8)"), ("A", "ATTACCANTI (6)")]:
    print(f"--- {titolo} ---")
    giocatori = [g for g in rosa_ideale if g["ruolo"] == ruolo_chiave]
    for g in giocatori:
        print(f"- {g['nome']} | Costo: {g['crediti']} crediti | FantaMedia: {g['fantamedia']}")
    print()
